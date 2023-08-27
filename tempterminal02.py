import pygame
import os

#colors
black = (0, 0, 0)
white = (255, 255, 255)
GREY1 = (204, 204, 204)
pygame.init()

def display_text(gwindow, text, color, x, y, font_size, Font):
    font = pygame.font.SysFont(Font, font_size)
    screen_text = font.render(text, True, color)
    screen_text_rect = screen_text.get_rect(center = (x, y))
    gwindow.blit(screen_text, [x,y])
    return screen_text_rect

def login_page(window_size, main_file_directory):
    gwindow = pygame.display.set_mode(window_size)
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

login_page((960, 560), os.getcwd())

pygame.quit()