import os

import mysql.connector
from dotenv import load_dotenv


class Database():
  def __init__(self):
    load_dotenv()
    self.SERVER = os.getenv('DB_SERVER')
    self.DB_NAME = os.getenv('DB_NAME')
    self.DB_USERNAME = os.getenv('DB_USERNAME')
    self.DB_PASSWORD = os.getenv('DB_PASSWORD')
    self.mydb = mysql.connector.connect(
      host=self.SERVER,
      database=self.DB_NAME,
      user=self.DB_USERNAME,
      password=self.DB_PASSWORD,
      ssl_disabled=True
    )

  def get_Drink(self,drink_ID : int):
    QUERY="SELECT `Name`, `Descrip`, `Price`, `Adelhyde`, `BronExtract`, `PowDekta`, `Flanergide`, `Karmotrine`, `aged`, `iced`, `blended`, `flavour`, `img`,`last_updated` FROM `drinks` WHERE `id`=%s"
    cursor = self.mydb.cursor(prepared=True)
    data = (drink_ID,)

    cursor.execute(QUERY,data)
    
    if(cursor.rowcount==0):
        return
    
    result=cursor.fetchone()
    number_of_rows=result[0]

    print(result)
    return result

    







    

