import os
from PIL import Image, ImageFont, ImageDraw

fontIn = ImageFont.truetype("fonts/va-11-hall-a-cyr-10px.ttf", 28)


def drawDrink(drinkdata):
    with Image.open("img/BackGround.jpg") as im:
        d1 = ImageDraw.Draw(im)
        d1.text((70, 105), "Bad Touch - 250$",(255, 255, 255),fontIn)

        with Image.open("img/BackGround.jpg") as imdrink:
            imdrink.show();

        im.show()
        im.save("test.jpg")

drawDrink("hello")
