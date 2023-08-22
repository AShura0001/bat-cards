import pygame


pygame.init()

window_size = (960, 560)
gwindow = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

#colors
black = (0, 0, 0)
white = (255, 255, 255)
GREY1 = (240, 240, 240)

fps = 60

def display_text(text, color, x, y, font_size):
    global font
    font = pygame.font.SysFont(None, font_size)
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
        display_text("BAT CARDS LOGIN", white, 388, 213, 33)
        pygame.display.update()
        # clock.tick(fps)
    
login_page(gwindow)
pygame.quit()