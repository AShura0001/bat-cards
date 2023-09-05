import pygame
import os

#colors
black = (0, 0, 0)
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

def dashboard_window(window_size, main_file_directory):
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
            mode_selector(window_size, main_file_directory)
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

def mode_selector(window_size, main_file_directory):
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
            solo_menu_selector(window_size, main_file_directory)
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

def solo_menu_selector(winodw_size, main_file_directory):
    solo_menu_window = pygame.display.set_mode(winodw_size)
    solo_menu_window.fill(black)
    event_flag = True

    universes_btn_image = pygame.image.load(os.path.join(main_file_directory, "assets", "universes_btn.png")).convert_alpha()
    universes_btn_image_rect = universes_btn_image.get_rect(center = (602, 350))
    free_play_btn_image = pygame.image.load(os.path.join(main_file_directory, "assets", "free_play_btn.png")).convert_alpha()
    free_play_btn_image_rect = free_play_btn_image.get_rect(center = (355, 350))
    while event_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                event_flag = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    event_flag = False
        
        solo_menu_window.blit(universes_btn_image, universes_btn_image_rect)
        solo_menu_window.blit(free_play_btn_image, free_play_btn_image_rect)
        press_ESC_text = display_text(solo_menu_window, "press ESC to exit", white, 19.55, 14.44, 17, "AGENCYR")
        Solo_menu_text = display_text(solo_menu_window, "Solo Menu", white, 270, 190, 90, "OLDENGL")
        pygame.display.update()

def game_p1(window_size , main_file_directory):
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
        for event in pygame.event.get():

            if start_flag:
                gwindow_1.fill(black)
                pygame.display.update()
                time.sleep(2)
                event_flag = False

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
            h = 82
            w = 56
            pygame.draw.rect(gwindow_1, uni_red, [(30 + (70*i), 60), (w, h)])
            pygame.draw.rect(gwindow_1, uni_red, [(30 + (70*i), 160), (w, h)])
            pygame.draw.rect(gwindow_1, uni_red, [(30 + (70*i), 260), (w, h)])
            pygame.draw.rect(gwindow_1, uni_red, [(30 + (70*i), 360), (w, h)])


        gwindow_1.blit(start_btn_game_window, start_btn_game_window_rect)
        gwindow_1.blit(pause_btn, pause_btn_rect)
        press_ESC_text = display_text(gwindow_1, "press ESC to exit", white, 19.55, 14.44, 17, "AGENCYR")
        pygame.display.update()

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

                if user_id_text_stored + str("\n") == data_set[0] and user_password_text_stored == data_set[1]:
                    submit_flag = False
                    dashboard_window(big_window_size, main_file_directory)
                    break
                else:
                    print("wrong credentials")
                    print (data_set)

        pygame.display.update()
