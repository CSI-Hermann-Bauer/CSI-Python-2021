#gun = M700
#ammo = 7.62x51mm M993
#building == Popular center 75m
#horizontal disance == Velocity * time
##t = [V₀ * sin(α) + √((V₀ * sin(α))² + 2 * g * h)] / g
import math
import json
from pathlib import Path
from ExperimentData import ExperimentData
import os


# gun = "M700"
# ammo= "7.62x51mm M993"
# ammo_speed=910
# building="Popular Center"
# building_height_M =75
# g= 9.8


# experimetnalData = {"gun": "M700",
#     "ammo": "7.62x51mm M993",
#     "ammo_speed": 910,
#     "building": "Popular Center",
#     "building_height_M": 75,
#     "g": 9.8}
 # Parallel Lists

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

# Planet Index
planet = input("Planet Name: ")
planetIndex = int(planets.index(planet))

def calcDistance(experimentalData:ExperimentData, g:float):
       time_s = math.sqrt((2*experimentalData.building_height_M / g))
       distance_m = experimentalData.ammo_speed * time_s

       print(f"If you fire an {experimentalData.gun} using {experimentalData.ammo} bullets from the top of {experimentalData.building} " +
              f"which is {experimentalData.building_height_M} meters at an angle of 0 degrees," +
              f" the bullet will travel {round(time_s, 2)} seconds for a distance of " +
              f"{round(distance_m, 2)} meters \n")
myDataSet = [
ExperimentData("M700","7.62x51mm M993",910,"Burj Khalifa",828, 9.8, planet),
ExperimentData("M700","7.62x51mm M993",910,"Shanghai Tower",632, 9.8, planet),
ExperimentData("M700","7.62x51mm M993",910,"Lotte World Center",554.5, 9.8, planet),
ExperimentData("M700","7.62x51mm M993",910,"Bank of America Tower",365.8, 9.8, planet),
ExperimentData("M700","7.62x51mm M993",910,"Popular Center",75, 9.8, planet)]


for expdata in myDataSet:
       calcDistance(expdata, float(g_ms2[planetIndex]))


myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, 'ExperimentDatas.json')

with open(myOutputFilePath, 'w') as outfile:
       json.dump(myDataSet[1].__dict__, outfile)


# deserialize = open(myOutputFilePath)

# experimentJson = json.loads(deserialize)

# for e in experimentJson:
#        ExperimentData(**e).run()