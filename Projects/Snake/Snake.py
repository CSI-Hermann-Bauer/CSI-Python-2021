import pygame

#initialize imported pygame
pygame.init()

#define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

#sets window size
dis=pygame.display.set_mode((800,600))
#updates display
pygame.display.update()
#sets caption
pygame.display.set_caption('Snake game by Edureka')
#variable used in while loop 
game_over=False

#variables updating the snake coordinates
x1 = 300
y1 = 300
 
x1_change = 0       
y1_change = 0

#clock to keep time
clock = pygame.time.Clock()

#while loop to keep window open
while not game_over:
    #get events and loop through them
    for event in pygame.event.get():
        #make window close if close button is pushed
        if event.type==pygame.QUIT:
            game_over = True
        #If key is pushed, update the coordinates accordint to key pushed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
    #update coordinates by adding the change
 
    x1 += x1_change
    y1 += y1_change
    #fill with white
    dis.fill(white)
    #add a new rectangle
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])
    #update display
    pygame.display.update()
    #sleep for a while
    clock.tick(30)
#clsoes display
pygame.quit()
#quits pygame
quit()