"""Code to run for StatusBot v0.1.

https://github.com/SuperShadowPlay/StatusBot
"""
import discord
import asyncio
import time
import config

#Global variables.
preventPrematureUpdates = False
client = discord.Client()
#Rename config variables for easier use.
TOKEN = config.TOKEN
ROLEID = config.ROLEID
#Find out which status to detect.
if config.statusDetect.lower() == 'offline':
    statusDetect = discord.Status.offline
elif config.statusDetect.lower() == 'online':
    statusDetect = discord.Status.online
elif config.statusDetect.lower() == 'idle':
    statusDetect = discord.Status.idle
elif config.statusDetect.lower() == 'dnd':
    statusDetect = discord.Status.dnd
else:
    print('''Valid value for \"statusDetect\" not found!
Check README.md for instructions on valid statusDetect values.
    \n''')
    input('Press enter to quit...')
    quit()
#Check for other null configs
if TOKEN == 'null' or ROLEID == 'null':
    print(
        '''Either your config file was not loaded correctly,
or you did not configure it!
    \n''')
    input('Press enter to quit...')
    quit()


def getTime():
    """Get time in H:M:S format."""
    _bigTime = time.strftime('%H:%M:%S')
    return _bigTime


@client.event
async def printStatus():
    """Print the status of the bot every 10 minutes."""
    global preventPrematureUpdates
    await client.wait_until_ready()
    while not client.is_closed:
        if preventPrematureUpdates is True:
            print('{0} still running || {1}'.format(client.user.name,
                  getTime()))
        await asyncio.sleep(600)


@client.event
async def on_member_update(before, after):
    """Scan members and see if they are the specified status or not."""
    if after.status == statusDetect:
        await client.add_roles(after, discord.Object(id=ROLEID))
    else:
        await client.remove_roles(after, discord.Object(
                                                    id=ROLEID))


@client.event
async def on_member_join(member):
	"""Checks the newly joined member's status and acts accordingly"""
	await client.send_message(member, '''{0} Welcome to Invisibois!
In order to begin chatting, you need to set your status to invisible.

If it isn't obvious, this chat is a general assembly of discord users
who are always invisible. You *are* allowed to go to other statuses,
but it is discouraged and you will not be able to chat while you are not invisible.'''.format(member.mention))

@client.event
async def on_message(message):
    """When a message is detected by the bot, this function is activated.

    This section consists of commands that can be sent via discord
    and allows users to interact with the bot.
    """
    #Don't reply to self
    if message.author == client.user:
        return
    if message.content == 'i/info':
        await client.send_message(message.channel, '''This bot gives a role
when a certain status (online, offline, idle, dnd) is detected,
and removes that role when that the user no
longer has the specified status.
--------------------
This bot is also open-source, and the source can be found at
https://github.com/SuperShadowPlay/StatusBot
--------------------
This bot has no other user commands
other than this one''')


@client.event
async def on_ready():
    """When bot is ready it will output a message and start afterwards."""
    global preventPrematureUpdates
    preventPrematureUpdates = True
    await client.change_presence(game=discord.Game(name='i/info'))
    print('Logged in as {0}, ID {1} at {2}'.format(client.user.name,
                                                   client.user.id, getTime()))
    print('''Status detection set to {0}
Role to give/take is ID {1}'''.format(statusDetect, ROLEID))
    print('------')

client.loop.create_task(printStatus())
client.run(TOKEN)
