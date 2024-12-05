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

def first_flight(id=None):
    
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
        cursor.execute(sql)
    else:
        print('Et ole vielä saanut ekalentoa!')


def Frequent_Flyer(id=None, lennetty=None):
    if lennetty is True:
        sql = 'SELECT otettu From achievements WHERE pelaaja_id = f{id} and achievement = "frequent_flyer"'
        cursor.execute(sql)
        results = cursor.fetchall()
        if results == False:
            sql = 'SELECT tracker FROM pelaaja WHERE id = f{id}'
            cursor.execute(sql)
            results = cursor.fetchall()
            if results >= 20:
                sql = f'Update otettu SET otettu = True WHERE pelaaja_id = {id} AND achievement = "frequent_flyer"'
                cursor.execute(sql)
                print('Olet saanut Frequent achievement!')#do something with the website pop up thingy to notife the user
                
                return None 
            else:
                sql = 'SELECT tracker From achievements WHERE pelaaja_id = f{id} and achievement = "frequent_flyer"'
                cursor.execute(sql)
                results = cursor.fetchall()
                diipadaabasuckmeoff = results[0] + 1
                sql = f'UPDATE pelaaja SET tracker = {diipadaabasuckmeoff} WHERE pelaaja_id = {id} and achievement = "frequent_flyer"'
                cursor.execute(sql)

def packed_planes(id=None, matkustajat=None, kapasiteetti=None):
    if matkustajat == kapasiteetti:
        sql = 'SELECT otettu FROM achievements WHERE pelaaja_id = f{id} and achievement = "packed_planes"'
        cursor.execute(sql)
        results = cursor.fetchall()
        if results == False:
            sql = f'Update otettu SET otettu = True WHERE pelaaja_id = {id} AND achievement = "packed_planes"'
            cursor.execute(sql)
            #alennus tai vitust rahaa
            print('Olet saanut Packed achievement!')#do something with the website pop up thingy to notife the user
                
            return None
    

def millionare(id=None):
    sql = 'SELECT otettu FROM achievements WHERE pelaaja_id = f{id} and achievement = "millionare"'
    cursor.execute(sql)
    results = cursor.fetchall()
    if results == False:
        sql = 'SELECT raha FROM pelaaja WHERE id = f{id}'
        cursor.execute(sql)
        results = cursor.fetchall()
        if 1000000 <= results[0]:
            return True