#gun = M700
#ammo = 7.62x51mm M993
#building == Popular center 75m

#horizontal disance == Velocity * time

##t = [V₀ * sin(α) + √((V₀ * sin(α))² + 2 * g * h)] / g

import math
import json
from pathlib import Path
   
class experimentalData:
       try:
              def __init__(self, JSON):
                     self.angle = float(JSON['angle'])
                     self.gun = JSON['gun']
                     self.ammo = JSON['ammo']
                     self.ammo_speed = float(JSON['ammo_speed'])
                     self.building = JSON['building']
                     self.building_height_M = float(JSON['building_height_M'])
                     self.g = float(JSON['g'])
       except:
              def __init__(self, angle:float, gun:str, ammo:str, ammo_speed:float, building:str, bulding_height_M:str, g:float):
                     self.angle = angle
                     self.gun = gun
                     self.ammo = ammo
                     self.ammo_speed = ammo_speed
                     self.building = building
                     self.building_height_M = bulding_height_M
                     self.g = g


def calcDistance(expData):
       t = (expData.ammo_speed * math.sin(expData.angle) + math.sqrt((expData.ammo_speed * math.sin(expData.angle))**2 + 2 * expData.g * expData.building_height_M)) / expData.g

       distance = expData.ammo_speed*t

       print(f"If you fire an {expData.gun} using {expData.ammo} bullets from the top of {expData.building}" +
              f"which is {expData.building_height_M} meters at an angle of {expData.angle} degrees," +
              f" the bullet will travel {round(t, 2)} seconds for a distance of " +
              f"{round(distance, 2)} meters")

calcDistance(experimentalData(json.load(open(Path(__file__).parents[0].joinpath("ExperimentalData.json")))))