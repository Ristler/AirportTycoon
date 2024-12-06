import mysql.connector
import random
import math
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
    def __init__(self):
        pass
    def myrsky(self,id):
        sql = f'update lentokone_inventory set saapumispvm = 4 where pelaaja_id = {id}'
        desc = '''
MYRSKY TULOSSA!! ET VOI LENTÄÄ KOLMEEN SEURAAVAAN PÄIVÄÄN'''
        cursor.execute(sql)
        return desc
    
    def erikois_vierailija(self,id):
        sql = f'select count(kauppa_id) from kauppa_inventory where pelaaja_id = {id}'
        cursor.execute(sql)
        kaupat = cursor.fetchall()
        kauppa_tulot = 2000*kaupat[0][0]
        cursor.execute(f"update pelaaja set raha = raha + {int(kauppa_tulot)} where id = {id}")
        v_id = random.randint(1,6)
        cursor.execute(f'select vierailija_nimi from erikois_vierailijat where vierailija_id = {v_id}')
        vierailija = cursor.fetchall()
        desc = f"Erikoisvierailija {vierailija[0][0]} tuli käymään lentokentälläsi ja sait lisää tuloja kaupoista {kauppa_tulot}"
        return desc
    
    def valtion_tuet(self,id):
        tuki = random.randint(10000,50000)
        desc =  f'''
                Valtio antaa sulle tukia {tuki}!'''
        cursor.execute(f'update pelaaja set raha = raha + {tuki} where id = {id}')
        return desc
    
    def valitse_tilanne(self):
        #valitsee tilanne listasta jonkun classin sisältävän tilanteen ja palauttaa sen
        tilanteet = [self.myrsky,self.erikois_vierailija, self.valtion_tuet,]
        valittu_tilanne = tilanteet[random.randint(0,2)]
        return valittu_tilanne


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
        sql = f'SELECT otettu From achievements WHERE pelaaja_id = {id} and achievement = "frequent_flyer"'
        cursor.execute(sql)
        results = cursor.fetchall()
        if results == False:
            sql = f'SELECT tracker FROM pelaaja WHERE id = {id}'
            cursor.execute(sql)
            results = cursor.fetchall()
            if results >= 20:
                sql = f'Update otettu SET otettu = True WHERE pelaaja_id = {id} AND achievement = "frequent_flyer"'
                cursor.execute(sql)
                print('Olet saanut Frequent achievement!')#do something with the website pop up thingy to notife the user
                
                return None 
            else:
                sql = f'SELECT tracker From achievements WHERE pelaaja_id = {id} and achievement = "frequent_flyer"'
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