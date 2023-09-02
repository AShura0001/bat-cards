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

def solo_menu_selector(winodw_size, main_file_directory):
    solo_menu_window = pygame.display.set_mode(winodw_size)
    solo_menu_window.fill(black)
    event_flag = True
    solo_btn_image = pygame.image.load(os.path.join(main_file_directory, "assets", "solo_mode_btn.png")).convert_alpha()
    solo_btn_image_rect = solo_btn_image.get_rect(center = (342, 300))

    multiplayer_btn_image = pygame.image.load(os.path.join(main_file_directory, "assets", "multiplayer_mode_btn.png")).convert_alpha()
    multiplayer_btn_image_rect = multiplayer_btn_image.get_rect(center = (610, 300))
    

    while event_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                event_flag = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    event_flag = False
        
        solo_menu_window.blit(solo_btn_image, solo_btn_image_rect)
        solo_menu_window.blit(multiplayer_btn_image, multiplayer_btn_image_rect)
        press_ESC_text = display_text(solo_menu_window, "press ESC to exit", white, 19.55, 14.44, 17, "AGENCYR")
        Solo_menu_text = display_text(solo_menu_window, "Solo Menu", white, 270, 190, 90, "OLDENGL")
        pygame.display.update()
solo_menu_selector(big_window_size, main_file_directory)
pygame.quit()