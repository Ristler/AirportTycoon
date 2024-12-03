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

def ekalento(id=None):
    
    sql = 'SELECT otettu FROM achievements WHERE pelaaja_id = f{id} and achievement = "ekalento"'
    cursor.execute(sql)
    results = cursor.fetchall()
    if results == False:
        sql = 'SELECT raha FROM pelaaja WHERE id = f{id}'
        cursor.execute(sql)
        results = cursor.fetchall()
        raha = results[0] + 5000
        sql = f'UPDATE pelaaja SET raha = {raha} WHERE id = {id}'
        cursor.execute(sql)
        sql = f'Update otettu SET otettu = True WHERE pelaaja_id = {id} AND achievement = "ekalento"'
    else:
        print('Et ole vielä saanut ekalentoa!')
        