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

        file = discord.File(drawInstan.getImagePath(dbInstance,drinkID), filename="Drink.jpeg")
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
    file = discord.File(drawInstan.drawCharacterTalk("Jill",(105,129,193),chars[charPose-1],message), filename="Drink.jpeg")
    await ctx.send(file=file)

@bot.command()
async def gill(ctx,asset,*,message=""):
    chars = ["img\gill\Gill.png",
             "img\gill\GillFuckboy.png",
             "img\gill\Gill0_0.png",
             "img\gill\GillFocus.png",
             "img\gill\GillSad.png"]
    try:
        charPose = int(asset)
    except:
        charPose=random.randint(1,len(chars))
        message = asset+" "+message
    
    if(charPose>len(chars) or charPose<=0):
        await ctx.send("Sprite selector has to be between 1 and "+ str(len(chars)))
        return
    file = discord.File(drawInstan.drawCharacterTalk("Gillian",(124,44,179),chars[charPose-1],message), filename="Drink.jpeg")
    await ctx.send(file=file)

@bot.command()
async def dana(ctx,asset,*,message=""):
    chars = ["img\dana\Dana.png",
             "img\dana\DanaWorry.png",
             "img\dana\DanaHelmet.png",
             "img\dana\DanaThink.png",
             "img\dana\DanaWorried.png",
             "img\dana\DanaSerious.png",
             "img\dana\KidDana.webp"]
    try:
        charPose = int(asset)
    except:
        charPose=random.randint(1,len(chars))
        message = asset+" "+message
    
    if(charPose>len(chars) or charPose<=0):
        await ctx.send("Sprite selector has to be between 1 and "+ str(len(chars)))
        return
    file = discord.File(drawInstan.drawCharacterTalk("Dana",(199,33,35),chars[charPose-1],message), filename="Drink.jpeg")
    await ctx.send(file=file)

@bot.command()
async def donovan(ctx,asset,*,message=""):
    chars = ["img\donovan\Donovan.png",
             "img\donovan\DonovanHappy.png",
             "img\donovan\DonovanLaugh.png"]
    try:
        charPose = int(asset)
    except:
        charPose=random.randint(1,len(chars))
        message = asset+" "+message
    
    if(charPose>len(chars) or charPose<=0):
        await ctx.send("Sprite selector has to be between 1 and "+ str(len(chars)))
        return
    file = discord.File(drawInstan.drawCharacterTalk("Mr. Donovan",(167,75,86),chars[charPose-1],message), filename="Drink.jpeg")
    await ctx.send(file=file)

@bot.command()
async def ingram(ctx,asset,*,message=""):
    chars = ["img\ingram\Ingram.png",
             "img\ingram\IngramEyesClosed.png"]
    try:
        charPose = int(asset)
    except:
        charPose=random.randint(1,len(chars))
        message = asset+" "+message
    
    if(charPose>len(chars) or charPose<=0):
        await ctx.send("Sprite selector has to be between 1 and "+ str(len(chars)))
        return
    file = discord.File(drawInstan.drawCharacterTalk("Ingram",(208,59,37),chars[charPose-1],message), filename="Drink.jpeg")
    await ctx.send(file=file)

@bot.command()
async def sei(ctx,asset,*,message=""):
    chars = ["img\sei\SeiHelmet.png",
             "img\sei\Sei.png",
             "img\sei\SeiSmile.png",
             "img\sei\SeiDrunk.png",
             "img\sei\SeiSad.png",
             "img\sei\SeiBandage.png",
             "img\sei\SeiBandageSad.png",
             "img\sei\SeiBandageTear.png",
             "img\sei\SeiBandageWorried.png",
             "img\sei\SeiBandagWorriedEyesClosed.png",
             "img\sei\SeiBandageHappy.png"]
    try:
        charPose = int(asset)
    except:
        charPose=random.randint(1,len(chars))
        message = asset+" "+message
    
    if(charPose>len(chars) or charPose<=0):
        await ctx.send("Sprite selector has to be between 1 and "+ str(len(chars)))
        return
    file = discord.File(drawInstan.drawCharacterTalk("Sei",(92,167,172),chars[charPose-1],message), filename="Drink.jpeg")
    await ctx.send(file=file)

@bot.command()
async def kim(ctx,asset,*,message=""):
    chars = ["img\kim\Kim.png",
             "img\kim\KimAngry.png",
             "img\kim\KimCry.png",
             "img\kim\KimMURDERMURDER.png"]
    try:
        charPose = int(asset)
    except:
        charPose=random.randint(1,len(chars))
        message = asset+" "+message
    
    if(charPose>len(chars) or charPose<=0):
        await ctx.send("Sprite selector has to be between 1 and "+ str(len(chars)))
        return
    file = discord.File(drawInstan.drawCharacterTalk("Kim",(193,124,207),chars[charPose-1],message), filename="Drink.jpeg")
    await ctx.send(file=file)

@bot.command()
async def dorothy(ctx,asset,*,message=""):
    chars = ["img\dorothy\Dorothy.png",
             "img\dorothy\DorothyCry.png",
             "img\dorothy\DorothyCry2.png",
             "img\dorothy\DorothyHeartEyes.png",
             "img\dorothy\DorothyInquisition.png",
             "img\dorothy\DorothyNoIdea.png",
             "img\dorothy\DorothyOnigiri.png",
             "img\dorothy\DorothyPout.png",
             "img\dorothy\DorothySad.png",
             "img\dorothy\DorothySmug.png",
             "img\dorothy\DorothySurprised.png",
             "img\dorothy\DorothyUnamused.png",
             "img\dorothy\DorothyKids.webp"]
    try:
        charPose = int(asset)
    except:
        charPose=random.randint(1,len(chars))
        message = asset+" "+message
    
    if(charPose>len(chars) or charPose<=0):
        await ctx.send("Sprite selector has to be between 1 and "+ str(len(chars)))
        return
    file = discord.File(drawInstan.drawCharacterTalk("Dorothy",(245,11,158),chars[charPose-1],message), filename="Drink.jpeg")
    await ctx.send(file=file)

@bot.command()
async def help(ctx):
    await ctx.send('Bot is being developed and tested. Contact AlpacaCharlie#7998 for more information')

@bot.command()
async def sdown(ctx):
    await ctx.send('Killing bot')
    exit()

bot.run(TOKEN)