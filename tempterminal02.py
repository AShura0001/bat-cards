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

    current_card_nos_1 = 26
    current_card_nos_2 = 26

    initial_time_sec = 10*60

    vertical_scroll_bar_pos = 70
    horizontal_scroll_bar_pos = 56



    card_placement_holder_1 = pygame.image.load(os.path.join(main_file_directory, "assets", "card_placement_holder.png")).convert_alpha()
    card_placement_holder_1_rect = card_placement_holder_1.get_rect(center = (298, 250))
    
    card_placement_holder_2 = pygame.image.load(os.path.join(main_file_directory, "assets", "card_placement_holder.png")).convert_alpha()
    card_placement_holder_2_rect = card_placement_holder_2.get_rect(center = (487, 250))


    time_counter_bar_1 = pygame.image.load(os.path.join(main_file_directory, "assets", "time_counter_bar_1.png")).convert_alpha()
    time_counter_bar_1_rect = time_counter_bar_1.get_rect(center = (380, 169))
    
    time_counter_bar_2 = pygame.image.load(os.path.join(main_file_directory, "assets", "time_counter_bar_2.png")).convert_alpha()
    time_counter_bar_2_rect = time_counter_bar_2.get_rect(center = (380, 355))

    scroll_bar_vertical = pygame.image.load(os.path.join(main_file_directory, "assets", "scroll bar vertical GW2.png")).convert_alpha()
    scroll_bar_vertical_rect = scroll_bar_vertical.get_rect(center = (950, 285))

    scroll_bar_horizontal = pygame.image.load(os.path.join(main_file_directory, "assets", "scroll bar horizontal GW2.png")).convert_alpha()
    scroll_bar_horizontal_rect = scroll_bar_horizontal.get_rect(center = (378, 548))

    cards_title_GW2 = pygame.image.load(os.path.join(main_file_directory, "assets", "cards_title_GW2.png")).convert_alpha()
    cards_title_GW2_rect = cards_title_GW2.get_rect(center = (858, 16))

    GW2_side_menu_panel = pygame.image.load(os.path.join(main_file_directory, "assets", "GW2_side_menu_panel.png")).convert_alpha()
    GW2_side_menu_panel_rect = GW2_side_menu_panel.get_rect(center = (858, 280))

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
        gwindow_2.blit(scroll_bar_horizontal, scroll_bar_horizontal_rect)
        horizontal_scroll_bar_indicator = pygame.draw.circle(gwindow_2, uni_red, (horizontal_scroll_bar_pos, 548), 5)


        gwindow_2.blit(GW2_side_menu_panel, GW2_side_menu_panel_rect)
        gwindow_2.blit(cards_title_GW2, cards_title_GW2_rect)
        gwindow_2.blit(scroll_bar_vertical, scroll_bar_vertical_rect)
        
        vertical_scroll_bar_indicator = pygame.draw.circle(gwindow_2, uni_red, (950, vertical_scroll_bar_pos), 5)


        current_card_text_1 = display_text(gwindow_2, str(current_card_nos_1), white, 4, 155, 24, "OLDENGL")
        current_card_text_2 = display_text(gwindow_2, str(current_card_nos_2), white, 730, 342, 24, "OLDENGL")
        press_ESC_text = display_text(gwindow_2, "press ESC to exit", white, 19.55, 14.44, 17, "AGENCYR")
        pygame.display.update()
        
        # while initial_time_sec > 0:
        #     initial_time_sec -= 1
        #     time.sleep(1)
        #     minutes = (initial_time_sec // 60)
        #     seconds = (initial_time_sec % 60)
        #     print (minutes,":",  seconds)

game_p2(big_window_size, main_file_directory)
pygame.quit()