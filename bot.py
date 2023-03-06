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

intents = discord.Intents(33280)
activity = discord.Game(name="&help")
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
    await drawCharacterByCommand(ctx,jillSprites,asset,1,"Jill",(105,129,193),message,364)

gillSprites = ["img\gill\Gill.png",
               "img\gill\GillFuckboy.png",
               "img\gill\Gill0_0.png",
               "img\gill\GillFocus.png",
               "img\gill\GillSad.png"]
@bot.command()
async def gill(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,gillSprites,asset,0,"Gillian",(124,44,179),message,422)

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
@bot.command()
async def dana(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,danaSprites,asset,4,"Dana",(199,33,35),message,414)

donovanSprites = ["img\donovan\Donovan.png",
                  "img\donovan\DonovanHappy.png",
                  "img\donovan\DonovanLaugh.png"]
@bot.command()
async def donovan(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,donovanSprites,asset,0,"Mr. Donovan",(167,75,86),message,412)

ingramSprites = ["img\ingram\Ingram.png",
                 "img\ingram\IngramEyesClosed.png"]
@bot.command()
async def ingram(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,ingramSprites,asset,0,"Ingram",(208,59,37),message,406)

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
@bot.command()
async def sei(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,seiSprites,asset,2,"Sei",(92,167,172),message,384)

kimSprites = ["img\kim\Kim.png",
              "img\kim\KimAngry.png",
              "img\kim\KimCry.png",
              "img\kim\KimMURDERMURDER.png"]
@bot.command()
async def kim(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,kimSprites,asset,0,"Kim",(193,124,207),message,382)

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
@bot.command()
async def dorothy(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,dorothySprites,asset,10,"Dorothy",(245,11,158),message,314)

jamieSprites = ["img\jamie\Jamie.png",
                "img\jamie\JamieThinking.png",
                "img\jamie\JamieThinkingHarder.png",
                "img\jamie\JamieWorried.png",
                "img\jamie\jamieOld.png",
                "img\jamie\jamie detail.png"]
@bot.command()
async def jamie(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,jamieSprites,asset,2,"Jamie",(162,120,52),message,438)

kiramikiSprites = ["img\kiramiki\KiraMiki.png",
                   "img\kiramiki\KiraMikiAngry.png",
                   "img\kiramiki\KiraMikiSmile.png",
                   "img\kiramiki\KiraMikiStare.png",
                   "img\kiramiki\KiraMikiOld1.png",
                   "img\kiramiki\KiraMikiOld2.png"]
@bot.command()
async def kiramiki(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,kiramikiSprites,asset,2,"*Kira* Miki",(50,114,52),message,388)

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
@bot.command()
async def alma(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,almaSprites,asset,4,"Alma",(248,190,65),message,418)

stellaSprites = ["img\stella\Stella.png",
                 "img\stella\StellaAwooo.png",
                 "img\stella\StellaBlush.png",
                "img\stella\StellaCry.png",
                "img\stella\StellaSmile.png",
                "img\stella\StellaSurprise.png",
                "img\stella\StellaTired.png",
                "img\stella\stellaOld.png",
                "img\stella\KidStella.webp"]
@bot.command()
async def stella(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,stellaSprites,asset,2,"Stella",(243,49,197),message,356)

artSprites = ["img\\artvondelay\\ArtVonDelay.png",
              "img\\artvondelay\\ArtVonDelayEyesClosed.png",
              "img\\artvondelay\\ArtVonDelaySurprised.png",
              "img\\artvondelay\\ArtVonDelayWorried.png",
              "img\\artvondelay\\artOld.png"]
@bot.command()
async def art(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,artSprites,asset,1,"Art",(201,201,201),message,356)

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
    await drawCharacterByCommand(ctx,nicoleSprites,asset,0,"Streaming-chan",(76,174,211),message,432)

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
@bot.command()
async def betty(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,bettySprites,asset,8,"Betty",(94,232,51),message,340)

dealSprites = ["img\deal\Deal.png",
               "img\deal\DealClosedEyes.png",
               "img\deal\dealOld.png"]
@bot.command()
async def deal(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,dealSprites,asset,1,"Deal",(204,255,112),message,388)

taylorSprites = ["img\\taylor\\Taylor.png"]
@bot.command()
async def taylor(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,taylorSprites,asset,0,"Taylor",(241,173,188),message,210)

virgilioSprites = ["img\\virgilio\\Virgilio.png",
                   "img\\virgilio\\VirgilioSmug.png",
                   "img\\virgilio\\VirgilioThinking.png",
                   "img\\virgilio\\VirgilioThinking.png",
                   "img\\virgilio\\armandio.png"]
@bot.command()
async def virgilio(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,virgilioSprites,asset,1,"Virgilio",(161,126,180),message,476)

brianSprites = ["img\\brian\\Brian.png",
                "img\\brian\\BrianEyesClosed.png"]
@bot.command()
async def brian(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,brianSprites,asset,0,"Brian",(223,191,68),message,396)

cassSprites = ["img\cass\Cass.png",
                "img\cass\CassEyesClosed.png",
                "img\cass\CassFocus.png"]
@bot.command()
async def cass(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,cassSprites,asset,0,"Cass",(168,121,176),message,162)

radShibaSprites = ["img\dogs\RadShiba.png"]
@bot.command()
async def radshiba(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,radShibaSprites,asset,0,"Rad Shiba",(242,242,92),message,222)

corgiSprites = ["img\dogs\corgi.png"]
@bot.command()
async def corgi(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,corgiSprites,asset,0,"Corgi",(242,242,92),message,222)

normaSprites = ["img\\norma\\Norma.png",
                "img\\norma\\NormaEyesClosed.png"]
@bot.command()
async def norma(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,normaSprites,asset,0,"Norma",(247,14,141),message,336)

gabbySprites = ["img\gabby\Gabby.png",
                "img\gabby\GabbyAngry.png",
                "img\gabby\GabbyAngryCry.png",
                "img\gabby\GabbyCry.png",
                "img\gabby\GabbyEyesClosed.png",
                "img\gabby\GabbyLookAway.png",
                "img\gabby\GabbyMoreAngry.png",
                "img\gabby\GabbySmile.png"]
@bot.command()
async def gabby(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,gabbySprites,asset,0,"Gabby",(148,101,117),message,354)

nachoSprites = ["img\dogs\\Nacho.png"]
@bot.command()
async def nacho(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,nachoSprites,asset,0,"Nacho",(155,87,110),message,222)

vellaSprites = ["img\\vella\\Vella.png",
                "img\\vella\\VellaEyesClosed.png"]
@bot.command()
async def vella(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,vellaSprites,asset,0,"\"Vella\"",(240,194,196),message,388)

essentiaSprites = ["img\essentia\Essentia.png",
                "img\essentia\EssentiaEyesClosed.png"]
@bot.command()
async def essentia(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,essentiaSprites,asset,0,"Essentia",(180,198,160),message,372)

lexiSprites = ["img\lexi\Lexi.png",
                "img\lexi\LexiEyesClosed.png"]
@bot.command()
async def lexi(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,lexiSprites,asset,0,"Lexi",(65,170,228),message,370)

tomcatSprites = ["img\\tomcat\\TOMCAT.png",
                "img\\tomcat\\TOMCATeyesClosed.png"]
@bot.command()
async def tomcat(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,tomcatSprites,asset,0,"TOMCAT",(248,242,194),message,418)

jessSprites = ["img\jess\Jess.png",
                "img\jess\JessEyesClosed.png"]
@bot.command()
async def jess(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,jessSprites,asset,0,"Jess",(238,105,124),message,428)

annaSprites = ["img\\anna\\Anna.png",
                "img\\anna\AnnaGlitch1.png",
                "img\\anna\AnnaGlitch2.png",
                "img\\anna\AnnaGlitch3.png",
                "img\\anna\AnnaGlitch4.png",
                "img\\anna\AnnaGlitch5.png",
                "img\\anna\\AnnaHappy.png",
                "img\\anna\\AnnaSmile.png",
                "img\\anna\\AnnaThinking.png",
                "img\\anna\\AnnaOld.png"]
@bot.command()
async def anna(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,annaSprites,asset,1,"Anna",(255,255,255),message,370)

marioSprites = ["img\mario\Mario.png",
                "img\mario\MarioHappy.png",
                "img\mario\MarioSad.png",
                "img\mario\MarioSadder.png",
                "img\mario\MarioSatisfied.png",
                "img\mario\MarioSurprise.png",
                "img\mario\MarioWorry.png"]
@bot.command()
async def mario(ctx,asset,*,message=""):
    await drawCharacterByCommand(ctx,marioSprites,asset,0,"Mario",(173,3,50),message,454)

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
        await ctx.send("Debe haber como mínimo un argumento")
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
                "kiramiki" : ["*Kira* Miki",kiramikiSprites,(50,114,52),2,388],
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
async def help(ctx):
    await ctx.send('&drink [id or name] - Shows info about the drink \n &rand - Shows info about a random drink \n &beer [jill or dana] message - Generates the scene when Jill and Dana are drinking on Jill\'s home \n &jill [sprite_id optional] text - Generates a image with the given text, without sprite id, the sprite is random \n Character aviable: &anna, &art, &betty, &brian, &cass, &dana, &deal,&radshiba, &nacho, &donovan, &dorothy, &essentia, &gabby, &gill, &ingram, &jamie, &jess, &jill, &kim, &kiramiki, &lexi, &mario, &nicole, &norma, &sei, &stella, &taylor, &tomcat, &vella, &virgilio \n Some characters have secret sprites that can\'t appear randomly')

@bot.command()
async def sdown(ctx):
    await ctx.send('Killing bot')
    exit()

bot.run(TOKEN)