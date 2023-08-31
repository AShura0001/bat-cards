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
mode_selector(big_window_size, main_file_directory)
pygame.quit()