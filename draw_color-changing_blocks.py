#!/usr/bin/env python
# -*-encoding=utf8 -*-

import pygame
import math
import random

def draw_block_black(pos_width, pos_height, screen, r, g, b):
    for x in range(0, pos_width*50):
        for y in range((pos_height-1)*50, pos_height*50):
            screen.set_at([x, y], [r, g, b])

def draw_block_white(pos_width, pos_height, screen, r, g, b):
    for x in range((pos_width-1)*49, pos_width*50):
        for y in range(0, pos_height*50):
            screen.set_at([x, y], [r, g, b])

def main():

    pygame.init()
    win_width, win_height = 1000, 1000
    screen = pygame.display.set_mode((win_width, win_height))

    
    while 1:

        timer = 0
        pos_width, pos_height = 1, 1

        while 1:
    
            if pos_width < 20 or pos_height < 20:
                
        
                if timer == 0:
                    
                    screen.fill(0)
                    timer = 100

                    if pos_width == 20:
                        pos_width = 0
                        pos_height += 1

                        for h in range(0, pos_height):
                            draw_block_black(20, h, screen, random.randint(1, 255),\
                            random.randint(1, 255), random.randint(1, 255))

                        draw_block_black(pos_width, pos_height, screen, random.randint(1, 255),\
                        random.randint(1, 255), random.randint(1, 255))

                    else:
                        pos_width += 1
                        for h in range(0, pos_height):
                            draw_block_black(20, h, screen, random.randint(1, 255),\
                            random.randint(1, 255), random.randint(1, 255))
                        draw_block_black(pos_width, pos_height, screen, random.randint(1, 255),\
                        random.randint(1, 255), random.randint(1, 255))

                    
                    pygame.display.flip()
    
            else:
                break
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

            timer -= 1


        timer = 0
        pos_width, pos_height = 1, 1
    
        while 1:
    
            if pos_width < 20 or pos_height < 20:
                
                if timer == 0:
                    
                    screen.fill([255, 255, 255])
                    timer = 100

                    if pos_height == 20:
                        pos_height = 0
                        pos_width += 1
                        
                        for w in range(0, pos_width):
                            draw_block_white(w, 20, screen, random.randint(1, 255),\
                            random.randint(1, 255), random.randint(1, 255))

                        draw_block_white(pos_width, pos_height, screen, random.randint(1, 255),\
                        random.randint(1, 255), random.randint(1, 255))

                    else:
                        pos_height += 1
                        for w in range(0, pos_width):
                            draw_block_white(w, 20, screen, random.randint(1, 255),\
                            random.randint(1, 255), random.randint(1, 255))
                        draw_block_white(pos_width, pos_height, screen, random.randint(1, 255),\
                        random.randint(1, 255), random.randint(1, 255))

                    
                    pygame.display.flip()
    
            else:
                break
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

            timer -= 1

if __name__ == '__main__':
    main()
