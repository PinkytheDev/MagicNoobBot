import discord
import requests
import random
import asyncio
from discord import Game
from discord.ext import commands

client = commands.Bot(command_prefix='.m')


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
    await client.process_commands(message)


@client.event
async def on_member_join(member):
    roles = discord.utils.get(member.server.roles, name='Members')
    await client.add_roles(member, role)
    await client.say(
        "Hey! Server Owner. But if you don't have **Members** role. Then, I prefer you to add it to make this function work.")
    await client.process_commands(message)


@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    print('Deleted Message > {}: {}'.format(author, content))
    await client.process_commands(message)


@client.command()
async def infobot():
    await client.say('Name: MagicNoob')
    await client.say('Role: Supreme')
    await client.say('Owner: Join My Minecraft Server or Mr Noob Pink')
    await client.say('Main Server: MagicNoob')


@client.command()
@commands.has_permissions(administrator=True)
async def say(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Deleted Message(s)')

@client.command(name='8ball',
                description="Answers yes/no",
                brief="Answers from the beyond. Do .m8ball for more info",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
    'That is a resounding no',
    'It is not looking likely',
    'Too hard to tell',
    'It is quite possible',
    'Definitely',
    'No',
    'This question is shit',
    'Fuck U',
    'Yes',
    'Hmmm???',
    'I dont think so!',
    'You Know What BYE!',
    'I dont know',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

#math

@client.command()
async def add(left : int, right : int):
    """Numbers + Numbers"""
await client.say(left + right)

@client.command()
async def subtract(left : int, right : int):
    """Numbers - Numbers"""
await client.say(left - right)

@client.command()
async def multiply(left : int, right : int):
    """Numbers x Numbers"""
await client.say(left * right)

@client.command()
async def divide(left : int, right : int)
    """Numbers // Numbers. Except Numbers // 0"""
    try:
        await client.say(left // right)
    except ZeroDivisionError:
        await client.say("The number can't be divided by ZERO")
    

client.run('NDY0ODMxMzI4MjYxNjM2MDk2.D12f6w.JqdtRBcotRl8axCIQnNrQyaO7Y8')
