import pygame
import os

#colors
black = (0, 0, 0)
white = (255, 255, 255)
GREY1 = (204, 204, 204)
uni_red = (200, 0, 0)



def display_text(gwindow, text, color, x, y, font_size, Font):
    font = pygame.font.SysFont(Font, font_size)
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
        
        print(Play_flag, Inventory_flag, Shop_flag, Guide_flag, Setting_flag, Logs_flag)
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
                if event.key == pygame.K_BACKSPACE:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_BACKSPACE]:
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
                    user_password_text += event.unicode
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

        display_text(gwindow, "BAT CARDS LOGIN", white, 206.66, 201.61, 33, "OCR A Extended")
        gwindow.blit(arrow_login_page, (arrow_login_page_rect))
        gwindow.blit(support_logo, (support_logo_rect))

        if not enter_user_id_flag and len(user_id_text) == 0:
            display_text(gwindow, "Enter user ID", GREY1, 213.04, 238.15, 28, "OCR A Extended")
        if not enter_password_flag and len(user_password_text) == 0: 
            display_text(gwindow, "Enter password", GREY1, 213.04, 285.67, 28, "OCR A Extended")
        
        if enter_user_id_flag:
            user_id_rect = pygame.draw.rect(gwindow, white, [206.66, 240.32, 435, 33])
            user_id_text_rect = display_text(gwindow, user_id_text, black, 213.04, 238.15, 28, "OCR A Extended")
            if user_id_text_rect.width > 434:
                user_id_text = user_id_text[1:] 

        if enter_password_flag:
            user_password_rect = pygame.draw.rect(gwindow, white, [206.66, 287, 435, 33])
            user_passowrd_text_rect = display_text(gwindow, user_password_text, black, 213.04, 285.67, 28, "OCR A Extended")
            if user_passowrd_text_rect.width > 434:
                user_password_text = user_password_text[1:]
        
        
        pygame.display.update()
