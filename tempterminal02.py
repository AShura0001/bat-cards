import pygame
import os
import time

#colors
black = (0, 0, 0)
white = (255, 255, 255)
GREY2 = (204, 204, 204)
uni_red = (200, 0, 0)


big_window_size = (960, 560)
small_window_size = (360, 500)
main_file_directory = os.getcwd()


pygame.init()

def display_text(gwindow, text, color, x, y, font_size, Font):
    font = pygame.font.Font(os.path.join(os.getcwd(), "assets", "{0}.TTF".format(Font)), font_size)
    screen_text = font.render(text, True, color)
    screen_text_rect = screen_text.get_rect(center = (x, y))
    gwindow.blit(screen_text, [x,y])
    return screen_text_rect


def game_p2(window_size , main_file_directory):
    gwindow_2 = pygame.display.set_mode(window_size)
    gwindow_2.fill(black)
    event_flag = True

    while event_flag:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                event_flag = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    event_flag = False

        press_ESC_text = display_text(gwindow_2, "press ESC to exit", white, 29.55, 24.44, 27, "AGENCYR")
        pygame.display.update()

game_p2(big_window_size, main_file_directory)
pygame.quit()