import pygame
import os
import time
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

def guide(window_size, main_file_directory, user_id_text_stored, user_password_text_stored):
    guide_window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Guide")
    guide_window.fill(black)
    event_flag = True
    point = 1
    dashboard_btn_flag = False
    while event_flag:
        if dashboard_btn_flag:
            event_flag = False
            dashboard_window(window_size, main_file_directory, user_id_text_stored, user_password_text_stored)
            break
        # pygame.draw.polygon(guide_window, white, [[10, 40], [20, 10], [20, 70]], 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                event_flag = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    event_flag = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if next_arrow.collidepoint(event.pos) and point<7:
                    point += 1
                    guide_window.fill(black)
                if back_arrow.collidepoint(event.pos) and point>1:
                    point -= 1
                    guide_window.fill(black)
                if dasboard_btn.collidepoint(event.pos):
                    dashboard_btn_flag = True
        display_text(guide_window, "Guide", white, 380, 15, 80, "COLONNA")
        next_arrow = pygame.draw.polygon(guide_window, white, [[945, 525], [915, 510], [915, 540]])
        back_arrow = pygame.draw.polygon(guide_window, white, [[20, 525], [50, 510], [50, 540]])
        if point == 1:
            l1 = "There are 52 cards in a deck (per universe). All cards are "
            l2 = "unique in their own way and all cards are sorted by rank from"
            l3 = "1 to 52 and are shown before the game starts. For eg:-"
            display_text(guide_window, "01.", white, 40, 140, 20, "OCRAEXT")
            display_text(guide_window, l1, white, 90, 140, 20, "OCRAEXT")
            display_text(guide_window, l2, white, 90, 170, 20, "OCRAEXT")
            display_text(guide_window, l3, white, 90, 200, 20, "OCRAEXT")
            i1 = pygame.image.load(os.path.join(main_file_directory, "assets", "guide pics", "1.1.png"))
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

            i1 = pygame.image.load(os.path.join(main_file_directory, "assets", "cards", "seven deadly sins cards", "3_merlin_normal.png"))
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

            i1 = pygame.image.load(os.path.join(main_file_directory, "assets", "guide pics", "3.1.png"))
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

            i1 = pygame.image.load(os.path.join(main_file_directory, "assets", "guide pics", "4.1.png"))
            i1 = pygame.transform.scale(i1, (300, 200))
            guide_window.blit(i1, [470, 120])

            i2 = pygame.image.load(os.path.join(main_file_directory, "assets", "guide pics", "4.2.png"))
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
            l5 = "While on turn player can click on one of the attribute button to"
            l6 = "choose the desired attribute and the attribute namewill show"
            l7 = "name will show up on the chosen attribute white space below"
            l8 = "with the respective attribute value on top of the card chosen"
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

            i1 = pygame.image.load(os.path.join(main_file_directory, "assets", "guide pics", "6.1.png"))
            i1 = pygame.transform.scale(i1, (200, 80))
            guide_window.blit(i1, [608, 107])

            i2 = pygame.image.load(os.path.join(main_file_directory, "assets", "guide pics", "6.2.png"))
            i2 = pygame.transform.scale(i2, (200, 80))
            guide_window.blit(i2, [624, 217])

            i3 = pygame.image.load(os.path.join(main_file_directory, "assets", "guide pics", "6.3.png"))
            i3 = pygame.transform.scale(i3, (100, 140))
            guide_window.blit(i3, [686, 317])

            i4 = pygame.image.load(os.path.join(main_file_directory, "assets", "guide pics", "6.4.png"))
            i4 = pygame.transform.scale(i4, (90, 50))
            guide_window.blit(i4, [580, 480])

        if point == 7:
            l1 = "The number of cards at hand + number of cards won are shown"
            l2 = "at the corner point as illustrated and when the value of this"
            l3 = "goes to 0 for any of the players (or computer) then the game"
            l4 = "will be over and the respective win or loss stats will be"
            l5 = "updated in the user history."
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

            i1 = pygame.image.load(os.path.join(main_file_directory, "assets", "guide pics", "7.1.png"))
            i1 = pygame.transform.scale(i1, (400, 100))
            guide_window.blit(i1, [207, 295])

            dasboard_btn = pygame.draw.rect(guide_window, white, [370, 490, 150, 50])
            display_text(guide_window, "Dashboard", black, 390, 505, 20, "OCRAEXT")

        pygame.display.update()

guide(big_window_size, main_file_directory)
pygame.quit()