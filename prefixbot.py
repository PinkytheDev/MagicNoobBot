import discord
from discord.ext import commands

TOKEN = "NDY0ODMxMzI4MjYxNjM2MDk2.DiE2YQ.j3jTWdwAJ8WVZPCSXVUKBG3-vu0"

client = commands.Bot(command_prefix="m.")


@client.event
async def on_ready():
    print("Logad on", client.user.name)


@client.event
async def on_message(message):
    user = message.author
    content = message.content
    print('{}: {}'.format(user, content))
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
    await client.process_commands(message)

@client.command(pass_context=True)
async def clear(ctx, amount=10):
    chat = ctx.message.channel
    limit = ctx.message.limit
    message = []
    async for message in client.logs_from(chat, limit-int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages deleted')


client.run(TOKEN)
