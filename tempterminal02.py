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

def game_p2(window_size , main_file_directory,
            user_id_text_stored, user_password_text_stored):
    
    gwindow_2 = pygame.display.set_mode(window_size)
    pygame.display.set_caption("B.A.T CARDS")
    gwindow_2.fill(black)
    event_flag = True
    event_flag_2 = False

    win = False
    loss = False

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

    r_flag = True
    a_flag = True
    h_flag = True
    d_flag = True
    s_flag = True
    i_flag = True

    #Two lists for all the 26 random cards distributed.
    card_set_1 = []
    card_set_2 = []

    #Two lists for all the cards won by the respective players.
    card_won_set_1 = []
    card_won_set_2 = []

    #loop to add random cards in the card_set_1 and card_set_2.
    #While making sure that no card is repeated in both the sets.
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

    mrk_val_hzntl = 0 #scroll bar indicator's value

    horizontal_scroll_bar_pos = 56

    #All the image assets required for this game window are loaded here.
    card_placement_holder_1 = pygame.image.load(
        os.path.join(main_file_directory, "assets",
                     "card_placement_holder.png")).convert_alpha()
    card_placement_holder_1_rect = card_placement_holder_1.get_rect(
                                                center = (278, 250))  
    
    card_placement_holder_2 = pygame.image.load(
        os.path.join(main_file_directory, "assets",
                     "card_placement_holder.png")).convert_alpha()
    card_placement_holder_2_rect = card_placement_holder_2.get_rect(
                                                center = (487, 250))

    time_counter_bar_1 = pygame.image.load(
        os.path.join(main_file_directory, "assets",
                     "time_counter_bar_1.png")).convert_alpha()
    time_counter_bar_1_rect = time_counter_bar_1.get_rect(center = (380, 169))
    
    time_counter_bar_2 = pygame.image.load(
        os.path.join(main_file_directory, "assets",
                     "time_counter_bar_2.png")).convert_alpha()
    time_counter_bar_2_rect = time_counter_bar_2.get_rect(center = (380, 355))

    scroll_bar_horizontal = pygame.image.load(
        os.path.join(main_file_directory, "assets",
                     "scroll bar horizontal GW2.png")).convert_alpha()
    scroll_bar_horizontal_rect = scroll_bar_horizontal.get_rect(
                                            center = (378, 548))
    
    horizontal_end_left_rect = pygame.Rect((0 , 538), (22, 20))
    horizontal_end_right_rect = pygame.Rect((738 , 538), (22, 20))

    cards_title_GW2 = pygame.image.load(
        os.path.join(main_file_directory, "assets",
                     "cards_title_GW2.png")).convert_alpha()
    cards_title_GW2_rect = cards_title_GW2.get_rect(center = (858, 16))

    GW2_side_menu_panel = pygame.image.load(
        os.path.join(main_file_directory, "assets",
                     "GW2_side_menu_panel.png")).convert_alpha()
    GW2_side_menu_panel_rect = GW2_side_menu_panel.get_rect(center = (858, 280))

    chosen_attribute_bg = pygame.image.load(
        os.path.join(main_file_directory, "assets",
                     "chosen_attribute.png")).convert_alpha()
    chosen_attribute_bg_rect = chosen_attribute_bg.get_rect(center = (384, 345))

    attribute_values_bg = pygame.image.load(
        os.path.join(main_file_directory, "assets",
                     "attribute_values_bg.png")).convert_alpha()
    attribute_values_bg_rect = attribute_values_bg.get_rect(center = (382, 171))

    place_button = pygame.image.load(
        os.path.join(main_file_directory, "assets",
                     "place_button.png")).convert_alpha()
    place_button_rect = place_button.get_rect(center = (385, 263))

    opponent_card_back = pygame.image.load(
        os.path.join(main_file_directory, "assets",
                     "opponent_card_back.png")).convert_alpha()

    horizontal_bar_markings = [(56 + (54*i)) for i in range(0, 13)]
    
    chosen_attribute_final_value = ""
    chosen_attribute_final_value_cpu = ""

    attributes_list = ["", "Rank", "ATK", "HP", "DP", "SP", "IQ"]
    
    while event_flag:
        
        total_cards_1 = len(card_set_1) + len(card_won_set_1)
        total_cards_2 = len(card_set_2) + len(card_won_set_2)
        for i in range (0, 6):
            #Displays a card back for computer's cards just for Aesthetics.
            opponent_card_back_rect = opponent_card_back.get_rect(
                                        center = (70+(i*120), 84))
            gwindow_2.blit(opponent_card_back, opponent_card_back_rect)

        if len(card_set_1)>0 and len(card_set_2)>0:
            
            #Runs the game unless the hand of any players is empty.
            gwindow_2.blit(attribute_values_bg, attribute_values_bg_rect)
            
            if card_holder_flag_1:
                gwindow_2.blit(
                    card_placement_holder_1, card_placement_holder_1_rect)
            if card_holder_flag_2:
                gwindow_2.blit(
                    card_placement_holder_2, card_placement_holder_2_rect)
            
            gwindow_2.blit(time_counter_bar_1, time_counter_bar_1_rect)
            gwindow_2.blit(time_counter_bar_2, time_counter_bar_2_rect)
            gwindow_2.blit(scroll_bar_horizontal, scroll_bar_horizontal_rect)
            horizontal_scroll_bar_indicator = pygame.draw.circle(
                gwindow_2, uni_red, (horizontal_scroll_bar_pos, 548), 5)


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
                    #Signals the initiation of ussage of horizontal scroll bar.
                    if scroll_bar_horizontal_rect.collidepoint(event.pos):
                        horizontal_indicator_flag = True
                    
                    if (horizontal_end_left_rect.collidepoint(event.pos) and
                        horizontal_scroll_bar_pos > 56):
                        
                        horizontal_scroll_bar_pos -= 54
                        mrk_val_hzntl = horizontal_bar_markings.index(
                            horizontal_scroll_bar_pos)
                        pygame.draw.rect(gwindow_2, black,
                                         ((104, 140),(231, 181) ))
                        pygame.draw.rect(gwindow_2, black,
                                         ((0, 379), (757 , 159)))
                        card_holder_flag_1 = True
                        card_indexes_2.clear()
                    
                    if (horizontal_end_right_rect.collidepoint(event.pos) and
                        horizontal_scroll_bar_pos < 704):
                    
                        horizontal_scroll_bar_pos += 54
                        mrk_val_hzntl = horizontal_bar_markings.index(
                            horizontal_scroll_bar_pos)
                        pygame.draw.rect(gwindow_2, black,
                                         ((104, 140),(231, 181) ))
                        pygame.draw.rect(gwindow_2, black,
                                         ((0, 379), (757 , 159)))
                        card_holder_flag_1 = True
                        card_indexes_2.clear()
                    
                    #By checking both flags the features for players to make
                    #make choices and place cards are enabled in this section.
                    if not card_lock_1 and turn_flag:
                        
                        #Had to use unnecessary variables like c_val, r_val etc.
                        #in order to keep the code within 80 chr limit.
                        if not attribute_lock_1 and current_turn:                
                            if rank_rect_btn.collidepoint(event.pos):
                                chosen_attribute_index = 1
                                c_val = card_indexes_2[chosen_card_index]
                                r_val = sevendeadlysins_index[c_val].rank
                                chosen_attribute_final_value = int(r_val)
                                attribute_flag = True
                            if attack_power_rect_btn.collidepoint(event.pos):
                                chosen_attribute_index = 2
                                c_val = card_indexes_2[chosen_card_index]
                                a_val = sevendeadlysins_index[c_val].ATK
                                chosen_attribute_final_value = int(a_val)
                                attribute_flag = True
                            if health_power_rect_btn.collidepoint(event.pos):
                                chosen_attribute_index = 3
                                c_val = card_indexes_2[chosen_card_index]
                                h_val = sevendeadlysins_index[c_val].HP
                                chosen_attribute_final_value = int(h_val)
                                attribute_flag = True
                            if defense_power_rect_btn.collidepoint(event.pos):
                                chosen_attribute_index = 4
                                c_val = card_indexes_2[chosen_card_index]
                                d_val = sevendeadlysins_index[c_val].DP
                                chosen_attribute_final_value = int(d_val)
                                attribute_flag = True
                            if speed_power_rect_btn.collidepoint(event.pos):
                                chosen_attribute_index = 5
                                c_val = card_indexes_2[chosen_card_index]
                                s_val = sevendeadlysins_index[c_val].SP
                                chosen_attribute_final_value = int(s_val)
                                attribute_flag = True
                            if battle_IQ_rect_btn.collidepoint(event.pos):
                                chosen_attribute_index = 6
                                c_val = card_indexes_2[chosen_card_index]
                                i_val = sevendeadlysins_index[c_val].IQ
                                chosen_attribute_final_value = int(i_val)
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
                            c_val = card_indexes_2[chosen_card_index]
                            r_flag = sevendeadlysins_index[c_val].rank_flag
                            a_flag = sevendeadlysins_index[c_val].atk_flag
                            h_flag = sevendeadlysins_index[c_val].hp_flag
                            d_flag = sevendeadlysins_index[c_val].dp_flag
                            s_flag = sevendeadlysins_index[c_val].sp_flag
                            i_flag = sevendeadlysins_index[c_val].iq_flag
                            
                            #Makes sure that the attributes are chosen for the
                            #card to be placed and the corresponding attribute
                            #value is loaded up.
                            if chosen_attribute_index == 1 and r_flag:
                                attribute_check = True
                                c_val = card_indexes_2[chosen_card_index]
                                r_val = sevendeadlysins_index[c_val].rank
                                chosen_attribute_final_value = int(r_val)
                            if chosen_attribute_index == 2 and a_flag:
                                attribute_check = True
                                c_val = card_indexes_2[chosen_card_index]
                                a_val = sevendeadlysins_index[c_val].ATK
                                chosen_attribute_final_value = int(a_val)
                            if chosen_attribute_index == 3 and h_flag:
                                attribute_check = True
                                c_val = card_indexes_2[chosen_card_index]
                                h_val = sevendeadlysins_index[c_val].HP
                                chosen_attribute_final_value = int(h_val)
                            if chosen_attribute_index == 4 and d_flag:
                                attribute_check = True
                                c_val = card_indexes_2[chosen_card_index]
                                d_val = sevendeadlysins_index[c_val].DP
                                chosen_attribute_final_value = int(d_val)
                            if chosen_attribute_index == 5 and s_flag:
                                attribute_check = True
                                c_val = card_indexes_2[chosen_card_index]
                                s_val = sevendeadlysins_index[c_val].SP
                                chosen_attribute_final_value = int(s_val)
                            if chosen_attribute_index == 6 and i_flag:
                                attribute_check = True
                                c_val = card_indexes_2[chosen_card_index]
                                i_val = sevendeadlysins_index[c_val].IQ
                                chosen_attribute_final_value = int(i_val)

                        #This place function is for when its the players turn
                        if (place_button_rect.collidepoint(event.pos) and
                            attribute_flag and
                            current_turn and
                            attribute_check and
                            chosen_attribute_final_value != ""):
                            
                            if chosen_card_index == len(card_indexes_2):
                                chosen_card_index -= 1
                            place_card_flag_1 = True
                            attribute_flag = True
                            
                            #The card is placed on user's turn and after the 
                            #comparison is done the cpu gets its turn.
                            card_lock_1 = True
                            turn_flag = False
                            attribute_lock_2 = False
                            
                            
                        #This place function is for when its the cpu's turn
                        if (place_button_rect.collidepoint(event.pos) and
                            attribute_flag and not
                            current_turn and
                            attribute_check and
                            chosen_attribute_final_value != ""):
                            
                            place_card_flag_1 = True
                            attribute_flag = True
                            
                            attribute_lock_1 = False
                            card_lock_1 = True
                            current_turn = True
                            card_lock_2 = False
                            
                            
                            if chosen_card_index == len(card_indexes_2):
                                chosen_card_index -= 1
                            
                        #This place function is for when an attribute is not
                        #Usable if used before.
                        #This is not required for the current version of program
                        #because cards get discarded after each use, but in 
                        #future versions cards might be reused and so this
                        #this code will be useful. 
                        if (place_button_rect.collidepoint(event.pos) 
                            and chosen_attribute_final_value != ""
                            and not attribute_check):
                            display_text(gwindow_2,
                                         "Attribute not usable", uni_red,
                                         385, 263, 12, "OCRAEXT")
                            
                    #This is the whole deck feature/button, which lets player
                    #see all the cards and their respective information from the
                    #whole deck.
                    if show_whole_deck_rect.collidepoint(event.pos):
                        event_flag_2 = True
                        m = 1
                        screen = pygame.display.set_mode([640, 480])
                        
                        while event_flag_2:
                            screen.fill(black)
                            display_text(screen, 
                                         "press ESC or quit to go back ingame",
                                          white, 15, 15, 16, "AGENCYR")
                            for event_2 in pygame.event.get():
                                if event_2.type == pygame.QUIT:
                                    event_flag_2 = False
                                    pygame.draw.rect(screen, black,
                                                     ((0, 0), (640, 480)))
                                    time.sleep(0.1)
                                    gwindow_2 = pygame.display.set_mode(
                                        (960,560))
                                    #This is not a defined function and resets
                                    #the window size because if not done, the 
                                    #game progress might get lost.
                                
                                elif event_2.type == pygame.KEYDOWN:
                                    if event_2.key == pygame.K_ESCAPE:
                                        event_flag_2 = False
                                        pygame.draw.rect(screen, black,
                                                         ((0, 0), (640, 480)))
                                        time.sleep(0.1)
                                        gwindow_2 = pygame.display.set_mode(
                                                                    960,560)
                                
                                elif event_2.type == pygame.MOUSEBUTTONDOWN:
                                    if (back_rect.collidepoint(event_2.pos) and
                                        m>1):
                                        m -= 1
                                    elif (next_rect.collidepoint(event_2.pos)
                                          and m<52):
                                        m += 1
                            
                            if event_flag_2:
                                
                                back_rect = pygame.draw.rect(screen, white,
                                                             (180, 390, 80, 40))
                                back_text = display_text(screen,
                                                         'Back', black,
                                                         200, 400, 20,"AGENCYR")
                                
                                next_rect = pygame.draw.rect(screen, white,
                                                             (400, 390, 80, 40))
                                next_text = display_text(screen,
                                                         'Next', black,
                                                         425, 400, 20,"AGENCYR")
                                
                                image = pygame.image.load(
                                    sevendeadlysins_index[m].card_image
                                                         ).convert_alpha()
                                image = pygame.transform.scale(image,
                                                               (104, 150))
                                screen.blit(image, [280, 50])
                                
                                name = sevendeadlysins_index[m].name
                                title = sevendeadlysins_index[m].title
                                form = sevendeadlysins_index[m].form
                                rank = sevendeadlysins_index[m].rank
                                atk = sevendeadlysins_index[m].ATK
                                hp = sevendeadlysins_index[m].HP
                                dp = sevendeadlysins_index[m].DP
                                sp = sevendeadlysins_index[m].SP
                                iq = sevendeadlysins_index[m].IQ

                                display_text(screen, (name+' - '+form),
                                             white, 215, 200, 20, "ARLRDBD")
                                display_text(screen, ("["+title+"]"),
                                             white, 215, 221, 12, "ARLRDBD")
                                display_text(screen, "rank: {}".format(rank),
                                             white, 200, 270, 15, "OCRAEXT")
                                display_text(screen, "ATK: {}".format(atk),
                                             white, 200, 305, 15, "OCRAEXT")
                                display_text(screen, "HP: {}".format(hp),
                                             white, 200, 340, 15, "OCRAEXT")
                                display_text(screen, "DP: {}".format(dp),
                                             white, 380, 270, 15, "OCRAEXT")
                                display_text(screen, "SP: {}".format(sp),
                                             white, 380, 305, 15, "OCRAEXT")
                                display_text(screen, "IQ: {}".format(iq),
                                             white, 380, 340, 15, "OCRAEXT")
                                
                            pygame.display.flip()
                            time.sleep(0.1)
                                    
                #Signals the end of interaction witht the horizontal scroll bar
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
                                mrk_val_hzntl = horizontal_bar_markings.index(
                                                    horizontal_scroll_bar_pos)
                                pygame.draw.rect(gwindow_2, black,
                                                 ((104, 140),(231, 181) ))
                                pygame.draw.rect(gwindow_2, black,
                                                 ((0, 379), (757 , 159)))
                                
                                card_holder_flag_1 = True
                                card_indexes_2.clear()
                                break

                    elif  event.type == pygame.MOUSEMOTION and event.rel[0] < 0:
                        
                        for marking in horizontal_bar_markings[:-1:-1]:
                        
                            if mouse[0] > marking:
                                horizontal_scroll_bar_pos = marking + 54
                                mrk_val_hzntl = horizontal_bar_markings.index(
                                                    horizontal_scroll_bar_pos)                    
                                pygame.draw.rect(gwindow_2, black,
                                                 ((104, 140),(231, 181) ))
                                pygame.draw.rect(gwindow_2, black,
                                                 ((0, 379), (757 , 159)))
                                card_holder_flag_1 = True
                                card_indexes_2.clear()
                                break
                
            #This section is dedicated to Creation and displaying of the button
            #for attributes for the cards.
            attack_power_rect_btn = pygame.draw.rect(gwindow_2, black_light,
                                                     ((19, 203), (196 , 32)))
            health_power_rect_btn = pygame.draw.rect(gwindow_2, black_light,
                                                     ((19, 244), (196 , 32)))
            defense_power_rect_btn = pygame.draw.rect(gwindow_2, black_light,
                                                      ((19, 285), (196 , 32)))

            if a_flag:
                attack_power_text = display_text(gwindow_2,
                                                 "Attack Power", white,
                                                 36, 203, 29, "COLONNA")
            if h_flag:    
                health_power_text = display_text(gwindow_2,
                                                 "Health Power", white,
                                                 36, 244, 29, "COLONNA")
            if d_flag:
                defense_power_text = display_text(gwindow_2,
                                                  "Defense Power", white,
                                                  27, 285, 29, "COLONNA")

            rank_rect_btn = pygame.draw.rect(gwindow_2, black_light,
                                             ((551, 203), (196 , 32)))
            speed_power_rect_btn = pygame.draw.rect(gwindow_2, black_light,
                                                    ((551, 244), (196 , 32)))
            battle_IQ_rect_btn = pygame.draw.rect(gwindow_2, black_light,
                                                  ((551, 285), (196 , 32)))

            if r_flag:
                rank_text = display_text(gwindow_2,
                                         "Rank", white,
                                         616, 203, 29, "COLONNA")
            if s_flag:
                speed_power_text = display_text(gwindow_2,
                                                "Speed Power", white,
                                                573, 244, 29, "COLONNA")
            if i_flag:
                battle_IQ_text = display_text(gwindow_2,
                                              "Battle IQ", white,
                                              598, 285, 29, "COLONNA")

            current_card_no_text_1 = display_text(gwindow_2,
                                                  str(total_cards_1), white,
                                                  730, 342, 24, "OLDENGL")
            current_card_no_text_2 = display_text(gwindow_2,
                                                  str(total_cards_2), white,
                                                  4, 155, 24, "OLDENGL")
            press_ESC_text = display_text(gwindow_2,
                                          "press ESC to exit", white,
                                          19.55, 14.44, 17, "AGENCYR")
            
            #This creates a temporary set of cards from the users hands that
            #needs to be shown below in the horizontal tab according to their
            #respective orders.
            card_indexes_2 = []
            for i in range((mrk_val_hzntl*4) , ((mrk_val_hzntl+1)*5)): 
                try:
                    card_indexes_2.append(card_set_1[i])
                except:
                    pass
            
            #This section makes sure the cards are displayed properly by first
            #creating a layer of black screen in the horizontal tab then
            #this displaying the cards (if any) accordingly.
            #This ensures that the cards from previous any other order don't
            #get displayed where they don't need to be.
            if len(card_indexes_2) == 0:
                pygame.draw.rect(gwindow_2, black, ((0, 379), (757 , 159)))
            if len(card_indexes_2) > 0:
                pygame.draw.rect(gwindow_2, black, ((0, 379), (757 , 159)))
                
                card_1 = pygame.image.load(
                    sevendeadlysins_index[card_indexes_2[0]].card_image
                                          ).convert_alpha()
                card_1 = pygame.transform.scale(card_1, (104, 140))
                card_1_rect = card_1.get_rect(center = (98+(200*0), 456))
                card_1_form = sevendeadlysins_index[card_indexes_2[0]].form
                card_1_name_info = display_text(gwindow_2,(
                    sevendeadlysins_index[card_indexes_2[0]].name + 
                    " [{}]".format(card_1_form)), white, 760, 35, 12, "OCRAEXT")
                card_1_rank = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[0]].rank),
                    white, 830, 72+(40*0), 12, "OCRAEXT")
                card_1_attack = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[0]].ATK),
                    white, 820, 72+(40*1), 12, "OCRAEXT")
                card_1_health = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[0]].HP),
                    white, 820, 72+(40*2), 12, "OCRAEXT")
                card_1_defense = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[0]].DP),
                    white, 923, 72+(40*0), 12, "OCRAEXT")
                card_1_speed = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[0]].SP),
                    white, 923, 72+(40*1), 12, "OCRAEXT")
                card_1_battle_IQ = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[0]].IQ),
                    white, 923, 72+(40*2), 12, "OCRAEXT")
                gwindow_2.blit(card_1, card_1_rect)

            if len(card_indexes_2) > 1:
                card_2 = pygame.image.load(
                    sevendeadlysins_index[card_indexes_2[1]].card_image
                                          ).convert_alpha()
                card_2 = pygame.transform.scale(card_2, (104, 140))
                card_2_form = sevendeadlysins_index[card_indexes_2[1]].form
                card_2_rect = card_2.get_rect(center = (98+(200*1), 456))
                card_2_name_info = display_text(gwindow_2, (
                    sevendeadlysins_index[card_indexes_2[1]].name +
                    " [{}]".format(card_2_form)), white, 760, 182, 12,"OCRAEXT")
                card_2_rank = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[1]].rank),
                    white, 830, 212+(32*0), 12, "OCRAEXT")
                card_2_attack = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[1]].ATK),
                    white, 820, 212+(32*1), 12, "OCRAEXT")
                card_2_health = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[1]].HP),
                    white, 820, 212+(32*2), 12, "OCRAEXT")
                card_2_defense = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[1]].DP),
                    white, 923, 212+(32*0), 12, "OCRAEXT")
                card_2_speed = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[1]].SP),
                    white, 923, 212+(32*1), 12, "OCRAEXT")
                card_2_battle_IQ = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[1]].IQ),
                    white, 923, 212+(32*2), 12, "OCRAEXT")
                gwindow_2.blit(card_2, card_2_rect)
            

            if len(card_indexes_2) > 2: 
                card_3 = pygame.image.load(
                    sevendeadlysins_index[card_indexes_2[2]].card_image
                                          ).convert_alpha()
                card_3 = pygame.transform.scale(card_3, (104, 140))
                card_3_form = sevendeadlysins_index[card_indexes_2[2]].form
                card_3_rect = card_1.get_rect(center = (98+(200*2), 456))
                card_3_name_info = display_text(gwindow_2, (
                    sevendeadlysins_index[card_indexes_2[2]].name +
                    " [{}]".format(card_3_form)), white, 760, 305, 12,"OCRAEXT")
                card_3_rank = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[2]].rank),
                    white, 830, 332+(32*0), 12, "OCRAEXT")
                card_3_attack = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[2]].ATK),
                    white, 820, 332+(32*1), 12, "OCRAEXT")
                card_3_health = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[2]].HP),
                    white, 820, 332+(32*2), 12, "OCRAEXT")
                card_3_defense = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[2]].DP),
                    white, 923, 332+(32*0), 12, "OCRAEXT")
                card_3_speed = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[2]].SP),
                    white, 923, 332+(32*1), 12, "OCRAEXT")
                card_3_battle_IQ = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[2]].IQ),
                    white, 923, 332+(32*2), 12, "OCRAEXT")
                gwindow_2.blit(card_3, card_3_rect)


            if len(card_indexes_2) > 3:
                card_4 = pygame.image.load(
                    sevendeadlysins_index[card_indexes_2[3]].card_image
                                          ).convert_alpha()
                card_4 = pygame.transform.scale(card_4, (104, 140))
                card_4_form = sevendeadlysins_index[card_indexes_2[3]].form
                card_4_rect = card_1.get_rect(center = (98+(200*3), 456))
                card_4_name_info = display_text(gwindow_2, (
                    sevendeadlysins_index[card_indexes_2[3]].name +
                    " [{}]".format(card_4_form)), white, 760, 424, 12,"OCRAEXT")
                card_4_rank = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[3]].rank),
                    white, 830, 450+(32*0), 12, "OCRAEXT")
                card_4_attack = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[3]].ATK),
                    white, 820, 450+(32*1), 12, "OCRAEXT")
                card_4_health = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[3]].HP),
                    white, 820, 450+(32*2), 12, "OCRAEXT")
                card_4_defense = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[3]].DP),
                    white, 923, 450+(32*0), 12, "OCRAEXT")
                card_4_speed = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[3]].SP),
                    white, 923, 450+(32*1), 12, "OCRAEXT")
                card_4_battle_IQ = display_text(gwindow_2, str(
                    sevendeadlysins_index[card_indexes_2[3]].IQ),
                    white, 923, 450+(32*2), 12, "OCRAEXT")
                gwindow_2.blit(card_4, card_4_rect)
            
            display_text(gwindow_2, chosen_attribute_final,
                         black, 359, 335, 20, "OCRAEXT")
            if not card_holder_flag_1:
                display_text(gwindow_2, str(chosen_attribute_final_value),
                             black, 260, 164, 18, "OCRAEXT")        


            #This section is for the CPU's work when its the players turn and
            #the Player has submitted his/her card.
            if not turn_flag and not attribute_lock_2:
                available_attribute_values = []
                for cpu_cards in card_set_2: 
                    if chosen_attribute_index == 1:
                        available_attribute_values.append(int(
                            sevendeadlysins_index[cpu_cards].rank))
                    if chosen_attribute_index == 2:
                        available_attribute_values.append(
                            sevendeadlysins_index[cpu_cards].ATK)
                    if chosen_attribute_index == 3:
                        available_attribute_values.append(
                            sevendeadlysins_index[cpu_cards].HP)
                    if chosen_attribute_index == 4:
                        available_attribute_values.append(
                            sevendeadlysins_index[cpu_cards].DP)
                    if chosen_attribute_index == 5:
                        available_attribute_values.append(
                            sevendeadlysins_index[cpu_cards].SP)
                    if chosen_attribute_index == 6:
                        available_attribute_values.append(
                            sevendeadlysins_index[cpu_cards].IQ)

                if chosen_attribute_index == 1:
                    chosen_attribute_final_value_cpu = min(
                                available_attribute_values)
                    chosen_card_index_cpu = available_attribute_values.index(
                        min(available_attribute_values))
                elif chosen_attribute_index in range (2, 7):
                    chosen_attribute_final_value_cpu = max(
                                available_attribute_values)
                    chosen_card_index_cpu = available_attribute_values.index(
                        max(available_attribute_values))

                card_holder_flag_2 = False
                attribute_lock_2 = True
                chosen_cpu_card_image = pygame.image.load(
                    sevendeadlysins_index[(
                        card_set_2[chosen_card_index_cpu])].card_image
                                                         ).convert_alpha()
                chosen_cpu_card_image = pygame.transform.scale(
                    chosen_cpu_card_image, (104, 140))
                card_lock_2 = True

            if card_lock_2:
                gwindow_2.blit(chosen_cpu_card_image,
                            card_placement_holder_2_rect)
                if not card_holder_flag_2:    
                    display_text(gwindow_2, str(chosen_attribute_final_value_cpu),
                                black, 466, 164, 18, "OCRAEXT")
                pygame.display.flip()
                
                     
            #This section is for the comparison of cards chosen by both the
            #player and the cpu and making sure everything is reset back to how
            #it needs to be.
            if attribute_lock_2 and card_lock_1:
                time.sleep(2)

                if chosen_attribute_index == 1:
                    
                    if (
                        (int(sevendeadlysins_index[(
                            card_indexes_2[chosen_card_index])].rank) ) < (
                                int(sevendeadlysins_index[(
                                    card_set_2[chosen_card_index_cpu])].rank))):
                        
                        card_won_set_1.append(card_set_2[chosen_card_index_cpu])
                        card_won_set_1.append(card_indexes_2[chosen_card_index])
                        card_set_1.remove(card_indexes_2[chosen_card_index])
                        card_set_2.remove(card_set_2[chosen_card_index_cpu])
                        pygame.draw.rect(gwindow_2, black,
                                         ((104, 140),(231, 181)))
                        pygame.draw.rect(gwindow_2, black,
                                         ((104, 140),(435, 181)))
                        card_holder_flag_1 = True
                        card_holder_flag_2 = True
                        card_lock_1 = False
                        chosen_attribute_index = 0
                        chosen_attribute_final_value_cpu = ""
                        chosen_attribute_final_value = ""
                        available_attribute_values.clear()
                    
                    elif ((int(sevendeadlysins_index[(
                        card_indexes_2[chosen_card_index])].rank)) > (
                            int(sevendeadlysins_index[(
                                card_set_2[chosen_card_index_cpu])].rank))): 

                        card_won_set_2.append(card_indexes_2[chosen_card_index])
                        card_won_set_2.append(card_set_2[chosen_card_index_cpu])
                        card_set_1.remove(card_indexes_2[chosen_card_index])
                        card_set_2.remove(card_set_2[chosen_card_index_cpu])
                        pygame.draw.rect(gwindow_2, black,
                                         ((104, 140),(231, 181)))
                        pygame.draw.rect(gwindow_2, black,
                                         ((104, 140),(435, 181)))
                        card_holder_flag_1 = True
                        card_holder_flag_2 = True
                        card_lock_1 = False
                        chosen_attribute_index = 0
                        chosen_attribute_final_value_cpu = ""
                        chosen_attribute_final_value = ""
                        available_attribute_values.clear()
                    
                    elif ((int(sevendeadlysins_index[(
                        card_indexes_2[chosen_card_index])].rank)) == (
                            int(sevendeadlysins_index[(
                                card_set_2[chosen_card_index_cpu])].rank))): 

                        card_set_1.remove(card_indexes_2[chosen_card_index])
                        card_set_2.remove(card_set_2[chosen_card_index_cpu])
                        pygame.draw.rect(gwindow_2, black,
                                         ((104, 140),(231, 181)))
                        pygame.draw.rect(gwindow_2, black,
                                         ((104, 140),(435, 181)))
                        card_holder_flag_1 = True
                        card_holder_flag_2 = True
                        card_lock_1 = False
                        chosen_attribute_index = 0
                        chosen_attribute_final_value_cpu = ""
                        chosen_attribute_final_value = ""
                        available_attribute_values.clear()

                if chosen_attribute_index == 2:
                    if ((sevendeadlysins_index[(
                        card_indexes_2[chosen_card_index])].ATK) > (
                            sevendeadlysins_index[(
                            card_set_2[chosen_card_index_cpu])].ATK)):
                        
                        card_won_set_1.append(card_set_2[chosen_card_index_cpu])
                        card_won_set_1.append(card_indexes_2[chosen_card_index])
                        card_set_1.remove(card_indexes_2[chosen_card_index])
                        card_set_2.remove(card_set_2[chosen_card_index_cpu])
                        pygame.draw.rect(gwindow_2, black,
                                        ((104, 140),(231, 181)))
                        pygame.draw.rect(gwindow_2, black,
                                        ((104, 140),(435, 181)))
                        card_holder_flag_1 = True
                        card_holder_flag_2 = True
                        card_lock_1 = False
                        chosen_attribute_index = 0
                        chosen_attribute_final_value_cpu = ""
                        chosen_attribute_final_value = ""
                        available_attribute_values.clear()
                    
                    elif ((sevendeadlysins_index[(
                        card_indexes_2[chosen_card_index])].ATK) < (
                            sevendeadlysins_index[(
                                card_set_2[chosen_card_index_cpu])].ATK)): 

                        card_won_set_2.append(card_indexes_2[chosen_card_index])
                        card_won_set_2.append(card_set_2[chosen_card_index_cpu])
                        card_set_1.remove(card_indexes_2[chosen_card_index])
                        card_set_2.remove(card_set_2[chosen_card_index_cpu])
                        pygame.draw.rect(gwindow_2, black,
                                         ((104, 140),(231, 181)))
                        pygame.draw.rect(gwindow_2, black,
                                         ((104, 140),(435, 181)))
                        card_holder_flag_1 = True
                        card_holder_flag_2 = True
                        card_lock_1 = False
                        chosen_attribute_index = 0
                        chosen_attribute_final_value_cpu = ""
                        chosen_attribute_final_value = ""
                        available_attribute_values.clear()
                    
                    elif ((sevendeadlysins_index[(
                        card_indexes_2[chosen_card_index])].ATK) == (
                            sevendeadlysins_index[(
                                card_set_2[chosen_card_index_cpu])].ATK)): 

                        card_set_1.remove(card_indexes_2[chosen_card_index])
                        card_set_2.remove(card_set_2[chosen_card_index_cpu])
                        pygame.draw.rect(gwindow_2, black,
                                         ((104, 140),(231, 181)))
                        pygame.draw.rect(gwindow_2, black,
                                         ((104, 140),(435, 181)))
                        card_holder_flag_1 = True
                        card_holder_flag_2 = True
                        card_lock_1 = False
                        chosen_attribute_index = 0
                        chosen_attribute_final_value_cpu = ""
                        chosen_attribute_final_value = ""
                        available_attribute_values.clear()
                

                if chosen_attribute_index == 3:
                    if ((sevendeadlysins_index[(
                        card_indexes_2[chosen_card_index])].HP) > (
                            sevendeadlysins_index[(
                            card_set_2[chosen_card_index_cpu])].HP)):
                        
                        card_won_set_1.append(card_set_2[chosen_card_index_cpu])
                        card_won_set_1.append(card_indexes_2[chosen_card_index])
                        card_set_1.remove(card_indexes_2[chosen_card_index])
                        card_set_2.remove(card_set_2[chosen_card_index_cpu])
                        pygame.draw.rect(gwindow_2, black,
                                        ((104, 140),(231, 181)))
                        pygame.draw.rect(gwindow_2, black,
                                        ((104, 140),(435, 181)))
                        card_holder_flag_1 = True
                        card_holder_flag_2 = True
                        card_lock_1 = False
                        chosen_attribute_index = 0
                        chosen_attribute_final_value_cpu = ""
                        chosen_attribute_final_value = ""
                        available_attribute_values.clear()
                    
                    elif ((sevendeadlysins_index[(
                        card_indexes_2[chosen_card_index])].HP) < (
                            sevendeadlysins_index[(
                                card_set_2[chosen_card_index_cpu])].HP)): 

                        card_won_set_2.append(card_indexes_2[chosen_card_index])
                        card_won_set_2.append(card_set_2[chosen_card_index_cpu])
                        card_set_1.remove(card_indexes_2[chosen_card_index])
                        card_set_2.remove(card_set_2[chosen_card_index_cpu])
                        pygame.draw.rect(gwindow_2, black,
                                         ((104, 140),(231, 181)))
                        pygame.draw.rect(gwindow_2, black,
                                         ((104, 140),(435, 181)))
                        card_holder_flag_1 = True
                        card_holder_flag_2 = True
                        card_lock_1 = False
                        chosen_attribute_index = 0
                        chosen_attribute_final_value_cpu = ""
                        chosen_attribute_final_value = ""
                        available_attribute_values.clear()
                    
                    elif ((sevendeadlysins_index[(
                        card_indexes_2[chosen_card_index])].HP) == (
                            sevendeadlysins_index[(
                                card_set_2[chosen_card_index_cpu])].HP)):
                        
                        card_set_1.remove(card_indexes_2[chosen_card_index])
                        card_set_2.remove(card_set_2[chosen_card_index_cpu])
                        pygame.draw.rect(gwindow_2, black,
                                            ((104, 140),(231, 181)))
                        pygame.draw.rect(gwindow_2, black,
                                            ((104, 140),(435, 181)))
                        card_holder_flag_1 = True
                        card_holder_flag_2 = True
                        card_lock_1 = False
                        chosen_attribute_index = 0
                        chosen_attribute_final_value_cpu = ""
                        chosen_attribute_final_value = ""
                        available_attribute_values.clear()

                

                if chosen_attribute_index == 4:
                    if ((sevendeadlysins_index[(
                        card_indexes_2[chosen_card_index])].DP) > (
                            sevendeadlysins_index[(
                            card_set_2[chosen_card_index_cpu])].DP)):
                        
                        card_won_set_1.append(card_set_2[chosen_card_index_cpu])
                        card_won_set_1.append(card_indexes_2[chosen_card_index])
                        card_set_1.remove(card_indexes_2[chosen_card_index])
                        card_set_2.remove(card_set_2[chosen_card_index_cpu])
                        pygame.draw.rect(gwindow_2, black,
                                        ((104, 140),(231, 181)))
                        pygame.draw.rect(gwindow_2, black,
                                        ((104, 140),(435, 181)))
                        card_holder_flag_1 = True
                        card_holder_flag_2 = True
                        card_lock_1 = False
                        chosen_attribute_index = 0
                        chosen_attribute_final_value_cpu = ""
                        chosen_attribute_final_value = ""
                        available_attribute_values.clear()
                    
                    elif ((sevendeadlysins_index[(
                        card_indexes_2[chosen_card_index])].DP) < (
                            sevendeadlysins_index[(
                                card_set_2[chosen_card_index_cpu])].DP)): 

                        card_won_set_2.append(card_indexes_2[chosen_card_index])
                        card_won_set_2.append(card_set_2[chosen_card_index_cpu])
                        card_set_1.remove(card_indexes_2[chosen_card_index])
                        card_set_2.remove(card_set_2[chosen_card_index_cpu])
                        pygame.draw.rect(gwindow_2, black,
                                         ((104, 140),(231, 181)))
                        pygame.draw.rect(gwindow_2, black,
                                         ((104, 140),(435, 181)))
                        card_holder_flag_1 = True
                        card_holder_flag_2 = True
                        card_lock_1 = False
                        chosen_attribute_index = 0
                        chosen_attribute_final_value_cpu = ""
                        chosen_attribute_final_value = ""
                        available_attribute_values.clear()
                
                    elif ((sevendeadlysins_index[(
                        card_indexes_2[chosen_card_index])].DP) == (
                            sevendeadlysins_index[(
                                card_set_2[chosen_card_index_cpu])].DP)):
                        
                        card_set_1.remove(card_indexes_2[chosen_card_index])
                        card_set_2.remove(card_set_2[chosen_card_index_cpu])
                        pygame.draw.rect(gwindow_2, black,
                                            ((104, 140),(231, 181)))
                        pygame.draw.rect(gwindow_2, black,
                                            ((104, 140),(435, 181)))
                        card_holder_flag_1 = True
                        card_holder_flag_2 = True
                        card_lock_1 = False
                        chosen_attribute_index = 0
                        chosen_attribute_final_value_cpu = ""
                        chosen_attribute_final_value = ""
                        available_attribute_values.clear()


                if chosen_attribute_index == 5:
                    if ((sevendeadlysins_index[(
                        card_indexes_2[chosen_card_index])].SP) > (
                            sevendeadlysins_index[(
                            card_set_2[chosen_card_index_cpu])].SP)):
                        
                        card_won_set_1.append(card_set_2[chosen_card_index_cpu])
                        card_won_set_1.append(card_indexes_2[chosen_card_index])
                        card_set_1.remove(card_indexes_2[chosen_card_index])
                        card_set_2.remove(card_set_2[chosen_card_index_cpu])
                        pygame.draw.rect(gwindow_2, black,
                                        ((104, 140),(231, 181)))
                        pygame.draw.rect(gwindow_2, black,
                                        ((104, 140),(435, 181)))
                        card_holder_flag_1 = True
                        card_holder_flag_2 = True
                        card_lock_1 = False
                        chosen_attribute_index = 0
                        chosen_attribute_final_value_cpu = ""
                        chosen_attribute_final_value = ""
                        available_attribute_values.clear()
                    
                    elif ((sevendeadlysins_index[(
                        card_indexes_2[chosen_card_index])].SP) < (
                            sevendeadlysins_index[(
                                card_set_2[chosen_card_index_cpu])].SP)): 

                        card_won_set_2.append(card_indexes_2[chosen_card_index])
                        card_won_set_2.append(card_set_2[chosen_card_index_cpu])
                        card_set_1.remove(card_indexes_2[chosen_card_index])
                        card_set_2.remove(card_set_2[chosen_card_index_cpu])
                        pygame.draw.rect(gwindow_2, black,
                                         ((104, 140),(231, 181)))
                        pygame.draw.rect(gwindow_2, black,
                                         ((104, 140),(435, 181)))
                        card_holder_flag_1 = True
                        card_holder_flag_2 = True
                        card_lock_1 = False
                        chosen_attribute_index = 0
                        chosen_attribute_final_value_cpu = ""
                        chosen_attribute_final_value = ""
                        available_attribute_values.clear()
                
                    elif ((sevendeadlysins_index[(
                        card_indexes_2[chosen_card_index])].SP) == (
                            sevendeadlysins_index[(
                                card_set_2[chosen_card_index_cpu])].SP)):
                        
                        card_set_1.remove(card_indexes_2[chosen_card_index])
                        card_set_2.remove(card_set_2[chosen_card_index_cpu])
                        pygame.draw.rect(gwindow_2, black,
                                            ((104, 140),(231, 181)))
                        pygame.draw.rect(gwindow_2, black,
                                            ((104, 140),(435, 181)))
                        card_holder_flag_1 = True
                        card_holder_flag_2 = True
                        card_lock_1 = False
                        chosen_attribute_index = 0
                        chosen_attribute_final_value_cpu = ""
                        chosen_attribute_final_value = ""
                        available_attribute_values.clear()



                if chosen_attribute_index == 6:
                    if ((sevendeadlysins_index[(
                        card_indexes_2[chosen_card_index])].IQ) > (
                            sevendeadlysins_index[(
                            card_set_2[chosen_card_index_cpu])].IQ)):
                        
                        card_won_set_1.append(card_set_2[chosen_card_index_cpu])
                        card_won_set_1.append(card_indexes_2[chosen_card_index])
                        card_set_1.remove(card_indexes_2[chosen_card_index])
                        card_set_2.remove(card_set_2[chosen_card_index_cpu])
                        pygame.draw.rect(gwindow_2, black,
                                        ((104, 140),(231, 181)))
                        pygame.draw.rect(gwindow_2, black,
                                        ((104, 140),(435, 181)))
                        card_holder_flag_1 = True
                        card_holder_flag_2 = True
                        card_lock_1 = False
                        chosen_attribute_index = 0
                        chosen_attribute_final_value_cpu = ""
                        chosen_attribute_final_value = ""
                        available_attribute_values.clear()
                    
                    elif ((sevendeadlysins_index[(
                        card_indexes_2[chosen_card_index])].IQ) < (
                            sevendeadlysins_index[(
                                card_set_2[chosen_card_index_cpu])].IQ)): 

                        card_won_set_2.append(card_indexes_2[chosen_card_index])
                        card_won_set_2.append(card_set_2[chosen_card_index_cpu])
                        card_set_1.remove(card_indexes_2[chosen_card_index])
                        card_set_2.remove(card_set_2[chosen_card_index_cpu])
                        pygame.draw.rect(gwindow_2, black,
                                         ((104, 140),(231, 181)))
                        pygame.draw.rect(gwindow_2, black,
                                         ((104, 140),(435, 181)))
                        card_holder_flag_1 = True
                        card_holder_flag_2 = True
                        card_lock_1 = False
                        chosen_attribute_index = 0
                        chosen_attribute_final_value_cpu = ""
                        chosen_attribute_final_value = ""
                        available_attribute_values.clear()
                
                    elif ((sevendeadlysins_index[(
                        card_indexes_2[chosen_card_index])].IQ) == (
                            sevendeadlysins_index[(
                                card_set_2[chosen_card_index_cpu])].IQ)):
                        
                        card_set_1.remove(card_indexes_2[chosen_card_index])
                        card_set_2.remove(card_set_2[chosen_card_index_cpu])
                        pygame.draw.rect(gwindow_2, black,
                                            ((104, 140),(231, 181)))
                        pygame.draw.rect(gwindow_2, black,
                                            ((104, 140),(435, 181)))
                        card_holder_flag_1 = True
                        card_holder_flag_2 = True
                        card_lock_1 = False
                        chosen_attribute_index = 0
                        chosen_attribute_final_value_cpu = ""
                        chosen_attribute_final_value = ""
                        available_attribute_values.clear()

                #This section is dedicated to Computer choosing the cards on its
                #own turn and changing flags for letting the player choose
                #his/her own card on the basis of computers attribute choice.
                if not turn_flag and len(card_set_2)> 0:
                    chosen_attribute_index = random.randint(1, 6)
                    chosen_attribute_final = attributes_list[(
                                                    chosen_attribute_index)]
                    
                    display_text(gwindow_2, chosen_attribute_final,
                                 black, 359, 335, 20, "OCRAEXT")
                    
                    available_attribute_values = []
                    available_attribute_values.clear()
                    for cpu_cards in card_set_2: 
                        if chosen_attribute_index == 1:
                            available_attribute_values.append(
                                int(sevendeadlysins_index[cpu_cards].rank))
                        if chosen_attribute_index == 2:
                            available_attribute_values.append(
                                sevendeadlysins_index[cpu_cards].ATK)
                        if chosen_attribute_index == 3:
                            available_attribute_values.append(
                                sevendeadlysins_index[cpu_cards].HP)
                        if chosen_attribute_index == 4:
                            available_attribute_values.append(
                                sevendeadlysins_index[cpu_cards].DP)
                        if chosen_attribute_index == 5:
                            available_attribute_values.append(
                                sevendeadlysins_index[cpu_cards].SP)
                        if chosen_attribute_index == 6:
                            available_attribute_values.append(
                                sevendeadlysins_index[cpu_cards].IQ)
                    

                    choice_luck = random.randint(1, 100)
                    #giving players a chance to win by making computer to do
                    #a deliberate wrong choice.
                    #Luck probability for best card to be banned is 2%.
                    #Luck probability for wrong or random choice is 50%.
                    if choice_luck == 11 or choice_luck == 8:
                        #In this lucky turn the player definitely won't have to
                        #worry about the strongest card computer holds under
                        #that chosen attribute.
                        if chosen_attribute_index == 1:
                            ban_cpu_c = available_attribute_values.index(
                                min(available_attribute_values))
                            card_set_2.remove(card_set_2[ban_cpu_c])
                            available_attribute_values.clear()
                            for cpu_cards in card_set_2:
                                available_attribute_values.append(
                                    int(sevendeadlysins_index[cpu_cards].rank))
                                
                            chosen_card_index_cpu = random.randint(
                                0, (len(available_attribute_values)-1))
                            r_val_1806 = sevendeadlysins_index[(
                                card_set_2[chosen_card_index_cpu])].rank
                            chosen_attribute_final_value_cpu = int(r_val_1806)
                        
                        elif chosen_attribute_index in range (2, 7):
                            ban_cpu_c = available_attribute_values.index(
                                max(available_attribute_values))
                            card_set_2.remove(card_set_2[ban_cpu_c])

                            available_attribute_values.clear()
                            for cpu_cards in card_set_2:
                                if chosen_attribute_index == 2:
                                    available_attribute_values.append(
                                        sevendeadlysins_index[cpu_cards].ATK)
                                if chosen_attribute_index == 3:
                                    available_attribute_values.append(
                                        sevendeadlysins_index[cpu_cards].HP)
                                if chosen_attribute_index == 4:
                                    available_attribute_values.append(
                                        sevendeadlysins_index[cpu_cards].DP)
                                if chosen_attribute_index == 5:
                                    available_attribute_values.append(
                                        sevendeadlysins_index[cpu_cards].SP)
                                if chosen_attribute_index == 6:
                                    available_attribute_values.append(
                                        sevendeadlysins_index[cpu_cards].IQ)
                            

                            chosen_card_index_cpu = random.randint(
                                0, (len(available_attribute_values)-1))
                            
                            if chosen_attribute_index == 2:
                                r_val_1806 = sevendeadlysins_index[(
                                    card_set_2[chosen_card_index_cpu])].ATK
                                chosen_attribute_final_value_cpu = r_val_1806
                            if chosen_attribute_index == 3:
                                r_val_1806 = sevendeadlysins_index[(
                                    card_set_2[chosen_card_index_cpu])].HP
                                chosen_attribute_final_value_cpu = r_val_1806
                            if chosen_attribute_index == 4:
                                r_val_1806 = sevendeadlysins_index[(
                                    card_set_2[chosen_card_index_cpu])].DP
                                chosen_attribute_final_value_cpu = r_val_1806
                            if chosen_attribute_index == 5:
                                r_val_1806 = sevendeadlysins_index[(
                                    card_set_2[chosen_card_index_cpu])].SP
                                chosen_attribute_final_value_cpu = r_val_1806
                            if chosen_attribute_index == 6:
                                r_val_1806 = sevendeadlysins_index[(
                                    card_set_2[chosen_card_index_cpu])].IQ
                                chosen_attribute_final_value_cpu = r_val_1806
                            
                    elif choice_luck%2 == 0:
                        #In this lucky turn the player might have a chance to
                        #be faced with the strongest card computer has as well
                        #as have the chance to not get hit by the strongest one.
                        if chosen_attribute_index == 1:
                            chosen_card_index_cpu = random.randint(
                                0, (len(available_attribute_values)-1))
                            r_val_1806 = sevendeadlysins_index[(
                                card_set_2[chosen_card_index_cpu])].rank
                            chosen_attribute_final_value_cpu = int(r_val_1806)
                        elif chosen_attribute_index in range (2, 7):
                            chosen_card_index_cpu = random.randint(
                                0, (len(available_attribute_values)-1))
                            if chosen_attribute_index == 2:
                                r_val_1806 = sevendeadlysins_index[(
                                    card_set_2[chosen_card_index_cpu])].ATK
                                chosen_attribute_final_value_cpu = r_val_1806
                            if chosen_attribute_index == 3:
                                r_val_1806 = sevendeadlysins_index[(
                                    card_set_2[chosen_card_index_cpu])].HP
                                chosen_attribute_final_value_cpu = r_val_1806
                            if chosen_attribute_index == 4:
                                r_val_1806 = sevendeadlysins_index[(
                                    card_set_2[chosen_card_index_cpu])].DP
                                chosen_attribute_final_value_cpu = r_val_1806
                            if chosen_attribute_index == 5:
                                r_val_1806 = sevendeadlysins_index[(
                                    card_set_2[chosen_card_index_cpu])].SP
                                chosen_attribute_final_value_cpu = r_val_1806
                            if chosen_attribute_index == 6:
                                r_val_1806 = sevendeadlysins_index[(
                                    card_set_2[chosen_card_index_cpu])].IQ
                                chosen_attribute_final_value_cpu = r_val_1806
                    
                    else:
                        if chosen_attribute_index == 1:
                            m_value_1806_i = available_attribute_values.index(
                                min(available_attribute_values))
                            m_value_1806 = sevendeadlysins_index[(
                                card_set_2[m_value_1806_i])].rank 
                            chosen_card_index_cpu = m_value_1806_i
                            chosen_attribute_final_value_cpu = int(m_value_1806)
                        elif chosen_attribute_index in range (2, 7):
                            m_value_1806_i = available_attribute_values.index(
                                max(available_attribute_values))
                            chosen_card_index_cpu = m_value_1806_i
                            if chosen_attribute_index == 2:
                                m_value_1806 = sevendeadlysins_index[(
                                    card_set_2[m_value_1806_i])].ATK
                                chosen_attribute_final_value_cpu = m_value_1806
                            if chosen_attribute_index == 3:
                                m_value_1806 = sevendeadlysins_index[(
                                    card_set_2[m_value_1806_i])].HP
                                chosen_attribute_final_value_cpu = m_value_1806
                            if chosen_attribute_index == 4:
                                m_value_1806 = sevendeadlysins_index[(
                                    card_set_2[m_value_1806_i])].DP 
                                chosen_attribute_final_value_cpu = m_value_1806
                            if chosen_attribute_index == 5:
                                m_value_1806 = sevendeadlysins_index[(
                                    card_set_2[m_value_1806_i])].SP
                                chosen_attribute_final_value_cpu = m_value_1806
                            if chosen_attribute_index == 6:
                                m_value_1806 = sevendeadlysins_index[(
                                    card_set_2[m_value_1806_i])].IQ
                                chosen_attribute_final_value_cpu = m_value_1806


                    time.sleep(2)
                    card_holder_flag_2 = False
                    attribute_lock_2 = True
                    card_lock_1 = False
                    attribute_lock_1 = True
                    turn_flag = True
                    current_turn = False
                    chosen_cpu_card_image = pygame.image.load(
                        sevendeadlysins_index[(
                            card_set_2[chosen_card_index_cpu])].card_image
                                                             ).convert_alpha()
                    chosen_cpu_card_image = pygame.transform.scale(
                        chosen_cpu_card_image, (104, 140))
                    card_lock_2 = True
            
            show_whole_deck_rect = pygame.draw.rect(gwindow_2, black_light,
                                                    ((760, 540), (195, 20)))
            display_text(gwindow_2, "Show whole deck", white,
                         780, 540, 17, "OCRAEXT")
        
        #Runs when one of the hand become empty.
        else:
            gwindow_2.fill(black)
            display_text(gwindow_2, "GAME OVER", white, 375, 200, 50, "COLONNA")
            
            if total_cards_1 > total_cards_2:
                display_text(gwindow_2, "Player 1 wins",
                             white, 375, 300, 50, "COLONNA")
                win = True
            
            elif total_cards_1 < total_cards_2:
                display_text(gwindow_2, "Player 2 wins",
                             white, 375, 300, 50, "COLONNA")
                loss = True
                user_data_packets[3] = "losses = {}\n".format(
                                           int(data_set[3])+1)
            
            dashboard_button = pygame.draw.rect(gwindow_2, white,
                                                ((380, 400), (200, 80)))
            dashboard_txt = display_text(gwindow_2, "Dashboard", black,
                                         388, 420, 35, "OCRAEXT")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    event_flag = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        event_flag = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    #Ends the program and calls the dashboard window again.
                    if dashboard_button.collidepoint(event.pos):
                        event_flag = False
            
        pygame.display.flip()
    
    #Opens user data file to access information as well as update it.
    user_info = open(
        os.path.join(main_file_directory,
                     "users", "{0}.batdata".format(user_id_text_stored)), "a+")
    user_info.seek(0)
    user_data_packets = user_info.readlines()
    data_set = []
    for packet in user_data_packets:
        data = packet.split(" = ")
        data_set.append(data[1])

    if win:
        user_data_packets[2] = "wins = {}\n".format(int(data_set[2])+1)
    elif loss:
        user_data_packets[3] = "losses = {}".format(int(data_set[3])+1)
    
    user_info.truncate(0)
    user_info.seek(0)
    user_info.writelines(user_data_packets)
    user_info.close()

    #calls dashboard menu
    # dashboard_window(window_size, main_file_directory,
    #                user_id_text_stored, user_password_text_stored)


game_p2(big_window_size, main_file_directory, "asdf", "asdf")
pygame.quit()