class experimentData:
    #    try:
    #           def __init__(self, JSON, i):
    #                  self.gun = JSON['Data'][i]['gun']
    #                  self.ammo = JSON['Data'][i]['ammo']
    #                  self.ammo_speed = float(JSON['Data'][i]['ammo_speed'])
    #                  self.building = JSON['Data'][i]['building']
    #                  self.building_height_M = float(JSON['Data'][i]['building_height_M'])
    #                  self.g = float(JSON['Data'][i]['g'])
    #    except:
    def __init__(self, angle:float, gun:str, ammo:str, ammo_speed:float, building:str, bulding_height_M:str, g:float):
        self.gun = gun
        self.ammo = ammo
        self.ammo_speed = ammo_speed
        self.building = building
        self.building_height_M = bulding_height_M
        self.g = g