# full apologies to non-me readers: this is absolutely too many comments
# never used python before though, so i simply am going to make this many notes so i can learn
# i am also going to consign this first bot code to the annals of time
# learned a lot about python! outdated syntax though, going to restart from new docs

import os # os module provides functions for interacting with directories
# need to import it to be able to interact with the underlying operating system
import random # imports the random module

import discord # import discord
from discord.ext import commands

intents = discord.Intents.default() # sets intents for bot, intents subscribe bots to specific events, see docs
# intents.members = True
# bot = commands.Bot(command_prefix='!', intents=intents)

from dotenv import load_dotenv # import load_dotenv from dotenv

load_dotenv() # take environment variables from .env
TOKEN = os.getenv('DISCORD_TOKEN') # assigns TOKEN to os function that retrieves DISCORD_TOKEN from .env
GUILD = os.getenv('DISCORD_GUILD') # assigns GUILD to os function that retrieves DISCORD_GUILD from .env

client = discord.Client(intents=intents) # assigns client to an instance of Client() from discord module
# a client handles events, tracks state, and generally interacts with and lets us connect to the discord api

@client.event # this is a decorator: syntax for calling higher order functions. decorators wrap functions, modifying behaviour
async def on_ready(): # asynchronous function called on_ready()
    print(f'{client.user.name} is connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


client.run(TOKEN) # runs bot using login token from .env