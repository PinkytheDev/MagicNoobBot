import discord
from discord.ext import commands

TOKEN = "NDY0ODMxMzI4MjYxNjM2MDk2.DiE2YQ.j3jTWdwAJ8WVZPCSXVUKBG3-vu0"

client = commands.Bot(command_prefix="m.")

@client.event
async def on_ready():
	print ("Logad on", client.user.name)
	
@client.event
async def on_message(message):
	user = message.author
	content = message.content
	print ('{}: {}'.format(user, content))
	await client.process_commands(message)
	
@client.event
async def on_message_delete(message):
	user = message.author
	content = message.content
	chat = message.channel
	
	await client.send_message(chat, '{}: {}'.format(user, content))
	await client.process_commands(message)
	
@client.command()
async def ping():
	await client.say("Pong!")
	
@client.command()
async def echo(*args):
	output = ''
	for words in args:
		output += word
		output += ' '
	await client.say(output)
	
client.run (TOKEN)
