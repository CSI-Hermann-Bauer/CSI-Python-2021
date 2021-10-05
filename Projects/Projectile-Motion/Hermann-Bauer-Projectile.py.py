#gun = M700
#ammo = 7.62x51mm M993
#building == Popular center 75m

#horizontal disance == Velocity * time

##t = [V₀ * sin(α) + √((V₀ * sin(α))² + 2 * g * h)] / g

import math
angle = 0
gun = "M700"
ammo = "7.62x51mm M993"
ammo_speed = 910
building = "Popular Center"
building_height_M = 75
g = 9.8


t = (ammo_speed * math.sin(angle) + math.sqrt((ammo_speed * math.sin(angle))**2 + 2 * g * building_height_M)) / g

distance = ammo_speed*t

print(f"If you fire an {gun} using {ammo} bullets from the top of {building}" +
       f"which is {building_height_M} meters at an angle of {angle} degrees," +
       f" the bullet will travel {round(t, 2)} seconds for a distance of " +
       f"{round(distance, 2)} meters")