import discord
from discord.ext import commands
import asyncio

TOKEN = 'OTk5OTU4OTA5MDM0OTc1MjYy.G9FC1a.mrOSldjRQ4XeX81ASFZz_ZV5Xyb1YDG-as8W6g'
GUILD = 'Project Buddies Chatroom'
ADMIN = 798441605752422401

DELAY = 1

intents = discord.Intents.all()
client =  commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print("{} is now online in:".format(client.user))
    for guild in client.guilds:
        print(guild.name)

async def log(message):
    logs = client.get_channel(1015945595652931606)
    if message.channel == logs:
        return None
    if message.embeds:
        await logs.send("[{}] / [{}]:".format(message.author, message.channel))
        await logs.send(embeds=message.embeds)
    else:
        await logs.send("[{}] / [{}]: {}".format(message.author, message.channel, message.content))

@client.event
async def on_message_edit(before, after):
    if before.content != after.content:
        await asyncio.sleep(DELAY)
        await log(after)

@client.event
async def on_message(message):
    await asyncio.sleep(DELAY)
    await log(message)

client.run(TOKEN)

