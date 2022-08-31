import os # os module provides functions for interacting with directories
# need to import it to be able to interact with the underlying operating system

import discord # import discord
intents = discord.Intents.default() # sets intents for bot, intents subscribe bots to specific events, see docs
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
async def on_member_join(member=discord.Member):
    print(f'Member {member.name} just joined the server.')

client.run(TOKEN) # runs bot using login token from .env