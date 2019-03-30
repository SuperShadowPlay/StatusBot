"""Invisible bot vAlpha."""
import discord
import asyncio
import time
TOKEN = 'NDQ5MzUxOTU2ODEzNzA5MzEz.XJ6HqA.R9UOPnApBBoS0O2H1dyZnQBnPZE'
preventPrematureUpdates = False

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
async def on_message(message):
    """on_message portion, it's a big mixed bag."""
    if message.content == '!status':
        await client.send_message(message.channel, 'You are {0}'.format(
                                message.author.status))
    if message.content == '!members':
        await client.send_message(message.channel,
                                  'Members are: {0}'.format(
                                   message.server.members))
                                   #Gives dict that can be iterated like below
    if message.content == '!memcon':
        for x in message.server.members:
            print('{0} is {1}'.format(x, x.status))


@client.event
async def on_ready():
    """When bot is ready it will output a message and start afterwards."""
    global preventPrematureUpdates
    preventPrematureUpdates = True
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(printStatus())
client.run(TOKEN)
