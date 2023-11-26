import pygame
import os
import time
from sevendeadlysins import sevendeadlysins_index
import random

#colors
black = (0, 0, 0)
black_light = (51, 51, 51)
white = (255, 255, 255)
GREY1 = (204, 204, 204)
uni_red = (200, 0, 0)



def display_text(gwindow, text, color, x, y, font_size, Font):
    font = pygame.font.Font(os.path.join(os.getcwd(), "assets", "{0}.TTF".format(Font)), font_size)
    screen_text = font.render(text, True, color)
    screen_text_rect = screen_text.get_rect(center = (x, y))
    gwindow.blit(screen_text, [x,y])
    return screen_text_rect


def support_window(window_size, main_file_directory):
    supp_window = pygame.display.set_mode(window_size, pygame.NOFRAME)
    event_flag = True
    discord_flag = False
    report_a_bug_flag = False

    supp_window.fill((black))
    discord_support_icon = pygame.image.load(os.path.join(main_file_directory, "assets", "discord_support_icon.png")).convert_alpha()
    discord_support_icon_rect = discord_support_icon.get_rect(center=(180, 180))

    report_a_bug_icon = pygame.image.load(os.path.join(main_file_directory, "assets", "report_a_bug_support_icon.png")).convert_alpha()
    report_a_bug_icon_rect = report_a_bug_icon.get_rect(center=(180, 304))

    red_cross = pygame.image.load(os.path.join(main_file_directory, "assets", "red_cross.png")).convert_alpha()
    red_cross_rect = red_cross.get_rect(center=(15, 16))

    while event_flag:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    event_flag = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if discord_support_icon_rect.collidepoint(event.pos):
                    discord_flag = True
                    report_a_bug_flag = False
                elif report_a_bug_icon_rect.collidepoint(event.pos):
                    report_a_bug_flag = True
                    discord_flag = False
                elif red_cross_rect.collidepoint(event.pos):
                    event_flag = False
                else:
                    discord_flag = False
                    report_a_bug_flag = False
                
        
        supp_window.blit(discord_support_icon, discord_support_icon_rect)
        supp_window.blit(report_a_bug_icon, report_a_bug_icon_rect)
        supp_window.blit(red_cross, red_cross_rect)
        pygame.display.update()

def dashboard_window(window_size, main_file_directory, user_id_text_stored, user_password_text_stored):
    dashboard_window = pygame.display.set_mode(window_size)
    event_flag = True

    Play_flag = False
    Inventory_flag = False
    Shop_flag = False
    Guide_flag = False
    Setting_flag = False
    Logs_flag = False

    exit_dashboard_btn = pygame.image.load(os.path.join(main_file_directory, "assets", "exit_dashboard_btn.png")).convert_alpha()
    exit_dashboard_btn_rect = exit_dashboard_btn.get_rect(center=(480, 468))

    dashboard_window.fill((black))
    while event_flag:

        if Play_flag:
            Play_flag = False
            mode_selector(window_size, main_file_directory, user_id_text_stored, user_password_text_stored)
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                event_flag = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    event_flag = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_dashboard_btn_rect.collidepoint(event.pos):
                    event_flag = False
                elif white_rectangle_1.collidepoint(event.pos):
                    Play_flag = True
                    Inventory_flag = False
                    Shop_flag = False
                    Guide_flag = False
                    Setting_flag = False
                    Logs_flag = False

                elif white_rectangle_2.collidepoint(event.pos):
                    Play_flag = False
                    Inventory_flag = True
                    Shop_flag = False
                    Guide_flag = False
                    Setting_flag = False
                    Logs_flag = False
                
                elif white_rectangle_3.collidepoint(event.pos):
                    Play_flag = False
                    Inventory_flag = False
                    Shop_flag = True
                    Guide_flag = False
                    Setting_flag = False
                    Logs_flag = False
                
                elif white_rectangle_4.collidepoint(event.pos):
                    Play_flag = False
                    Inventory_flag = False
                    Shop_flag = False
                    Guide_flag = True
                    Setting_flag = False
                    Logs_flag = False
                
                elif white_rectangle_5.collidepoint(event.pos):
                    Play_flag = False
                    Inventory_flag = False
                    Shop_flag = False
                    Guide_flag = False
                    Setting_flag = True
                    Logs_flag = False
                
                elif white_rectangle_6.collidepoint(event.pos):
                    Play_flag = False
                    Inventory_flag = False
                    Shop_flag = False
                    Guide_flag = False
                    Setting_flag = False
                    Logs_flag = True
                
                else:
                    Play_flag = False
                    Inventory_flag = False
                    Shop_flag = False
                    Guide_flag = False
                    Setting_flag = False
                    Logs_flag = False

        white_rectangle_1 = pygame.draw.rect(dashboard_window, white, ((260,297), (216, 35)))
        white_rectangle_2 = pygame.draw.rect(dashboard_window, white, ((260,341), (216, 35)))
        white_rectangle_3 = pygame.draw.rect(dashboard_window, white, ((260,385), (216, 35)))

        white_rectangle_4 = pygame.draw.rect(dashboard_window, white, ((480,297), (216, 35)))
        white_rectangle_5 = pygame.draw.rect(dashboard_window, white, ((480,341), (216, 35)))
        white_rectangle_6 = pygame.draw.rect(dashboard_window, white, ((480,385), (216, 35)))

        dashboard_window.blit(exit_dashboard_btn, exit_dashboard_btn_rect)

        bat_text = display_text(dashboard_window, "B.A.T", white, 339, 144, 100, "OLDENGL")
        cards_text = display_text(dashboard_window, "CARDS", white, 430, 240.5, 36, "COLONNA")
        press_ESC_text = display_text(dashboard_window, "press ESC to exit", white, 19.55, 14.44, 17, "AGENCYR")

        Play_btn_text = display_text(dashboard_window, "Play", black, 336.26, 300, 28, "ARLRDBD")
        Inventory_btn_text = display_text(dashboard_window, "Inventory", black, 300, 345, 28, "ARLRDBD")
        Shop_btn_text = display_text(dashboard_window, "Shop", black, 338.47, 390, 28, "ARLRDBD")

        Guide_btn_text = display_text(dashboard_window, "Guide", black, 545, 300, 28, "ARLRDBD")
        Setting_btn_text = display_text(dashboard_window, "Setting", black, 535, 345, 28, "ARLRDBD")
        Logs_btn_text = display_text(dashboard_window, "Logs", black, 550, 390, 28, "ARLRDBD")
        
        # print(Play_flag, Inventory_flag, Shop_flag, Guide_flag, Setting_flag, Logs_flag)
        pygame.display.update()

def mode_selector(window_size, main_file_directory, user_id_text_stored, user_password_text_stored):
    mode_selector_window = pygame.display.set_mode(window_size)
    mode_selector_window.fill(black)

    solo_btn_image = pygame.image.load(os.path.join(main_file_directory, "assets", "solo_mode_btn.png")).convert_alpha()
    solo_btn_image_rect = solo_btn_image.get_rect(center = (342, 300))

    multiplayer_btn_image = pygame.image.load(os.path.join(main_file_directory, "assets", "multiplayer_mode_btn.png")).convert_alpha()
    multiplayer_btn_image_rect = multiplayer_btn_image.get_rect(center = (610, 300))
    event_flag = True
    solo_mode_flag = False
    multiplayer_mode_flag = False


    while event_flag:
        if solo_mode_flag:
            solo_mode_flag = False
            solo_menu_selector(window_size, main_file_directory, user_id_text_stored, user_password_text_stored)
            break
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                event_flag = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    event_flag = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if solo_btn_image_rect.collidepoint(event.pos):
                    solo_mode_flag = True
                    multiplayer_mode_flag = False
                elif multiplayer_btn_image_rect.collidepoint(event.pos):
                    multiplayer_mode_flag = True
                    solo_mode_flag = False

        mode_selector_window.blit(solo_btn_image, solo_btn_image_rect)
        mode_selector_window.blit(multiplayer_btn_image, multiplayer_btn_image_rect)
        
        press_ESC_text = display_text(mode_selector_window, "press ESC to exit", white, 19.55, 14.44, 17, "AGENCYR")
        Choose_mode_text = display_text(mode_selector_window, "Choose A Mode", white, 194.83, 170, 90, "OLDENGL")
        pygame.display.update()

def solo_menu_selector(window_size, main_file_directory, user_id_text_stored, user_password_text_stored):
    solo_menu_window = pygame.display.set_mode(window_size)
    solo_menu_window.fill(black)
    event_flag = True
    free_play_flag = False

    universes_btn_image = pygame.image.load(os.path.join(main_file_directory, "assets", "universes_btn.png")).convert_alpha()
    universes_btn_image_rect = universes_btn_image.get_rect(center = (602, 350))
    free_play_btn_image = pygame.image.load(os.path.join(main_file_directory, "assets", "free_play_btn.png")).convert_alpha()
    free_play_btn_image_rect = free_play_btn_image.get_rect(center = (355, 350))
    while event_flag:

        if free_play_flag:
            free_play_flag = False
            game_p1(window_size, main_file_directory, user_id_text_stored, user_password_text_stored)
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                event_flag = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    event_flag = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if universes_btn_image_rect.collidepoint(event.pos):
                    continue
                if free_play_btn_image_rect.collidepoint(event.pos):
                    free_play_flag = True
        
        text_1 = display_text(solo_menu_window, "FREE PLAY ONLY VERSION [seven deadly sins deck]", uni_red, (window_size[0]//2)-300, (window_size[1]- 150), 20, "OCRAEXT")
        solo_menu_window.blit(universes_btn_image, universes_btn_image_rect)
        solo_menu_window.blit(free_play_btn_image, free_play_btn_image_rect)
        press_ESC_text = display_text(solo_menu_window, "press ESC to exit", white, 19.55, 14.44, 17, "AGENCYR")
        Solo_menu_text = display_text(solo_menu_window, "Solo Menu", white, 270, 190, 90, "OLDENGL")
        pygame.display.update()

def game_p1(window_size , main_file_directory, user_id_text_stored, user_password_text_stored):
    gwindow_1 = pygame.display.set_mode(window_size)
    gwindow_1.fill(black)
    event_flag = True
    start_flag = False
    pause_flag = False




    start_btn_game_window = pygame.image.load(os.path.join(main_file_directory, "assets", "start_btn_game_window.png")).convert_alpha()
    start_btn_game_window_rect = start_btn_game_window.get_rect(center = (480, 500))

    pause_btn = pygame.image.load(os.path.join(main_file_directory, "assets", "pause_btn.png")).convert_alpha()
    pause_btn_rect = pause_btn.get_rect(center = (917, 25))

    while event_flag:

        if start_flag:
            time.sleep(2)
            start_flag = False
            result =  game_p2(window_size, main_file_directory, user_id_text_stored, user_password_text_stored)
            break
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                event_flag = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    event_flag = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_btn_game_window_rect.collidepoint(event.pos):
                    start_flag = True
                if pause_btn_rect.collidepoint(event.pos):
                    pause_flag = True


        for i in range (0, 13):
            h = 75
            w = 45
            # pygame.draw.rect(gwindow_1, uni_red, [(30 + (70*i), 60), (w, h)])
            # pygame.draw.rect(gwindow_1, uni_red, [(30 + (70*i), 160), (w, h)])
            # pygame.draw.rect(gwindow_1, uni_red, [(30 + (70*i), 260), (w, h)])
            # pygame.draw.rect(gwindow_1, uni_red, [(30 + (70*i), 360), (w, h)])
            card_1 = pygame.image.load(sevendeadlysins_index[i+1].card_image).convert_alpha()
            card_1 = pygame.transform.scale(card_1, (w, h))
            gwindow_1.blit(card_1, (30 + (70*i), 60))
            card_2 = pygame.image.load(sevendeadlysins_index[i+2].card_image).convert_alpha()
            card_2 = pygame.transform.scale(card_2, (w, h))
            gwindow_1.blit(card_2, (30 + (70*i), 160))
            card_3 = pygame.image.load(sevendeadlysins_index[i+3].card_image).convert_alpha()
            card_3 = pygame.transform.scale(card_3, (w, h))
            gwindow_1.blit(card_3, (30 + (70*i), 260))
            card_4 = pygame.image.load(sevendeadlysins_index[i+4].card_image).convert_alpha()
            card_4 = pygame.transform.scale(card_4, (w, h))
            gwindow_1.blit(card_4, (30 + (70*i), 360))

        gwindow_1.blit(start_btn_game_window, start_btn_game_window_rect)
        gwindow_1.blit(pause_btn, pause_btn_rect)
        press_ESC_text = display_text(gwindow_1, "press ESC to exit", white, 19.55, 14.44, 17, "AGENCYR")
        pygame.display.update()

def game_p2(window_size , main_file_directory, user_id_text_stored, user_password_text_stored):
    gwindow_2 = pygame.display.set_mode(window_size)
    gwindow_2.fill(black)
    event_flag = True
    event_flag_2 = False


    current_turn = True
    chosen_attribute_index = 0
    attribute_flag = False
    card_holder_flag_1 = True
    card_holder_flag_2 = True
    place_card_flag_1 = False
    place_card_flag_2 = False
    card_lock_1 = False
    card_lock_2 = False
    attribute_lock_2 = False
    attribute_lock_1 = False
    turn_flag = True
    

    chosen_card_index = 0

    rank_usable_flag = True
    attack_usable_flag = True
    health_usable_flag = True
    defense_usable_flag = True
    speed_usable_flag = True
    battle_IQ_usable_flag = True


    num_cards_avl = 16
    card_set_1 = []
    card_set_2 = []
    card_won_set_1 = []
    card_won_set_2 = []

    while (len(card_set_1) < 26) :
        card_rank_a = random.randint(1, 52)
        if (card_rank_a not in card_set_1):
            card_set_1.append(card_rank_a)

    while (len(card_set_2) < 26) :
        card_rank_b = random.randint(1, 52)
        if (card_rank_b not in card_set_1) and (card_rank_b not in card_set_2):
            card_set_2.append(card_rank_b)

    card_set_1.sort()
    card_set_2.sort()
    horizontal_indicator_flag = False

    mark_value_horizontal = 0

    initial_time_sec = 10*60

    horizontal_scroll_bar_pos = 56

    card_placement_holder_1 = pygame.image.load(os.path.join(main_file_directory,"assets", "card_placement_holder.png")).convert_alpha()
    card_placement_holder_1_rect = card_placement_holder_1.get_rect(center = (278, 250))  
    
    card_placement_holder_2 = pygame.image.load(os.path.join(main_file_directory, "assets", "card_placement_holder.png")).convert_alpha()
    card_placement_holder_2_rect = card_placement_holder_2.get_rect(center = (487, 250))


    time_counter_bar_1 = pygame.image.load(os.path.join(main_file_directory, "assets", "time_counter_bar_1.png")).convert_alpha()
    time_counter_bar_1_rect = time_counter_bar_1.get_rect(center = (380, 169))
    
    time_counter_bar_2 = pygame.image.load(os.path.join(main_file_directory, "assets", "time_counter_bar_2.png")).convert_alpha()
    time_counter_bar_2_rect = time_counter_bar_2.get_rect(center = (380, 355))

    scroll_bar_horizontal = pygame.image.load(os.path.join(main_file_directory, "assets", "scroll bar horizontal GW2.png")).convert_alpha()
    scroll_bar_horizontal_rect = scroll_bar_horizontal.get_rect(center = (378, 548))
    horizontal_end_left_rect = pygame.Rect((0 , 538), (22, 20))
    horizontal_end_right_rect = pygame.Rect((738 , 538), (22, 20))

    cards_title_GW2 = pygame.image.load(os.path.join(main_file_directory, "assets", "cards_title_GW2.png")).convert_alpha()
    cards_title_GW2_rect = cards_title_GW2.get_rect(center = (858, 16))

    GW2_side_menu_panel = pygame.image.load(os.path.join(main_file_directory, "assets", "GW2_side_menu_panel.png")).convert_alpha()
    GW2_side_menu_panel_rect = GW2_side_menu_panel.get_rect(center = (858, 280))

    chosen_attribute_bg = pygame.image.load(os.path.join(main_file_directory, "assets", "chosen_attribute.png")).convert_alpha()
    chosen_attribute_bg_rect = chosen_attribute_bg.get_rect(center = (384, 345))

    attribute_values_bg = pygame.image.load(os.path.join(main_file_directory, "assets", "attribute_values_bg.png")).convert_alpha()
    attribute_values_bg_rect = attribute_values_bg.get_rect(center = (382, 171))

    place_button = pygame.image.load(os.path.join(main_file_directory, "assets", "place_button.png")).convert_alpha()
    place_button_rect = place_button.get_rect(center = (385, 263))

    opponent_card_back = pygame.image.load(os.path.join(main_file_directory, "assets", "opponent_card_back.png")).convert_alpha()

    horizontal_bar_markings = [(56 + (54*i)) for i in range(0, 13)]
    
    chosen_attribute_final_value = ""
    chosen_attribute_final_value_cpu = ""

    attributes_list = ["", "Rank", "ATK", "HP", "DP", "SP", "IQ"]
    while event_flag:
        for i in range (0, 6):
            opponent_card_back_rect = opponent_card_back.get_rect(center = (70+(i*120), 84))
            gwindow_2.blit(opponent_card_back, opponent_card_back_rect)

        if len(card_set_1)>0 and len(card_set_2)>0:

            gwindow_2.blit(attribute_values_bg, attribute_values_bg_rect)
            if card_holder_flag_1:
                gwindow_2.blit(card_placement_holder_1, card_placement_holder_1_rect)
            if card_holder_flag_2:
                gwindow_2.blit(card_placement_holder_2, card_placement_holder_2_rect)
            gwindow_2.blit(time_counter_bar_1, time_counter_bar_1_rect)
            gwindow_2.blit(time_counter_bar_2, time_counter_bar_2_rect)
            gwindow_2.blit(scroll_bar_horizontal, scroll_bar_horizontal_rect)
            horizontal_scroll_bar_indicator = pygame.draw.circle(gwindow_2, uni_red, (horizontal_scroll_bar_pos, 548), 5)


            gwindow_2.blit(GW2_side_menu_panel, GW2_side_menu_panel_rect)
            gwindow_2.blit(cards_title_GW2, cards_title_GW2_rect)

            chosen_attribute_final = attributes_list[chosen_attribute_index]


            gwindow_2.blit(chosen_attribute_bg, chosen_attribute_bg_rect)
            gwindow_2.blit(place_button, place_button_rect)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    event_flag = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        event_flag = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # print(event.pos)
                    if scroll_bar_horizontal_rect.collidepoint(event.pos):
                        horizontal_indicator_flag = True
                    if horizontal_end_left_rect.collidepoint(event.pos) and horizontal_scroll_bar_pos > 56:
                        horizontal_scroll_bar_pos -= 54
                        mark_value_horizontal = horizontal_bar_markings.index(horizontal_scroll_bar_pos)
                        pygame.draw.rect(gwindow_2, black, ((104, 140),(231, 181) ))
                        pygame.draw.rect(gwindow_2, black, ((0, 379), (757 , 159)))
                        card_holder_flag_1 = True
                        card_indexes_2.clear()
                    if horizontal_end_right_rect.collidepoint(event.pos) and horizontal_scroll_bar_pos < 704:
                        horizontal_scroll_bar_pos += 54
                        mark_value_horizontal = horizontal_bar_markings.index(horizontal_scroll_bar_pos)
                        pygame.draw.rect(gwindow_2, black, ((104, 140),(231, 181) ))
                        pygame.draw.rect(gwindow_2, black, ((0, 379), (757 , 159)))
                        card_holder_flag_1 = True
                        card_indexes_2.clear()
                    
                    if not card_lock_1 and turn_flag:
                            
                        if not attribute_lock_1 and current_turn:
                            
                            if rank_rect_btn.collidepoint(event.pos):
                                chosen_attribute_index = 1
                                chosen_attribute_final_value = sevendeadlysins_index[card_indexes_2[chosen_card_index]].rank
                                attribute_flag = True
                            if attack_power_rect_btn.collidepoint(event.pos):
                                chosen_attribute_index = 2
                                chosen_attribute_final_value = sevendeadlysins_index[card_indexes_2[chosen_card_index]].ATK
                                attribute_flag = True
                            if health_power_rect_btn.collidepoint(event.pos):
                                chosen_attribute_index = 3
                                chosen_attribute_final_value = sevendeadlysins_index[card_indexes_2[chosen_card_index]].HP
                                attribute_flag = True
                            if defense_power_rect_btn.collidepoint(event.pos):
                                chosen_attribute_index = 4
                                chosen_attribute_final_value = sevendeadlysins_index[card_indexes_2[chosen_card_index]].DP
                                attribute_flag = True
                            if speed_power_rect_btn.collidepoint(event.pos):
                                chosen_attribute_index = 5
                                chosen_attribute_final_value = sevendeadlysins_index[card_indexes_2[chosen_card_index]].SP
                                attribute_flag = True
                            if battle_IQ_rect_btn.collidepoint(event.pos):
                                chosen_attribute_index = 6
                                chosen_attribute_final_value = sevendeadlysins_index[card_indexes_2[chosen_card_index]].IQ
                                attribute_flag = True
        

        
                        if card_1_rect.collidepoint(event.pos):
                            card_holder_flag_1 = False
                            gwindow_2.blit(card_1, card_placement_holder_1_rect)
                            chosen_card_index = 0

                        if card_2_rect.collidepoint(event.pos):
                            card_holder_flag_1 = False
                            gwindow_2.blit(card_2, card_placement_holder_1_rect)
                            chosen_card_index = 1
                        if card_3_rect.collidepoint(event.pos):
                            card_holder_flag_1 = False
                            chosen_card_index = 2
                            gwindow_2.blit(card_3, card_placement_holder_1_rect)
                        if card_4_rect.collidepoint(event.pos):
                            card_holder_flag_1 = False
                            gwindow_2.blit(card_4, card_placement_holder_1_rect)
                            chosen_card_index = 3

                        if not card_holder_flag_1:
                            rank_usable_flag = sevendeadlysins_index[card_indexes_2[chosen_card_index]].rank_flag
                            attack_usable_flag = sevendeadlysins_index[card_indexes_2[chosen_card_index]].atk_flag
                            health_usable_flag = sevendeadlysins_index[card_indexes_2[chosen_card_index]].hp_flag
                            defense_usable_flag = sevendeadlysins_index[card_indexes_2[chosen_card_index]].dp_flag
                            speed_usable_flag = sevendeadlysins_index[card_indexes_2[chosen_card_index]].sp_flag
                            battle_IQ_usable_flag = sevendeadlysins_index[card_indexes_2[chosen_card_index]].iq_flag
                            if chosen_attribute_index == 1 and rank_usable_flag:
                                attribute_check = True
                                chosen_attribute_final_value = sevendeadlysins_index[card_indexes_2[chosen_card_index]].rank
                            if chosen_attribute_index == 2 and attack_usable_flag:
                                attribute_check = True
                                chosen_attribute_final_value = sevendeadlysins_index[card_indexes_2[chosen_card_index]].ATK
                            if chosen_attribute_index == 3 and health_usable_flag:
                                attribute_check = True
                                chosen_attribute_final_value = sevendeadlysins_index[card_indexes_2[chosen_card_index]].HP
                            if chosen_attribute_index == 4 and defense_usable_flag:
                                attribute_check = True
                                chosen_attribute_final_value = sevendeadlysins_index[card_indexes_2[chosen_card_index]].DP
                            if chosen_attribute_index == 5 and speed_usable_flag:
                                attribute_check = True
                                chosen_attribute_final_value = sevendeadlysins_index[card_indexes_2[chosen_card_index]].SP
                            if chosen_attribute_index == 6 and battle_IQ_usable_flag:
                                attribute_check = True
                                chosen_attribute_final_value = sevendeadlysins_index[card_indexes_2[chosen_card_index]].IQ

                        
                        if place_button_rect.collidepoint(event.pos) and attribute_flag and current_turn and attribute_check:
                            # print("w2")
                            place_card_flag_1 = True
                            attribute_flag = True
                            
                            if chosen_attribute_index == 1:
                                sevendeadlysins_index[card_indexes_2[chosen_card_index]].rank_flag = False
                            if chosen_attribute_index == 2:
                                sevendeadlysins_index[card_indexes_2[chosen_card_index]].atk_flag = False
                            if chosen_attribute_index == 3:
                                sevendeadlysins_index[card_indexes_2[chosen_card_index]].hp_flag = False
                            if chosen_attribute_index == 4:
                                sevendeadlysins_index[card_indexes_2[chosen_card_index]].dp_flag = False
                            if chosen_attribute_index == 5:
                                sevendeadlysins_index[card_indexes_2[chosen_card_index]].sp_flag = False
                            if chosen_attribute_index == 6:
                                sevendeadlysins_index[card_indexes_2[chosen_card_index]].iq_flag = False    

                            # current_turn = False
                            card_lock_1 = True
                            turn_flag = False

                        if place_button_rect.collidepoint(event.pos) and attribute_flag and not current_turn and attribute_check :
                            place_card_flag_1 = True
                            attribute_flag = True
                            # print("w1")                        
                            if chosen_attribute_index == 1:
                                sevendeadlysins_index[card_indexes_2[chosen_card_index]].rank_flag = False
                            if chosen_attribute_index == 2:
                                sevendeadlysins_index[card_indexes_2[chosen_card_index]].atk_flag = False
                            if chosen_attribute_index == 3:
                                sevendeadlysins_index[card_indexes_2[chosen_card_index]].hp_flag = False
                            if chosen_attribute_index == 4:
                                sevendeadlysins_index[card_indexes_2[chosen_card_index]].dp_flag = False
                            if chosen_attribute_index == 5:
                                sevendeadlysins_index[card_indexes_2[chosen_card_index]].sp_flag = False
                            if chosen_attribute_index == 6:
                                sevendeadlysins_index[card_indexes_2[chosen_card_index]].iq_flag = False
                            
                            attribute_lock_1 = False
                            card_lock_1 = True
                            current_turn = True
                            card_lock_2 = False
                            

                        if place_button_rect.collidepoint(event.pos) and not attribute_check:
                            # print("Attribute not usable")
                            display_text(gwindow_2, "Attribute not usable", uni_red, 385, 263, 12, "OCRAEXT")
                            
                    if show_whole_deck_rect.collidepoint(event.pos):
                        event_flag_2 = True
                        m = 1
                        screen = pygame.display.set_mode([640, 480])
                        while event_flag_2:
                            screen.fill(black)
                            for event_2 in pygame.event.get():
                                if event_2.type == pygame.QUIT:
                                    event_flag_2 = False
                                    pygame.draw.rect(screen, black, ((0, 0), (640, 480)))
                                    time.sleep(0.1)
                                    gwindow_2 = pygame.display.set_mode([960, 560])
                                elif event_2.type == pygame.KEYDOWN:
                                    if event_2.key == pygame.K_ESCAPE:
                                        event_flag_2 = False
                                        pygame.draw.rect(screen, black, ((0, 0), (640, 480)))
                                        time.sleep(0.1)
                                        gwindow_2 = pygame.display.set_mode([960, 560])
                                elif event_2.type == pygame.MOUSEBUTTONDOWN:
                                    # print(event_2.pos)
                                    if back_rect.collidepoint(event_2.pos) and m>1:
                                        m -= 1
                                    elif next_rect.collidepoint(event_2.pos) and m<52:
                                        m += 1
                            if event_flag_2:
                                back_rect = pygame.draw.rect(screen, white, ((180, 390), (80, 40)))
                                back_text = display_text(screen, 'Back', black, 200, 400, 20, "AGENCYR")
                                next_rect = pygame.draw.rect(screen, white, ((400, 390), (80, 40)))
                                next_text = display_text(screen, 'Next', black, 425, 400, 20, "AGENCYR")
                                image = pygame.image.load(sevendeadlysins_index[m].card_image).convert_alpha()
                                name = sevendeadlysins_index[m].name
                                title = sevendeadlysins_index[m].title
                                form = sevendeadlysins_index[m].form
                                rank = sevendeadlysins_index[m].rank
                                atk = sevendeadlysins_index[m].ATK
                                hp = sevendeadlysins_index[m].HP
                                dp = sevendeadlysins_index[m].DP
                                sp = sevendeadlysins_index[m].SP
                                iq = sevendeadlysins_index[m].IQ

                                display_text(screen, (name+' - '+form), white, 215, 200, 20, "ARLRDBD")
                                display_text(screen, ("["+title+"]"), white, 215, 221, 12, "ARLRDBD")
                                display_text(screen, "rank: {}".format(rank), white, 200, 270, 15, "OCRAEXT")
                                display_text(screen, "ATK: {}".format(atk), white, 200, 305, 15, "OCRAEXT")
                                display_text(screen, "HP: {}".format(hp), white, 200, 340, 15, "OCRAEXT")
                                display_text(screen, "DP: {}".format(dp), white, 380, 270, 15, "OCRAEXT")
                                display_text(screen, "SP: {}".format(sp), white, 380, 305, 15, "OCRAEXT")
                                display_text(screen, "IQ: {}".format(iq), white, 380, 340, 15, "OCRAEXT")
                                image = pygame.transform.scale(image, (104, 150))
                                screen.blit(image, [280, 50])
                            pygame.display.flip()
                            time.sleep(0.1)
                                    

                if event.type == pygame.MOUSEBUTTONUP:
                    horizontal_indicator_flag = False
                
                
                if horizontal_indicator_flag:
                    mouse = pygame.mouse.get_pos()
                    if mouse[0] in horizontal_bar_markings:
                        horizontal_scroll_bar_pos = mouse[0]
                    elif  event.type == pygame.MOUSEMOTION and event.rel[0] > 0:
                        for marking in horizontal_bar_markings[1:]:
                            if mouse[0] < marking:
                                horizontal_scroll_bar_pos = marking - 54
                                mark_value_horizontal = horizontal_bar_markings.index(horizontal_scroll_bar_pos)
                                pygame.draw.rect(gwindow_2, black, ((104, 140),(231, 181) ))
                                pygame.draw.rect(gwindow_2, black, ((0, 379), (757 , 159)))
                                
                                card_holder_flag_1 = True
                                card_indexes_2.clear()
                                break
                    elif  event.type == pygame.MOUSEMOTION and event.rel[0] < 0:
                        for marking in horizontal_bar_markings[:-1:-1]:
                            if mouse[0] > marking:
                                horizontal_scroll_bar_pos = marking + 54
                                mark_value_horizontal = horizontal_bar_markings.index(horizontal_scroll_bar_pos)                    
                                pygame.draw.rect(gwindow_2, black, ((104, 140),(231, 181) ))
                                pygame.draw.rect(gwindow_2, black, ((0, 379), (757 , 159)))
                                card_holder_flag_1 = True
                                card_indexes_2.clear()
                                break
                
            
            attack_power_rect_btn = pygame.draw.rect(gwindow_2, black_light, ((19, 203), (196 , 32)))
            health_power_rect_btn = pygame.draw.rect(gwindow_2, black_light, ((19, 244), (196 , 32)))
            defense_power_rect_btn = pygame.draw.rect(gwindow_2, black_light, ((19, 285), (196 , 32)))

            if attack_usable_flag:
                attack_power_text = display_text(gwindow_2, "Attack Power", white, 36, 203, 29, "COLONNA")
            if health_usable_flag:    
                health_power_text = display_text(gwindow_2, "Health Power", white, 36, 244, 29, "COLONNA")
            if defense_usable_flag:
                defense_power_text = display_text(gwindow_2, "Defense Power", white, 27, 285, 29, "COLONNA")

            rank_rect_btn = pygame.draw.rect(gwindow_2, black_light, ((551, 203), (196 , 32)))
            speed_power_rect_btn = pygame.draw.rect(gwindow_2, black_light, ((551, 244), (196 , 32)))
            battle_IQ_rect_btn = pygame.draw.rect(gwindow_2, black_light, ((551, 285), (196 , 32)))

            if rank_usable_flag:
                rank_text = display_text(gwindow_2, "Rank", white, 616, 203, 29, "COLONNA")
            if speed_usable_flag:
                speed_power_text = display_text(gwindow_2, "Speed Power", white, 573, 244, 29, "COLONNA")
            if battle_IQ_usable_flag:
                battle_IQ_text = display_text(gwindow_2, "Battle IQ", white, 598, 285, 29, "COLONNA")

            current_card_no_text_1 = display_text(gwindow_2, str(len(card_set_1) + len(card_won_set_1)), white, 730, 342, 24, "OLDENGL")
            current_card_no_text_2 = display_text(gwindow_2, str(len(card_set_2) + len(card_won_set_2)), white, 4, 155, 24, "OLDENGL")
            press_ESC_text = display_text(gwindow_2, "press ESC to exit", white, 19.55, 14.44, 17, "AGENCYR")
            
        
            card_indexes_2 = []
            for i in range((mark_value_horizontal*4) , ((mark_value_horizontal+1)*5)): 
                try:
                    card_indexes_2.append(card_set_1[i])
                except:
                    pass
            
            if len(card_indexes_2) == 0:
                pygame.draw.rect(gwindow_2, black, ((0, 379), (757 , 159)))
            if len(card_indexes_2) > 0:
                pygame.draw.rect(gwindow_2, black, ((0, 379), (757 , 159)))
                card_1 = pygame.image.load(sevendeadlysins_index[card_indexes_2[0]].card_image).convert_alpha()
                card_1 = pygame.transform.scale(card_1, (104, 140))
                card_1_rect = card_1.get_rect(center = (98+(200*0), 456))
                card_1_name_info = display_text(gwindow_2, (sevendeadlysins_index[card_indexes_2[0]].name + " [{}]".format(sevendeadlysins_index[card_indexes_2[0]].form)), white, 760, 35, 12, "OCRAEXT")
                card_1_rank = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[0]].rank), white, 830, 72+(40*0), 12, "OCRAEXT")
                card_1_attack = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[0]].ATK), white, 820, 72+(40*1), 12, "OCRAEXT")
                card_1_health = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[0]].HP), white, 820, 72+(40*2), 12, "OCRAEXT")
                card_1_defense = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[0]].DP), white, 923, 72+(40*0), 12, "OCRAEXT")
                card_1_speed = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[0]].SP), white, 923, 72+(40*1), 12, "OCRAEXT")
                card_1_battle_IQ = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[0]].IQ), white, 923, 72+(40*2), 12, "OCRAEXT")
                gwindow_2.blit(card_1, card_1_rect)

            if len(card_indexes_2) > 1:
                card_2 = pygame.image.load(sevendeadlysins_index[card_indexes_2[1]].card_image).convert_alpha()
                card_2 = pygame.transform.scale(card_2, (104, 140))
                card_2_rect = card_2.get_rect(center = (98+(200*1), 456))
                card_2_name_info = display_text(gwindow_2, (sevendeadlysins_index[card_indexes_2[1]].name + " [{}]".format(sevendeadlysins_index[card_indexes_2[1]].form)), white, 760, 182, 12, "OCRAEXT")
                card_2_rank = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[1]].rank), white, 830, 212+(32*0), 12, "OCRAEXT")
                card_2_attack = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[1]].ATK), white, 820, 212+(32*1), 12, "OCRAEXT")
                card_2_health = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[1]].HP), white, 820, 212+(32*2), 12, "OCRAEXT")
                card_2_defense = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[1]].DP), white, 923, 212+(32*0), 12, "OCRAEXT")
                card_2_speed = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[1]].SP), white, 923, 212+(32*1), 12, "OCRAEXT")
                card_2_battle_IQ = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[1]].IQ), white, 923, 212+(32*2), 12, "OCRAEXT")
                gwindow_2.blit(card_2, card_2_rect)
            

            if len(card_indexes_2) > 2: 
                card_3 = pygame.image.load(sevendeadlysins_index[card_indexes_2[2]].card_image).convert_alpha()
                card_3 = pygame.transform.scale(card_3, (104, 140))
                card_3_rect = card_1.get_rect(center = (98+(200*2), 456))
                card_3_name_info = display_text(gwindow_2, (sevendeadlysins_index[card_indexes_2[2]].name + " [{}]".format(sevendeadlysins_index[card_indexes_2[2]].form)), white, 760, 305, 12, "OCRAEXT")
                card_3_rank = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[2]].rank), white, 830, 332+(32*0), 12, "OCRAEXT")
                card_3_attack = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[2]].ATK), white, 820, 332+(32*1), 12, "OCRAEXT")
                card_3_health = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[2]].HP), white, 820, 332+(32*2), 12, "OCRAEXT")
                card_3_defense = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[2]].DP), white, 923, 332+(32*0), 12, "OCRAEXT")
                card_3_speed = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[2]].SP), white, 923, 332+(32*1), 12, "OCRAEXT")
                card_3_battle_IQ = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[2]].IQ), white, 923, 332+(32*2), 12, "OCRAEXT")
                gwindow_2.blit(card_3, card_3_rect)


            if len(card_indexes_2) > 3:
                card_4 = pygame.image.load(sevendeadlysins_index[card_indexes_2[3]].card_image).convert_alpha()
                card_4 = pygame.transform.scale(card_4, (104, 140))
                card_4_rect = card_1.get_rect(center = (98+(200*3), 456))
                card_4_name_info = display_text(gwindow_2, (sevendeadlysins_index[card_indexes_2[3]].name + " [{}]".format(sevendeadlysins_index[card_indexes_2[3]].form)), white, 760, 424, 12, "OCRAEXT")
                card_4_rank = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[3]].rank), white, 830, 450+(32*0), 12, "OCRAEXT")
                card_4_attack = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[3]].ATK), white, 820, 450+(32*1), 12, "OCRAEXT")
                card_4_health = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[3]].HP), white, 820, 450+(32*2), 12, "OCRAEXT")
                card_4_defense = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[3]].DP), white, 923, 450+(32*0), 12, "OCRAEXT")
                card_4_speed = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[3]].SP), white, 923, 450+(32*1), 12, "OCRAEXT")
                card_4_battle_IQ = display_text(gwindow_2, str(sevendeadlysins_index[card_indexes_2[3]].IQ), white, 923, 450+(32*2), 12, "OCRAEXT")
                gwindow_2.blit(card_4, card_4_rect)
            
            display_text(gwindow_2, chosen_attribute_final, black, 359, 335, 20, "OCRAEXT")
            if not card_holder_flag_1:
                display_text(gwindow_2, str(chosen_attribute_final_value), black, 260, 164, 18, "OCRAEXT")        
            if not card_holder_flag_2:    
                display_text(gwindow_2, str(chosen_attribute_final_value_cpu), black, 466, 164, 18, "OCRAEXT")

            if not turn_flag and not attribute_lock_2:
                available_attribute_values = []
                for cpu_cards in card_set_2: 
                    if chosen_attribute_index == 1:
                        available_attribute_values.append(int(sevendeadlysins_index[cpu_cards].rank))
                    if chosen_attribute_index == 2:
                        available_attribute_values.append(sevendeadlysins_index[cpu_cards].ATK)
                    if chosen_attribute_index == 3:
                        available_attribute_values.append(sevendeadlysins_index[cpu_cards].HP)
                    if chosen_attribute_index == 4:
                        available_attribute_values.append(sevendeadlysins_index[cpu_cards].DP)
                    if chosen_attribute_index == 5:
                        available_attribute_values.append(sevendeadlysins_index[cpu_cards].SP)
                    if chosen_attribute_index == 6:
                        available_attribute_values.append(sevendeadlysins_index[cpu_cards].IQ)

                if chosen_attribute_index == 1:
                    chosen_card_index_cpu = available_attribute_values.index(min(available_attribute_values))
                elif chosen_attribute_index in range (2, 7):
                    chosen_card_index_cpu = available_attribute_values.index(max(available_attribute_values))

                card_holder_flag_2 = False
                attribute_lock_2 = True
                chosen_cpu_card_image = pygame.image.load(sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].card_image).convert_alpha()
                chosen_cpu_card_image = pygame.transform.scale(chosen_cpu_card_image, (104, 140))
                card_lock_2 = True

            if card_lock_2:
                gwindow_2.blit(chosen_cpu_card_image, card_placement_holder_2_rect)     
            
            if attribute_lock_2 and card_lock_1:
                time.sleep(2)
                if chosen_attribute_index == 1:
                    if int(sevendeadlysins_index[card_indexes_2[chosen_card_index]].rank) > int(sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].rank):
                        # print(sevendeadlysins_index[card_indexes_2[chosen_card_index-1]].rank, sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].rank)
                        card_won_set_1.append(card_set_2[chosen_card_index_cpu])
                        card_won_set_1.append(card_indexes_2[chosen_card_index])
                        # print (sevendeadlysins_index[card_indexes_2[chosen_card_index]].name)
                        # print (sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].name)
                        card_set_1.remove(card_indexes_2[chosen_card_index])
                        card_set_2.remove(card_set_2[chosen_card_index_cpu])
                        # print("Player 1 wins this card")
                        pygame.draw.rect(gwindow_2, black, ((104, 140),(231, 181) ))
                        pygame.draw.rect(gwindow_2, black, ((104, 140),(435, 181) ))
                        card_holder_flag_1 = True
                        card_holder_flag_2 = True
                        card_lock_1 = False
                    elif int(sevendeadlysins_index[card_indexes_2[chosen_card_index]].rank) < int(sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].rank): 
                        # print(sevendeadlysins_index[card_indexes_2[chosen_card_index-1]].rank, sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].rank)
                        card_won_set_2.append(card_indexes_2[chosen_card_index])
                        card_won_set_2.append(card_set_2[chosen_card_index_cpu])
                        # print (sevendeadlysins_index[card_indexes_2[chosen_card_index]].name)
                        # print (sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].name)
                        card_set_1.remove(card_indexes_2[chosen_card_index])
                        card_set_2.remove(card_set_2[chosen_card_index_cpu])
                        # print("Player 2 wins this card")
                        pygame.draw.rect(gwindow_2, black, ((104, 140),(231, 181) ))
                        pygame.draw.rect(gwindow_2, black, ((104, 140),(435, 181) ))
                        card_holder_flag_1 = True
                        card_holder_flag_2 = True
                        card_lock_1 = False
                if chosen_attribute_index in range (2, 7):
                    # print(len(card_indexes_2))
                    # print(chosen_card_index)
                    if sevendeadlysins_index[card_indexes_2[chosen_card_index]].ATK > sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].ATK:
                        # print(sevendeadlysins_index[card_indexes_2[chosen_card_index-1]].ATK, sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].ATK)
                        card_won_set_1.append(card_set_2[chosen_card_index_cpu])
                        card_won_set_1.append(card_indexes_2[chosen_card_index])
                        # print (sevendeadlysins_index[card_indexes_2[chosen_card_index]].name)
                        # print (sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].name)
                        card_set_1.remove(card_indexes_2[chosen_card_index])
                        card_set_2.remove(card_set_2[chosen_card_index_cpu])
                        # print("Player 1 wins this card")
                        pygame.draw.rect(gwindow_2, black, ((104, 140),(231, 181) ))
                        pygame.draw.rect(gwindow_2, black, ((104, 140),(435, 181) ))
                        card_holder_flag_1 = True
                        card_holder_flag_2 = True
                        card_lock_1 = False
                    elif sevendeadlysins_index[card_indexes_2[chosen_card_index]].ATK < sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].ATK: 
                        # print(sevendeadlysins_index[card_indexes_2[chosen_card_index-1]].ATK, sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].ATK)
                        card_won_set_2.append(card_indexes_2[chosen_card_index])
                        card_won_set_2.append(card_set_2[chosen_card_index_cpu])
                        # print (sevendeadlysins_index[card_indexes_2[chosen_card_index]].name)
                        # print (sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].name)
                        card_set_1.remove(card_indexes_2[chosen_card_index])
                        card_set_2.remove(card_set_2[chosen_card_index_cpu])
                        # print("Player 2 wins this card")
                        pygame.draw.rect(gwindow_2, black, ((104, 140),(231, 181) ))
                        pygame.draw.rect(gwindow_2, black, ((104, 140),(435, 181) ))
                        card_holder_flag_1 = True
                        card_holder_flag_2 = True
                        card_lock_1 = False
                
                
                if not turn_flag and len(card_set_2)> 0:
                    chosen_attribute_index = random.randint(1, 6)
                    chosen_attribute_final = attributes_list[chosen_attribute_index]
                    display_text(gwindow_2, chosen_attribute_final, black, 359, 335, 20, "OCRAEXT")
                    available_attribute_values = []
                    available_attribute_values.clear()
                    for cpu_cards in card_set_2: 
                        if chosen_attribute_index == 1:
                            available_attribute_values.append(int(sevendeadlysins_index[cpu_cards].rank))
                        if chosen_attribute_index == 2:
                            available_attribute_values.append(sevendeadlysins_index[cpu_cards].ATK)
                        if chosen_attribute_index == 3:
                            available_attribute_values.append(sevendeadlysins_index[cpu_cards].HP)
                        if chosen_attribute_index == 4:
                            available_attribute_values.append(sevendeadlysins_index[cpu_cards].DP)
                        if chosen_attribute_index == 5:
                            available_attribute_values.append(sevendeadlysins_index[cpu_cards].SP)
                        if chosen_attribute_index == 6:
                            available_attribute_values.append(sevendeadlysins_index[cpu_cards].IQ)
                    
                    choice_luck = random.randint(1, 100)
                    if choice_luck == 11 or choice_luck == 8:
                        if chosen_attribute_index == 1:
                            non_choosing_card_index_cpu = available_attribute_values.index(min(available_attribute_values))
                            card_set_2.remove(card_set_2[non_choosing_card_index_cpu])
                            for cpu_cards in card_set_2:
                                available_attribute_values.append(int(sevendeadlysins_index[cpu_cards].rank))
                            chosen_card_index_cpu = random.randint(1, len(available_attribute_values))
                            chosen_attribute_final_value_cpu = sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].rank
                        
                        elif chosen_attribute_index in range (2, 7):
                            non_choosing_card_index_cpu = available_attribute_values.index(max(available_attribute_values))
                            card_set_2.remove(card_set_2[non_choosing_card_index_cpu])
                            for cpu_cards in card_set_2:
                                if chosen_attribute_index == 2:
                                    available_attribute_values.append(sevendeadlysins_index[cpu_cards].ATK)
                                if chosen_attribute_index == 3:
                                    available_attribute_values.append(sevendeadlysins_index[cpu_cards].HP)
                                if chosen_attribute_index == 4:
                                    available_attribute_values.append(sevendeadlysins_index[cpu_cards].DP)
                                if chosen_attribute_index == 5:
                                    available_attribute_values.append(sevendeadlysins_index[cpu_cards].SP)
                                if chosen_attribute_index == 6:
                                    available_attribute_values.append(sevendeadlysins_index[cpu_cards].IQ)
                            chosen_card_index_cpu = random.randint(1, len(available_attribute_values))
                            if chosen_attribute_index == 2:
                                chosen_attribute_final_value_cpu = sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].ATK
                            if chosen_attribute_index == 3:
                                chosen_attribute_final_value_cpu = sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].HP
                            if chosen_attribute_index == 4:
                                chosen_attribute_final_value_cpu = sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].DP
                            if chosen_attribute_index == 5:
                                chosen_attribute_final_value_cpu = sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].SP
                            if chosen_attribute_index == 6:
                                chosen_attribute_final_value_cpu = sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].IQ
                    
                    elif choice_luck%2 == 0:
                        if chosen_attribute_index == 1:
                            chosen_card_index_cpu = random.randint(1, len(available_attribute_values))
                            chosen_attribute_final_value_cpu = sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].rank
                        elif chosen_attribute_index in range (2, 7):
                            chosen_card_index_cpu = random.randint(1, len(available_attribute_values))
                            if chosen_attribute_index == 2:
                                chosen_attribute_final_value_cpu = sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].ATK
                            if chosen_attribute_index == 3:
                                chosen_attribute_final_value_cpu = sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].HP
                            if chosen_attribute_index == 4:
                                chosen_attribute_final_value_cpu = sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].DP
                            if chosen_attribute_index == 5:
                                chosen_attribute_final_value_cpu = sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].SP
                            if chosen_attribute_index == 6:
                                chosen_attribute_final_value_cpu = sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].IQ

                    else:
                        if chosen_attribute_index == 1:
                            chosen_card_index_cpu = available_attribute_values.index(min(available_attribute_values))
                            chosen_attribute_final_value_cpu = sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].rank
                        elif chosen_attribute_index in range (2, 7):
                            chosen_card_index_cpu = available_attribute_values.index(max(available_attribute_values))
                            if chosen_attribute_index == 2:
                                chosen_attribute_final_value_cpu = sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].ATK
                            if chosen_attribute_index == 3:
                                chosen_attribute_final_value_cpu = sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].HP
                            if chosen_attribute_index == 4:
                                chosen_attribute_final_value_cpu = sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].DP
                            if chosen_attribute_index == 5:
                                chosen_attribute_final_value_cpu = sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].SP
                            if chosen_attribute_index == 6:
                                chosen_attribute_final_value_cpu = sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].IQ


                    time.sleep(2)
                    card_holder_flag_2 = False
                    attribute_lock_2 = True
                    card_lock_1 = False
                    attribute_lock_1 = True
                    turn_flag = True
                    current_turn = False
                    # print (sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].name)
                    chosen_cpu_card_image = pygame.image.load(sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].card_image).convert_alpha()
                    chosen_cpu_card_image = pygame.transform.scale(chosen_cpu_card_image, (104, 140))
                    card_lock_2 = True
            show_whole_deck_rect = pygame.draw.rect(gwindow_2, black_light, ((760, 540), (195, 20)))
            display_text(gwindow_2, "Show whole deck", white, 780, 540, 17, "OCRAEXT")
        else:
            gwindow_2.fill(black)
            display_text(gwindow_2, "GAME OVER", white, 300, 200, 50, "COLONNA")
            
            if (len(card_won_set_1) + len(card_set_1)) > (len(card_won_set_2) + len(card_set_2)):
                display_text(gwindow_2, "Player 1 wins", white, 300, 300, 50, "COLONNA")
                win = True
            elif (len(card_won_set_1) + len(card_set_1)) < (len(card_won_set_2) + len(card_set_2)):
                display_text(gwindow_2, "Player 2 wins", white, 300, 300, 50, "COLONNA")
                loss = True
                user_data_packets[3] = "losses = {}\n".format(int(data_set[3])+1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    event_flag = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        event_flag = False
            

    
        pygame.display.flip()
    user_info = open(os.path.join(main_file_directory, "users", "{0}.batdata".format(user_id_text_stored)), "a+")
    user_info.seek(0)
    user_data_packets = user_info.readlines()
    data_set = []
    for packet in user_data_packets:
        data = packet.split(" = ")
        data_set.append(data[1])

    if win:
        user_data_packets[2] = "wins = {}\n".format(int(data_set[2])+1)
    elif loss:
        user_data_packets[3] = "losses = {}\n".format(int(data_set[3])+1)
    user_info.close()

def login_page(big_window_size, small_window_size, main_file_directory):
    gwindow = pygame.display.set_mode(big_window_size)
    arrow_login_page = pygame.image.load(os.path.join(main_file_directory, "assets", "arrow_login_page.png")).convert_alpha()
    arrow_login_page_rect = arrow_login_page.get_rect(center=(668.5, 300.5))
    user_id_text = ""
    user_id_text_stored = ""
    id_writing_flag = False
    user_password_text = ""
    user_password_text_stored = ""
    password_writing_flag = False

    support_logo = pygame.image.load(os.path.join(main_file_directory, "assets", "support_logo.png")).convert_alpha()
    support_logo = pygame.transform.scale(support_logo, (47, 47))
    support_logo_rect = support_logo.get_rect(center = (936.5 ,536.5))
    gwindow.fill(black)
    event_flag = True

    enter_user_id_flag = False
    enter_password_flag = False
    submit_flag = False
    support_flag = False

    user_id_rect = pygame.draw.rect(gwindow, white, [206.66, 240.32, 435, 33])
    user_password_rect = pygame.draw.rect(gwindow, white, [206.66, 287, 435, 33])
    arrow_login_circle = pygame.draw.circle(gwindow, white, (671, 301), 21)
    
    while event_flag:

        if support_flag:
            support_window(small_window_size, main_file_directory)
            support_flag = False
            event_flag = False
            login_page(big_window_size, small_window_size, main_file_directory)
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                event_flag = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    event_flag = False
                
                if event.key == pygame.K_RETURN and password_writing_flag:
                    submit_flag = True
                    enter_user_id_flag = False
                    enter_password_flag = False
                    id_writing_flag = False
                    password_writing_flag = False

                # if event.key == pygame.K_TAB and id_writing_flag:
                #     enter_user_id_flag = False
                #     id_writing_flag = False
                #     enter_password_flag = True
                #     password_writing_flag = True
                
                # if event.key == pygame.K_TAB and password_writing_flag:
                #     enter_password_flag = False
                #     password_writing_flag = False
                #     enter_user_id_flag = True
                #     id_writing_flag = True


                if event.key == pygame.K_BACKSPACE:
                    if enter_user_id_flag:
                        user_id_text = user_id_text[:-1]
                        user_id_text_stored = user_id_text_stored[:-1]
                    elif enter_password_flag:
                        user_password_text = user_password_text[:-1]
                        user_password_text_stored = user_password_text_stored[:-1]


                elif id_writing_flag and enter_user_id_flag:
                    user_id_text += event.unicode
                    user_id_text_stored += event.unicode
                
                elif password_writing_flag and enter_password_flag:
                    user_password_text += "*"
                    user_password_text_stored += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if user_id_rect.collidepoint(event.pos):
                    enter_user_id_flag = True
                    id_writing_flag = True
                    enter_password_flag = False
                    password_writing_flag = False
                    submit_flag = False

                elif user_password_rect.collidepoint(event.pos):
                    enter_password_flag = True
                    password_writing_flag = True
                    enter_user_id_flag = False
                    id_writing_flag = False
                    submit_flag = False
                
                elif arrow_login_circle.collidepoint(event.pos):
                    submit_flag = True
                    enter_user_id_flag = False
                    enter_password_flag = False
                    id_writing_flag = False
                    password_writing_flag = False
                
                elif support_logo_rect.collidepoint(event.pos):
                    support_flag = True
                    enter_user_id_flag = False
                    enter_password_flag = False
                    submit_flag = False
                    id_writing_flag = False
                    password_writing_flag = False

                else:
                    enter_user_id_flag = False
                    enter_password_flag = False
                    submit_flag = False
                    support_flag = False
                    id_writing_flag = False
                    password_writing_flag = False

        display_text(gwindow, "BAT CARDS LOGIN", white, 206.66, 201.61, 33, "OCRAEXT")
        gwindow.blit(arrow_login_page, (arrow_login_page_rect))
        gwindow.blit(support_logo, (support_logo_rect))

        if not enter_user_id_flag and len(user_id_text) == 0:
            display_text(gwindow, "Enter user ID", GREY1, 213.04, 238.15, 28, "OCRAEXT")
        if not enter_password_flag and len(user_password_text) == 0: 
            display_text(gwindow, "Enter password", GREY1, 213.04, 285.67, 28, "OCRAEXT")
        
        if enter_user_id_flag:
            user_id_rect = pygame.draw.rect(gwindow, white, [206.66, 240.32, 435, 33])
            user_id_text_rect = display_text(gwindow, user_id_text, black, 213.04, 238.15, 28, "OCRAEXT")
            if user_id_text_rect.width > 434:
                user_id_text = user_id_text[1:] 

        if enter_password_flag:
            user_password_rect = pygame.draw.rect(gwindow, white, [206.66, 287, 435, 33])
            user_passowrd_text_rect = display_text(gwindow, user_password_text, black, 213.04, 285.67, 28, "OCRAEXT")
            if user_passowrd_text_rect.width > 434:
                user_password_text = user_password_text[1:]
        
        if submit_flag:
            user_info = open(os.path.join(main_file_directory, "users", "{0}.batdata".format(user_id_text_stored)), "a+")
            user_info.seek(0)
            content = user_info.read()
            if len(content) == 0:
                user_info.write("username = ")
                user_info.write(str(user_id_text_stored))
                user_info.write("\n")
                user_info.write("password = ")
                user_info.write(str(user_password_text_stored))
                user_info.write("\n")
                user_info.write("wins = 0\n")
                user_info.write("losses = 0\n")
        
                event_flag = False
                submit_flag = False
                dashboard_window(big_window_size, main_file_directory)
                user_info.close()
            else:
                user_info.seek(0)
                user_data_packets = user_info.readlines()
                data_set = []
                for packet in user_data_packets:
                    data = packet.split(" = ")
                    data_set.append(data[1])
                user_info.close()

                if user_id_text_stored + str("\n") == data_set[0] and user_password_text_stored + str("\n") == data_set[1]:
                    submit_flag = False
                    dashboard_window(big_window_size, main_file_directory, user_id_text_stored, user_password_text_stored)
                    break
                else:
                    print("wrong credentials")
                    print (data_set)

        pygame.display.update()
