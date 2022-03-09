import pygame

#initialize imported pygame
pygame.init()
#sets window size
dis=pygame.display.set_mode((400,300))
#updates display
pygame.display.update()
#sets caption
pygame.display.set_caption('Snake game by Edureka')
#variable used in while loop 
game_over=False

#while loop to keep window open
while not game_over:
    for event in pygame.event.get():
        print(event) 
#clsoes display
pygame.quit()
#quits pygame
quit()