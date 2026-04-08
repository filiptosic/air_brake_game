import sys
import pygame
import time
import math

clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Air Brake Game")
screen = pygame.display.set_mode((900, 720))
pygame.key.set_repeat(2000, 1000)
radar_len = 50
radar = (100,100)
radar_len = 50
angle = 0
while True:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_1]:
        print("pressed")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        screen.fill((0, 0, 0))
        radar = (100,100)
        
        x = radar[0] + math.cos(math.radians(angle)) * radar_len
        y = radar[1] + math.sin(math.radians(angle)) * radar_len

        # then render the line radar->(x,y)
        pygame.draw.line(screen, ("red"), radar, (x,y), 1)
        pygame.draw.rect(screen, (255, 0, 0), (0, 0, 100, 100)) 
        pygame.draw.line(screen, (0, 0, 255), (0, 0), (100, 50), 7)
        pygame.display.flip()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                angle += 10
                print("hello world")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                print("hello world")
    clock.tick(60)