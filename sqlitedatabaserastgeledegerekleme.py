import sqlite3
import random
import time
import datetime

connnection = sqlite3.connect("dersler.db")

cursor=connnection.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Tablo1 ('zaman' REAL,'tarih' TEXT,'anahtarkelime' TEXT,'deger' REAL)")

def rastgeledegerekle():
    zaman = time.time()
    tarih = str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S'))
    anahtarkelime = "Python Sqlite3"
    deger = random.randrange(0,10)
    cursor.execute("INSERT INTO Tablo1 (zaman,tarih,anahtarkelime,deger) VALUES (?,?,?,?)",(zaman,tarih,anahtarkelime,deger))
    connnection.commit()

tabloolustur()

i=0
while (i<10):
    rastgeledegerekle()
    time.sleep(1)
    i +=1
connnection.close()