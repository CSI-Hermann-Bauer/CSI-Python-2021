import pygame
import time

#initialize imported pygame
pygame.init()

#define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

#define dimentions
dis_width = 800
dis_height  = 600

#sets window size
dis = pygame.display.set_mode((dis_width, dis_width))

#define x1 and x 2 as half of the width and len
x1 = dis_width/2
y1 = dis_height/2
 
#set size for snake block
snake_block=10

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
#set speed for snake
snake_speed = 30

#set font
font_style = pygame.font.SysFont(None, 50)
 
 #output message
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

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
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

#chec if snake leaves and if so end game
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True
    #update coordinates by adding the change
    x1 += x1_change
    y1 += y1_change
    #fill background  with white
    dis.fill(white)
    #add a new rectangle
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])
    #update display
    pygame.display.update()
    #sleep for a while
    clock.tick(snake_speed)

#print you lost
message("You lost",red)
#umpdate display
pygame.display.update()
#sleep
time.sleep(2)
#clsoes display
pygame.quit()
#quits pygame
quit()