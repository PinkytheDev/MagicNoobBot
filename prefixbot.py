import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!", "M!", "m!help")

TOKEN = "NDY0ODMxMzI4MjYxNjM2MDk2.DiE2YQ.j3jTWdwAJ8WVZPCSXVUKBG3-vu0"

@client.event
async def on_ready():
	print ("Logged in as")
	print (client.user.name)
	print ("---------------")

		
client.run(TOKEN)
