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

async def drawCharacterByCommand(ctx,spriteList,asset,secret,charName,charColor,message):
    chars = spriteList
    try:
        charPose = int(asset)
    except:
        charPose=random.randint(1,len(chars)-secret)
        message = asset+" "+message
    
    if(charPose>len(chars) or charPose<=0):
        await ctx.send("Sprite selector has to be between 1 and "+ str(len(chars)))
        message = asset+" "+message
        charPose=random.randint(1,len(chars)-secret)

    file = discord.File(drawInstan.drawCharacterTalk(charName,charColor,chars[charPose-1],message), filename="Drink.jpeg")
    await ctx.send(file=file)

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

jillSprites = ["img\jill\Jill.webp",
        "img\jill\JillShocked.png",
        "img\jill\JillUh.png",
        "img\jill\JillSad.png",
        "img\jill\JillSmile.png",
        "img\jill\JillHappy.png",
        "img\jill\KidJill.webp"]
@bot.command()
async def jill(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,jillSprites,asset,1,"Jill",(105,129,193),message)

gillSprites = ["img\gill\Gill.png",
               "img\gill\GillFuckboy.png",
               "img\gill\Gill0_0.png",
               "img\gill\GillFocus.png",
               "img\gill\GillSad.png"]
@bot.command()
async def gill(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,gillSprites,asset,0,"Gillian",(124,44,179),message)

danaSprites = ["img\dana\Dana.png",
               "img\dana\DanaWorry.png",
               "img\dana\DanaHelmet.png",
               "img\dana\DanaThink.png",
               "img\dana\DanaWorried.png",
               "img\dana\DanaSerious.png",
               "img\dana\KidDana.webp"]
@bot.command()
async def dana(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,danaSprites,asset,1,"Dana",(199,33,35),message)

donovanSprites = ["img\donovan\Donovan.png",
                  "img\donovan\DonovanHappy.png",
                  "img\donovan\DonovanLaugh.png"]
@bot.command()
async def donovan(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,donovanSprites,asset,0,"Mr. Donovan",(167,75,86),message)

ingramSprites = ["img\ingram\Ingram.png",
                 "img\ingram\IngramEyesClosed.png"]
@bot.command()
async def ingram(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,ingramSprites,asset,0,"Ingram",(208,59,37),message)

seiSprites = ["img\sei\SeiHelmet.png",
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
@bot.command()
async def sei(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,seiSprites,asset,0,"Sei",(92,167,172),message)

kimSprites = ["img\kim\Kim.png",
              "img\kim\KimAngry.png",
              "img\kim\KimCry.png",
              "img\kim\KimMURDERMURDER.png"]
@bot.command()
async def kim(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,kimSprites,asset,0,"Kim",(193,124,207),message)

dorothySprites = ["img\dorothy\Dorothy.png",
                  "img\dorothy\DorothyHeartMouth.png",
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
@bot.command()
async def dorothy(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,dorothySprites,asset,1,"Dorothy",(245,11,158),message)

jamieSprites = ["img\jamie\Jamie.png",
                "img\jamie\JamieThinking.png",
                "img\jamie\JamieThinkingHarder.png",
                "img\jamie\JamieWorried.png"]
@bot.command()
async def jamie(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,jamieSprites,asset,0,"Jamie",(162,120,52),message)

kiramikiSprites = ["img\kiramiki\KiraMiki.png",
                   "img\kiramiki\KiraMikiAngry.png",
                   "img\kiramiki\KiraMikiSmile.png",
                   "img\kiramiki\KiraMikiStare.png",
                   "img\kiramiki\KiraMikiOld1.png",
                   "img\kiramiki\KiraMikiOld2.png"]
@bot.command()
async def kiramiki(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,kiramikiSprites,asset,2,"*Kira* Miki",(50,114,52),message)

almaSprites = ["img\\alma\Alma.png",
               "img\\alma\AlmaDrunk.png",
               "img\\alma\AlmaEmbarrassed.png",
               "img\\alma\AlmaHappy.png",
               "img\\alma\AlmaIdontknowwhattocallthisface.png",
               "img\\alma\AlmaPointyFinger.png",
               "img\\alma\AlmaSerious.png",
               "img\\alma\AlmaSmug.png",
               "img\\alma\AlmaTired.png",
               "img\\alma\AlmaWorried.png",
               "img\\alma\AlmaKid.webp"]
@bot.command()
async def alma(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,almaSprites,asset,0,"Alma",(248,190,65),message)

stellaSprites = ["img\stella\Stella.png",
                 "img\stella\StellaAwooo.png",
                 "img\stella\StellaBlush.png",
                "img\stella\StellaCry.png",
                "img\stella\StellaSmile.png",
                "img\stella\StellaSurprise.png",
                "img\stella\StellaTired.png",
                "img\stella\KidStella.webp"]
@bot.command()
async def stella(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,stellaSprites,asset,1,"Stella",(243,49,197),message)

artSprites = ["img\\artvondelay\ArtVonDelay.png",
              "img\\artvondelay\ArtVonDelayEyesClosed.png",
              "img\\artvondelay\ArtVonDelaySurprised.png",
              "img\\artvondelay\ArtVonDelayWorried.png"]
@bot.command()
async def art(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,artSprites,asset,0,"Art",(201,201,201),message)

nicoleSprites = ["img\\nicole\\Nicole.png",
                 "img\\nicole\\NicoleAwoo.png",
                 "img\\nicole\\NicoleDrunk.png",
                 "img\\nicole\\NicoleDrunkYay.png",
                 "img\\nicole\\NicoleFanGirl.png",
                 "img\\nicole\\NicoleHappy.png",
                 "img\\nicole\\NicolePout.png",
                 "img\\nicole\\NicoleUltraYay.png"]
@bot.command()
async def nicole(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,nicoleSprites,asset,0,"Streaming-chan",(76,174,211),message)

bettySprites = ["img\\betty\Betty.png",
                "img\\betty\BettyDrunk.png",
                "img\\betty\BettyWhenLilim.png",
                "img\\betty\BettyWhenNoLilim.png",
                "img\\betty\BettyWorried.png",
                "img\\betty\KidBetty.webp"]
@bot.command()
async def betty(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,bettySprites,asset,1,"Betty",(94,232,51),message)

dealSprites = ["img\deal\Deal.png",
               "img\deal\DealClosedEyes.png"]
@bot.command()
async def deal(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,dealSprites,asset,0,"Deal",(204,255,112),message)

taylorSprites = ["img\\taylor\\Taylor.png"]
@bot.command()
async def taylor(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,taylorSprites,asset,0,"Taylor",(241,173,188),message)

virgilioSprites = ["img\\virgilio\\Virgilio.png",
                   "img\\virgilio\\VirgilioSmug.png",
                   "img\\virgilio\\VirgilioThinking.png",
                   "img\\virgilio\\VirgilioThinking.png"]
@bot.command()
async def virgilio(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,virgilioSprites,asset,0,"Virgilio",(161,126,180),message)

brianSprites = ["img\\brian\\Brian.png",
                "img\\brian\\BrianEyesClosed.png"]
@bot.command()
async def brian(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,brianSprites,asset,0,"Brian",(223,191,68),message)

cassSprites = ["img\cass\Cass.png",
                "img\cass\CassEyesClosed.png",
                "img\cass\CassFocus.png"]
@bot.command()
async def cass(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,cassSprites,asset,0,"Cass",(168,121,176),message)

radShibaSprites = ["img\dogs\RadShiba.png"]
@bot.command()
async def radshiba(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,radShibaSprites,asset,0,"Rad Shiba",(242,242,92),message)

@bot.command()
async def help(ctx):
    await ctx.send('Bot is being developed and tested.')

@bot.command()
async def sdown(ctx):
    await ctx.send('Killing bot')
    exit()

bot.run(TOKEN)