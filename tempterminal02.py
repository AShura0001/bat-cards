import pygame
import os

#colors
black = (0, 0, 0)
white = (255, 255, 255)
GREY1 = (204, 204, 204)
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

dashboard_window(big_window_size, main_file_directory)
pygame.quit()