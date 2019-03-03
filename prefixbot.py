import discord
from discord import Game
from discord.ext import commands

TOKEN = 'NDY0ODMxMzI4MjYxNjM2MDk2.D12f6w.JqdtRBcotRl8axCIQnNrQyaO7Y8'

client = commands.Bot(command_prefix = '.m')

@client.event
async def on_ready():
    await client.change_presence(game=Game(name='MagicNoob | .m'))
    print('The bot is connected')
    print('Discord Application is being online')
    print('Connected on Application ' + client.user.name)

@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))
    
@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await client.send_message(channel, '@{} has deleted a message'.format(author))
    print('Deleted message > {}: {}'.format(author, content))

client.run(TOKEN)
