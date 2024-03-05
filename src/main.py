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

        pygame.display.flip()

        clock.tick(240)

pygame.display.set_caption("Game Start Screen")
start_screen()
pygame.display.set_caption("Game Running")
game_loop()

pygame.quit()
