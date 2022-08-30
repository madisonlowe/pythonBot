import os # os module provides functions for interacting with directories
# need to import it to be able to interact with the underlying operating system

import discord # import discord
from dotenv import load_dotenv # import load_dotenv from dotenv

load_dotenv() # take environment variables from .env
TOKEN = os.getenv('DISCORD_TOKEN') # assigns TOKEN to os function that retrieves DISCORD_TOKEN from .env

client = discord.Client() # assigns client to an instance of Client() from discord module
# a client handles events, tracks state, and generally interacts with and lets us connect to the discord api

@client.event # this is a decorator: syntax for calling higher order functions. decorators wrap functions, modifying behaviour
async def on_ready(): # asynchronous function called on_ready()
    print(f'{client.user} has connected to Discord!') 
# some stackoverflow guy says we could end this function with: on_ready = client.event(on_ready)
# the @ symbol is a shorthand to eliminating having to type that, though

client.run(TOKEN) # runs bot using login token from .env