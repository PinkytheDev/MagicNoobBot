import random
import asyncio
from discord import Game
from discord.ext.commands import Bot
BOT_PREFIX = ("?", "!", "M!", "m!", "/")

client = Bot (command_prefix=BOT_PREFIX)

@client.command (name='8ball',
                                     description="Answers a yes/no question.",
                                    brief="Answers from the beyond. Do m!help 8ball for more informations.",
                                    aliases= ['eight_ball', 'eightball', '8_ball','8','Mr Noob Pink'] ,
                                    pass_context=True)
async def eight_ball (context) :
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
	
	await client.say (random.choice (possible_responses) + ", " + context.message.author.mention)
	
@client.command (name='hello',
                                     description="Answers : Sup ,Hello ,Hey Man ,Hey.",
                                     brief="Answers from the beyond. Do m!help hello for more informations.",
                                     aliases= ['sup', 'Hello', 'Hey', 'hey'] ,
                                     pass_context=True)
async def eight_ball (context) :
	possible_responses = [
	'Sup',
	'Hello',
	'Hey Man',
	'Hey', 
	] 
	
	await client.say (random.choice (possible_responses) + ", " + context.message.author.mention)
	
@client.command (name='Ping',
                                     description="Answers : Pong.",
                                     brief="Answers from the beyond. Do m!help Ping for more informations.",
                                     aliases= ['ping'] ,
                                     pass_context=True)
async def eight_ball (context) :
	possible_responses = [
	'Pong'
	] 	                                    
	
	await client.say (random.choice (possible_responses) )
	
@client.command (name='Cookie',
                                     description="Answers : A Cookie Emoji.",
                                     brief="Answers from the beyond. Do m!help Cookie for more informations.",
                                     aliases= ['cookie'] ,
                                     pass_context=True)
async def eight_ball (context) :
	possible_responses = [
	':cookie:'
	]
	
	await client.say (random.choice (possible_responses) )                        
	
@client.command (name='Poop',
                                     description="Answers : A Poop Emoji.",
                                     brief="Answers from the beyond. Do m!help Poop for more informations.",
                                     aliases= ['poop'] ,
                                     pass_context=True)
async def eight_ball (context) :
	possible_responses = [
	':poop:'
	]
	
	await client.say (random.choice (possible_responses) )    	
	
@client.command ( )
async def square (number) :
	squared_value = int (number) * int (number)
	await client.say (str (number) + " squared is " + str (squared_value) )
	
	
	
@client.event	
async def on_ready ( ) :
	await client.change_presence (game=Game (name="MagicNoob | M!help") )
	print ("Logged in as " + client.user.name)


@client.command()
async def kick(ctx, member: discord.Member=None):
	if not member:
		await ctx.send("Please specify a member")
		return
        await member.kick()
	await ctx.send(f"{member.mention} got kicked")

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.kick( )
    await ctx.send(f"{member.mention} got kicked")
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to kick people")
 
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.ban( )
    await ctx.send(f"{member.mention} got ban")
@ban.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to ban people")
 
@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please specify a member")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.add_roles(role)
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to mute people")
 
 
@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please specify a member")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.remove_roles(role)
@mute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to unmute people")
				  
client.run ("NDY0ODMxMzI4MjYxNjM2MDk2.DiE2YQ.j3jTWdwAJ8WVZPCSXVUKBG3-vu0")
