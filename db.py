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
    QUERY="SELECT d.`Name`, d.`Descrip`, d.`Price`, d.`Adelhyde`, d.`BronExtract`, d.`PowDekta`, d.`Flanergide`, d.`Karmotrine`, d.`aged`, d.`iced`, d.`blended`, f.Name, d.`img`,d.`last_updated`,d.id FROM `drinks` d JOIN flavour f ON d.flavour=f.id WHERE d.`id`=%s"
    cursor = self.mydb.cursor(prepared=True)
    data = (drink_ID,)

    cursor.execute(QUERY,data)
    
    if(cursor.rowcount==0):
        return
    
    result=cursor.fetchone()
    
    QUERY="SELECT t.Name FROM `drink_type` dt JOIN types t ON t.id=dt.type_id WHERE `drink_id`=%s"
    cursor.execute(QUERY,data)
    types=[]
    results = cursor.fetchall()
    for row in results:
      types.append(row[0])
    
    result= result + (types,)
    print(result)
    return result

    







    

