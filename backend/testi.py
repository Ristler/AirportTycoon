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

tilanteet().valitse_tilanne(12)