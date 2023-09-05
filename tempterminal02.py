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

    card_placement_holder_1 = pygame.image.load(os.path.join(main_file_directory, "assets", "card_placement_holder.png")).convert_alpha()
    card_placement_holder_1_rect = card_placement_holder_1.get_rect(center = (298, 250))
    
    card_placement_holder_2 = pygame.image.load(os.path.join(main_file_directory, "assets", "card_placement_holder.png")).convert_alpha()
    card_placement_holder_2_rect = card_placement_holder_2.get_rect(center = (487, 250))


    time_counter_bar_1 = pygame.image.load(os.path.join(main_file_directory, "assets", "time_counter_bar_1.png")).convert_alpha()
    time_counter_bar_1_rect = time_counter_bar_1.get_rect(center = (380, 169))
    
    time_counter_bar_2 = pygame.image.load(os.path.join(main_file_directory, "assets", "time_counter_bar_2.png")).convert_alpha()
    time_counter_bar_2_rect = time_counter_bar_2.get_rect(center = (380, 355))

    while event_flag:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                event_flag = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    event_flag = False

        gwindow_2.blit(card_placement_holder_1, card_placement_holder_1_rect)
        gwindow_2.blit(card_placement_holder_2, card_placement_holder_2_rect)
        gwindow_2.blit(time_counter_bar_1, time_counter_bar_1_rect)
        gwindow_2.blit(time_counter_bar_2, time_counter_bar_2_rect)

        press_ESC_text = display_text(gwindow_2, "press ESC to exit", white, 19.55, 14.44, 17, "AGENCYR")
        pygame.display.update()

game_p2(big_window_size, main_file_directory)
pygame.quit()