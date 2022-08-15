import mysql.connector as msql
from mysql.connector import Error
import json


with open('pass.json') as f:
    DATA = json.load(f)
    HOST = DATA["host"]
    USER = DATA["user"]
    PASSWORD = DATA["password"]



def connect_bd():
    """Connect to the database

    @return Connector to the database 
    """
    try:
        conn = msql.connect(host=HOST, 
                            user=USER,  
                                password=PASSWORD) #give ur username, password
        if conn.is_connected():
            cursor = conn.cursor()
            #cursor.execute("CREATE DATABASE oxyCiterne")
            
        return conn
    except Error as e:
        print("Error while connecting to MySQL", e)



def stream_citerne(conn,nomC,pourcentage,pression,dateC,temps) -> None:

    """Streaming the data and store it to the database

    @param conn Connector to the database
    @param nomC 
    @param pourcentage Value to be added 
    @param pression Value to be added
    @param dateC Value of the date
    @param temps Value of time  

    """

    request = "insert into oxyciterne.citernes(pourcentage,pression,dateC,temps,nomC) values(%s,%s,%s,%s,%s)"
    params =(pourcentage,pression,dateC,temps,nomC)
    with conn as db :
        with db.cursor() as c:
            c.execute(request, params)
            db.commit()
            print("ligne ajoutée")
