import pygame
import time
import random

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

#define function for game
def gameLoop():
    game_over=False
    game_close = False
    #variables updating the snake coordinates
    x1 = dis_width/2
    y1 = dis_height/2
    x1_change = 0       
    y1_change = 0

    #add food location variables at random 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

#while loop to keep window open
    while not game_over:
        #WHAT TO DO IF CLOSE   
        while game_close == True:
            #background white
            dis.fill(white)
            #print You lost
            message("You Lost! Press Q-Quit or C-Play Again", red)
            #update display
            pygame.display.update()
            #check events
            for event in pygame.event.get():
                #chek letter hit and act accordingly 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        #check events and update locations according to key
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
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
        #loose if hit border
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        #change variables
        x1 += x1_change
        y1 += y1_change
        #fill background white
        dis.fill(white)
        #add food
        pygame.draw.rect(dis, "blue", [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        #update display
        pygame.display.update()
        #print "yummy" if snake over food
        if x1 == foodx and y1 == foody:
            print("Yummy!!")
        #snake speed
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()

