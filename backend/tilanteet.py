import mysql.connector
import random
import math
import json
from flask import Flask, request, Response, jsonify, redirect, render_template
from flask_cors import CORS
app = Flask(__name__, template_folder='../FRONT', static_folder='../FRONT', static_url_path='/')

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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

@app.route('/achievements', methods=['GET'])

def fetch_achievements(id):
    
    sql = f'SELECT * FROM achievements WHERE id = {id}'
    cursor.execute(sql)
    results = cursor.fetchall()
    return jsonify(results)
    

def first_flight(id=None):
    print('jotain  dkdkdkkdkdöasjfölaskdfjöalskdfjöalskdjföalskdfjölaskdf')

    sql = f'SELECT taken FROM achievements WHERE id = {id} and name = "ekalento"'
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results[0][0])
    if results[0][0] == False:
        print('on totta')
        sql = f'SELECT raha FROM pelaaja WHERE id = {id}'
        cursor.execute(sql)
        results = cursor.fetchall()
        raha = results[0][0] + 5000
        sql = f'UPDATE pelaaja SET raha = {raha} WHERE id = {id}'
        cursor.execute(sql)
        sql = f'Update achievements SET taken = True WHERE id = {id} AND name = "ekalento"'
        cursor.execute(sql)
        return True
    elif results[0][0] == True:
        print('olet saanut jo ekan lennon!')
        return False


def Frequent_Flyer(id=None, lennetty=None):
    if lennetty is True:
        sql = f'SELECT taken From achievements WHERE pelaaja_id = {id} and name = "frequent_flyer"'
        cursor.execute(sql)
        results = cursor.fetchall()
        if results[0][0] == False:
            sql = f'SELECT tracker FROM pelaaja WHERE id = {id}'
            cursor.execute(sql)
            results = cursor.fetchall()
            if results[0][0] >= 20:
                sql = f'Update taken SET taken = True WHERE pelaaja_id = {id} AND name = "frequent_flyer"'
                cursor.execute(sql)
                print('Olet saanut Frequent name!')#do something with the website pop up thingy to notife the user
                
                return None 
            else:
                sql = f'SELECT tracker From achievements WHERE pelaaja_id = {id} and name = "frequent_flyer"'
                cursor.execute(sql)
                results = cursor.fetchall()
                diipadaabasuckmeoff = results[0][0] + 1
                sql = f'UPDATE pelaaja SET tracker = {diipadaabasuckmeoff} WHERE pelaaja_id = {id} and name = "frequent_flyer"'
                cursor.execute(sql)

def packed_planes(id=None, matkustajat=None, kapasiteetti=None):
    if matkustajat == kapasiteetti:
        sql = f'SELECT taken FROM achievements WHERE pelaaja_id = {id} and name = "packed_planes"'
        cursor.execute(sql)
        results = cursor.fetchall()
        if results[0][0] == False:
            sql = f'Update taken SET taken = True WHERE pelaaja_id = {id} AND name = "packed_planes"'
            cursor.execute(sql)
            #alennus tai vitust rahaa
            print('Olet saanut Packed name!')#do something with the website pop up thingy to notife the user
                
            return None
    

def millionares(id=None):
    sql = f'SELECT taken FROM achievements WHERE pelaaja_id = {id} and name = "millionare"'
    cursor.execute(sql)
    results = cursor.fetchall()
    if results[0][0] == False:
        sql = f'SELECT raha FROM pelaaja WHERE id = {id}'
        cursor.execute(sql)
        results = cursor.fetchall()
        if 1000000 <= results[0][0]:
            return True
        
def smooth_operation(id=None):
    sql = f'SELECT tracker FROM achievements WHERE pelaaja_id = {id} and name = "smoothoperation"'
    cursor.execute(sql)
    results = cursor.fetchall()
    track = results[0][0] + 1
    sql = f'SELECT taken FROM achievements WHERE pelaaja_id = {id} and name = "smoothoperation"'
    cursor.execute(sql)
    results = cursor.fetchall()
    if track[0][0] >= 10 and results[0][0] == False:
        sql = f'Update taken SET taken = True WHERE pelaaja_id = {id} AND name = "smoothoperation"'
        cursor.execute(sql)
        print('Olet saanut smooth operation name!')#do something with the website pop up thingy to notife the user customer satisfaction

    sql = f'UPDATE pelaaja SET tracker = {track} WHERE pelaaja_id = {id} and name = "smoothoperation"'
    cursor.execute(sql)

def debt_free(id=None):
    sql = f'SELECT taken FROM achievements WHERE pelaaja_id = {id} and name = "debt_free"'
    cursor.execute(sql)
    results = cursor.fetchall()
    if results[0][0] == False:
        sql = f'SELECT raha FROM pelaaja WHERE id = {id}'
        cursor.execute(sql)
        results = cursor.fetchall()
        money = results[0][0] + 25000
        sql = f'UPDATE pelaaja SET raha = {money} WHERE id = {id}'
        cursor.execute(sql)
        sql = f'Update taken SET taken = True WHERE pelaaja_id = {id} AND name = "debt_free"'
        cursor.execute(sql)
        print('Olet saanut Debt Free namein!')#do something with the website pop up thingy to notife the

def airport_tycoon(id=None):
    sql = 'SELECT taken FROM achievements WHERE pelaaja_id = f{id} and name = "airport_tycoon"'
    cursor.execute(sql)
    results = cursor.fetchall()
    if results[0][0] == False:
        sql = 'SELECT raha FROM pelaaja WHERE id = f{id}'
        cursor.execute(sql)
        results = cursor.fetchall()
        money = results[0][0] + 50000  #can be some other reward like more actions per day if posible or just a free store or plane
        sql = f'UPDATE pelaaja SET raha = {money} WHERE id = {id}'
        cursor.execute(sql)
        sql = f'Update taken SET taken = True WHERE pelaaja_id = {id} AND name = "airport_tycoon"'
        cursor.execute(sql) 
        print('Olet saanut Airport Tycoon namein!')#do something with the website pop up thingy to notife the user
        
    