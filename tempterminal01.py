import pygame
import os

pygame.init()

window_size = (960, 560)
gwindow = pygame.display.set_mode(window_size)
main_file_directory = os.getcwd()

#colors
black = (0, 0, 0)
white = (255, 255, 255)
GREY1 = (204, 204, 204)

#images
arrow_login_page = pygame.image.load(os.path.join(main_file_directory, "assets", "arrow_login_page.png")).convert_alpha()
arrow_login_page_rect = arrow_login_page.get_rect(center=(668.5, 300.5))

support_logo = pygame.image.load(os.path.join(main_file_directory, "assets", "support_logo.png")).convert_alpha()
support_logo = pygame.transform.scale(support_logo, (47, 47))
support_logo_rect = support_logo.get_rect(center = (936.5 ,536.5))

def display_text(text, color, x, y, font_size, Font):
    font = pygame.font.SysFont(Font, font_size)
    screen_text = font.render(text, True, color)
    gwindow.blit(screen_text, [x,y])

def login_page(gwindow):
    gwindow.fill(black)
    event_flag = True
    while event_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                event_flag = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    event_flag = False
        display_text("BAT CARDS LOGIN", white, 206.66, 201.61, 33, "OCR A Extended")
        pygame.draw.rect(gwindow, white,[206.66, 240.32, 435, 33])
        pygame.draw.rect(gwindow, white,[206.66, 287, 435, 33])
        pygame.draw.circle(gwindow, white, (671, 301), 21)
        gwindow.blit(arrow_login_page, (arrow_login_page_rect))
        gwindow.blit(support_logo, (support_logo_rect))
        display_text("Enter user ID", GREY1, 213.04, 238.15, 28, "OCR A Extended")
        display_text("Enter password", GREY1, 213.04, 285.67, 28, "OCR A Extended")
        pygame.display.update()
    
login_page(gwindow)
pygame.quit()