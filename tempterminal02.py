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

    chosen_attribute_index = 0
    attribute_flag = False
    card_holder_flag_1 = True
    card_holder_flag_2 = True
    place_card_flag_1 = False
    place_card_flag_2 = False
    attribute_lock_1 = False
    attribute_lock_2 = False
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

    while (len(card_set_1) < 8) :
        card_rank_a = random.randint(1, 16)
        if (card_rank_a not in card_set_1):
            card_set_1.append(card_rank_a)

    while (len(card_set_2) < 8) :
        card_rank_b = random.randint(1, 16)
        if (card_rank_b not in card_set_1) and (card_rank_b not in card_set_2):
            card_set_2.append(card_rank_b)

    card_set_1.sort()
    card_set_2.sort()
    horizontal_indicator_flag = False

    current_card_nos_1 = 26
    current_card_nos_2 = 26
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

    place_button = pygame.image.load(os.path.join(main_file_directory, "assets", "place_button.png")).convert_alpha()
    place_button_rect = place_button.get_rect(center = (385, 263))

    opponent_card_back = pygame.image.load(os.path.join(main_file_directory, "assets", "opponent_card_back.png")).convert_alpha()
    for i in range (0, 6):
        opponent_card_back_rect = opponent_card_back.get_rect(center = (70+(i*120), 84))
        gwindow_2.blit(opponent_card_back, opponent_card_back_rect)

    horizontal_bar_markings = [(56 + (54*i)) for i in range(0, 13)]
    

    attributes_list = ["", "Rank", "Attack Power", "Health Power", "Defense Power", "Speed Power", "Battle IQ"]
    while event_flag:
        

        print(chosen_attribute_index)
        print (card_holder_flag_1, card_holder_flag_2)

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
                if scroll_bar_horizontal_rect.collidepoint(event.pos):
                    horizontal_indicator_flag = True
                if horizontal_end_left_rect.collidepoint(event.pos) and horizontal_scroll_bar_pos > 56:
                    horizontal_scroll_bar_pos -= 54
                    mark_value_horizontal = horizontal_bar_markings.index(horizontal_scroll_bar_pos)
                if horizontal_end_right_rect.collidepoint(event.pos) and horizontal_scroll_bar_pos < 704:
                    horizontal_scroll_bar_pos += 54
                    mark_value_horizontal = horizontal_bar_markings.index(horizontal_scroll_bar_pos)
                
                if not attribute_lock_1 and turn_flag:
                    if rank_rect_btn.collidepoint(event.pos):
                        chosen_attribute_index = 1
                        attribute_flag = True
                    if attack_power_rect_btn.collidepoint(event.pos):
                        chosen_attribute_index = 2
                        attribute_flag = True
                    if health_power_rect_btn.collidepoint(event.pos):
                        chosen_attribute_index = 3
                        attribute_flag = True
                    if defense_power_rect_btn.collidepoint(event.pos):
                        chosen_attribute_index = 4
                        attribute_flag = True
                    if speed_power_rect_btn.collidepoint(event.pos):
                        chosen_attribute_index = 5
                        attribute_flag = True
                    if battle_IQ_rect_btn.collidepoint(event.pos):
                        chosen_attribute_index = 6
                        attribute_flag = True

                    if card_1_rect.collidepoint(event.pos):
                        card_holder_flag_1 = False
                        gwindow_2.blit(card_1, card_placement_holder_1_rect)
                        chosen_card_index = 1

                    if card_2_rect.collidepoint(event.pos):
                        card_holder_flag_1 = False
                        gwindow_2.blit(card_2, card_placement_holder_1_rect)
                        chosen_card_index = 2
                    if card_3_rect.collidepoint(event.pos):
                        card_holder_flag_1 = False
                        chosen_card_index = 3
                        gwindow_2.blit(card_3, card_placement_holder_1_rect)
                    if card_4_rect.collidepoint(event.pos):
                        card_holder_flag_1 = False
                        gwindow_2.blit(card_4, card_placement_holder_1_rect)
                        chosen_card_index = 4

                    if not card_holder_flag_1:
                        rank_usable_flag = sevendeadlysins_index[card_indexes_2[chosen_card_index]].rank_flag
                        attack_usable_flag = sevendeadlysins_index[card_indexes_2[chosen_card_index]].atk_flag
                        health_usable_flag = sevendeadlysins_index[card_indexes_2[chosen_card_index]].hp_flag
                        defense_usable_flag = sevendeadlysins_index[card_indexes_2[chosen_card_index]].dp_flag
                        speed_usable_flag = sevendeadlysins_index[card_indexes_2[chosen_card_index]].sp_flag
                        battle_IQ_usable_flag = sevendeadlysins_index[card_indexes_2[chosen_card_index]].iq_flag
                    
                    if place_button_rect.collidepoint(event.pos) and attribute_flag == True:
                        place_card_flag_1 = True
                        attribute_lock_1 = True
                        turn_flag = False
                        if chosen_attribute_index == 1:
                            sevendeadlysins_index[chosen_card_index].rank_flag = False
                        if chosen_attribute_index == 2:
                            sevendeadlysins_index[chosen_card_index].atk_flag = False
                        if chosen_attribute_index == 3:
                            sevendeadlysins_index[chosen_card_index].hp_flag = False
                        if chosen_attribute_index == 4:
                            sevendeadlysins_index[chosen_card_index].dp_flag = False
                        if chosen_attribute_index == 5:
                            sevendeadlysins_index[chosen_card_index].sp_flag = False
                        if chosen_attribute_index == 6:
                            sevendeadlysins_index[chosen_card_index].iq_flag = False

                                

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
                            break
                elif  event.type == pygame.MOUSEMOTION and event.rel[0] < 0:
                    for marking in horizontal_bar_markings[:-1:-1]:
                        if mouse[0] > marking:
                            horizontal_scroll_bar_pos = marking + 54
                            mark_value_horizontal = horizontal_bar_markings.index(horizontal_scroll_bar_pos)
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

        current_card_no_text_1 = display_text(gwindow_2, str(len(card_set_1)), white, 4, 155, 24, "OLDENGL")
        current_card_no_text_2 = display_text(gwindow_2, str(len(card_set_2)), white, 730, 342, 24, "OLDENGL")
        press_ESC_text = display_text(gwindow_2, "press ESC to exit", white, 19.55, 14.44, 17, "AGENCYR")
        
        if mark_value_horizontal < 2:
            card_indexes_2 = []
            for i in range((mark_value_horizontal*4) , ((mark_value_horizontal+1)*5)): card_indexes_2.append(card_set_1[i])
            
            
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

        
        gwindow_2.blit(card_1, card_1_rect)
        gwindow_2.blit(card_2, card_2_rect)
        gwindow_2.blit(card_3, card_3_rect)
        gwindow_2.blit(card_4, card_4_rect)
        
        display_text(gwindow_2, chosen_attribute_final, black, 330, 335, 18, "OCRAEXT")
        

        if not turn_flag and not attribute_lock_2:
            available_attribute_values = []
            for cpu_cards in card_set_2: 
                if chosen_attribute_index == 1:
                    available_attribute_values.append(sevendeadlysins_index[cpu_cards].rank)
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

        if attribute_lock_2:
            gwindow_2.blit(chosen_cpu_card_image, card_placement_holder_2_rect)     
        
        if attribute_lock_2 and attribute_lock_1:
            time.sleep(1)
            if chosen_attribute_index == 1:
                if int(sevendeadlysins_index[card_indexes_2[chosen_card_index]].rank) < int(sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].rank):
                    card_set_1.append(card_set_2[chosen_card_index_cpu])
                    card_set_2.remove(card_set_2[chosen_card_index_cpu])
                    print("Player 1 wins this card")
                    card_holder_flag_1 = True
                    card_holder_flag_2 = True
                elif int(sevendeadlysins_index[card_indexes_2[chosen_card_index]].rank) < int(sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].rank): 
                    card_set_2.append(card_set_1[chosen_card_index])
                    card_set_1.remove(card_set_1[chosen_card_index])
                    print("Player 2 wins this card")
                    pygame.draw.rect(gwindow_2, black, ((104, 140),(174, 110) ))
                    pygame.draw.rect(gwindow_2, black, ((104, 140),(183, 110) ))
                    card_holder_flag_1 = True
                    card_holder_flag_2 = True
            if chosen_attribute_index in range (2, 7):
                if sevendeadlysins_index[card_indexes_2[chosen_card_index]].ATK > sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].ATK:
                    card_set_2.append(card_set_1[chosen_card_index_cpu])
                    card_set_1.remove(card_set_1[chosen_card_index_cpu])
                    print("Player 1 wins this card")
                    pygame.draw.rect(gwindow_2, black, ((104, 140),(174, 110) ))
                    pygame.draw.rect(gwindow_2, black, ((104, 140),(183, 110) ))
                    card_holder_flag_1 = True
                    card_holder_flag_2 = True
                elif sevendeadlysins_index[card_indexes_2[chosen_card_index]].ATK > sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].ATK: 
                    card_set_1.append(card_set_2[chosen_card_index_cpu])
                    card_set_2.remove(card_set_2[chosen_card_index_cpu])
                    print("Player 2 wins this card")
                    pygame.draw.rect(gwindow_2, black, ((104, 140),(174, 110) ))
                    pygame.draw.rect(gwindow_2, black, ((104, 140),(183, 110) ))
                    card_holder_flag_1 = True
                    card_holder_flag_2 = True

            
            
            if not turn_flag:
                chosen_attribute_index = random.randint(1, 7)
                chosen_attribute_final = attributes_list[chosen_attribute_index]
                display_text(gwindow_2, chosen_attribute_final, black, 330, 335, 18, "OCRAEXT")
                available_attribute_values = []
                available_attribute_values.clear()
                for cpu_cards in card_set_2: 
                    if chosen_attribute_index == 1:
                        available_attribute_values.append(sevendeadlysins_index[cpu_cards].rank)
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


                time.sleep(2)
                card_holder_flag_2 = False
                attribute_lock_2 = False
                attribute_lock_1 = False
                turn_flag = True
                chosen_cpu_card_image = pygame.image.load(sevendeadlysins_index[card_set_2[chosen_card_index_cpu]].card_image).convert_alpha()
                chosen_cpu_card_image = pygame.transform.scale(chosen_cpu_card_image, (104, 140))

    
        pygame.display.update()
game_p2(big_window_size, main_file_directory)
pygame.quit()