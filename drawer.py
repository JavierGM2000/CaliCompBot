import os
import textwrap
from PIL import Image, ImageFont, ImageDraw, ImageOps

fontIn = ImageFont.truetype("fonts/va-11-hall-a-cyr-10px.ttf", 28)


def drawDrink(drinkdata):
    with Image.open("img/BackGround.jpg") as im:
        d1 = ImageDraw.Draw(im)
        d1.text((70, 105), "Bad Touch - 250$", (255, 255, 255), fontIn)
        desc = "We are nothing but mamals after all."
        lines = textwrap.wrap(desc, width=37)
        y_text =330
        for line in lines:
            d1.text((70, y_text), line, (255, 255, 255), fontIn)
            y_text += 30    

    # resize image to fit  600, 175
    # image center should be in 370, 237
        with Image.open("img/drinks/Bad_Touch.webp") as imdrink:
            imdrink = ImageOps.contain(imdrink, (600, 175))
            width, height = imdrink.size
            posx = 370-round((width/2))
            posy = 237-round((height/2))
            im.paste(imdrink, (posx, posy), imdrink)

        ice=1
        if(ice==1):
            with Image.open("img\Ice.jpg") as imIce:
                im.paste(imIce, (724, 246))

        aged=0
        if(aged==1):
            with Image.open("img\Age.jpg") as imAge:
                im.paste(imAge, (724, 366))

        adel=0
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
        
        bron=2
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
        
        powdD=2
        fila=0
        columna=0
        i=0
        with Image.open("img\PwdD10Plus.jpg") as imBronPlus, Image.open("img\PwdD.jpg") as imBron:
            while powdD>0 and i<10:
                if powdD>10:
                    im.paste(imBronPlus, (1156+18*columna, 280+36*fila))
                else:
                    im.paste(imBron, (1156+18*columna, 280+36*fila))

                columna+=1
                if columna==5:
                    columna=0
                    fila=1
                i+=1
                powdD-=1

        flan=2
        fila=0
        columna=0
        i=0
        with Image.open("img\Flan10Plus.jpg") as imBronPlus, Image.open("img\Flan.jpg") as imBron:
            while flan>0 and i<10:
                if flan>10:
                    im.paste(imBronPlus, (856+18*columna, 400+36*fila))
                else:
                    im.paste(imBron, (856+18*columna, 400+36*fila))

                columna+=1
                if columna==5:
                    columna=0
                    fila=1
                i+=1
                flan-=1
        
        karmo=4
        fila=0
        columna=0
        i=0
        with Image.open("img\Karmo10Plus.jpg") as imBronPlus, Image.open("img\Karmo.jpg") as imBron:
            while karmo>0 and i<10:
                if karmo>10:
                    im.paste(imBronPlus, (1156+18*columna, 400+36*fila))
                else:
                    im.paste(imBron, (1156+18*columna, 400+36*fila))

                columna+=1
                if columna==5:
                    columna=0
                    fila=1
                i+=1
                karmo-=1

        im.show()
        #im.save("test2.jpg")


drawDrink(3)

