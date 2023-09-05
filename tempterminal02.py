import pygame
import os
import time

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

game_p1(big_window_size, main_file_directory)
pygame.quit()