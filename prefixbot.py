import discord
from discord.ext import commands


import datetime

client = commands.Bot(command_prefix=".")

TOKEN = "NDY0ODMxMzI4MjYxNjM2MDk2.DiE2YQ.j3jTWdwAJ8WVZPCSXVUKBG3-vu0"

@client.event
async def on_ready():
	print ("Logged in as")
	print (client.user.name)
	print ("---------------")
	
	
@client.event
async def on_message(message):
	user = message.author
	msg = message.content
	print (f"{user} : {msg}")
	await client.process_commands(message)
	
	
	
@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await client.send_message(channel, '{}: {}'.format(author, content))
    await client.process_commands(message)
	
	
	
@client.command()
async def ping ():
    await client.say('Pong!')
    await client.process_commands(message)

	
			
@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)
    await client.process_commands(message)
    
    
@client.command()
asyn def embed(ctx):
	embed = discord.Embed(title="Title", description="Description", colour=discord.Color.green(), url="https://www.google.com")
	
	await ctx

		
client.run(TOKEN)
