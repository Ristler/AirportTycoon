import random
class tilanteet():
    def __init__(self):
        pass
    def myrsky(self,id):
        sql = f'update lentokone_inventory set saapumispvm = 4 where pelaaja_id = {id}'
        print(f'''
MYRSKY TULOSSA!! ET VOI LENTÄÄ KOLMEEN SEURAAVAAN PÄIVÄÄN''')
        
    def erikois_vierailija(self,id):
        sql = f'select kauppa_id from kauppa_inventory where pelaaja_id = {id}'
        print("erikois vierailija")

    def valtion_tuet(self,id):
        tuki = random.randint(10000,50000)
        desc =  f'''
                Valtio antaa sulle tukia {tuki}!'''
        print(desc)
    def valitse_tilanne(self,id):
        tilanteet = [self.myrsky,self.erikois_vierailija, self.valtion_tuet]
        return tilanteet[random.randint(0,2)](id)


sql3 = f"INSERT INTO achievements (id, name, tracker, taken, description) VALUES 
        ({pelaaja.id}, 'ekalento', 0, False, 'Successfully complete your first flight.'),
        ({pelaaja.id}, 'frequent_flyer', 0, False, 'Complete 20 flights.'),
	    ({pelaaja.id}, 'packed_planes', 0, False, 'Fill a plane to 100% capacity for the first time.'),
	    ({pelaaja.id}, 'millionare', 0, False, 'Earn $1,000,000 in total revenue.'),
	    ({pelaaja.id}, 'smoothoperation', 0, False, 'Go 15 days without any canceled flights.'),
	    ({pelaaja.id}, 'debt_free', 0, False, 'Fully repay your first loan.'),
	    ({pelaaja.id}, 'airport_tycoon', 0, False, 'Own 10 planes .')"
cursor.execute(sql3)