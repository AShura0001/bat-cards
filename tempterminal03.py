import pygame
import os
import time
from sevendeadlysins import sevendeadlysins_index
import random

#colors
black = (0, 0, 0)
white = (255, 255, 255)
GREY2 = (204, 204, 204)
black_light = (26, 26, 26)
uni_red = (200, 0, 0)


big_window_size = (960, 560)
small_window_size = (360, 500)
main_file_directory = os.getcwd()


pygame.init()


def display_text(gwindow, text, color, x, y, font_size, Font):
    """This function is used to display text on the pygame gwindow at (x, y)"""
    
    #font object is defined for the text to be displayed.
    font = pygame.font.Font(
        os.path.join(os.getcwd(), "assets", "{0}.TTF".format(Font)),font_size)

    #text is rendered and stored in screen_text.
    screen_text = font.render(text, True, color)
    screen_text_rect = screen_text.get_rect(center = (x, y))
    gwindow.blit(screen_text, [x,y])
 
    #screen_text_rect is returned so that it can be used to check for
    #for further mouse events in other functions.
    return screen_text_rect

def test_window():
    window = pygame.display.set_mode((960,560))
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    flag = False
            if event.type == pygame.KEYDOWN:
                t = event.unicode
                print(t)
        
        dashboard_button = pygame.draw.rect(window, white,
                                    ((380, 400), (200, 80)))
        dashboard_txt = display_text(window, "Dashboard", black,
                                388, 420, 35, "OCRAEXT")

        pygame.display.update()

test_window()
pygame.quit()
