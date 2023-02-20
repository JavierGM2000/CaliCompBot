# bot.py
import os

import random

import discord
from discord.ext.commands import Bot, Context
from discord.ext import commands

from db import Database
from drawer import Drawer

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

drawInstan = Drawer()

intents = discord.Intents(33280)
activity = discord.Game(name="Showing info about drinks that change lives")
bot = Bot(command_prefix="&",intents=intents,activity=activity)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def rand(ctx):
    drinkID = random.randint(1, 31)
    
    with Database() as dbInstance:
        file = discord.File(drawInstan.getImagePath(dbInstance,drinkID), filename="Drink.jpg")
        await ctx.send(file=file)

@bot.command()
async def drink_by_id(ctx, drinkID):
    try:
        drinkID = int(drinkID)
    except:
        drinkID = 0
    
    with Database() as dbInstance:
        file = discord.File(drawInstan.getImagePath(dbInstance,drinkID), filename="Drink.jpg")
        await ctx.send(file=file)
    
@bot.command()
async def drink(ctx, *,drinkName):
    with Database() as dbInstance:
        try:
            drinkID = int(drinkName)
        except:
            drinkID = dbInstance.getIdByName(drinkName)

        file = discord.File(drawInstan.getImagePath(dbInstance,drinkID), filename="Drink.jpg")
        await ctx.send(file=file)

@bot.command()
async def jill(ctx,asset,*,message=""):
    chars = ["img\jill\Jill.webp",
             "img\jill\JillShocked.png",
             "img\jill\JillUh.png",
             "img\jill\JillSad.png",
             "img\jill\JillSmile.png",
             "img\jill\JillHappy.png",
             "img\jill\KidJill.webp"]
    try:
        charPose = int(asset)
    except:
        charPose=random.randint(1,len(chars))
        message = asset+" "+message
    
    if(charPose>len(chars) or charPose<=0):
        await ctx.send("Sprite selector has to be between 1 and "+ str(len(chars)))
        return
    file = discord.File(drawInstan.drawCharacterTalk("Jill",(105,129,193),chars[charPose-1],message), filename="Drink.jpg")
    await ctx.send(file=file)



@bot.command()
async def help(ctx):
    await ctx.send('Bot is being developed and tested. Contact AlpacaCharlie#7998 for more information')

bot.run(TOKEN)