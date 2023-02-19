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

  def __enter__(self):
        return self

  def __exit__(self, type, value, traceback):
    self.mydb.close()

  #Gets a drink ID and checks if the number coincides with any drink id on the database.
  #If the id doesn't exist, or the recieved value is not a number return 0, the ID of the no drink drink
  def verifyDrinkId(self,drink_ID):
    if not isinstance(drink_ID, int):
      return 0

    QUERY="SELECT COUNT(*) FROM `drinks` WHERE `id`=%s"
    cursor = self.mydb.cursor(prepared=True)
    data = (drink_ID,)

    cursor.execute(QUERY,data)
    
    result=cursor.fetchone()

    if result[0]!=0:
      return drink_ID
    else:
      return 0
  
  #Gets the ID of a drink by name, if the name doesnt coincide with any drink it will return 0, the ID of the no drink drink
  def getIdByName(self,name:str):
    name = name.lower()
    QUERY="SELECT `id` FROM `drinks` WHERE LOWER(`Name`)=%s LIMIT 0, 1"
    data = (name,)
    print("name is "+name)
    cursor = self.mydb.cursor(prepared=True)
    cursor.execute(QUERY,data)
    result=cursor.fetchone()
    if( not result is None ):
      return result[0]
    else :
      cursor.fetchone()
    
    data = (name,)
    QUERY="SELECT `drink_id` FROM `drink_alias` WHERE LOWER(`name`)=%s LIMIT 0, 1"
    cursor.execute(QUERY,data)
    result=cursor.fetchone()
    if( not result is None ):
      return result[0]

    return 0

  #Given a drink id and a timestamp, returns True if the update date is newer than the given timstamp
  def checkIfUpdated(self,drink_ID,timestamp):
    QUERY="SELECT `last_updated`>from_unixtime(%s) FROM drinks WHERE id=%s"
    cursor = self.mydb.cursor(prepared=True)
    data = (timestamp,drink_ID)
    cursor.execute(QUERY,data)
    result=cursor.fetchone()
    return (False, True)[result[0]==1]

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
    
    results = cursor.fetchall()
    types=[row[0] for row in results]
    
    result= result + (types,)
    print(result)
    return result

    







    

