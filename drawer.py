import os
import textwrap
import re
import random
from PIL import Image, ImageFont, ImageDraw, ImageOps
from db import Database
import time

fontIn = ImageFont.truetype("fonts/va-11-hall-a-cyr-10px.ttf", 28)
fontInSmall = ImageFont.truetype("fonts/va-11-hall-a-cyr-10px.ttf", 20)

class Drawer():
    def drawDrink(self,drinkdata):
        with Image.open("img/BackGround.jpg") as im:
            d1 = ImageDraw.Draw(im)
            d1.text((70, 105), drinkdata[0]+" - $"+str(drinkdata[2]), (255, 255, 255), fontIn)
            d1.text((376, 175), drinkdata[11], (255, 255, 255), fontIn)
            desc = drinkdata[1]
            lines = textwrap.wrap(desc, width=37)
            y_text =330
            for line in lines:
                d1.text((70, y_text), line, (255, 255, 255), fontIn)
                y_text += 30 

            i=0
            for line in drinkdata[15]:
                d1.text((376, 212+36*i), line, (255, 255, 255), fontIn)
                i += 1 


        # resize image to fit  288, 175
        # image center should be in 370, 237
            with Image.open("img/drinks/"+drinkdata[12]) as imdrink:
                imdrink = ImageOps.contain(imdrink, (288, 175))
                width, height = imdrink.size
                posx = 214-round((width/2))
                posy = 237-round((height/2))
                im.paste(imdrink, (posx, posy), imdrink)

            ice=drinkdata[9]
            if(ice==1):
                with Image.open("img\Ice.jpg") as imIce:
                    im.paste(imIce, (724, 246))

            aged=drinkdata[8]
            if(aged==1):
                with Image.open("img\Age.jpg") as imAge:
                    im.paste(imAge, (724, 366))

            blend=drinkdata[10]
            if(blend==1):
                with Image.open("img\Blend.jpg") as imBlend:
                    im.paste(imBlend, (954, 366))
                    d1.text((962, 506), "Blended", (255, 255, 255), fontInSmall)
                    

            
            adel=drinkdata[3]
            fila=0
            columna=0
            i=0
            with Image.open("img\Adel10Plus.jpg") as imAdelPlus, Image.open("img\Adel.jpg") as imAdel:
                while adel>0 and i<10:
                    if adel>10:
                        im.paste(imAdelPlus, (856+18*columna, 280+36*fila))
                    else:
                        im.paste(imAdel, (856+18*columna, 280+36*fila))

                    columna+=1
                    if columna==5:
                        columna=0
                        fila=1
                    i+=1
                    adel-=1
            
            bron=drinkdata[4]
            fila=0
            columna=0
            i=0
            with Image.open("img\Bron10Plus.jpg") as imBronPlus, Image.open("img\Bron.jpg") as imBron:
                while bron>0 and i<10:
                    if bron>10:
                        im.paste(imBronPlus, (1006+18*columna, 280+36*fila))
                    else:
                        im.paste(imBron, (1006+18*columna, 280+36*fila))

                    columna+=1
                    if columna==5:
                        columna=0
                        fila=1
                    i+=1
                    bron-=1
            
            powdD=drinkdata[5]
            fila=0
            columna=0
            i=0
            with Image.open("img\PwdD10Plus.jpg") as imPwdDplus, Image.open("img\PwdD.jpg") as imPwdD:
                while powdD>0 and i<10:
                    if powdD>10:
                        im.paste(imPwdDplus, (1156+18*columna, 280+36*fila))
                    else:
                        im.paste(imPwdD, (1156+18*columna, 280+36*fila))

                    columna+=1
                    if columna==5:
                        columna=0
                        fila=1
                    i+=1
                    powdD-=1

            flan=drinkdata[6]
            fila=0
            columna=0
            i=0
            with Image.open("img\Flan10Plus.jpg") as imFlanPlus, Image.open("img\Flan.jpg") as imFlan:
                while flan>0 and i<10:
                    if flan>10:
                        im.paste(imFlanPlus, (856+18*columna, 400+36*fila))
                    else:
                        im.paste(imFlan, (856+18*columna, 400+36*fila))

                    columna+=1
                    if columna==5:
                        columna=0
                        fila=1
                    i+=1
                    flan-=1
            
            print(drinkdata[7])
            karmo=(drinkdata[7],30)[drinkdata[7]>20]
            fila=0
            columna=0
            i=0
            with Image.open("img\Karmo10Plus.jpg") as imKarmoPlus, Image.open("img\Karmo.jpg") as imKarmo, Image.open("img\KarmoQuestion.jpg") as imKarmQuest:
                while karmo>0 and i<10:
                    if karmo>20:
                        im.paste(imKarmQuest, (1156+18*columna, 400+36*fila))
                    elif karmo>10:
                        im.paste(imKarmoPlus, (1156+18*columna, 400+36*fila))
                    else:
                        im.paste(imKarmo, (1156+18*columna, 400+36*fila))

                    columna+=1
                    if columna==5:
                        columna=0
                        fila=1
                    i+=1
                    karmo-=1

            #im.show()
            ts = time.time()
            img_path = "img/generated/"+str(drinkdata[14])+"_"+str(ts)+".jpeg"
            im.save(img_path, subsampling=0, quality=95)
            return img_path

    def drawCharacterTalk(self,charName:str,charColor,charPath:str, message:str,charHeight:int=430):
        finalMessage= charName + ": " + message
        finalMessage = finalMessage[0:200]
        lines = textwrap.wrap(finalMessage, width=50)
        with Image.open("img/BackGroundChat.jpg") as im:
            d1 = ImageDraw.Draw(im)
            y_text =556
            for line in lines:
                d1.text((46, y_text), line, (255, 255, 255), fontIn)
                y_text += 30 
            d1.text((46,556),charName+":",charColor,fontIn)
            d1.text((880,566),"Generated with ",(255, 255, 255),fontIn)
            d1.text((880,596),"CalicompBot",(255, 255, 255),fontIn)
            with Image.open(charPath) as imChar:
                imChar = ImageOps.contain(imChar, (660, charHeight),Image.BOX)
                width, height = imChar.size
                posx = 369-round((width/2))
                posy = 536-round(height)
                im.paste(imChar, (posx, posy), imChar)

            ts = time.time()
            imgPath = "img/generatedChat/Gen"+str(ts)+"-"+str(random.randint(0,9999))+".jpeg"
            im.save(imgPath,format='JPEG', subsampling=0, quality=95)
            return (imgPath)
    
    def drawCharacterGif(self,charName:str,charColor,charPath:str, message:str,charHeight:int=430):
        maxtextLength = 200 - len(charName+": ")
        if(len(message)>maxtextLength):
            message = message[0:maxtextLength]
        else:
            maxtextLength = len(message)
        generatedImages = []
        i=0
        while i <= maxtextLength:
            i+=1
            finalMessage= charName + ": " + message[0:i]
            finalMessage = finalMessage[0:200]
            lines = textwrap.wrap(finalMessage, width=50)
            with Image.open("img/BackGroundChat.jpg") as im:
                d1 = ImageDraw.Draw(im)
                y_text =556
                for line in lines:
                    d1.text((46, y_text), line, (255, 255, 255), fontIn)
                    y_text += 30 
                d1.text((46,556),charName+":",charColor,fontIn)
                d1.text((880,566),"Generated with ",(255, 255, 255),fontIn)
                d1.text((880,596),"CalicompBot",(255, 255, 255),fontIn)
                with Image.open(charPath) as imChar:
                    imChar = ImageOps.contain(imChar, (660, charHeight),Image.BOX)
                    width, height = imChar.size
                    posx = 369-round((width/2))
                    posy = 536-round(height)
                    im.paste(imChar, (posx, posy), imChar)

                generatedImages.append(im)
                if(i==maxtextLength):
                    for x in range(50):
                        generatedImages.append(im)


        ts = time.time()
        imgPath = "img/generatedChat/Gen"+str(ts)+"-"+str(random.randint(0,9999))+".gif"
        generatedImages[0].save(imgPath, format="GIF", append_images=generatedImages[1:],save_all=True, duration=50, loop=0)
        return (imgPath)
        
    def drawBeerScene(self,charId,message):
        if(charId==1):
            name = "Jill: "
            charColor = (105,129,193)
        else:
            name = "Dana: "
            charColor = (199,33,35)

        message = name + message
        with Image.open("img\BackGroundBeer.jpg") as im:
            d1 = ImageDraw.Draw(im)
            lines = textwrap.wrap(message, width=46)
            yheigh = 490
            for line in lines:
                d1.text((96, yheigh), line, (255, 255, 255), fontIn)
                yheigh += 30 
            
            d1.text((96,490),name,charColor,fontIn)
            d1.text((80,650),"Generated with CalicomBot",(255, 255, 255),fontIn)
            ts = time.time()
            imgPath = "img/generatedBeer/Gen"+str(ts)+"-"+str(random.randint(0,9999))+".jpeg"
            im.save(imgPath,format='JPEG', subsampling=0, quality=95)
            return (imgPath)

    #Gets the path of the image with a drink id
    def getImagePath(self,dbConnection:Database,drink_ID:int):
        searchID =  dbConnection.verifyDrinkId(drink_ID)
        for file in os.listdir("img/generated"):
            fileData= re.split(r'[_.]',file)
            if int(fileData[0])==searchID:
                print("File found\n")
                if dbConnection.checkIfUpdated(searchID,fileData[1]):
                    print("Drink updated, must generate new file ")
                    os.remove("img/generated/"+file)
                    return self.drawDrink(dbConnection.get_Drink(searchID))
                else:
                    print("Drink not updated, can use generated file")
                    return("img/generated/"+file)
        
        print("File doesn't exist. Must create a new one")
        return self.drawDrink(dbConnection.get_Drink(searchID))

#drawInstance = Drawer()
#drawInstance.drawCharacterTalk("Jill",(104,129,196),"test","Why are there so many cirno fumos here")