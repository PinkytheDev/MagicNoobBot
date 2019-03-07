import discord
from discord import Game
from discord.ext import commands

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
    await client.process_commands(message)

@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await client.send_message(channel, '@{} has deleted a message'.format(author))
    print('Deleted message > {}: {}'.format(author, content))
    await client.process_commands(message)

@client.command()
async def infobot():
    await client.say('Name: MagicNoob')
    await client.say('Role: Supreme')
    await client.say('Owner: Join My Minecraft Server or Mr Noob Pink')
    await client.say('Main Server: MagicNoob')

@client.command()
async def say(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

@client.command(pass_context=True, adminstrator=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Deleted Message(s)')

@client.command (name='8ball',
                                     description="Answers a yes/no question.",
                                    brief="Answers from the beyond. Do m!help 8ball for more informations.",
                                    aliases= ['eight_ball', 'eightball', '8_ball','8','Mr Noob Pink'] ,
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
	
	await client.say(random.choice(possible_responses) + "," + context.message.author.mention)

client.run('NDY0ODMxMzI4MjYxNjM2MDk2.D12f6w.JqdtRBcotRl8axCIQnNrQyaO7Y8')
