import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='peli',
    user='root',
    password='1234',
    autocommit=True
)
cursor = connection.cursor()

class tilanteet():
    def __init__(self,nimi):
        self.nimi = nimi
    def myrsky(self,user):
        sql = f'update lentokone_inventory set saapumispvm = 4 where pelaaja_id = {user["id"]}'
        print(f'''
MYRSKY TULOSSA!! ET VOI LENTÄÄ KOLMEEN SEURAAVAAN PÄIVÄÄN''')
        cursor.execute(sql)
    def erikois_vierailija(self,user):
        sql = f'select kauppa_id from kauppa_inventory where pelaaja_id = {user["id"]}'
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results) 