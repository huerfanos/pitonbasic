import sqlite3
connection = sqlite3.connect("dersler.db")
cursor = connection.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler('ad' TEXT,'soyad' TEXT,'numara' INT,'ogrencinotu' INT)")
def degerekle():
    cursor.execute("INSERT INTO ogrenciler VALUES ('Murat peker','Haydar',1212,90)")
    connection.commit()
    connection.close()
tabloolustur()
degerekle()

