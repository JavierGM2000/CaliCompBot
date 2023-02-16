# bot.py
import os

import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


intents = discord.Intents(512)
client = discord.Client(command_prefix="/",intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command()
async def drink_by_id(ctx, drinkID : int):
    await ctx.send(f'You passed {arg1} and {arg2}')

client.run(TOKEN)