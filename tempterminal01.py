import pygame


pygame.init()

window_size = (960, 560)
gwindow = pygame.display.set_mode(window_size)


#colors
black = (0, 0, 0)
white = (255, 255, 255)
GREY1 = (240, 240, 240)


def display_text(text, color, x, y, font_size, Font):
    font = pygame.font.SysFont(Font, font_size)
    screen_text = font.render(text, True, color)
    gwindow.blit(screen_text, [x,y])

def login_page(gwindow):
    event_flag = True
    while event_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                event_flag = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    event_flag = False
        display_text("BAT CARDS LOGIN", white, 388.3289, 213.8026, 33, "OCR A Extended")
        gwindow.fill(black)
        pygame.display.update()
    
login_page(gwindow)
pygame.quit()