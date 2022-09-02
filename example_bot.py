# This example requires the 'message_content' intent.
import os 
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user: # checks whether message author IS the bot, to prevent recursion
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)