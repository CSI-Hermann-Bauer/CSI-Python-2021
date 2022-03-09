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
    #get events and loop through them
    for event in pygame.event.get():
        #make window close if close button is pushed
        if event.type==pygame.QUIT:
            game_over=True
    #draw snake
    pygame.draw.rect(dis, "blue" ,[200,150,10,10])
    pygame.display.update()
#clsoes display
pygame.quit()
#quits pygame
quit()