from random import random
from types import NoneType
from datetime import date, timedelta
from geopy.distance import geodesic as gd
import random
import mysql.connector
import json
from flask import Flask, request, Response, jsonify, redirect, render_template
import tilanteet
import math
tilanteet = tilanteet.tilanteet()

from flask_cors import CORS

#### old code pieces for hindsight is 2020 type beat
lentokone = {
   "id" : 0,
   "tyyppi" : "",
   "määrä" : 0,
   "kunto" : 0,
   "hinta" : 0,
   "bensa" : 0,
   "efficiency" : 0,
   "saapumispvm" : 0,
   "location": ""
}

global Onkolennetty
Onkolennetty = False



##YHDISTÄÄ FRONTIIN FOLDERIIN ETTII SIELT HTML
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

choices = []
#lista = [0,0,0,0,0,0,0]
#tallenna pelaaja clienttiin
class User:
    def __init__(self,id, nimi, raha, laina, erapaiva, paiva, rating):
        self.id = id
        self.nimi =nimi
        self.raha = raha
        self.laina = laina
        self.erapaiva = erapaiva
        self.paiva = paiva
        self.rating = rating

@app.route('/')
def auth():
    return render_template('auth.html')



@app.route('/login', methods=['POST', 'GET'])      

#login function, user gets assigned the database values, eräpäivä and päivä are for the loan.
def login():

    username = request.form['username']
    password_input = request.form['password']
    sql = "SELECT * FROM `pelaaja` WHERE nimi = %s AND salasana = %s"
    cursor.execute(sql, (username, password_input))
    results = cursor.fetchall()

    if not results:
        return jsonify({"message": "Invalid username or password"}), 401

    elif results:
        for row in results:
            global pelaaja
            pelaaja = User(row[0], row[1], row[2], row[3], row[4], row[5], row[7])
        return jsonify({"user": pelaaja.nimi , "id":pelaaja.id, "raha": pelaaja.raha,
                        "laina":pelaaja.laina, "Eräpäivä": pelaaja.erapaiva, "Päivä":pelaaja.paiva,
                        "rating": pelaaja.rating})
                    

@app.route('/createplayer', methods=['POST', 'GET'])      
#create player function, checks if username is taken and creates a new user.
def createplayer():

    username = request.form['username']
    if not isNameTaken(username):
        password_input = request.form['password']
        sql = "INSERT INTO `pelaaja` (nimi, salasana) VALUES (%s, %s)"
        cursor.execute(sql, (username, password_input))
        sql2 = "SELECT * FROM `pelaaja` WHERE nimi = %s AND salasana = %s"
        cursor.execute(sql2, (username, password_input))
        results = cursor.fetchall()
        for row in results:
                    global pelaaja
                    pelaaja = User(row[0],row[1],row[2],row[3],row[4],row[5],row[7])
        return jsonify({"user": pelaaja.nimi , "id":pelaaja.id, "raha": pelaaja.raha,
                        "laina":pelaaja.laina, "Eräpäivä": pelaaja.erapaiva, "Päivä":pelaaja.paiva,
                        "rating": pelaaja.rating})
    if isNameTaken(username):
        return jsonify({"message": "Username is already taken"}), 400

def updateUser():
        userID = pelaaja.id
        sql = f"SELECT * FROM `pelaaja` WHERE id = ({userID})"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        if results:
            row = results[0]
            pelaaja.nimi = row[1]
            pelaaja.raha = row[2]
            pelaaja.laina = row[3]
            pelaaja.erapaiva = row[4]
            pelaaja.paiva = row[5]
            pelaaja.rating = row[7]
            return
        
def isNameTaken(playerName):
        sql = f"SELECT nimi FROM `pelaaja`"
        cursor.execute(sql)
        result = cursor.fetchall()

        for i in result:
            if i[0] == playerName:
                return True
        else:
            return False
        




class Inventory:
    def __init__(self, konelista, kauppalista):
        self.lista = konelista
        self.kauppalista = kauppalista



class Store(Inventory):
    def __init__(self, lista, id, tyyppi, määrä, kunto, maara, hinta, bensa, efficiency):
        super().__init__(lista)





def Tulostus(data):
    line = '\u2550'*79
    print("\u2554"+ line +"\u2557")
    for i, plane in enumerate(data):
        choices.append(plane[0])
        print(f"\u2551id: {plane[0]}\t\t\t",f"määrä: {plane[2]} penkkiä\t",f"hinta: {plane[4]} euroa\t\t",f" kulutusteho: {plane[6]}\t","", sep='\u2551')
        print(f"\u2551tyyppi: {plane[1]}",f"kunto: {plane[3]} %\t\t",f"bensamäärä: {plane[5]}L\t","\t\t\t\t\t\u2551", sep="\u2551")
        if i+1 < len(data):
            print("\u2560"+ line+ "\u2563")
    print("\u255a" + line + "\u255d")



##TODO THIS IS URGENT
@app.route('/prepare', methods=['POST'])

def prepare():

    data = request.json
    lentokone_id = data.get("plane_id")
    print("TESTIIIIIIII", lentokone_id)
    sql = (f"select lentokone.id, lentokone.tyyppi, lentokone.kapasiteetti, lentokone_inventory.kunto, lentokone.hinta, lentokone_inventory.fuel, lentokone.efficiency from lentokone INNER JOIN lentokone_inventory ON lentokone.id = lentokone_inventory.lentokone_id  WHERE lentokone_inventory.lentokone_id = {lentokone_id} and lentokone_inventory.pelaaja_id = {pelaaja.id}")
    cursor.execute(sql)
    resultss = cursor.fetchall() #resultssssssssssssssssssssssss
                #return jsonify(resultss)
    print(resultss)

    for row in resultss:
        lentokone["id"] = row[0]
        lentokone["tyyppi"] = row[1]
        lentokone["määrä"] = row[2]
        lentokone["kunto"] = row[3]
        lentokone["hinta"] = row[4]
        lentokone["bensa"] = row[5]
        lentokone["efficiency"] = row[6]
    if lentokone is resultss[0]:
        return
    json_paketti = {}
    print("Matkustajat nousevat koneeseen..")
    määränpää,bensa = Haetaanmaaranpaa(lentokone["bensa"], lentokone["efficiency"])
    if(määränpää == 0):
        return
    json_paketti.update({"Bensankulutus:": bensa})

    indeksi = 0
    tyytyväisyys = pelaaja.rating
    paikka = 0
    lipunhinta = 200
    while indeksi < lentokone["määrä"]:
        randomi = random.random()
        if tyytyväisyys >= randomi:
            paikka += 1
        indeksi += 1
    json_paketti.update({"Varatut paikat" : paikka})
    #if planebrokey(lentokone, paikka, pelaaja.id) == False:
    rahat = pelaaja.raha + lipunhinta * paikka

    sql = f"UPDATE pelaaja SET raha = {rahat} WHERE id = pelaaja.id"
    pelaaja.raha = rahat
    cursor.execute(sql)
    json_paketti.update({"plane brokey" : False})
    json_paketti.update({"tuotto" : lipunhinta*paikka})
    #else:
    #    json_paketti.update({"plane brokey" : True})
    #    return

    lentokone["bensa"] = lentokone["bensa"] - bensa
    json_paketti.update({"bensan kulutus" : bensa})
    json_paketti.update({"latitude" : määränpää[1]})
    json_paketti.update({"longitude": määränpää[2]})
    #lentokone["saapumispvm"] = 3
    sql = f"UPDATE lentokone_inventory set fuel = fuel - {bensa} where lentokone_id = {lentokone['id']} and pelaaja_id = {pelaaja.id}"
    cursor.execute(sql)
    #sql = f"UPDATE lentokone_inventory set saapumispvm = {lentokone['saapumispvm']} where lentokone_id = {lentokone['id']}"
    #cursor.execute(sql)
    Onkolennetty = True
    print("JSON PAKETTI PREPARESSA:", json_paketti)
    return jsonify(json_paketti)
    #lentomatka(lentokone)

def Haetaanmaaranpaa(bensa, efficiency):
    MatkaKM = (bensa*3.84)/efficiency
    longitude = 24.963301
    latitude = 60.3172
    sql = f"SELECT iso_country, latitude_deg, longitude_deg, name from airport where type='medium_airport' or type='large_airport' or type='small_airport'"
    cursor.execute(sql)
    countries = cursor.fetchall()
    suodatut_maat= [country for country in countries if gd((latitude,longitude),(country[1],country[2])).km <= MatkaKM]
    if len(suodatut_maat) == 1:
        print("eioo tarpeeks bensaa lentää minnekkään. lentokone palaa kentälle...")
        return 0, 0


    #vanha versio maiden lajittelusta:
    #for country in countries:
    #    if(gd((latitude,longitude),(country[1],country[2])).km <= MatkaKM):
    #        print(MatkaKM - gd((latitude,longitude),(country[1],country[2])).km)
    #        suodatut_maat.append(country)

    valittu_maa = suodatut_maat[random.randint(0,len(suodatut_maat))]

    bensankulutus = (gd((latitude,longitude),(valittu_maa[1],valittu_maa[2])).km * efficiency)/3.84


    return valittu_maa, bensankulutus

@app.route('/listaa_lentokoneet', methods=['GET'])
def listaaLentokoneet():
    if not pelaaja:  # Varmista, että pelaaja on kirjautuneena
        return jsonify({"message": "Pelaaja ei ole kirjautunut."}), 401
    print("Listataan Lentokoneet:")
    sql = (
        f"select lentokone.id, lentokone.tyyppi, lentokone.kapasiteetti, lentokone_inventory.kunto, lentokone.hinta, lentokone_inventory.fuel, lentokone.efficiency from lentokone, lentokone_inventory where lentokone.id = lentokone_inventory.lentokone_id and lentokone_inventory.pelaaja_id = {pelaaja.id} and lentokone_inventory.saapumispvm = 0")

    cursor.execute(sql)
    planes = cursor.fetchall()
    if not planes:
        return jsonify({"message": "Ei saatavilla olevia lentokoneita"}), 404
    
    planesList = [
        {"id": lentokone[0], "tyyppi": lentokone[1], "kapasiteetti": lentokone[2], "kunto": lentokone[3], "hinta": lentokone[4], "fuel": lentokone[5], "efficiency": lentokone[6] }
        for lentokone in planes
    ]
    print(planesList)
    return jsonify(planesList)

    
@app.route('/valitse_lentokone', methods=['POST'])
def valitseLentokone():
   
    while True:
        try:
            print("Minkä lentokoneet valitset?")
            inputt = (int(input()))

            if inputt in x:
                sql = (
                    f"select lentokone.id, lentokone.tyyppi, lentokone.kapasiteetti, lentokone_inventory.kunto, lentokone.hinta, lentokone_inventory.fuel, lentokone.efficiency from lentokone INNER JOIN lentokone_inventory ON lentokone.id = lentokone_inventory.lentokone_id  WHERE lentokone_inventory.lentokone_id = {inputt} and lentokone_inventory.pelaaja_id = {pelaaja.id}")
                cursor.execute(sql)
                resultss = cursor.fetchall() #resultssssssssssssss
                #return jsonify(resultss)
                print(resultss)

                for row in resultss:
                    lentokone["id"] = row[0]
                    lentokone["tyyppi"] = row[1]
                    lentokone["määrä"] = row[2]
                    lentokone["kunto"] = row[3]
                    lentokone["hinta"] = row[4]
                    lentokone["bensa"] = row[5]
                    lentokone["efficiency"] = row[6]
                ##TÄHÄ SE PREPARE FUNCTION EHK KU ON VALINNU LENTOKONEEN, NYT LAITOIN VAA INTERFACE ET VOI TESTAA

            elif inputt not in x:
                print("cmon bro ei sul tollast lentokonetta oo")
                #return jsonify({"error": "ei ole tommosta konetta"})
                break
            elif inputt == 0:
                print("palataan käyttöjärjestelmään")
                #return jsonify({"Palataan käyttöjärjestelmään"})
                break
        except ValueError:
            print("damn kirjoita NUMERO.....")
            return jsonify({"error": "MISINPUT IT WAS A MISINPUT"})
        return jsonify(lentokone)

    


##PROBABLY BROKEN
def planebrokey(kone, asiakkaat, pelaajaid):
    sql = f"SELECT kunto FROM lentokone_inventory where lentokone_id = {kone['id']}"
    cursor.execute(sql)
    kunto = cursor.fetchall()[0][0]
    print(kunto)
    kunto = kunto - 5
    sql = f"UPDATE lentokone_inventory set kunto = {kunto} where lentokone_id = {kone['id']}"
    cursor.execute(sql)
    lentokone["kunto"] = lentokone["kunto"] - 5

    rikki_randomi = random.random()
    if kunto < 60:
        if kunto*0.7/100 < rikki_randomi:
            sql = f"SELECT raha FROM pelaaja where id = {pelaajaid}"
            cursor.execute(sql)
            raha = cursor.fetchall()[0][0]
            raha = raha - (asiakkaat * 100)
            raha = raha - (asiakkaat * 200)
            sql = f"UPDATE pelaaja SET raha = {raha} WHERE id = {pelaajaid}"
            pelaaja.id = raha
            cursor.execute(sql)
            return True
    elif kunto < 80:
        if kunto*0.9/100 < rikki_randomi:
            sql = f"SELECT raha FROM pelaaja where id = {pelaajaid}"
            cursor.execute(sql)
            raha = cursor.fetchall()[0][0]
            print(raha)
            raha = raha - (asiakkaat * 100)
            raha = raha - (asiakkaat * 200)
            sql = f"UPDATE pelaaja SET raha = {raha} WHERE id = {pelaajaid}"
            pelaaja.raha = raha
            cursor.execute(sql)
            return True
    else:
        return False

#@app.route('/getPlane/<int:id>', methods=['GET'])
def getPlane(id):

    sql = f"SELECT tyyppi, hinta, kunto, maxfuel FROM `lentokone` WHERE id = {id}"
    cursor.execute(sql)
    results = cursor.fetchall()
    if results:
        tyyppi, hinta, kunto, maxfuel = results[0]
        return tyyppi, hinta, kunto, maxfuel



# #@app.route('/ostalentokone', methods=['GET'])
# def OstaLentokone():

#     print("")
#     print("Tervetuloa kauppaan!")
#     print("Jos haluat poistua, kirjoita: 0")
#     sql = f"SELECT id, tyyppi, kapasiteetti, kunto, hinta, maxfuel, efficiency FROM `lentokone`"
#     cursor.execute(sql)
#     results = cursor.fetchall()

#     Tulostus(results)
#     while True:
#         updateUser()
#         try:
#             print("")
#             choice = int(input("Valitse minkä mallin ostat: "))
#             print("Jos haluat poistua, kirjoita: 0")

#             if choice == 0:
#                 print("")
#                 print("Palaa takaisin käyttöliittymään...")
#                 return

#             if choice in choices:
#                 tyyppi, hinta, kunto, maxfuel = getPlane(choice)
#                 print("-------------------------")
#                 print("Valitsit lentokoneen: ", tyyppi)
#                 print("Lentokoneen hinta on", hinta)
#                 print("-------------------------")

#                 validate = int(input("Oletko varma, että haluat ostaa tämän lentokoneen? Kyllä(1) Ei(2): "))

#                 if validate == 1:
#                     money = pelaaja.raha
#                     sql1 = f"SELECT lentokone_id, pelaaja_id from `lentokone_inventory` WHERE lentokone_id = {choice} AND pelaaja_id = {pelaaja.id}"
#                     cursor.execute(sql1)
#                     x = cursor.fetchall()

#                     if money >= hinta and not x:
#                         userID = pelaaja.id
#                         sql1= f"INSERT INTO `lentokone_inventory` (pelaaja_id, lentokone_id, kunto, fuel, tunniste) VALUES ({userID}, {choice}, 100, {maxfuel}, {choice})"
#                         sql2 = f"UPDATE `pelaaja` SET raha = raha - {hinta} WHERE id = {pelaaja.id}"
#                         cursor.execute(sql1)
#                         cursor.execute(sql2)
#                         updateUser()
#                         print("Ostit juuri itsellesi mahtavan lentokoneen!")
#                         print("Rahasi ostoksen jälkeen: ", pelaaja.raha)
#                     elif x:
#                         print("")
#                         print("Omistat jo tämän lentokoneen")
#                     elif money < hinta:
#                         print("Sinulla ei ole tarpeeksi rahaa tähän lentokoneeseen")
#                 if validate == 2:
#                     print("Palataan takaisin käyttöliittymään...")
#                     return
#             else:
#                 print("Virheellinen lentokone")
#         except ValueError:
#             print("")
#             print("Syöte täytyy olla numero!")


@app.route('/kaupat', methods=['GET'])
def hae_kaupat():
    if not pelaaja:  # Varmista, että pelaaja on kirjautuneena
        return jsonify({"message": "Pelaaja ei ole kirjautunut."}), 401

    query = """
        SELECT id, tyyppi, hinta, teema 
        FROM kaupat 
        WHERE id NOT IN (
            SELECT kauppa_id 
            FROM kauppa_inventory 
            WHERE pelaaja_id = %s
        )
    """
    cursor.execute(query, (pelaaja.id,))
    shops = cursor.fetchall()

    if not shops:
        return jsonify({"message": "Ei saatavilla olevia kauppoja."}), 404

    kaupat = [
        {"id": shop[0], "tyyppi": shop[1], "hinta": shop[2], "teema": shop[3]}
        for shop in shops
    ]
    return jsonify(kaupat)

@app.route('/osta_kauppa', methods=['POST'])
def osta_kauppa():
    if not pelaaja:  # Varmista, että pelaaja on kirjautuneena
        return jsonify({"message": "Pelaaja ei ole kirjautunut."}), 401

    data = request.json
    shop_id = data.get("shop_id")

    # Tarkista, löytyykö kauppa ja pelaajalla varaa ostaa
    cursor.execute("SELECT hinta FROM kaupat WHERE id = %s", (shop_id,))
    shop = cursor.fetchone()
    if not shop:
        return jsonify({"message": "Kauppa ei löytynyt."}), 404

    shop_price = shop[0]

    if pelaaja.raha < shop_price:
        return jsonify({"message": "Köyhät rahat ei riitä!"}), 400

    # Päivitä pelaajan rahat ja lisää kauppa inventoryyn
    new_balance = pelaaja.raha - shop_price
    cursor.execute("UPDATE pelaaja SET raha = %s WHERE id = %s", (new_balance, pelaaja.id))
    cursor.execute("INSERT INTO kauppa_inventory (pelaaja_id, kauppa_id) VALUES (%s, %s)", (pelaaja.id, shop_id))
    connection.commit()

    # Päivitä pelaajan rahatilanne
    pelaaja.raha = new_balance

    return jsonify({"message": f"Pelaaja {pelaaja.nimi} onnistuneesti osti kaupan {shop_id}!"})






##WORK IN PROGRESS TO BUY PLANES
@app.route('/planes', methods=['GET'])
def hae_lentokoneet():
    if not pelaaja:  # Varmista, että pelaaja on kirjautuneena
        return jsonify({"message": "Pelaaja ei ole kirjautunut."}), 401


##SELECT LENTOKONE_ID MIGHT BE WRONG, 
    query = """
        SELECT id, tyyppi, kapasiteetti, hinta, efficiency, maxfuel 
        FROM lentokone 
        WHERE id NOT IN (
            SELECT lentokone_id 
            FROM lentokone_inventory 
            WHERE pelaaja_id = %s
        )
    """
    cursor.execute(query, (pelaaja.id,))
    planes = cursor.fetchall()

    if not planes:
        return jsonify({"message": "Ei saatavilla olevia lentokoneita"}), 404


##TEST IF THIS WORKS. 
    planesList = [
        {"id": lentokone[0], "tyyppi": lentokone[1], "kapasiteetti": lentokone[2], "hinta": lentokone[3], "efficiency": lentokone[4], "maxfuel": lentokone[5] }
        for lentokone in planes
    ]
    return jsonify(planesList)


@app.route('/buy_plane', methods=['POST'])
def osta_lentokone():
    if not pelaaja:  # Varmista, että pelaaja on kirjautuneena
        return jsonify({"message": "Pelaaja ei ole kirjautunut."}), 401

    data = request.json
    plane_id = data.get("plane_id")
    
    # Tarkista, löytyykö lentokone ja pelaajalla varaa ostaa
    cursor.execute("SELECT hinta FROM lentokone WHERE id = %s", (plane_id,))
    plane = cursor.fetchone()
    plane1 = str(plane_id)
    if not plane:
        return jsonify({"message": "Lentokonetta ei löytynyt.Id on "+plane1}), 404

    plane_price = plane[0]

    if pelaaja.raha < plane_price:
        return jsonify({"message": "Köyhät rahat ei riitä!"}), 400

    # Päivitä pelaajan rahat ja lisää kauppa inventoryyn
    new_balance = pelaaja.raha - plane_price
    cursor.execute("UPDATE pelaaja SET raha = %s WHERE id = %s", (new_balance, pelaaja.id))
    cursor.execute("INSERT INTO lentokone_inventory (pelaaja_id, lentokone_id) VALUES (%s, %s)", (pelaaja.id, plane_id))
    connection.commit()

    # Päivitä pelaajan rahatilanne
    pelaaja.raha = new_balance

    return jsonify({"message": f"Pelaaja {pelaaja.nimi} onnistuneesti osti lentokoneen {plane_id}!"})

@app.route('/newday', methods=['GET'])
def uusi_paiva():
    json_paketti = []
    #lasketaan kuinka monta kauppaa on ja kerrataan se tonnilla ja ratingillä
    cursor.execute(f'select count(kauppa_id) from kauppa_inventory where pelaaja_id = {pelaaja.id}')
    result = cursor.fetchall()
    maara = result[0]
    kauppa_tulot = math.floor(1000*maara[0]*pelaaja.rating)
    pelaaja.raha += kauppa_tulot
    pelaaja.paiva += timedelta(days=1)
    cursor.execute(f'update pelaaja set raha = raha + {kauppa_tulot}, päivä = "{pelaaja.paiva}" where id = {pelaaja.id}')
    
    
    #ota tää pois kun olet korjannut Otalainaa() ja Tarkistalainaa()
    #konkurssi variable tarkistaa onko lentokenttämennyt konkurssiin
    viesti,konkurssi = tarkistalaina()
    if (konkurssi == True):
        return jsonify(viesti)
    json_paketti.append(viesti)
    json_paketti.append(f'kaupat tuotti tulosta: {kauppa_tulot} rahanmäärä on nyt {pelaaja.raha}')

    sql = f"select lentokone_id, saapumispvm from lentokone_inventory where pelaaja_id = {pelaaja.id}"
    cursor.execute(sql)
    results = cursor.fetchall()
    for lentokone in results:
        kone = getPlane(lentokone[0])
        if lentokone[1]-1 == 0:
            json_paketti.append(f"Kone f{kone[0]} on saapunut lentokentälle")

            if lentokone[1]  > 0:
                pvm = lentokone[1]
                pvm -= 1
                sql = f"UPDATE lentokone_inventory SET saapumispvm = {pvm} WHERE pelaaja_id = {pelaaja.id} and lentokone_id = {lentokone[0]}"
                cursor.execute(sql)
    global Onkolennetty
    if Onkolennetty == True:
        Onkolennetty = False #Lisää frequent flyer achievement function
        cursor.execute("")

    cursor.execute(f'select pvm from tilanteet where pelaaja_id = {pelaaja.id}')
    
    results = cursor.fetchall()
    print(results)
    #jos ei ole tilanne päivä
    if(results[0][0] > 0):
        tilanne = results[0][0]
        tilanne -= 1
        cursor.execute(f'update tilanteet set pvm = {tilanne} where pelaaja_id={pelaaja.id}')
        if(tilanne == 1):
            json_paketti.append("päivä tuntuu vähän mysteeriseltä... tuntuu että pian tapahtuu jotain")
    #jos on tilanne päivä        
    elif(results[0][0] == 0):
        desc = tilanteet.valitse_tilanne()
        new_desc = desc(id=pelaaja.id)
        json_paketti.append(new_desc)
        print(new_desc)
        uus_tilanne_pvm = random.randint(7,12)
        cursor.execute(f'update tilanteet set pvm = {uus_tilanne_pvm} where pelaaja_id={pelaaja.id}')
    return json.dumps(json_paketti)





















#lainaa saa vertaamalla tyytyväisyyden määrää ja eräpäivä on 2 viikkoa
#@app.route('/otalainaa', methods=['GET'])
def Otalainaa():
    tyytyväisyys = pelaaja.rating
    maksimi = 500000 * tyytyväisyys
    #pitää muokkaa että se toimii frontendin kanssa
    #laina = int(input(f"Olet valtuutettu lainaamaan enintään:{maksimi} Euroa. \n paljonko otat lainaa?:"))
    if pelaaja.erapaiva == None and laina <= maksimi:
        pelaaja.laina = laina * 1.2
        pelaaja.erapaiva = pelaaja.paiva + timedelta(days=14)
        pelaaja.raha = pelaaja.raha + laina
        return jsonify(f"Lainaa on maksettavana(+ korot): {laina*1.2} \n Lainan eräpäivä on: {pelaaja.erapaiva}")
    elif laina > maksimi:
        return jsonify("et ole valtuutettu liian isoon summaan")
    else:
        return jsonify (f"Sinulla on vanhempaa lainaa {pelaaja.laina} euroa. et ole valtuutettu lainan ottamiseen.", False)



#tarkistaa ja maksaa lainan
#@app.route('/tarkistalaina', methods=['GET'])
def tarkistalaina():

    if pelaaja.erapaiva is None or pelaaja.erapaiva  == '0000-00-00':
        return ("sinulla ei ole velkaa", False)
    if pelaaja.paiva == pelaaja.erapaiva and pelaaja.laina > 0:
        #palauttaa json_pakettiin stringin joka menee takasin uusi_paiva funktioon
        return "|||||tänään on viimeinen päivä maksaa lainat pois!|||||"
    elif pelaaja.paiva > pelaaja.erapaiva and pelaaja.laina > 0:
        cursor.execute(f"delete from achievements where id = {pelaaja.id}")
        cursor.execute(f"delete from kauppa_inventory where pelaaja_id = {pelaaja.id}")
        cursor.execute(f"delete from lentokone_inventory where pelaaja_id = {pelaaja.id}")
        cursor.execute(f"delete from pelaaja where id = {pelaaja.id}")
        return ("et pystynyt maksaa lainaa pois. peli päättyy", True)
        #lisää tähän kommenot jossa poistetaan koko käyttäjä

    if pelaaja.raha > 0 and pelaaja.laina > 0:
        maara = (pelaaja.laina if pelaaja.raha >= pelaaja.laina else pelaaja.raha)
        pelaaja.laina -= maara
        pelaaja.raha -= maara
        cursor.execute(f"update pelaaja set (raha = raha - {maara}, laina = laina - {maara}) where id = {pelaaja.id}")
        return(f"Pankki velotti tililtäsi {maara} euroa, sinulla on nyt {pelaaja.laina} euroa maksamatta", False)

# def interface():
#     temp = vars(pelaaja)
#     for item in temp:
#         print(temp[item])
#     while(True):
#         pelaaja.paiva += timedelta(days=1)
#         print("Tänään on: ", pelaaja.paiva)
#         tarkistalaina()
#         sql = f"select lentokone_id, saapumispvm from lentokone_inventory where pelaaja_id = {pelaaja.id}"
#         cursor.execute(sql)
#         results = cursor.fetchall()
#         for lentokone in results:
#             kone = getPlane(lentokone[0])
#             if lentokone[1]-1 == 0:
#                 print("Kone", kone[0], " on saapunut lentokentälle")
#             if lentokone[1]  > 0:
#                 pvm = lentokone[1]
#                 pvm -= 1
#                 sql = f"UPDATE lentokone_inventory SET saapumispvm = {pvm} WHERE pelaaja_id = {pelaaja.id} and lentokone_id = {lentokone[0]}"
#                 cursor.execute(sql)

#         while(True):
#             print("USER INTERFACE RAHA: ", pelaaja.raha)
#             print("")
#             print("Lennä (1)")
#             print("Osta lentokone (2)")
#             print("Osta kauppa (3)")
#             print("Hae pankista lainaa(4)")
#             print("Siirry toiseen päivään (5)")
#             print("Kokeile tilanteita (6) (testausta)")
#             print("Lopeta peli (0)")
#             print("")
#             inputti = str(input("Valintasi:"))

#             match inputti:
#                 case "1":
#                     prepare()
#                 case "2":
#                     OstaLentokone()
#                 case "3":
#                     osta_kauppa(pelaaja.id)
#                 case "4":
#                     Otalainaa()
#                 case "5":

#                     break
#                 case "6":
#                     tilanteet.erikois_vierailija(pelaaja)
#                 case "0":
#                     sql = f"update pelaaja set raha = {pelaaja.raha},laina = {pelaaja.laina},eräpäivä = '{pelaaja.erapaiva}',päivä = '{pelaaja.paiva}'  ,rating = {pelaaja.rating} where id = {pelaaja.id}"
#                     cursor.execute(sql)
#                     cursor.close()
#                     exit()

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)