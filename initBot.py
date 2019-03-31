"""Code to run for StatusBot v0.1
https://github.com/SuperShadowPlay/StatusBot"""
import discord
import asyncio
import time
from config import *
preventPrematureUpdates = False
#Role id (which role will be assigned to remove/give permissions)

client = discord.Client()


def getTime():
    """Get time in H:M:S format."""
    _bigTime = time.strftime('%H:%M:%S')
    return _bigTime


@client.event
async def printStatus():
    """Print the status of the bot every two minutes."""
    global preventPrematureUpdates
    await client.wait_until_ready()
    while not client.is_closed:
        if preventPrematureUpdates is True:
            print('{0} still running at {1}'.format(client.user.name,
                  getTime()))
        await asyncio.sleep(120)


@client.event
async def on_member_update(before, after):
    """Scan members and see if they are offline/invisible or not."""
    if after.status == discord.Status.offline:
        await client.add_roles(after, discord.Object(id=ROLEID))
    else:
        await client.remove_roles(after, discord.Object(
                                                    id=ROLEID))
    asyncio.sleep(1)


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
        `https://github.com/SuperShadowPlay/StatusBot`
        --------------------
        (This bot has no other user commands
        other than this one)''')


@client.event
async def on_ready():
    """When bot is ready it will output a message and start afterwards."""
    global preventPrematureUpdates
    preventPrematureUpdates = True
    await client.change_presence(game=discord.Game(name='i/help for commands'))
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(printStatus())
client.run(TOKEN)
