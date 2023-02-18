# bot.py
import os

import discord
from discord.ext.commands import Bot, Context
from discord.ext import commands

from db import Database
from drawer import Drawer

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

dbInstance = Database()
drawInstan = Drawer(dbInstance)

intents = discord.Intents(33280)
activity = discord.Game(name="Showing info about drinks that change lives")
bot = Bot(command_prefix="&",intents=intents,activity=activity)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def drink_by_id(ctx, drinkID):
    if not isinstance(drinkID, int):
      drinkID = 0
    file = discord.File(drawInstan.getImagePath(drinkID), filename="Drink.jpg")
    await ctx.send(file=file)
    

@bot.command()
async def help(ctx):
    await ctx.send('Bot is being developed and tested. Contact AlpacaCharlie#7998 for more information')

bot.run(TOKEN)