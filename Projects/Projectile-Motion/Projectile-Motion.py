#gun = M700
#ammo = 7.62x51mm M993
#building == Popular center 75m

#horizontal disance == Velocity * time

##t = [V₀ * sin(α) + √((V₀ * sin(α))² + 2 * g * h)] / g

import math
import json
from pathlib import Path
import ExperimentData 

# experimetnalData = {"gun": "M700",
#     "ammo": "7.62x51mm M993",
#     "ammo_speed": 910,
#     "building": "Popular Center",
#     "building_height_M": 75,
#     "g": 9.8}
   
def calcDistance(experimentalData):
       time_s = math.sqrt((2*experimentalData.building_height_M / experimentalData.g))
       distance_m = experimentalData.ammo_speed * time_s

       print(f"If you fire an {experimentalData.gun} using {experimentalData.ammo} bullets from the top of {experimentalData.building}" +
              f"which is {experimentalData.building_height_M} meters at an angle of 0 degrees," +
              f" the bullet will travel {round(time_s, 2)} seconds for a distance of " +
              f"{round(distance_m, 2)} meters \n")


for i in range(4):
       calcDistance(ExperimentData.experimentData(json.load(open(Path(__file__).parents[0].joinpath("ExperimentalData.json"))),i))