import discord
from discord import Game
from discord import commands

TOKEN = 'NDY0ODMxMzI4MjYxNjM2MDk2.D12f6w.JqdtRBcotRl8axCIQnNrQyaO7Y8'

client = commands.Bot(command_prefix = '.m')

@client.event
async def on_ready():
    await client.change_presence(game=Game(name='MagicNoob | m.'))
    print('The bot is connected')
    print('Discord Application is being online')
    print('Connected on Application' + client.user.name)

client.run(TOKEN)
