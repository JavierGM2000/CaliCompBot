import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()
SERVER = os.getenv('DB_SERVER')
DB_NAME = os.getenv('DB_NAME')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')


mydb = mysql.connector.connect(
  host=SERVER,
  database=DB_NAME,
  user=DB_USERNAME,
  password=DB_PASSWORD,
  ssl_disabled=True
)

def get_Drink(drink_ID):
    QUERY="SELECT `Name`, `Descrip`, `Price`, `Adelhyde`, `BronExtract`, `PowDekta`, `Flanergide`, `Karmotrine`, `aged`, `iced`, `blended`, `flavour`, `img` FROM `drinks` WHERE `id`=%s"
    cursor = mydb.cursor(prepared=True)
    data = (drink_ID,)

    cursor.execute(QUERY,data)
    
    if(cursor.rowcount==0):
        return;
    
    result=cursor.fetchone()
    number_of_rows=result[0]

    

    print(result)

get_Drink(1)

    

