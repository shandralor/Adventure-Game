"""Using function wait:

import keyboard

keyboard.wait("p")
print("You pressed p")

It will wait for you to press p and continue the code as it is pressed.

"""
import pygame
import os
#used to get date from a location(ex get images)

WIDTH, HEIGHT = 1600, 900
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
SBUTTON_W, SBUTTON_H = 570, 500

START_BUTTON = pygame.image.load(os.path.join('Assets', 'start-button.png'))
SBUTTON = pygame.transform.scale(START_BUTTON,(128,128))
BACKGROUND = pygame.image.load(os.path.join('Assets', 'game_background_4.png'))
BG = pygame.transform.scale(BACKGROUND, (1600, 900))


pygame.display.set_caption("Adventure Game")

FPS = 60

WHITE = (255, 255, 255)

def draw_window():
    WINDOW.blit(BACKGROUND, (0,0))
#blit draws a new surface(image or text) on the screen
    WINDOW.blit(SBUTTON, (SBUTTON_W, SBUTTON_H))
    pygame.display.update()

def main():
  #Set a clock object to control game speed  
    clock = pygame.time.Clock()
    run = True

    while run:

        clock.tick(FPS)
#check all possible events the in the game
        for event in pygame.event.get():
#Checking if user closed the window
            if event.type == pygame.QUIT:
                run = False
        draw_window()  



    pygame.quit()


#This makes sure the game only runs if this file(main.py)is run directly
if __name__ == "__main__":
    main()

