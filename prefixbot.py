import discord
import random
import math
import json
import asyncio
import time, datetime
 
##                  ##
## Sentry Variables ##
##                  ##
 
client = discord.Client()
msg = discord.Message()
bot_admin = ['399175572153958401']
userdata = {'000000000000000000': {'name':'Clyde', 'gold':10000, 'wins':10, 'losses':2}
            }
 
 
##                     ##
## Command Definitions ##
##                     ##
 
class role():
    def __init__(self, role, user, channel):
        self.role = role
        self.user = user
        self.channel = channel
 
 
 
class admin():
    def __init__(self, msg):
        self.msg = msg
        self.author = msg.author
       
    def check_is_admin(msg): # self
        if msg.author.id in bot_admin:
            return True
        else:
            return False
 
    def eval(msg): # self
        if admin.check_is_admin(msg):
            result = ":arrow_forward: :customs: Input \n```python\n"+" ".join(msg.content.split()[1:])+"```\n"
            result += ":white_check_mark: :airplane_departure: Output \n```python\n"+eval(" ".join(msg.content.split()[1:]))+"```"
        else:
            result = ":negative_squared_cross_mark: :passport_control: Insufficient Permissions, only Bot Admins may use this command."
        return result
 
    def save(msg): # self
        if admin.check_is_admin(msg):
            file_save = open('data.json', 'w')
            json.dump(userdata, file_save)
            file_save.close()
            return "Data Saved to `data.json`."
        else:
            print("You cannot execute this command.")
 
    def load(msg): # self
        if admin.check_is_admin(msg):
            file_load = open('data.json', 'r')
            json.load(file_load)
            file_load.close()
            return "Data Loaded from `data.json`."
        else:
            print("You cannot execute this command.")
 
##            ##
## When Ready ##
##            ##
 
@client.event
async def on_ready():
    print("Discord Client Name: "+client.user.name)
    print("Discord Client ID: "+client.user.id)
    await client.change_presence(game=discord.Game(name="tos! | https://discord.gg/gPd4bCm"))
 
##            ##
## On Message ##
##            ##
 
@client.event
async def on_message(msg):
    if msg.content.lower() == "tos!":
        await client.send_message(msg.channel, "Test Command Successful!")
 
    elif msg.content.lower().startswith('tos!stats'):
        if msg.author.id in userdata:
 
            result = '```fix\n'
            result += 'Name: '+userdata[msg.author.id]['name']+'\n'
            result += 'Gold: '+str(userdata[msg.author.id]['gold'])+'\n'
            result += 'Wins: '+str(userdata[msg.author.id]['wins'])+'\n'
            result += 'Losses: '+str(userdata[msg.author.id]['losses'])+'\n'
            result += '```'
 
            await client.send_message(msg.channel, result)
 
        else:
            userdata[msg.author.id] = {'name': 'IN-DEV!', 'gold': 0, 'wins': 0, 'losses': 0}
 
            result = '```fix\n'
            result += 'Name: '+userdata[msg.author.id]['name']+'\n'
            result += 'Gold: '+str(userdata[msg.author.id]['gold'])+'\n'
            result += 'Wins: '+str(userdata[msg.author.id]['wins'])+'\n'
            result += 'Losses: '+str(userdata[msg.author.id]['losses'])+'\n'
            result += '```'
 
            await client.send_message(msg.channel, result)
 
        pass
    elif msg.content.lower() == "tos!botstats":
        pass # await client.send_message(msg.channel, <add code here>)
 
    elif msg.content.lower().startswith('tos!eval'):
        await client.send_message(msg.channel, admin.eval(msg))
   
    elif msg.content.lower().startswith('tos!save'):
        await client.send_message(msg.channel, admin.save(msg))
 
    elif msg.content.lower().startswith('tos!load'):
        await client.send_message(msg.channel, admin.load(msg))
       
##                ##
## Run the client ##
##                ##
 
if __name__ == '__main__':
    print("\nInitalising Bot Client...\n")
    try:
        client.login("NDY0ODMxMzI4MjYxNjM2MDk2.DiE2YQ.j3jTWdwAJ8WVZPCSXVUKBG3-vu0")
    except Exception as e:
        print(e)
