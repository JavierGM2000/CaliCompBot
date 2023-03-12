# bot.py
import os

import random

import discord
from discord import app_commands
from discord.ext.commands import Bot, Context
from discord.ext import commands

from db import Database
from drawer import Drawer

from dotenv import load_dotenv

from PIL import Image

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

drawInstan = Drawer()

async def drawCharacterByCommand(ctx,spriteList,asset,secret,charName,charColor,message,charHeight:int=536):
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

    file = discord.File(drawInstan.drawCharacterTalk(charName,charColor,chars[charPose-1],message,charHeight), filename="Drink.jpeg")
    await ctx.send(file=file)

async def drawCharacterByCommandGif(ctx,spriteList,asset,secret,charName,charColor,message,charHeight:int=536):
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

    file = discord.File(drawInstan.drawCharacterGif(charName,charColor,chars[charPose-1],message,charHeight), filename="Conversation.gif")
    await ctx.send(file=file)

async def drawCharacterByCommandTalk(ctx,spriteList,mouthlist,asset,secret,charName,charColor,message,charHeight:int=536):
    print("Called draw character talk")
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

    print(chars[charPose-1][0])
    print(chars[charPose-1][1])
    print(chars[charPose-1][2])
    if chars[charPose-1][1] >= 0:
        selectedMouth = mouthlist[chars[charPose-1][1]]
    else:
        selectedMouth = None
    file = discord.File(drawInstan.drawCharacterTalkGilf(charName,charColor,chars[charPose-1][0],selectedMouth,chars[charPose-1][2],message,charHeight), filename="Conversation.gif")
    await ctx.send(file=file)

intents = discord.Intents(33280)
activity = discord.Game(name="New commands! Use &help")
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
jillSpritesTest = [["img\jill\Jill.webp",0,(32,81)],
        ["img\jill\JillShocked.png",0,(32,81)],
        ["img\jill\JillUh.png",0,(32,81)],
        ["img\jill\JillSad.png",0,(32,81)],
        ["img\jill\JillSmile.png",0,(32,81)],
        ["img\jill\JillHappy.png",0,(32,81)],
        ["img\jill\KidJill.webp",-1,(32,81)]]
jillMouths = [["img\jill\mouths\mouth1.png",
               "img\jill\mouths\mouth2.png",
               "img\jill\mouths\mouth3.png",
               "img\jill\mouths\mouth4.png"]]
@bot.command()
async def jill(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,jillSprites,asset,1,"Jill",(105,129,193),message,364)

@bot.command()
async def jillgif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,jillSprites,asset,1,"Jill",(105,129,193),message,364)

@bot.command()
async def jilltalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,jillSpritesTest,jillMouths,asset,1,"Jill",(105,129,193),message,364)

gillSprites = ["img\gill\Gill.png",
               "img\gill\GillFuckboy.png",
               "img\gill\Gill0_0.png",
               "img\gill\GillFocus.png",
               "img\gill\GillSad.png"]
gillSpritesTest = [["img\gill\Gill.png",0,(70,86)],
               ["img\gill\GillFuckboy.png",0,(70,86)],
               ["img\gill\Gill0_0.png",0,(70,86)],
               ["img\gill\GillFocus.png",0,(70,86)],
               ["img\gill\GillSad.png",0,(70,86)]]
gillmouths = [["img\gill\mouth\mouth1.png",
               "img\gill\mouth\mouth2.png",
               "img\gill\mouth\mouth3.png",
               "img\gill\mouth\mouth4.png"]]
@bot.command()
async def gill(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,gillSprites,asset,0,"Gillian",(124,44,179),message,422)
@bot.command()
async def gillgif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,gillSprites,asset,0,"Gillian",(124,44,179),message,422)
@bot.command()
async def gilltalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,gillSpritesTest,gillmouths,asset,0,"Gillian",(124,44,179),message,422)

danaSprites = ["img\dana\Dana.png",
               "img\dana\DanaWorry.png",
               "img\dana\DanaHelmet.png",
               "img\dana\DanaThink.png",
               "img\dana\DanaWorried.png",
               "img\dana\DanaSerious.png",
               "img\dana\zane.png",
               "img\dana\zane2.png",
               "img\dana\zane3.png",
               "img\dana\KidDana.webp"]
danaSpritesTest = [["img\dana\Dana.png",0,(61,103)],
               ["img\dana\DanaWorry.png",0,(61,103)],
               ["img\dana\DanaHelmet.png",-1,(61,103)],
               ["img\dana\DanaThink.png",0,(61,103)],
               ["img\dana\DanaWorried.png",0,(61,103)],
               ["img\dana\DanaSerious.png",0,(61,103)],
               ["img\dana\zane.png",-1,(61,103)],
               ["img\dana\zane2.png",-1,(61,103)],
               ["img\dana\zane3.png",-1,(61,103)],
               ["img\dana\KidDana.webp",-1,(61,103)]]
danaMouths = [["img\dana\mouths\mouth1.png",
               "img\dana\mouths\mouth2.png",
               "img\dana\mouths\mouth3.png"]]
@bot.command()
async def dana(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,danaSprites,asset,4,"Dana",(199,33,35),message,414)
@bot.command()
async def danagif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,danaSprites,asset,4,"Dana",(199,33,35),message,414)
@bot.command()
async def danatalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,danaSpritesTest,danaMouths,asset,4,"Dana",(199,33,35),message,414)

donovanSprites = ["img\donovan\Donovan.png",
                  "img\donovan\DonovanHappy.png",
                  "img\donovan\DonovanLaugh.png"]
donovanSpritesTest = [["img\donovan\Donovan.png",0,(41,70)],
                  ["img\donovan\DonovanHappy.png",0,(41,70)],
                  ["img\donovan\DonovanLaugh.png",0,(41,70)]]

donovanMouths = [["img\donovan\mouth\mouth1.png",
                  "img\donovan\mouth\mouth2.png",
                  "img\donovan\mouth\mouth3.png",
                  "img\donovan\mouth\mouth2.png"]]
@bot.command()
async def donovan(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,donovanSprites,asset,0,"Mr. Donovan",(167,75,86),message,412)
@bot.command()
async def donovangif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,donovanSprites,asset,0,"Mr. Donovan",(167,75,86),message,412)
@bot.command()
async def donovantalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,donovanSpritesTest,donovanMouths,asset,0,"Mr. Donovan",(167,75,86),message,412)

ingramSprites = ["img\ingram\Ingram.png",
                 "img\ingram\IngramEyesClosed.png"]
ingramSpritestest = [["img\ingram\Ingram.png",0,(89,79)],
                 ["img\ingram\IngramEyesClosed.png",0,(88,79)]]
ingramMouths = [["img\ingram\mouths\mouth1.png",
                 "img\ingram\mouths\mouth2.png",
                 "img\ingram\mouths\mouth3.png",
                 "img\ingram\mouths\mouth2.png",]]
@bot.command()
async def ingram(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,ingramSprites,asset,0,"Ingram",(208,59,37),message,406)
@bot.command()
async def ingramgif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,ingramSprites,asset,0,"Ingram",(208,59,37),message,406)
@bot.command()
async def ingramtalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,ingramSpritestest,ingramMouths,asset,0,"Ingram",(208,59,37),message,406)

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
              "img\sei\SeiBandageHappy.png",
              "img\sei\seiOld.png",
              "img\sei\KidSei.webp"]
seiSpritesTest = [["img\sei\SeiHelmet.png",-1,(52,81)],
              ["img\sei\Sei.png",1,(52,81)],
              ["img\sei\SeiSmile.png",1,(52,82)],
              ["img\sei\SeiDrunk.png",0,(60,80)],
              ["img\sei\SeiSad.png",1,(53,82)],
              ["img\sei\SeiBandage.png",2,(52,79)],
              ["img\sei\SeiBandageSad.png",2,(52,79)],
              ["img\sei\SeiBandageTear.png",2,(52,79)],
              ["img\sei\SeiBandageWorried.png",2,(52,79)],
              ["img\sei\SeiBandagWorriedEyesClosed.png",2,(52,79)],
              ["img\sei\SeiBandageHappy.png",2,(52,79)],
              ["img\sei\seiOld.png",-1,(0,0)],
              ["img\sei\KidSei.webp",-1,(0,0)]]
seimouths = [["img\sei\mouths\mouthdrunk1.png",
              "img\sei\mouths\mouthdrunk2.png",
              "img\sei\mouths\mouthdrunk3.png",
              "img\sei\mouths\mouthdrunk2.png"],
              ["img\sei\mouths\suitmouth1.png",
               "img\sei\mouths\suitmouth2.png",
               "img\sei\mouths\suitmouth3.png",
               "img\sei\mouths\suitmouth2.png"],
                ["img\sei\mouths\\bandagemouth1.png",
                 "img\sei\mouths\\bandagemouth2.png",
                 "img\sei\mouths\\bandagemouth3.png",
                 "img\sei\mouths\\bandagemouth2.png"]]
@bot.command()
async def sei(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,seiSprites,asset,2,"Sei",(92,167,172),message,384)
@bot.command()
async def seigif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,seiSprites,asset,2,"Sei",(92,167,172),message,384)
@bot.command()
async def seitalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,seiSpritesTest,seimouths,asset,2,"Sei",(92,167,172),message,384)

kimSprites = ["img\kim\Kim.png",
              "img\kim\KimAngry.png",
              "img\kim\KimCry.png",
              "img\kim\KimMURDERMURDER.png"]
kimSpritesTest = [["img\kim\Kim.png",0,(29,96)],
              ["img\kim\KimAngry.png",0,(29,96)],
              ["img\kim\KimCry.png",0,(29,96)],
              ["img\kim\KimMURDERMURDER.png",0,(29,96)]]

kimmouths = [["img\kim\mouth\mouth1.png",
              "img\kim\mouth\mouth2.png",
              "img\kim\mouth\mouth3.png",
              "img\kim\mouth\mouth2.png"]]
@bot.command()
async def kim(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,kimSprites,asset,0,"Kim",(193,124,207),message,382)
@bot.command()
async def kimgif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,kimSprites,asset,0,"Kim",(193,124,207),message,382)
@bot.command()
async def kimtalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,kimSpritesTest,kimmouths,asset,0,"Kim",(193,124,207),message,382)

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
                  "img\dorothy\dorothyOld.png",
                  "img\dorothy\dorothy-cat.png",
                  "img\dorothy\dorothy detail.png",
                  "img\dorothy\dorothy detail cat.png",
                  "img\dorothy\sprite-corte_18.png",
                  "img\dorothy\dorothy-lost.png",
                  "img\dorothy\dorothy-pachi.png",
                  "img\dorothy\dorothy-puchero.png",
                  "img\dorothy\dorothy-smug.png",
                  "img\dorothy\DorothyKids.webp"]
dorothySpritesTest = [["img\dorothy\Dorothy.png",2,(41,75)],
                  ["img\dorothy\DorothyHeartMouth.png",0,(40,73)],
                  ["img\dorothy\DorothyCry.png",-1,(0,0)],
                  ["img\dorothy\DorothyCry2.png",-1,(0,0)],
                  ["img\dorothy\DorothyHeartEyes.png",1,(37,77)],
                  ["img\dorothy\DorothyInquisition.png",2,(72,75)],
                  ["img\dorothy\DorothyNoIdea.png",2,(41,75)],
                  ["img\dorothy\DorothyOnigiri.png",2,(41,74)],
                  ["img\dorothy\DorothyPout.png",2,(41,75)],
                  ["img\dorothy\DorothySad.png",2,(41,75)],
                  ["img\dorothy\DorothySmug.png",2,(41,75)],
                  ["img\dorothy\DorothySurprised.png",2,(41,75)],
                  ["img\dorothy\DorothyUnamused.png",2,(41,75)],
                  ["img\dorothy\dorothyOld.png",-1,(0,0)],
                  ["img\dorothy\dorothy-cat.png",-1,(0,0)],
                  ["img\dorothy\dorothy detail.png",-1,(0,0)],
                  ["img\dorothy\dorothy detail cat.png",-1,(0,0)],
                  ["img\dorothy\sprite-corte_18.png",-1,(0,0)],
                  ["img\dorothy\dorothy-lost.png",-1,(0,0)],
                  ["img\dorothy\dorothy-pachi.png",-1,(0,0)],
                  ["img\dorothy\dorothy-puchero.png",-1,(0,0)],
                  ["img\dorothy\dorothy-smug.png",-1,(0,0)],
                  ["img\dorothy\DorothyKids.webp",-1,(0,0)]]
dorothymouths=[["img\dorothy\mouth\HeartMouth1.png",
                "img\dorothy\mouth\HeartMouth2.png"],
                ["img\dorothy\mouth\drunkMouth1.png",
                 "img\dorothy\mouth\drunkMouth2.png",
                 "img\dorothy\mouth\drunkMouth3.png",
                 "img\dorothy\mouth\drunkMouth2.png"],
                 ["img\dorothy\mouth\mouth1.png",
                  "img\dorothy\mouth\mouth2.png",
                  "img\dorothy\mouth\mouth3.png",
                  "img\dorothy\mouth\mouth2.png"]]
@bot.command()
async def dorothy(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,dorothySprites,asset,10,"Dorothy",(245,11,158),message,314)
@bot.command()
async def dorothygif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,dorothySprites,asset,10,"Dorothy",(245,11,158),message,314)
@bot.command()
async def dorothytalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,dorothySpritesTest,dorothymouths,asset,10,"Dorothy",(245,11,158),message,314)

jamieSprites = ["img\jamie\Jamie.png",
                "img\jamie\JamieThinking.png",
                "img\jamie\JamieThinkingHarder.png",
                "img\jamie\JamieWorried.png",
                "img\jamie\jamieOld.png",
                "img\jamie\jamie detail.png"]
jamieSpritesTest = [["img\jamie\Jamie.png",0,(66,92)],
                ["img\jamie\JamieThinking.png",0,(66,91)],
                ["img\jamie\JamieThinkingHarder.png",0,(66,91)],
                ["img\jamie\JamieWorried.png",0,(66,91)],
                ["img\jamie\jamieOld.png",-1,(0,0)],
                ["img\jamie\jamie detail.png",-1,(0,0)]]
jamiemouth=[["img\jamie\mouth\jamieMouth.png",
             "img\jamie\mouth\jamieMouth2.png",
             "img\jamie\mouth\jamieMouth3.png",
             "img\jamie\mouth\jamieMouth2.png"]]
@bot.command()
async def jamie(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,jamieSprites,asset,2,"Jamie",(162,120,52),message,438)
@bot.command()
async def jamiegif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,jamieSprites,asset,2,"Jamie",(162,120,52),message,438)
@bot.command()
async def jamietalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,jamieSpritesTest,jamiemouth,asset,2,"Jamie",(162,120,52),message,438)

kiramikiSprites = ["img\kiramiki\KiraMiki.png",
                   "img\kiramiki\KiraMikiAngry.png",
                   "img\kiramiki\KiraMikiSmile.png",
                   "img\kiramiki\KiraMikiStare.png",
                   "img\kiramiki\KiraMikiOld1.png",
                   "img\kiramiki\KiraMikiOld2.png"]
kiramikiSpritesTest = [["img\kiramiki\KiraMiki.png",0,(52,79)],
                   ["img\kiramiki\KiraMikiAngry.png",0,(52,79)],
                   ["img\kiramiki\KiraMikiSmile.png",0,(52,79)],
                   ["img\kiramiki\KiraMikiStare.png",0,(52,79)],
                   ["img\kiramiki\KiraMikiOld1.png",-1,(0,0)],
                   ["img\kiramiki\KiraMikiOld2.png",-1,(0,0)]]
kiramikimouths=[["img\kiramiki\mouths\mouth1.png",
           "img\kiramiki\mouths\mouth2.png",
           "img\kiramiki\mouths\mouth3.png",
           "img\kiramiki\mouths\mouth2.png"]]
@bot.command()
async def kiramiki(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,kiramikiSprites,asset,2,"*Kira* Miki",(47,106,150),message,388)
@bot.command()
async def kiramikigif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,kiramikiSprites,asset,2,"*Kira* Miki",(47,106,150),message,388)
@bot.command()
async def kiramikitalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,kiramikiSpritesTest,kiramikimouths,asset,2,"*Kira* Miki",(47,106,150),message,388)

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
               "img\\alma\keki2.png",
               "img\\alma\keki3.png",
               "img\\alma\keki 3 detail.png",
               "img\\alma\AlmaKid.webp"]
almaSpritesTest = [["img\\alma\Alma.png",1,(43,103)],
               ["img\\alma\AlmaDrunk.png",0,(48,110)],
               ["img\\alma\AlmaEmbarrassed.png",0,(47,110)],
               ["img\\alma\AlmaHappy.png",1,(43,103)],
               ["img\\alma\AlmaIdontknowwhattocallthisface.png",1,(43,103)],
               ["img\\alma\AlmaPointyFinger.png",2,(54,103)],
               ["img\\alma\AlmaSerious.png",1,(42,104)],
               ["img\\alma\AlmaSmug.png",1,(43,103)],
               ["img\\alma\AlmaTired.png",1,(43,103)],
               ["img\\alma\AlmaWorried.png",1,(43,103)],
               ["img\\alma\keki2.png",-1,(0,0)],
               ["img\\alma\keki3.png",-1,(0,0)],
               ["img\\alma\keki 3 detail.png",-1,(0,0)],
               ["img\\alma\AlmaKid.webp",-1,(0,0)]]
almamouth= [[
             "img\\alma\mouth\drunkmouth2.png",
             "img\\alma\mouth\drunkmouth3.png",
             "img\\alma\mouth\drunkmouth4.png",
             "img\\alma\mouth\drunkmouth5.png",
             "img\\alma\mouth\drunkmouth4.png",
             "img\\alma\mouth\drunkmouth3.png"],
             ["img\\alma\mouth\mouth0.png",
              "img\\alma\mouth\mouth1.png",
              "img\\alma\mouth\mouth2.png",
              "img\\alma\mouth\mouth3.png",
              "img\\alma\mouth\mouth2.png",
              "img\\alma\mouth\mouth1.png"],
              ["img\\alma\mouth\mouth0.png",
              "img\\alma\mouth\mouth2.png"]]
@bot.command()
async def alma(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,almaSprites,asset,4,"Alma",(248,190,65),message,418)
@bot.command()
async def almagif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,almaSprites,asset,4,"Alma",(248,190,65),message,418)
@bot.command()
async def almatalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,almaSpritesTest,almamouth,asset,4,"Alma",(248,190,65),message,418)

stellaSprites = ["img\stella\Stella.png",
                 "img\stella\StellaAwooo.png",
                 "img\stella\StellaBlush.png",
                "img\stella\StellaCry.png",
                "img\stella\StellaSmile.png",
                "img\stella\StellaSurprise.png",
                "img\stella\StellaTired.png",
                "img\stella\stellaOld.png",
                "img\stella\KidStella.webp"]
stellaSpritesTest = [["img\stella\Stella.png",0,(63,79)],
                 ["img\stella\StellaAwooo.png",0,(63,90)],
                 ["img\stella\StellaBlush.png",0,(61,93)],
                ["img\stella\StellaCry.png",0,(62,79)],
                ["img\stella\StellaSmile.png",0,(63,90)],
                ["img\stella\StellaSurprise.png",0,(63,90)],
                ["img\stella\StellaTired.png",0,(63,79)],
                ["img\stella\stellaOld.png",-1,(0,0)],
                ["img\stella\KidStella.webp",-1,(0,0)]]
stellamouths = [["img\stella\mouth\Mouth0.png",
                 "img\stella\mouth\Mouth1.png",
                 "img\stella\mouth\Mouth2.png",
                 "img\stella\mouth\Mouth3.png"]]
@bot.command()
async def stella(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,stellaSprites,asset,2,"Stella",(243,49,197),message,356)
@bot.command()
async def stellagif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,stellaSprites,asset,2,"Stella",(243,49,197),message,356)
@bot.command()
async def stellatalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,stellaSpritesTest,stellamouths,asset,2,"Stella",(243,49,197),message,356)

artSprites = ["img\\artvondelay\\ArtVonDelay.png",
              "img\\artvondelay\\ArtVonDelayEyesClosed.png",
              "img\\artvondelay\\ArtVonDelaySurprised.png",
              "img\\artvondelay\\ArtVonDelayWorried.png",
              "img\\artvondelay\\artOld.png"]
artSpritesTestt = [["img\\artvondelay\\ArtVonDelay.png",0,(51,59)],
              ["img\\artvondelay\\ArtVonDelayEyesClosed.png",0,(51,59)],
              ["img\\artvondelay\\ArtVonDelaySurprised.png",0,(51,59)],
              ["img\\artvondelay\\ArtVonDelayWorried.png",0,(51,59)],
              ["img\\artvondelay\\artOld.png",-1,(51,59)]]
artMouth = [["img\\artvondelay\mouth\mouth0.png",
             "img\\artvondelay\mouth\mouth1.png",
             "img\\artvondelay\mouth\mouth2.png",
             "img\\artvondelay\mouth\mouth3.png"]]
@bot.command()
async def art(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,artSprites,asset,1,"Art",(201,201,201),message,356)
@bot.command()
async def artgif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,artSprites,asset,1,"Art",(201,201,201),message,356)
@bot.command()
async def arttalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,artSpritesTestt,artMouth,asset,1,"Art",(201,201,201),message,356)

nicoleSprites = ["img\\nicole\\Nicole.png",
                 "img\\nicole\\NicoleAwoo.png",
                 "img\\nicole\\NicoleDrunk.png",
                 "img\\nicole\\NicoleDrunkYay.png",
                 "img\\nicole\\NicoleFanGirl.png",
                 "img\\nicole\\NicoleHappy.png",
                 "img\\nicole\\NicolePout.png",
                 "img\\nicole\\NicoleUltraYay.png"]
nicoleSpritesTest = [["img\\nicole\\Nicole.png",2,(68,115)],
                 ["img\\nicole\\NicoleAwoo.png",1,(75,117)],
                 ["img\\nicole\\NicoleDrunk.png",1,(75,117)],
                 ["img\\nicole\\NicoleDrunkYay.png",1,(75,117)],
                 ["img\\nicole\\NicoleFanGirl.png",2,(68,115)],
                 ["img\\nicole\\NicoleHappy.png",2,(68,115)],
                 ["img\\nicole\\NicolePout.png",0,(83,116)],
                 ["img\\nicole\\NicoleUltraYay.png",1,(75,117)]]
nicolemouths = [["img\\nicole\mouth\pout0.png",
                 "img\\nicole\mouth\pout1.png"],
                 ["img\\nicole\mouth\mouth0.png",
                  "img\\nicole\mouth\mouth1.png",
                  "img\\nicole\mouth\mouth2.png",
                  "img\\nicole\mouth\mouth3.png"],
                  ["img\\nicole\mouth\mouth0.png",
                   "img\\nicole\mouth\\normalMouth1.png",
                   "img\\nicole\mouth\\normalMouth2.png"]]
@bot.command()
async def nicole(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,nicoleSprites,asset,0,"Streaming-chan",(76,174,211),message,432)
@bot.command()
async def nicolegif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,nicoleSprites,asset,0,"Streaming-chan",(76,174,211),message,432)
@bot.command()
async def nicoletalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,nicoleSpritesTest,nicolemouths,asset,0,"Streaming-chan",(76,174,211),message,432)

bettySprites = ["img\\betty\Betty.png",
                "img\\betty\BettyDrunk.png",
                "img\\betty\BettyWhenLilim.png",
                "img\\betty\BettyWhenNoLilim.png",
                "img\\betty\BettyWorried.png",
                "img\\betty\\vet.png",
                "img\\betty\\vet 2.png",
                "img\\betty\\vet 3.png",
                "img\\betty\\drunk vet.png",
                "img\\betty\\vet drunk 2.png",
                "img\\betty\\vet drunk 3.png",
                "img\\betty\\vet smug.png",
                "img\\betty\\KidBetty.webp"]
bettySpritesTest = [["img\\betty\Betty.png",0,(49,68)],
                ["img\\betty\BettyDrunk.png",1,(52,67)],
                ["img\\betty\BettyWhenLilim.png",1,(53,67)],
                ["img\\betty\BettyWhenNoLilim.png",0,(50,68)],
                ["img\\betty\BettyWorried.png",0,(50,68)],
                ["img\\betty\\vet.png",-1,(0,0)],
                ["img\\betty\\vet 2.png",-1,(0,0)],
                ["img\\betty\\vet 3.png",-1,(0,0)],
                ["img\\betty\\drunk vet.png",-1,(0,0)],
                ["img\\betty\\vet drunk 2.png",-1,(0,0)],
                ["img\\betty\\vet drunk 3.png",-1,(0,0)],
                ["img\\betty\\vet smug.png",-1,(0,0)],
                ["img\\betty\\KidBetty.webp",-1,(0,0)]]
bettymouths = [["img\\betty\mouth\mouth0.png",
                "img\\betty\mouth\mouth1.png",
                "img\\betty\mouth\mouth2.png",
                "img\\betty\mouth\mouth3.png"],
                ["img\\betty\mouth\mouth0.png",
                 "img\\betty\mouth\drunkmouth1.png",
                 "img\\betty\mouth\drunkmouth2.png"]]
@bot.command()
async def betty(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,bettySprites,asset,8,"Betty",(94,232,51),message,340)
@bot.command()
async def bettygif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,bettySprites,asset,8,"Betty",(94,232,51),message,340)
@bot.command()
async def bettytalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,bettySpritesTest,bettymouths,asset,8,"Betty",(94,232,51),message,340)

dealSprites = ["img\deal\Deal.png",
               "img\deal\DealClosedEyes.png",
               "img\deal\dealOld.png"]
dealSpritesTest = [["img\deal\Deal.png",0,(26,85)],
               ["img\deal\DealClosedEyes.png",0,(26,85)],
               ["img\deal\dealOld.png",-1,(0,0)]]
dealmouth = [["img\deal\mouth\mouth0.png",
              "img\deal\mouth\mouth1.png",
              "img\deal\mouth\mouth2.png",
              "img\deal\mouth\mouth1.png"]]
@bot.command()
async def deal(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,dealSprites,asset,1,"Deal",(204,255,112),message,388)
@bot.command()
async def dealgif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,dealSprites,asset,1,"Deal",(204,255,112),message,388)
@bot.command()
async def dealtalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,dealSpritesTest,dealmouth,asset,1,"Deal",(204,255,112),message,388)

taylorSprites = ["img\\taylor\\Taylor.png"]
@bot.command()
async def taylor(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,taylorSprites,asset,0,"Taylor",(241,173,188),message,210)
@bot.command()
async def taylorgif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,taylorSprites,asset,0,"Taylor",(241,173,188),message,210)
@bot.command()
async def taylortalkf(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,taylorSprites,asset,0,"Taylor",(241,173,188),message,210)

virgilioSprites = ["img\\virgilio\\Virgilio.png",
                   "img\\virgilio\\VirgilioSmug.png",
                   "img\\virgilio\\VirgilioThinking.png",
                   "img\\virgilio\\VirgilioThinking.png",
                   "img\\virgilio\\armandio.png"]
virgilioSpritesTest = [["img\\virgilio\\Virgilio.png",0,(90,95)],
                   ["img\\virgilio\\VirgilioSmug.png",0,(90,95)],
                   ["img\\virgilio\\VirgilioThinking.png",0,(90,94)],
                   ["img\\virgilio\\armandio.png",-1,(0,0)]]
virgiliomouths = [["img\\virgilio\mouth\mouth0.png",
                   "img\\virgilio\mouth\mouth1.png",
                   "img\\virgilio\mouth\mouth2.png",
                   "img\\virgilio\mouth\mouth3.png"]]
@bot.command()
async def virgilio(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,virgilioSprites,asset,1,"Virgilio",(161,126,180),message,476)
@bot.command()
async def virgiliogif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,virgilioSprites,asset,1,"Virgilio",(161,126,180),message,476)
@bot.command()
async def virgiliotalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,virgilioSpritesTest,virgiliomouths,asset,1,"Virgilio",(161,126,180),message,476)

brianSprites = ["img\\brian\\Brian.png",
                "img\\brian\\BrianEyesClosed.png"]
brianSpritesTest = [["img\\brian\\Brian.png",0,(39,61)],
                ["img\\brian\\BrianEyesClosed.png",0,(39,61)]]
brianMouth = [["img\\brian\mouth\mouth0.png",
               "img\\brian\mouth\mouth1.png",
               "img\\brian\mouth\mouth3.png"]]
@bot.command()
async def brian(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,brianSprites,asset,0,"Brian",(223,191,68),message,396)
@bot.command()
async def briangif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,brianSprites,asset,0,"Brian",(223,191,68),message,396)
@bot.command()
async def briantalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,brianSpritesTest,brianMouth,asset,0,"Brian",(223,191,68),message,396)

cassSprites = ["img\cass\Cass.png",
                "img\cass\CassEyesClosed.png",
                "img\cass\CassFocus.png"]
cassSpritesTest = [["img\cass\Cass.png",0,(108,41)],
                ["img\cass\CassEyesClosed.png",0,(108,41)],
                ["img\cass\CassFocus.png",0,(108,41)]]
cassMouth =[["img\cass\mouth\mouth0.png",
             "img\cass\mouth\mouth1.png",
             "img\cass\mouth\mouth2.png"]]
@bot.command()
async def cass(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,cassSprites,asset,0,"Cass",(168,121,176),message,162)
@bot.command()
async def cassgif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,cassSprites,asset,0,"Cass",(168,121,176),message,162)
@bot.command()
async def casstalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,cassSpritesTest,cassMouth,asset,0,"Cass",(168,121,176),message,162)

radShibaSprites = ["img\dogs\RadShiba.png"]
radShibaSpritesTest = [["img\dogs\RadShiba.png",0,(33,60)]]
radshibaMouths = [["img\dogs\mouths\Shibamouth0.png",
                   "img\dogs\mouths\Shibamouth1.png"]]
@bot.command()
async def radshiba(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,radShibaSprites,asset,0,"Rad Shiba",(242,242,92),message,222)
@bot.command()
async def radshibagif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,radShibaSprites,asset,0,"Rad Shiba",(242,242,92),message,222)
@bot.command()
async def radshibatalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,radShibaSpritesTest,radshibaMouths,asset,0,"Rad Shiba",(242,242,92),message,222)

corgiSprites = ["img\dogs\corgi.png"]
corgiSpritesTest = [["img\dogs\corgi.png",-1,(0,0)]]
@bot.command()
async def corgi(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,corgiSprites,asset,0,"Corgi",(242,242,92),message,222)
@bot.command()
async def corgigif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,corgiSprites,asset,0,"Corgi",(242,242,92),message,222)
@bot.command()
async def corgitalk(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,corgiSpritesTest,[],asset,0,"Corgi",(242,242,92),message,222)

normaSprites = ["img\\norma\\Norma.png",
                "img\\norma\\NormaEyesClosed.png"]
normaSpritesTest = [["img\\norma\\Norma.png",0,(43,77)],
                ["img\\norma\\NormaEyesClosed.png",0,(43,77)]]
normaMouth = [["img\\norma\mouth\mouth0.png",
               "img\\norma\mouth\mouth1.png",
               "img\\norma\mouth\mouth2.png"]]
@bot.command()
async def norma(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,normaSprites,asset,0,"Norma",(247,14,141),message,336)
@bot.command()
async def normagif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,normaSprites,asset,0,"Norma",(247,14,141),message,336)
@bot.command()
async def normatalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,normaSpritesTest,normaMouth,asset,0,"Norma",(247,14,141),message,336)

gabbySprites = ["img\gabby\Gabby.png",
                "img\gabby\GabbyAngry.png",
                "img\gabby\GabbyAngryCry.png",
                "img\gabby\GabbyCry.png",
                "img\gabby\GabbyEyesClosed.png",
                "img\gabby\GabbyLookAway.png",
                "img\gabby\GabbyMoreAngry.png",
                "img\gabby\GabbySmile.png"]
gabbySpritesTest = [["img\gabby\Gabby.png",0,(66,73)],
                ["img\gabby\GabbyAngry.png",0,(65,73)],
                ["img\gabby\GabbyAngryCry.png",0,(66,73)],
                ["img\gabby\GabbyCry.png",0,(66,73)],
                ["img\gabby\GabbyEyesClosed.png",0,(66,73)],
                ["img\gabby\GabbyLookAway.png",0,(68,73)],
                ["img\gabby\GabbyMoreAngry.png",0,(66,73)],
                ["img\gabby\GabbySmile.png",0,(68,73)]]
gabbyMouth = [["img\gabby\mouth\mouth0.png",
               "img\gabby\mouth\mouth1.png",
               "img\gabby\mouth\mouth2.png",
               "img\gabby\mouth\mouth3.png"]]
@bot.command()
async def gabby(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,gabbySprites,asset,0,"Gabby",(148,101,117),message,354)
@bot.command()
async def gabbygif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,gabbySprites,asset,0,"Gabby",(148,101,117),message,354)
@bot.command()
async def gabbytalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,gabbySpritesTest,gabbyMouth,asset,0,"Gabby",(148,101,117),message,354)

nachoSprites = ["img\dogs\\Nacho.png"]
nachoSpritesTest = [["img\dogs\\Nacho.png",0,(34,60)]]
@bot.command()
async def nacho(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,nachoSprites,asset,0,"Nacho",(155,87,110),message,222)
@bot.command()
async def nachogif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,nachoSprites,asset,0,"Nacho",(155,87,110),message,222)
@bot.command()
async def nachotalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,nachoSpritesTest,radshibaMouths,asset,0,"Nacho",(155,87,110),message,222)

vellaSprites = ["img\\vella\\Vella.png",
                "img\\vella\\VellaEyesClosed.png"]
vellaSpritesTest = [["img\\vella\\Vella.png",0,(87,77)],
                ["img\\vella\\VellaEyesClosed.png",0,(87,77)]]
vellamouths = [["img\\vella\mouth\mouth0.png",
                "img\\vella\mouth\mouth1.png",
                "img\\vella\mouth\mouth2.png"]]
@bot.command()
async def vella(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,vellaSprites,asset,0,"\"Vella\"",(240,194,196),message,388)
@bot.command()
async def vellagif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,vellaSprites,asset,0,"\"Vella\"",(240,194,196),message,388)
@bot.command()
async def vellatalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,vellaSpritesTest,vellamouths,asset,0,"\"Vella\"",(240,194,196),message,388)

essentiaSprites = ["img\essentia\Essentia.png",
                "img\essentia\EssentiaEyesClosed.png"]
essentiaSpritesTest = [["img\essentia\Essentia.png",0,(16,69)],
                ["img\essentia\EssentiaEyesClosed.png",0,(16,69)]]
essentiaMouth = [["img\essentia\mouth\mouth0.png",
                  "img\essentia\mouth\mouth1.png",
                  "img\essentia\mouth\mouth2.png"]]
@bot.command()
async def essentia(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,essentiaSprites,asset,0,"Essentia",(180,198,160),message,372)
@bot.command()
async def essentiagif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,essentiaSprites,asset,0,"Essentia",(180,198,160),message,372)
@bot.command()
async def essentiatalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,essentiaSpritesTest,essentiaMouth,asset,0,"Essentia",(180,198,160),message,372)

lexiSprites = ["img\lexi\Lexi.png",
                "img\lexi\LexiEyesClosed.png"]
lexiSpritesTest = [["img\lexi\Lexi.png",0,(77,88)],
                ["img\lexi\LexiEyesClosed.png",0,(77,88)]]
leximouths = [["img\lexi\mouth\mouth0.png",
               "img\lexi\mouth\mouth1.png",
               "img\lexi\mouth\mouth2.png"]]
@bot.command()
async def lexi(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,lexiSprites,asset,0,"Lexi",(65,170,228),message,370)
@bot.command()
async def lexigif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,lexiSprites,asset,0,"Lexi",(65,170,228),message,370)
@bot.command()
async def lexitalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,lexiSpritesTest,leximouths,asset,0,"Lexi",(65,170,228),message,370)

tomcatSprites = ["img\\tomcat\\TOMCAT.png",
                "img\\tomcat\\TOMCATeyesClosed.png"]
tomcatSpritesTest = [["img\\tomcat\\TOMCAT.png",0,(58,102)],
                ["img\\tomcat\\TOMCATeyesClosed.png",0,(58,102)]]
tomcatMouth = [["img\\tomcat\mouth\mouth0.png",
                "img\\tomcat\mouth\mouth1.png",
                "img\\tomcat\mouth\mouth2.png"]]
@bot.command()
async def tomcat(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,tomcatSprites,asset,0,"TOMCAT",(248,242,194),message,418)
@bot.command()
async def tomcatgif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,tomcatSprites,asset,0,"TOMCAT",(248,242,194),message,418)
@bot.command()
async def tomcattalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,tomcatSpritesTest,tomcatMouth,asset,0,"TOMCAT",(248,242,194),message,418)

jessSprites = ["img\jess\Jess.png",
                "img\jess\JessEyesClosed.png"]
jessSpritesTest = [["img\jess\Jess.png",0,(74,114)],
                ["img\jess\JessEyesClosed.png",0,(74,84)]]
jessmouth = [["img\jess\mouth\mouth0.png",
              "img\jess\mouth\mouth1.png",
              "img\jess\mouth\mouth2.png"]]
@bot.command()
async def jess(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,jessSprites,asset,0,"Jess",(238,105,124),message,428)
@bot.command()
async def jessgif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,jessSprites,asset,0,"Jess",(238,105,124),message,428)
@bot.command()
async def jesstalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,jessSpritesTest,jessmouth,asset,0,"Jess",(238,105,124),message,428)

annaSprites = ["img\\anna\\Anna.png",
                "img\\anna\\AnnaGlitch1.png",
                "img\\anna\\AnnaGlitch2.png",
                "img\\anna\\AnnaGlitch3.png",
                "img\\anna\\AnnaGlitch4.png",
                "img\\anna\\AnnaGlitch5.png",
                "img\\anna\\AnnaHappy.png",
                "img\\anna\\AnnaSmile.png",
                "img\\anna\\AnnaThinking.png",
                "img\\anna\\AnnaOld.png"]
annaSpritesTest = [["img\\anna\\Anna.png",0,(41,80)],
                ["img\\anna\\AnnaGlitch1.png",-1,(41,80)],
                ["img\\anna\\AnnaGlitch2.png",-1,(41,80)],
                ["img\\anna\\AnnaGlitch3.png",-1,(41,80)],
                ["img\\anna\\AnnaGlitch4.png",-1,(41,80)],
                ["img\\anna\\AnnaGlitch5.png",-1,(41,80)],
                ["img\\anna\\AnnaHappy.png",0,(41,80)],
                ["img\\anna\\AnnaSmile.png",0,(41,80)],
                ["img\\anna\\AnnaThinking.png",0,(41,80)],
                ["img\\anna\\AnnaOld.png",-1,(41,80)]]
annamouth=[["img\\anna\mouth\mouth0.png",
            "img\\anna\mouth\mouth1.png",
            "img\\anna\mouth\mouth2.png"]]
@bot.command()
async def anna(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,annaSprites,asset,1,"Anna",(255,255,255),message,370)
@bot.command()
async def annagif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,annaSprites,asset,1,"Anna",(255,255,255),message,370)
@bot.command()
async def annatalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,annaSpritesTest,annamouth,asset,1,"Anna",(255,255,255),message,370)

marioSprites = ["img\mario\Mario.png",
                "img\mario\MarioHappy.png",
                "img\mario\MarioSad.png",
                "img\mario\MarioSadder.png",
                "img\mario\MarioSatisfied.png",
                "img\mario\MarioSurprise.png",
                "img\mario\MarioWorry.png"]
marioSpritesTest = [["img\mario\Mario.png",0,(82,85)],
                ["img\mario\MarioHappy.png",0,(82,85)],
                ["img\mario\MarioSad.png",0,(82,86)],
                ["img\mario\MarioSadder.png",0,(82,85)],
                ["img\mario\MarioSatisfied.png",0,(82,84)],
                ["img\mario\MarioSurprise.png",0,(82,85)],
                ["img\mario\MarioWorry.png",0,(82,86)]]
marioMouth= [["img\mario\mouth\mouth0.png",
              "img\mario\mouth\mouth1.png",
              "img\mario\mouth\mouth2.png"]]
@bot.command()
async def mario(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,marioSprites,asset,0,"Mario",(173,3,50),message,454)
@bot.command()
async def mariogif(ctx,asset,*,message=""):
    await drawCharacterByCommandGif(ctx,marioSprites,asset,0,"Mario",(173,3,50),message,454)
@bot.command()
async def mariotalk(ctx,asset,*,message=""):
    await drawCharacterByCommandTalk(ctx,marioSpritesTest,marioMouth,asset,0,"Mario",(173,3,50),message,454)

@bot.command()
async def beer(ctx,character:str,*,message=""):
    if(character.lower()=="jill"):
        charID=1
    elif(character.lower()=="dana"):
        charID=2
    else:
        await ctx.send("The first argument must be Jill or Dana")
        return
    
    file = discord.File(drawInstan.drawBeerScene(charID,message), filename="Beer.jpeg")
    await ctx.send(file=file)

@bot.command()
async def beertalk(ctx,*,message=""):
    if message=="":
       await ctx.send("Data must be given for this command to work")
       return 
    
    arguments = message.split('//')
    if(len(arguments)<=1):
        await ctx.send("There has to be at least one argument")
        return
    elif(len(arguments)>=12):
        await ctx.send("Can't have more than 10 arguments")
        return

    errors = []
    result = []
    i = 0
    for arg in arguments:
        i+=1
        charData = arg.split(';')
        if(len(charData)<=1 or len(charData)>2):
            errors.append("Error in argument "+ str(i))
            continue
        
        if (charData[0].lower()=="jill"):
            charID=1
        elif(charData[0].lower()=="dana"):
            charID=2
        else:
            errors.append("The first argument must be Jill or Dana in argument " + str(i))
            continue

        result.append(drawInstan.drawBeerScene(charID,charData[1])) 
        
    
    for err in errors:
        await ctx.send(err)

    files = []
    for res in result:
        files.append(discord.File(res, filename="Beer.jpeg"))

    await ctx.send(files=files)

characters = {
                "jill" : ["Jill",jillSprites,(105,129,193),1,364],
                "gill" : ["Gill",gillSprites,(124,44,179),0,422],
                "dana" : ["Dana",danaSprites,(199,33,35),4,414],
                "donovan" : ["Mr. Donovan",donovanSprites,(167,75,86),0,412],
                "sei" : ["Sei",seiSprites,(92,167,172),2,384],
                "kim" : ["Kim",kimSprites,(193,124,207),0,382],
                "dorothy" : ["Dorothy",dorothySprites,(245,11,158),10,314],
                "jamie" : ["Jamie",jamieSprites,(162,120,52),2,438],
                "kiramiki" : ["*Kira* Miki",kiramikiSprites,(47,106,150),2,388],
                "alma" : ["Alma",almaSprites,(248,190,65),4,418],
                "stella" : ["Stella",stellaSprites,(243,49,197),2,356],
                "art" : ["Art",artSprites,(201,201,201),1,356],
                "nicole" : ["Streaming-chan",nicoleSprites,(76,174,211),0,432],
                "betty" : ["Betty",bettySprites,(94,232,51),8,340],
                "deal" : ["Deal",dealSprites,(204,255,112),1,388],
                "taylor" : ["Taylor",taylorSprites,(241,173,188),0,210],
                "virgilio" : ["Virgilio",virgilioSprites,(161,126,180),1,476],
                "brian" : ["Brian",brianSprites,(223,191,68),0,396],
                "cass" : ["Cass",cassSprites,(168,121,176),0,162],
                "radshiba" : ["Rad Shiba",radShibaSprites,(242,242,92),0,222],
                "corgi" : ["Corgia",corgiSprites,(242,242,92),0,222],
                "norma" : ["Norma",normaSprites,(247,14,141),0,336],
                "gabby" : ["Gabby",gabbySprites,(148,101,117),0,354],
                "nacho" : ["Nacho",nachoSprites,(155,87,110),0,222],
                "vella" : ["\"Vella\"",vellaSprites,(240,194,196),0,388],
                "essentia" : ["Essentia",essentiaSprites,(180,198,160),0,372],
                "lexi" : ["Lexi",lexiSprites,(65,170,228),0,370],
                "tomcat" : ["TOMCAT",tomcatSprites,(248,242,194),0,418],
                "jess" : ["Jess",jessSprites,(238,105,124),0,428],
                "anna" : ["Anna",annaSprites,(255,255,255),1,370],
                "mario" : ["Mario",marioSprites,(173,3,50),0,454],
            }

@bot.command()
async def conversation(ctx,*,message=""):
    if message=="":
        await ctx.send("Data must be given for this command to work")
        return
    arguments = message.split('//')
    if(len(arguments)>=15):
        await ctx.send("Can't have more than 150 arguments")
        return

    errors = []
    result = []
    i = 0
    for arg in arguments:
        i+=1
        charData = arg.split(';')
        if(len(charData)<=1 or len(charData)>3):
            errors.append("Error in argument "+ str(i))
            continue

        if charData[0].lower() in characters:
            charInfo = characters.get(charData[0].lower())
            if(len(charData)==3):
                messagePost=2
                spriteID=int(charData[1])
                if(spriteID>len(charInfo[1]) or spriteID<=0):
                    errors.append("Sprite selector has to be between 1 and "+ str(len(charInfo[1]))+" in argument "+ str(i))
                    spriteID=random.randint(1,len(charInfo[1])-int(charInfo[3]))
                
            else:
                messagePost=1
                print(charData[0].lower())
                spriteID=random.randint(1,len(charInfo[1])-int(charInfo[3]))
            
            result.append(discord.File(drawInstan.drawCharacterTalk(charInfo[0],charInfo[2],charInfo[1][spriteID-1],charData[messagePost],charInfo[4]), filename="Drink.jpeg"))
        else:
            errors.append("Character not found in argument "+ str(i))
            continue

    for err in errors:
        await ctx.send(err)

    await ctx.send(files=result)

@bot.command()
async def conversation2(ctx,*,message=""):
    if message=="":
        await ctx.send("Data must be given for this command to work")
        return
    arguments = message.split('//')
    if(len(arguments)>=15):
        await ctx.send("Can't have more than 150 arguments")
        return

    errors = []
    result = []
    i = 0
    for arg in arguments:
        i+=1
        charData = arg.split(';')
        if(len(charData)<=1 or len(charData)>3):
            errors.append("Error in argument "+ str(i))
            continue

        if charData[0].lower() in characters:
            charInfo = characters.get(charData[0].lower())
            if(len(charData)==3):
                messagePost=2
                spriteID=int(charData[1])
                if(spriteID>len(charInfo[1]) or spriteID<=0):
                    errors.append("Sprite selector has to be between 1 and "+ str(len(charInfo[1]))+" in argument "+ str(i))
                    spriteID=random.randint(1,len(charInfo[1])-int(charInfo[3]))
                
            else:
                messagePost=1
                print(charData[0].lower())
                spriteID=random.randint(1,len(charInfo[1])-int(charInfo[3]))
            
            result.append(discord.File(drawInstan.drawCharacterTalk(charInfo[0],charInfo[2],charInfo[1][spriteID-1],charData[messagePost],charInfo[4]), filename="Drink.jpeg"))
        else:
            errors.append("Character not found in argument "+ str(i))
            continue

    for err in errors:
        await ctx.send(err)

    for file in result:
        await ctx.send(file=file)

@bot.command()
async def conversation3(ctx,*,message=""):
    
    if message=="":
        await ctx.send("Data must be given for this command to work")
        return
    arguments = message.split('//')
    if(len(arguments)>=15):
        await ctx.send("Can't have more than 150 arguments")
        return

    errors = []
    result = []
    i = 0
    for arg in arguments:
        i+=1
        charData = arg.split(';')
        if(len(charData)<=1 or len(charData)>3):
            errors.append("Error in argument "+ str(i))
            continue

        if charData[0].lower() in characters:
            charInfo = characters.get(charData[0].lower())
            if(len(charData)==3):
                messagePost=2
                spriteID=int(charData[1])
                if(spriteID>len(charInfo[1]) or spriteID<=0):
                    errors.append("Sprite selector has to be between 1 and "+ str(len(charInfo[1]))+" in argument "+ str(i))
                    spriteID=random.randint(1,len(charInfo[1])-int(charInfo[3]))
                
            else:
                messagePost=1
                print(charData[0].lower())
                spriteID=random.randint(1,len(charInfo[1])-int(charInfo[3]))
            
            result.append(drawInstan.drawCharacterTalk(charInfo[0],charInfo[2],charInfo[1][spriteID-1],charData[messagePost],charInfo[4]))
        else:
            errors.append("Character not found in argument "+ str(i))
            continue

    for err in errors:
        await ctx.send(err)

    frames = []
    for file in result:
        frames.append(Image.open(file))

    frames[0].save("img\generatedChat\conversation.gif", format="GIF", append_images=frames[1:],save_all=True, duration=2000, loop=0)
    discFile=discord.File("img\generatedChat\conversation.gif", filename="Conversation.gif")
    await ctx.send(file=discFile)

@bot.command()
async def conversationgif(ctx,*,message=""):
    
    if message=="":
        await ctx.send("Data must be given for this command to work")
        return
    arguments = message.split('//')
    if(len(arguments)>=15):
        await ctx.send("Can't have more than 15 arguments")
        return

    errors = []
    result = []
    i = 0
    for arg in arguments:
        i+=1
        charData = arg.split(';')
        if(len(charData)<=1 or len(charData)>3):
            errors.append("Error in argument "+ str(i))
            continue

        if charData[0].lower() in characters:
            charInfo = characters.get(charData[0].lower())
            if(len(charData)==3):
                messagePost=2
                spriteID=int(charData[1])
                if(spriteID>len(charInfo[1]) or spriteID<=0):
                    errors.append("Sprite selector has to be between 1 and "+ str(len(charInfo[1]))+" in argument "+ str(i))
                    spriteID=random.randint(1,len(charInfo[1])-int(charInfo[3]))
                
            else:
                messagePost=1
                print(charData[0].lower())
                spriteID=random.randint(1,len(charInfo[1])-int(charInfo[3]))
            
            result.append(drawInstan.drawCharacterGif(charInfo[0],charInfo[2],charInfo[1][spriteID-1],charData[messagePost],charInfo[4]))
        else:
            errors.append("Character not found in argument "+ str(i))
            continue

    for err in errors:
        await ctx.send(err)

    frames = []
    for file in result:
        frames.append(Image.open(file))

    frames[0].save("img\generatedChat\conversation.gif", format="GIF", append_images=frames[1:],save_all=True, duration=50, loop=0)
    discFile=discord.File("img\generatedChat\conversation.gif", filename="Conversation.gif")
    await ctx.send(file=discFile)

@bot.command()
async def help(ctx):
    await ctx.send('&drink [id or name] - Shows info about the drink \n &rand - Shows info about a random drink \n &beer [jill or dana] message - Generates the scene when Jill and Dana are drinking on Jill\'s home \n &jill [sprite_id optional] text - Generates a image with the given text, without sprite id, the sprite is random \n Character aviable: &anna, &art, &betty, &brian, &cass, &dana, &deal,&radshiba, &nacho, &donovan, &dorothy, &essentia, &gabby, &gill, &ingram, &jamie, &jess, &jill, &kim, &kiramiki, &lexi, &mario, &nicole, &norma, &sei, &stella, &taylor, &tomcat, &vella, &virgilio \n Some characters have secret sprites that can\'t appear randomly \n Add gif after a character name to see a funky effect. Ex: &jill -> &jillgif')

@bot.command()
async def sdown(ctx):
    await ctx.send('Killing bot')
    exit()

bot.run(TOKEN)