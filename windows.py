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

def support_window(window_size, main_file_directory):
    """This is the function which is used to display the support options"""

    supp_window = pygame.display.set_mode(window_size, pygame.NOFRAME)
    event_flag = True
    discord_flag = False
    report_a_bug_flag = False

    supp_window.fill((black))
    
    discord_support_icon = pygame.image.load(
        os.path.join(main_file_directory, "assets", 
                     "discord_support_icon.png")).convert_alpha()
    
    discord_support_icon_rect = discord_support_icon.get_rect(center=(180, 180))

    report_a_bug_icon = pygame.image.load(
        os.path.join(main_file_directory, "assets",
                     "report_a_bug_support_icon.png")).convert_alpha()
    
    report_a_bug_icon_rect = report_a_bug_icon.get_rect(center=(180, 304))

    red_cross = pygame.image.load(
        os.path.join(main_file_directory, "assets",
                     "red_cross.png")).convert_alpha()
    
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

def dashboard_window(window_size, main_file_directory,
                     user_id_text_stored, user_password_text_stored):
    
    dashboard_window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("B.A.T CARDS")
    event_flag = True

    Play_flag = False
    Inventory_flag = False
    Shop_flag = False
    Guide_flag = False
    Setting_flag = False
    Logs_flag = False

    exit_dashboard_btn = pygame.image.load(
                        os.path.join(main_file_directory, "assets",
                                    "exit_dashboard_btn.png")).convert_alpha()
    
    exit_dashboard_btn_rect = exit_dashboard_btn.get_rect(center=(480, 468))

    dashboard_window.fill((black))
    while event_flag:

        if Play_flag:
            Play_flag = False
            #Calls the mode_selector function/window and breaks the loop.
            mode_selector(window_size, main_file_directory,
                          user_id_text_stored, user_password_text_stored)
            break   #Breaking loop increases the programm speed and prevents
                    #unnecessary display of any previous windows.
        
        if Inventory_flag:
            Inventory_flag = False
            #Calls the inventory function/window and breaks the loop.
            inventory(window_size, main_file_directory,
                      user_id_text_stored, user_password_text_stored)
            break  #Breaking loop increases the programm speed and prevents
                   #unnecessary display of any previous windows.
        
        if Guide_flag:
            Guide_flag = False
            #Calls the guide function/window and breaks the loop.``
            guide(window_size, main_file_directory,
                  user_id_text_stored, user_password_text_stored)
            break  #Breaking loop increases the programm speed and prevents
                   #unnecessary display of any previous windows.
        
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

        white_rectangle_1 = pygame.draw.rect(dashboard_window, white,
                                             ((260,297), (216, 35)))
        white_rectangle_2 = pygame.draw.rect(dashboard_window, white,
                                             ((260,341), (216, 35)))
        white_rectangle_3 = pygame.draw.rect(dashboard_window, white,
                                             ((260,385), (216, 35)))

        white_rectangle_4 = pygame.draw.rect(dashboard_window, white,
                                             ((480,297), (216, 35)))
        white_rectangle_5 = pygame.draw.rect(dashboard_window, white,
                                             ((480,341), (216, 35)))
        white_rectangle_6 = pygame.draw.rect(dashboard_window, white,
                                             ((480,385), (216, 35)))

        dashboard_window.blit(exit_dashboard_btn, exit_dashboard_btn_rect)

        bat_text = display_text(dashboard_window,"B.A.T",
                                white, 339, 144, 100, "OLDENGL")
        cards_text = display_text(dashboard_window, "CARDS",
                                  white, 430, 240.5, 36, "COLONNA")
        press_ESC_text = display_text(dashboard_window, "press ESC to exit",
                                      white, 19.55, 14.44, 17, "AGENCYR")

        Play_btn_text = display_text(dashboard_window, "Play",
                                     black, 336.26, 300, 28, "ARLRDBD")
        Inventory_btn_text = display_text(dashboard_window, "Inventory",
                                          black, 300, 345, 28, "ARLRDBD")
        Shop_btn_text = display_text(dashboard_window, "Shop",
                                     black, 338.47, 390, 28, "ARLRDBD")
        shop_na_text = display_text(dashboard_window, "N/A",
                                    uni_red, 413, 400, 15, "OCRAEXT")

        Guide_btn_text = display_text(dashboard_window, "Guide",
                                      black, 545, 300, 28, "ARLRDBD")
        Setting_btn_text = display_text(dashboard_window, "Setting",
                                        black, 535, 345, 28, "ARLRDBD")
        setting_na_text = display_text(dashboard_window, "N/A",
                                       uni_red, 640, 355, 15, "OCRAEXT")
        Logs_btn_text = display_text(dashboard_window, "Logs",
                                     black, 550, 390, 28, "ARLRDBD")
        logs_na_text = display_text(dashboard_window, "N/A",
                                    uni_red, 620, 400, 15, "OCRAEXT")
        
        pygame.display.update()

def guide(window_size, main_file_directory,
          user_id_text_stored, user_password_text_stored):
    
    guide_window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("B.A.T CARDS")
    guide_window.fill(black)
    event_flag = True
    point = 1 #indicates the slide number on the guide window.
    dashboard_btn_flag = False

    while event_flag:

        if dashboard_btn_flag:
            event_flag = False
            #Calls the dashboard function/window and breaks the loop.
            dashboard_window(window_size, main_file_directory,
                             user_id_text_stored, user_password_text_stored)
            break #Breaking loop increases the programm speed and prevents
                  #unnecessary display of any previous windows.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                event_flag = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    event_flag = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_arrow.collidepoint(event.pos) and point<7:
                    point += 1
                    guide_window.fill(black)
                if back_arrow.collidepoint(event.pos) and point>1:
                    point -= 1
                    guide_window.fill(black)
                
        display_text(guide_window, "Guide", white, 380, 15, 80, "COLONNA")
        
        #Creating Triangles to help user move through guide slides.
        next_arrow = pygame.draw.polygon(guide_window, white,
                                         [[945, 525], [915, 510], [915, 540]])
        back_arrow = pygame.draw.polygon(guide_window, white,
                                         [[20, 525], [50, 510], [50, 540]])
        
        if point == 1:
            l1 = "There are 52 cards in a deck (per universe). All cards are "
            l2 = "unique in their own way and all cards are sorted by rank from"
            l3 = "1 to 52 and are shown before the game starts. For eg:-"
            display_text(guide_window, "01.", white, 40, 140, 20, "OCRAEXT")
            display_text(guide_window, l1, white, 90, 140, 20, "OCRAEXT")
            display_text(guide_window, l2, white, 90, 170, 20, "OCRAEXT")
            display_text(guide_window, l3, white, 90, 200, 20, "OCRAEXT")
            
            i1 = pygame.image.load(
                os.path.join(main_file_directory, "assets",
                             "guide pics", "1.1.png"))
            i1 = pygame.transform.scale(i1, (450, 260))
            guide_window.blit(i1, [225, 255])
            
        if point == 2:
            l1 = "Each card has 6 attributes that are unique to each card and"
            l2 = "their values depend on the rank or rating of the respective"
            l3 = "card. The attributes [denotation] (range) are as follows:- "
            l4 = "Rank [Rank] (1 to 52)"
            l5 = "ATTACK POWER [ATK] (0 to 5000)"
            l6 = "HEALTH POWER [HP] (0 to 5000)"
            l7 = "DEFENSE POWER [DP] (0 to 5000)"
            l8 = "SPEED POWER [SP] (0 to 5000)"
            l9 = "BATTLE IQ [IQ] (0 to 5000)"

            display_text(guide_window, "02.", white, 40, 140, 20, "OCRAEXT")
            display_text(guide_window, l1, white, 90, 140, 20, "OCRAEXT")
            display_text(guide_window, l2, white, 90, 170, 20, "OCRAEXT")
            display_text(guide_window, l3, white, 90, 200, 20, "OCRAEXT")

            display_text(guide_window, l4, white, 90, 280, 20, "OCRAEXT")
            display_text(guide_window, l5, white, 90, 310, 20, "OCRAEXT")
            display_text(guide_window, l6, white, 90, 340, 20, "OCRAEXT")
            display_text(guide_window, l7, white, 90, 370, 20, "OCRAEXT")
            display_text(guide_window, l8, white, 90, 400, 20, "OCRAEXT")
            display_text(guide_window, l9, white, 90, 430, 20, "OCRAEXT")

            i1 = pygame.image.load(
                os.path.join(main_file_directory, "assets", "cards", 
                             "seven deadly sins cards", "3_merlin_normal.png"))
            i1 = pygame.transform.scale(i1, (240, 290))
            guide_window.blit(i1, [500, 245])
        
        if point == 3:
            l1 = "The game starts with the computer shuffling the deck randomly"
            l2 = "providing the players with 26 random cards sorted according to"
            l3 = "their ranks. And player is given the first turn to choose"
            l4 = "a card from the hand and one of its respective attributes"

            display_text(guide_window, "03.", white, 40, 140, 20, "OCRAEXT")
            display_text(guide_window, l1, white, 90, 140, 20, "OCRAEXT")
            display_text(guide_window, l2, white, 90, 170, 20, "OCRAEXT")
            display_text(guide_window, l3, white, 90, 200, 20, "OCRAEXT")
            display_text(guide_window, l4, white, 90, 230, 20, "OCRAEXT")

            i1 = pygame.image.load(
                os.path.join(main_file_directory, "assets",
                             "guide pics", "3.1.png"))
            i1 = pygame.transform.scale(i1, (650, 260))
            guide_window.blit(i1, [140, 265])
        
        if point == 4:
            l1 = "To view further information"
            l2 = "regarding the cards displayed at"
            l3 = "the bottom tab, look at the" 
            l4 = "right vertical tab where"
            l5 = "information regarding respective"
            l6 = "cards are displayed."
            l7 = "You can also use 'Show Whole Deck' feature at the bottom of"
            l8 = "the right vertical tab to access all the 52 cards available in"
            l9 = "the deck and their respective informations."

            display_text(guide_window, "04.", white, 40, 140, 20, "OCRAEXT")
            display_text(guide_window, l1, white, 90, 140, 15, "OCRAEXT")
            display_text(guide_window, l2, white, 90, 170, 15, "OCRAEXT")
            display_text(guide_window, l3, white, 90, 200, 15, "OCRAEXT")
            display_text(guide_window, l4, white, 90, 230, 15, "OCRAEXT")
            display_text(guide_window, l5, white, 90, 260, 15, "OCRAEXT")
            display_text(guide_window, l6, white, 90, 290, 15, "OCRAEXT")

            display_text(guide_window, l7, white, 90, 360, 20, "OCRAEXT")
            display_text(guide_window, l8, white, 90, 390, 20, "OCRAEXT")
            display_text(guide_window, l9, white, 90, 420, 20, "OCRAEXT")

            i1 = pygame.image.load(
                os.path.join(main_file_directory, "assets",
                             "guide pics", "4.1.png"))
            i1 = pygame.transform.scale(i1, (300, 200))
            guide_window.blit(i1, [470, 120])

            i2 = pygame.image.load(
                os.path.join(main_file_directory, "assets",
                             "guide pics", "4.2.png"))
            i2 = pygame.transform.scale(i2, (300, 100))
            guide_window.blit(i2, [375, 465])
        
        if point == 5:
            l1 = "At each turn player (or computer) choooses a card and one of"
            l2 = "its respective attribute from the 6 aforementioned attributes"
            l3 = "and the opposing team (not on turn) chooses a card from their"
            l4 = "hand based on the chosen attribute and then both the values"
            l5 = "of the chosen attribute of the chosen cards are compared."
            l6 = "The card with higher attribute value (except rank) wins"
            l7 = "and both the cards are removed from the hands of both parties"
            l8 = "and added to the wining parties winning set whose cards can't"
            l9 = "be accessed by the players during the whole match."
            l10 = "Note:- In the case of rank attribute being chosen, the card"
            l11 = "with lower rank number is supposedly higher rank card and"
            l12 = "out of both the cards the one with lower rank number wins"

            display_text(guide_window, "05.", white, 40, 140, 20, "OCRAEXT")
            display_text(guide_window, l1, white, 90, 140, 20, "OCRAEXT")
            display_text(guide_window, l2, white, 90, 170, 20, "OCRAEXT")
            display_text(guide_window, l3, white, 90, 200, 20, "OCRAEXT")
            display_text(guide_window, l4, white, 90, 230, 20, "OCRAEXT")
            display_text(guide_window, l5, white, 90, 260, 20, "OCRAEXT")
            display_text(guide_window, l6, white, 90, 290, 20, "OCRAEXT")
            display_text(guide_window, l7, white, 90, 320, 20, "OCRAEXT")
            display_text(guide_window, l8, white, 90, 350, 20, "OCRAEXT")
            display_text(guide_window, l9, white, 90, 380, 20, "OCRAEXT")

            display_text(guide_window, l10, white, 90, 450, 20, "OCRAEXT")
            display_text(guide_window, l11, white, 90, 480, 20, "OCRAEXT")
            display_text(guide_window, l12, white, 90, 510, 20, "OCRAEXT")

        if point == 6:
            l1 = "To choose a card from the hand simply click on the required"
            l2 = "card from the bottom tab (use scroll bar for more cards)."
            l3 = "After clicking on the required card it shows up in middle"
            l4 = "with 6 attribute buttons as shown in the illustration."
            l5 = "While on turn player can click on one of the attribute button"
            l6 = "to choose the desired attribute and the attribute name will"
            l7 = "show up on the chosen attribute white space below with the"
            l8 = "respective attribute value on top of the card chosen."
            l9 = "To finish placing the desired card just simply press the"
            l10 = "Place button in the middle and the card will be submitted"

            display_text(guide_window, "06.", white, 40, 140, 20, "OCRAEXT")
            display_text(guide_window, l1, white, 90, 140, 13, "OCRAEXT")
            display_text(guide_window, l2, white, 90, 170, 13, "OCRAEXT")
            
            display_text(guide_window, l3, white, 90, 230, 13, "OCRAEXT")
            display_text(guide_window, l4, white, 90, 260, 13, "OCRAEXT")

            display_text(guide_window, l5, white, 90, 320, 13, "OCRAEXT")
            display_text(guide_window, l6, white, 90, 350, 13, "OCRAEXT")
            display_text(guide_window, l7, white, 90, 380, 13, "OCRAEXT")
            display_text(guide_window, l8, white, 90, 410, 13, "OCRAEXT")

            display_text(guide_window, l9, white, 90, 470, 13, "OCRAEXT")
            display_text(guide_window, l10, white, 90, 500, 13, "OCRAEXT")

            i1 = pygame.image.load(
                os.path.join(main_file_directory, "assets",
                             "guide pics", "6.1.png"))
            i1 = pygame.transform.scale(i1, (200, 80))
            guide_window.blit(i1, [608, 107])

            i2 = pygame.image.load(
                os.path.join(main_file_directory, "assets",
                             "guide pics", "6.2.png"))
            i2 = pygame.transform.scale(i2, (200, 80))
            guide_window.blit(i2, [624, 217])

            i3 = pygame.image.load(
                os.path.join(main_file_directory, "assets",
                             "guide pics", "6.3.png"))
            i3 = pygame.transform.scale(i3, (100, 140))
            guide_window.blit(i3, [686, 317])

            i4 = pygame.image.load(
                os.path.join(main_file_directory, "assets",
                             "guide pics", "6.4.png"))
            i4 = pygame.transform.scale(i4, (90, 50))
            guide_window.blit(i4, [580, 480])

        if point == 7:
            l1 = "The number of cards at hand + number of cards won are shown"
            l2 = "at the corner point as illustrated and when the no. of cards"
            l3 = "in hand goes to 0 for any of the players (or computer) then"
            l4 = "the game will be over and the respective win or loss stats "
            l5 = "will be updated in the user history."
            l6 = "Win or Loss stats can be accessed in the inventory from the"
            l7 = "dashboard menu."

            display_text(guide_window, "07.", white, 40, 140, 20, "OCRAEXT")
            display_text(guide_window, l1, white, 90, 140, 20, "OCRAEXT")
            display_text(guide_window, l2, white, 90, 170, 20, "OCRAEXT")
            display_text(guide_window, l3, white, 90, 200, 20, "OCRAEXT")
            display_text(guide_window, l4, white, 90, 230, 20, "OCRAEXT")
            display_text(guide_window, l5, white, 90, 260, 20, "OCRAEXT")

            display_text(guide_window, l6, white, 90, 420, 20, "OCRAEXT")
            display_text(guide_window, l7, white, 90, 450, 20, "OCRAEXT")

            i1 = pygame.image.load(
                os.path.join(main_file_directory, "assets",
                             "guide pics", "7.1.png"))
            i1 = pygame.transform.scale(i1, (400, 100))
            guide_window.blit(i1, [207, 295])

            #Create a button to return to dashboard menu
            dasboard_btn = pygame.draw.rect(guide_window, white,
                                            [370, 490, 150, 50])
            display_text(guide_window, "Dashboard",
                         black, 390, 505, 20, "OCRAEXT")
            for event_2 in pygame.event.get():
                if event_2.type == pygame.QUIT:
                    event_flag = False
                if event_2.type == pygame.KEYDOWN:
                    if event_2.key == pygame.K_ESCAPE:
                        event_flag = False

                if event_2.type == pygame.MOUSEBUTTONDOWN:
                    #If the mouse button is pressed on the dashboard button
                    #then the dashboard window flag is set to True.
                    if dasboard_btn.collidepoint(event_2.pos):
                        dashboard_btn_flag = True
                    if next_arrow.collidepoint(event_2.pos) and point<7:
                        point += 1
                        guide_window.fill(black)
                    if back_arrow.collidepoint(event_2.pos) and point>1:
                        point -= 1
                        guide_window.fill(black)

        pygame.display.update()

def inventory(window_size, main_file_directory,
              user_id_text_stored, user_password_text_stored):
    
    inventory_window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("B.A.T CARDS")
    inventory_window.fill(black)
    event_flag = True
    dashboard_flag = False

    while event_flag:
    
        if dashboard_flag:
            event_flag = False
            #Calls the dashboard function/window and breaks the loop.
            dashboard_window(window_size, main_file_directory, user_id_text_stored, user_password_text_stored)
            break #Breaking loop increases the programm speed and prevents
                  #unnecessary display of any previous windows.
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                event_flag = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    event_flag = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dashboard_menu_btn.collidepoint(event.pos):
                    dashboard_flag = True

        #User data is accessed to collect user's name and win/loss stats.
        user_info = open(
            os.path.join(main_file_directory, "users",
                         "{0}.batdata".format(user_id_text_stored)), "a+")
        user_info.seek(0)
        user_data_packets = user_info.readlines()
        data_set = []
        for packet in user_data_packets:
            data = packet.split(" = ")
            data_set.append(data[1].strip())

        #Create a border around the inventory window.
        pygame.draw.rect(inventory_window, white, [0, 0, window_size[0], window_size[1]], 5)
        
        #Create a button to return to dashboard menu
        dashboard_menu_btn = pygame.draw.rect(inventory_window, white, [380, 435, 200, 100])
        display_text(inventory_window, "Dashboard", black, 400, 465, 32, "OCRAEXT")
        
        press_ESC_text = display_text(inventory_window,
                                      "press ESC to exit", white,
                                      19.55, 14.44, 17, "AGENCYR")
        
        #Display the header of the inventory window and user's name.
        display_text(inventory_window, "Inventory",
                     white, (window_size[1]//2) + 50, 10, 70, "ARLRDBD")
        display_text (inventory_window, "User: {}".format(data_set[0].strip()),
                      white, (window_size[1]//2) + 150, 90, 18, "OCRAEXT")
        
        
        WINS = display_text(inventory_window,
                            "WINS", white, 90, 200, 90, "ARLRDBD")
        display_text(inventory_window,
                     str(data_set[2].strip()), white, 180, 300, 60, "ARLRDBD")
        
        LOSSES = display_text(inventory_window,
                              "LOSSES", white, 520, 200, 90, "ARLRDBD")
        display_text(inventory_window,
                     str(data_set[3].strip()), white, 700, 300, 60, "ARLRDBD")

        pygame.display.update()

def mode_selector(window_size, main_file_directory,
                  user_id_text_stored, user_password_text_stored):

    mode_selector_window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("B.A.T CARDS")
    mode_selector_window.fill(black)

    solo_btn_image = pygame.image.load(
        os.path.join(main_file_directory, "assets",
                     "solo_mode_btn.png")).convert_alpha()
    solo_btn_image_rect = solo_btn_image.get_rect(center = (342, 300))

    multiplayer_btn_image = pygame.image.load(
        os.path.join(main_file_directory, "assets",
                     "multiplayer_mode_btn.png")).convert_alpha()
    multiplayer_btn_image_rect = multiplayer_btn_image.get_rect(center = (610, 300))
    
    event_flag = True
    solo_mode_flag = False
    multiplayer_mode_flag = False

    while event_flag:
    
        if solo_mode_flag:
            solo_mode_flag = False
            # Calls the solo_menu_selector function/window and breaks the loop.
            solo_menu_selector(window_size, main_file_directory, user_id_text_stored, user_password_text_stored)
            break #Breaking loop increases the programm speed and prevents
                    #unnecessary display of any previous windows.
            
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
        
        press_ESC_text = display_text(mode_selector_window,
                                      "press ESC to exit", white,
                                      19.55, 14.44, 17, "AGENCYR")
        
        Choose_mode_text = display_text(mode_selector_window,
                                        "Choose A Mode", white,
                                        194.83, 170, 90, "OLDENGL")
        pygame.display.update()

def solo_menu_selector(window_size, main_file_directory,
                       user_id_text_stored, user_password_text_stored):
    
    solo_menu_window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("B.A.T CARDS")
    solo_menu_window.fill(black)
    event_flag = True
    free_play_flag = False

    universes_btn_image = pygame.image.load(
        os.path.join(main_file_directory, "assets",
                     "universes_btn.png")).convert_alpha()
    universes_btn_image_rect = universes_btn_image.get_rect(center = (602, 350))
    
    free_play_btn_image = pygame.image.load(
        os.path.join(main_file_directory, "assets",
                  "free_play_btn.png")).convert_alpha()
    free_play_btn_image_rect = free_play_btn_image.get_rect(center = (355, 350))
    
    while event_flag:

        if free_play_flag:
            free_play_flag = False
            #Calls the game function/window and breaks the loop.
            game_p1(window_size, main_file_directory, user_id_text_stored, user_password_text_stored)
            break #Breaking loop increases the programm speed and prevents
                  #unnecessary display of any previous windows.
        
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
        
        text_1 = display_text(
            solo_menu_window, "FREE PLAY ONLY VERSION [seven deadly sins deck]",
            uni_red, 180, 130, 20, "OCRAEXT")
        
        solo_menu_window.blit(universes_btn_image, universes_btn_image_rect)
        solo_menu_window.blit(free_play_btn_image, free_play_btn_image_rect)
        
        press_ESC_text = display_text(solo_menu_window,
                                      "press ESC to exit", white,
                                      19.55, 14.44, 17, "AGENCYR")
        
        Solo_menu_text = display_text(solo_menu_window,
                                      "Solo Menu", white,
                                      270, 190, 90, "OLDENGL")
        
        pygame.display.update()

def game_p1(window_size , main_file_directory,
            user_id_text_stored, user_password_text_stored):

    gwindow_1 = pygame.display.set_mode(window_size)
    pygame.display.set_caption("B.A.T CARDS")
    gwindow_1.fill(black)
    event_flag = True
    start_flag = False
    pause_flag = False

    start_btn_game_window = pygame.image.load(
        os.path.join(main_file_directory, "assets",
                     "start_btn_game_window.png")).convert_alpha()
    start_btn_game_window_rect = start_btn_game_window.get_rect(
                                            center = (480, 500))

    pause_btn = pygame.image.load(
        os.path.join(main_file_directory, "assets",
                     "pause_btn.png")).convert_alpha()
    pause_btn_rect = pause_btn.get_rect(center = (917, 25))

    while event_flag:

        if start_flag:
            time.sleep(2)
            start_flag = False
            #Calls the game function/window and breaks the loop.
            result =  game_p2(window_size, main_file_directory,
                              user_id_text_stored, user_password_text_stored)
            break #Breaking loop increases the programm speed and prevents
                  #unnecessary display of any previous windows.
        
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


                for column_count in range (1, 14):
                    h = 80
                    w = 40
                    #row_count varies from 0 to 3 for each column and helps in
                    #keeping the y-coordinate of all cards in same row same.
                    row_count = 0

                    for card_num in range (
                        (((column_count-1)*4)+1), ((column_count*4)+1)):
                        #This complicated range of card_num helps to keep the
                        #card numbers in each column different from other column
                        #and also keeps the cards in ascending order.
                        card = pygame.image.load(
                            sevendeadlysins_index[card_num].card_image
                            ).convert_alpha()
                        card = pygame.transform.scale(card, (w, h))
                        gwindow_1.blit(card,[65*column_count, 55+100*row_count])
                        row_count += 1

        gwindow_1.blit(start_btn_game_window, start_btn_game_window_rect)
        gwindow_1.blit(pause_btn, pause_btn_rect)
        press_ESC_text = display_text(gwindow_1,
                                      "press ESC to exit", white,
                                      19.55, 14.44, 17, "AGENCYR")
        pygame.display.update()

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
                    if scroll_bar_horizontal_rect.collidepoint(event.pos):
                        horizontal_indicator_flag = True
                    
                    if (horizontal_end_left_rect.collidepoint(event.pos) and
                        horizontal_scroll_bar_pos > 56):
                        
                        horizontal_scroll_bar_pos -= 54
                        mrk_val_hzntl = horizontal_bar_markings.index(
                            horizontal_scroll_bar_pos)
                        pygame.draw.rect(gwindow_2, black, ((104, 140),(231, 181) ))
                        pygame.draw.rect(gwindow_2, black, ((0, 379), (757 , 159)))
                        card_holder_flag_1 = True
                        card_indexes_2.clear()
                    
                    if (horizontal_end_right_rect.collidepoint(event.pos) and
                        horizontal_scroll_bar_pos < 704):
                    
                        horizontal_scroll_bar_pos += 54
                        mrk_val_hzntl = horizontal_bar_markings.index(
                            horizontal_scroll_bar_pos)
                        pygame.draw.rect(gwindow_2, black, ((104, 140),(231, 181) ))
                        pygame.draw.rect(gwindow_2, black, ((0, 379), (757 , 159)))
                        card_holder_flag_1 = True
                        card_indexes_2.clear()
                    
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

                        if (place_button_rect.collidepoint(event.pos) and
                            attribute_flag and
                            current_turn and
                            attribute_check and
                            chosen_attribute_final_value != ""):
                            
                            if chosen_card_index == len(card_indexes_2):
                                chosen_card_index -= 1
                            place_card_flag_1 = True
                            attribute_flag = True
                            
                            # current_turn = False
                            card_lock_1 = True
                            turn_flag = False

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

                        if (place_button_rect.collidepoint(event.pos) 
                            and chosen_attribute_final_value != ""
                            and not attribute_check):
                            display_text(gwindow_2,
                                         "Attribute not usable", uni_red,
                                         385, 263, 12, "OCRAEXT")
                            
                    if show_whole_deck_rect.collidepoint(event.pos):
                        event_flag_2 = True
                        m = 1
                        screen = pygame.display.set_mode([640, 480])
                        
                        while event_flag_2:
                            screen.fill(black)

                            for event_2 in pygame.event.get():
                                if event_2.type == pygame.QUIT:
                                    event_flag_2 = False
                                    pygame.draw.rect(screen, black,
                                                     ((0, 0), (640, 480)))
                                    time.sleep(0.1)
                                    gwindow_2 = pygame.display.set_mode(
                                        (960,560))
                                
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
            
        
            card_indexes_2 = []
            for i in range((mrk_val_hzntl*4) , ((mrk_val_hzntl+1)*5)): 
                try:
                    card_indexes_2.append(card_set_1[i])
                except:
                    pass
            
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
            if not card_holder_flag_2:    
                display_text(gwindow_2, str(chosen_attribute_final_value_cpu),
                             black, 466, 164, 18, "OCRAEXT")

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
                    chosen_card_index_cpu = available_attribute_values.index(
                        min(available_attribute_values))
                elif chosen_attribute_index in range (2, 7):
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
                        if chosen_attribute_index == 1:
                            ban_cpu_c = available_attribute_values.index(
                                min(available_attribute_values))
                            card_set_2.remove(card_set_2[ban_cpu_c])
                            for cpu_cards in card_set_2:
                                available_attribute_values.append(
                                    int(sevendeadlysins_index[cpu_cards].rank))
                            chosen_card_index_cpu = random.randint(
                                1, len(available_attribute_values))
                            r_val_1806 = sevendeadlysins_index[(
                                card_set_2[chosen_card_index_cpu])].rank
                            chosen_attribute_final_value_cpu = int(r_val_1806)
                        
                        elif chosen_attribute_index in range (2, 7):
                            ban_cpu_c = available_attribute_values.index(
                                max(available_attribute_values))
                            card_set_2.remove(card_set_2[ban_cpu_c])
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
                            
                            mp_2 = random.randint(
                                1, len(available_attribute_values))
                            mp_122 = available_attribute_values.index(mp_2)
                            chosen_card_index_cpu = mp_122
                            
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
                        if chosen_attribute_index == 1:
                            chosen_card_index_cpu = random.randint(
                                1, len(available_attribute_values))
                            r_val_1806 = sevendeadlysins_index[(
                                card_set_2[chosen_card_index_cpu])].rank
                            chosen_attribute_final_value_cpu = int(r_val_1806)
                        elif chosen_attribute_index in range (2, 7):
                            chosen_card_index_cpu = random.randint(
                                1, len(available_attribute_values))
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
            display_text(gwindow_2, "GAME OVER", white, 300, 200, 50, "COLONNA")
            
            if total_cards_1 > total_cards_2:
                display_text(gwindow_2, "Player 1 wins",
                             white, 300, 300, 50, "COLONNA")
                win = True
            
            elif total_cards_1 < total_cards_2:
                display_text(gwindow_2, "Player 2 wins",
                             white, 300, 300, 50, "COLONNA")
                loss = True
                user_data_packets[3] = "losses = {}\n".format(
                                           int(data_set[3])+1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    event_flag = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
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
    dashboard_window(window_size, main_file_directory,
                   user_id_text_stored, user_password_text_stored)

def login_page(big_window_size, small_window_size, main_file_directory):
    
    gwindow = pygame.display.set_mode(big_window_size)
    arrow_login_page = pygame.image.load(
        os.path.join(main_file_directory,
                     "assets", "arrow_login_page.png")).convert_alpha()
    
    arrow_login_page_rect = arrow_login_page.get_rect(center=(668.5, 300.5))
    user_id_text = ""
    user_id_text_stored = ""
    id_writing_flag = False
    user_password_text = ""
    user_password_text_stored = ""
    password_writing_flag = False

    support_logo = pygame.image.load(
        os.path.join(main_file_directory,
                     "assets", "support_logo.png")).convert_alpha()
    support_logo = pygame.transform.scale(support_logo, (47, 47))
    support_logo_rect = support_logo.get_rect(center = (936.5 ,536.5))
    
    gwindow.fill(black)
    event_flag = True

    enter_user_id_flag = False
    enter_password_flag = False
    submit_flag = False
    support_flag = False

    user_id_rect = pygame.draw.rect(gwindow, white, [206.66, 240.32, 435, 33])
    user_password_rect = pygame.draw.rect(gwindow, white, [206.66, 287, 435,33])
    arrow_login_circle = pygame.draw.circle(gwindow, white, (671, 301), 21)
    
    while event_flag:

        if support_flag:
            #Calls support window function.
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
                    
        display_text(gwindow, "Input data is case insensitive",
                     white, 10, 540, 18, "OCRAEXT")
        display_text(gwindow, "BAT CARDS LOGIN",
                     white, 206.66, 201.61, 33, "OCRAEXT")
        gwindow.blit(arrow_login_page, (arrow_login_page_rect))
        gwindow.blit(support_logo, (support_logo_rect))

        if not enter_user_id_flag and len(user_id_text) == 0:
            display_text(gwindow, "Enter user ID",
                         GREY1, 213.04, 238.15, 28, "OCRAEXT")
        if not enter_password_flag and len(user_password_text) == 0: 
            display_text(gwindow, "Enter password",
                         GREY1, 213.04, 285.67, 28, "OCRAEXT")
        
        if enter_user_id_flag:
            user_id_rect = pygame.draw.rect(gwindow, white,
                                            [206.66, 240.32, 435, 33])
            user_id_text_rect = display_text(gwindow, user_id_text, black,
                                             213.04, 238.15, 28, "OCRAEXT")
            if user_id_text_rect.width > 434:
                user_id_text = user_id_text[1:] 

        if enter_password_flag:
            user_password_rect = pygame.draw.rect(gwindow, white,
                                                  [206.66, 287, 435, 33])
            user_passowrd_text_rect = display_text(gwindow, user_password_text,
                                                   black, 213.04, 285.67, 28,
                                                   "OCRAEXT")
            
            if user_passowrd_text_rect.width > 434:
                user_password_text = user_password_text[1:]
        
        if submit_flag and len(user_id_text_stored)>0 and len(user_password_text_stored)>0:
            #Opens data file corresponding to the user data provided
            #Incase the data file is not available one will be created since the
            #file is opened in append mode i.e user will be registered.
            try:
                user_info = open(
                    os.path.join(main_file_directory,
                                 "users", "{0}.batdata".format(
                                     user_id_text_stored)), "a+")
                user_info.seek(0)
                content = user_info.read()
                #Registering the new user with provided details.
                if len(content) == 0:
                    user_info.write("username = "+ str(user_id_text_stored) + "\n")
                    user_info.write(
                        "password = " + str(user_password_text_stored) + "\n")
                    user_info.write("wins = 0\n")
                    user_info.write("losses = 0")
            
                    event_flag = False
                    submit_flag = False
                    dashboard_window(big_window_size, main_file_directory,
                                     user_id_text_stored, user_password_text_stored)
                    user_info.close()
                #Logging in the exisiting user with provided details.
                else:
                    user_info.seek(0)
                    user_data_packets = user_info.readlines()
                    data_set = []
                    for packet in user_data_packets:
                        data = packet.split(" = ")
                        data_set.append(data[1].strip())
                    user_info.close()
    
                    if (user_id_text_stored  == data_set[0] and
                         user_password_text_stored == data_set[1]):
                        submit_flag = False
                        event_flag = False
                        dashboard_window(big_window_size, main_file_directory, user_id_text_stored, user_password_text_stored)
                        break
                    
                    else:
                        display_text(gwindow,
                                     "*Incorrect Credentials Please Try Again",
                                     uni_red, 210, 330, 18, "OCRAEXT")
                        enter_user_id_flag = False
                        enter_password_flag = False
                        user_id_text = ""
                        user_id_text_stored = ""
                        user_password_text = ""
                        user_password_text_stored = ""
                        user_id_rect = pygame.draw.rect(gwindow, white,
                                                        [206.66, 240.32, 435, 33])
                        user_password_rect = pygame.draw.rect(gwindow, white,
                                                              [206.66, 287, 435, 33])
            
            except:
                display_text(gwindow,
                         "Enter only alpha-numeric values from ASCII",
                         uni_red, 210, 350, 18, "OCRAEXT")

        pygame.display.update()
