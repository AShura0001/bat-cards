import pygame
import os
import time
from sevendeadlysins import sevendeadlysins_index


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
    font = pygame.font.Font(os.path.join(os.getcwd(), 
                                         "assets", "{0}.TTF".format(Font)), 
                                         font_size)
    screen_text = font.render(text, True, color)
    screen_text_rect = screen_text.get_rect(center = (x, y))
    gwindow.blit(screen_text, [x,y])
    return screen_text_rect


def game_p2(window_size , main_file_directory):
    gwindow_2 = pygame.display.set_mode(window_size)
    gwindow_2.fill(black)
    event_flag = True
    vertical_indicator_flag = False
    horizontal_indicator_flag = False

    current_card_nos_1 = 26
    current_card_nos_2 = 26
    mark_value_vertical = 1
    mark_value_horizontal = 1

    initial_time_sec = 10*60

    vertical_scroll_bar_pos = 70
    horizontal_scroll_bar_pos = 56

    card_placement_holder_1 = pygame.image.load(os.path.join(main_file_directory,"assets", "card_placement_holder.png")).convert_alpha()
    card_placement_holder_1_rect = card_placement_holder_1.get_rect(center = (278, 250))
    
    card_placement_holder_2 = pygame.image.load(os.path.join(main_file_directory, "assets", "card_placement_holder.png")).convert_alpha()
    card_placement_holder_2_rect = card_placement_holder_2.get_rect(center = (487, 250))


    time_counter_bar_1 = pygame.image.load(os.path.join(main_file_directory, "assets", "time_counter_bar_1.png")).convert_alpha()
    time_counter_bar_1_rect = time_counter_bar_1.get_rect(center = (380, 169))
    
    time_counter_bar_2 = pygame.image.load(os.path.join(main_file_directory, "assets", "time_counter_bar_2.png")).convert_alpha()
    time_counter_bar_2_rect = time_counter_bar_2.get_rect(center = (380, 355))

    scroll_bar_vertical = pygame.image.load(os.path.join(main_file_directory, "assets", "scroll bar vertical GW2.png")).convert_alpha()
    scroll_bar_vertical_rect = scroll_bar_vertical.get_rect(center = (950, 285))
    vertical_end_upper_rect = pygame.Rect((940 , 32), (20, 12))
    vertical_end_lower_rect = pygame.Rect((940 , 523), (20, 12))

    scroll_bar_horizontal = pygame.image.load(os.path.join(main_file_directory, "assets", "scroll bar horizontal GW2.png")).convert_alpha()
    scroll_bar_horizontal_rect = scroll_bar_horizontal.get_rect(center = (378, 548))
    horizontal_end_left_rect = pygame.Rect((0 , 538), (22, 20))
    horizontal_end_right_rect = pygame.Rect((738 , 538), (22, 20))

    cards_title_GW2 = pygame.image.load(os.path.join(main_file_directory, "assets", "cards_title_GW2.png")).convert_alpha()
    cards_title_GW2_rect = cards_title_GW2.get_rect(center = (858, 16))

    GW2_side_menu_panel = pygame.image.load(os.path.join(main_file_directory, "assets", "GW2_side_menu_panel.png")).convert_alpha()
    GW2_side_menu_panel_rect = GW2_side_menu_panel.get_rect(center = (858, 280))

    chosen_attribute = pygame.image.load(os.path.join(main_file_directory, "assets", "chosen_attribute.png")).convert_alpha()
    chosen_attribute_rect = chosen_attribute.get_rect(center = (384, 345))

    place_button = pygame.image.load(os.path.join(main_file_directory, "assets", "place_button.png")).convert_alpha()
    place_button_rect = place_button.get_rect(center = (385, 263))

    vertical_bar_markings = [(70 + (36*i)) for i in range(0, 13)]
    horizontal_bar_markings = [(56 + (54*i)) for i in range(0, 13)]

    while event_flag:
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


        gwindow_2.blit(chosen_attribute, chosen_attribute_rect)
        gwindow_2.blit(place_button, place_button_rect)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                event_flag = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    event_flag = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # print (pygame.mouse.get_pos())
                if scroll_bar_vertical_rect.collidepoint(event.pos):
                    vertical_indicator_flag = True
                    horizontal_indicator_flag = False
                if scroll_bar_horizontal_rect.collidepoint(event.pos):
                    horizontal_indicator_flag = True
                    vertical_indicator_flag = False
                if (vertical_end_upper_rect.collidepoint(event.pos) and vertical_scroll_bar_pos > 70):
                    vertical_scroll_bar_pos -= 36
                    mark_value_vertical -= 1
                if vertical_end_lower_rect.collidepoint(event.pos) and vertical_scroll_bar_pos < 502:
                    vertical_scroll_bar_pos += 36
                    mark_value_vertical += 1
                if horizontal_end_left_rect.collidepoint(event.pos) and horizontal_scroll_bar_pos > 56:
                    horizontal_scroll_bar_pos -= 54
                    mark_value_horizontal -= 1
                if horizontal_end_right_rect.collidepoint(event.pos) and horizontal_scroll_bar_pos < 704:
                    horizontal_scroll_bar_pos += 54
                    mark_value_horizontal += 1

            if event.type == pygame.MOUSEBUTTONUP:
                vertical_indicator_flag = False
                horizontal_indicator_flag = False
            
            if vertical_indicator_flag:
                mouse = pygame.mouse.get_pos()
                if mouse[1] in vertical_bar_markings:
                    vertical_scroll_bar_pos = mouse[1]
                elif  event.type == pygame.MOUSEMOTION and event.rel[1] > 0:
                    for marking in vertical_bar_markings[1:]:
                        if mouse[1] < marking:
                            vertical_scroll_bar_pos = marking - 36
                            mark_value_vertical = vertical_bar_markings.index(marking)
                            break
                elif  event.type == pygame.MOUSEMOTION and event.rel[1] < 0:
                    for marking in vertical_bar_markings[:-1:-1]:
                        if mouse[1] > marking:
                            vertical_scroll_bar_pos = marking + 36
                            mark_value_vertical = vertical_bar_markings.index(marking)
                            break
            
            if horizontal_indicator_flag:
                mouse = pygame.mouse.get_pos()
                if mouse[0] in horizontal_bar_markings:
                    horizontal_scroll_bar_pos = mouse[0]
                elif  event.type == pygame.MOUSEMOTION and event.rel[0] > 0:
                    for marking in horizontal_bar_markings[1:]:
                        if mouse[0] < marking:
                            horizontal_scroll_bar_pos = marking - 54
                            mark_value_horizontal = horizontal_bar_markings.index(marking)
                            break
                elif  event.type == pygame.MOUSEMOTION and event.rel[0] < 0:
                    for marking in horizontal_bar_markings[:-1:-1]:
                        if mouse[0] > marking:
                            horizontal_scroll_bar_pos = marking + 54
                            mark_value_horizontal = horizontal_bar_markings.index(marking)
                            break
            
        
        attack_power_rect_btn = pygame.draw.rect(gwindow_2, black_light, ((19, 203), (196 , 32)))
        health_power_rect_btn = pygame.draw.rect(gwindow_2, black_light, ((19, 244), (196 , 32)))
        defense_power_rect_btn = pygame.draw.rect(gwindow_2, black_light, ((19, 285), (196 , 32)))

        attack_power_text = display_text(gwindow_2, "Attack Power", white, 36, 203, 29, "COLONNA")
        health_power_text = display_text(gwindow_2, "Health Power", white, 36, 244, 29, "COLONNA")
        defense_power_text = display_text(gwindow_2, "Defense Power", white, 27, 285, 29, "COLONNA")

        rank_rect_btn = pygame.draw.rect(gwindow_2, black_light, ((551, 203), (196 , 32)))
        speed_power_rect_btn = pygame.draw.rect(gwindow_2, black_light, ((551, 244), (196 , 32)))
        battle_IQ_rect_btn = pygame.draw.rect(gwindow_2, black_light, ((551, 285), (196 , 32)))

        rank_text = display_text(gwindow_2, "Rank", white, 616, 203, 29, "COLONNA")
        speed_power_text = display_text(gwindow_2, "Speed Power", white, 573, 244, 29, "COLONNA")
        battle_IQ_text = display_text(gwindow_2, "Battle IQ", white, 598, 285, 29, "COLONNA")

        current_card_no_text_1 = display_text(gwindow_2, str(current_card_nos_1), white, 4, 155, 24, "OLDENGL")
        current_card_no_text_2 = display_text(gwindow_2, str(current_card_nos_2), white, 730, 342, 24, "OLDENGL")
        press_ESC_text = display_text(gwindow_2, "press ESC to exit", white, 19.55, 14.44, 17, "AGENCYR")
        

        print(mark_value_horizontal, mark_value_vertical)
        pygame.display.update()
        
        # while initial_time_sec > 0:
        #     initial_time_sec -= 1
        #     time.sleep(1)
        #     minutes = (initial_time_sec // 60)
        #     seconds = (initial_time_sec % 60)
        #     print (minutes,":",  seconds)

game_p2(big_window_size, main_file_directory)
pygame.quit()