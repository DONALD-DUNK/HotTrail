#Bennett Judd
import pygame
from block import block
from player import player
from time import sleep

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

def start_screen():
    screen.fill((0, 0, 0))
    hottrail = pygame.image.load('hottrail.gif')
    imac = hottrail.get_rect(center=(1920//2, 1080//2 -200))
    screen.blit(hottrail, imac) 

    
    text = font.render('Press any key to start the game', True, (255, 255, 255))
    text_rect = text.get_rect(center=(1920//2, 1080//2 + 100))
    screen.blit(text, text_rect)
    pygame.display.flip()
    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                wait = False


        

def game_loop():
    jump = 1
    jheight = 0
    lx = 0
    lvx = 0
    ly = 0
    lvy = 0
    ac = 0.03
    max_speed = 4
    max_acceleration = 0.5
    deceleration = 0.95
    grav = 1.5
    
    
    p1 = player(lx + 50, ly + 50)
   
    pygame.display.flip() 
    running = True
    while running:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
                running = False
        screen.fill((0,0,0))
        b1 = block(75,725)
        b2 = block(100,775)
        b3 = block(50,775)
     
  
        b1.load_image('Box.png', 50, 50)
        b1.display(screen)
        b2.load_image('Box.png', 50, 50)
        b2.display(screen)
        b3.load_image('Box.png', 50, 50)
        b3.display(screen)
        

        pygame.draw.line(screen, (255, 255, 255), (0, 825), (1920,825), 2)
   
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            
            lvx = min(lvx + ac, max_speed)
        elif keys[pygame.K_a]:
            
            lvx = max(lvx - ac, -max_speed)
        else:
            lvx *= deceleration

        if keys[pygame.K_w] |  keys[pygame.K_SPACE]:
            
            p1.y -= 2 * jump
            jheight += 10
            if jheight >= 100:
                jump -= 0.01
           
                              
        else:        
            jump = 1
            jheight = 0
        
        p1.y += lvy
        p1.x += lvx

        if p1.y < 800:
            grav += 1
        p1.y += int(0.02 * grav)
        if p1.y > 800:
            p1.y = 800
            grav = 1.5
        p1.display(screen)

        if p1.y >= (b1.y - (b1.height/2)) and p1.y <= (b1.y - (b1.height/2)+10) and p1.x >= (b1.x - b1.width/2) and p1.x <= (b1.x+25 + b1.width/2):

            p1.y = (b1.y - b1.height/2)
            grav = 0
        if p1.x >= ((b1.x - b1.width/2)-2) and p1.x < b1.x and p1.y > (b1.y - b1.height/2) and p1.y < (b1.y+50 + b1.height/2):
            p1.x = ((b1.x - b1.width/2)-2)
        if p1.x <= ((b1.x+25 + b1.width/2)+2) and p1.x > b1.x and p1.y > (b1.y - b1.height/2) and p1.y < (b1.y+50 + b1.height/2):
            p1.x = ((b1.x+25 + b1.width/2)+2)

        if p1.y >= (b2.y - (b2.height/2)) and p1.y <= (b2.y - (b2.height/2)+10) and p1.x >= (b2.x - b2.width/2) and p1.x <= (b2.x+25 + b2.width/2):

            p1.y = (b2.y - b2.height/2)
            grav = 0
        if p1.x >= ((b2.x - b2.width/2)-2) and p1.x < b2.x and p1.y > (b2.y - b2.height/2) and p1.y < (b2.y+50 + b2.height/2):
            p1.x = ((b2.x - b2.width/2)-2)
        if p1.x <= ((b2.x+25 + b2.width/2)+2) and p1.x > b2.x and p1.y > (b2.y - b2.height/2) and p1.y < (b2.y+50 + b2.height/2):
            p1.x = ((b2.x+25 + b2.width/2)+2)


        if p1.y >= (b3.y - (b3.height/2)) and p1.y <= (b3.y - (b3.height/2)+10) and p1.x >= (b3.x - b3.width/2) and p1.x <= (b3.x+25 + b3.width/2):

            p1.y = (b3.y - b3.height/2)
            grav = 0
        if p1.x >= ((b3.x - b3.width/2)-2) and p1.x < b3.x and p1.y > (b3.y - b3.height/2) and p1.y < (b3.y+50 + b3.height/2):
            p1.x = ((b3.x - b3.width/2)-2)
        if p1.x <= ((b3.x+25 + b3.width/2)+2) and p1.x > b3.x and p1.y > (b3.y - b3.height/2) and p1.y < (b3.y+50 + b3.height/2):
            p1.x = ((b3.x+25 + b3.width/2)+2)    
        
       
        
          
        pygame.display.flip()
        print(b1.y + (b1.height/2))
       

       

        clock.tick(240)

pygame.display.set_caption("Game Start Screen")
start_screen()
pygame.display.set_caption("Game Running")
game_loop()

pygame.quit()
