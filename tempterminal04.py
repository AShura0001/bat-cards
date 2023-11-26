import pygame
import time
from sevendeadlysins import sevendeadlysins_index


white = [255, 255, 255]
black = [0, 0, 0]
red = [255, 0, 0]

pygame.init()
screen = pygame.display.set_mode([640, 480])
event_flag_2 = True

# for i in range (1, 53):
#     image = pygame.image.load(sevendeadlysins_index[i].card_image).convert_alpha()
#     screen.blit(image, [260, 50])

def display_text(text, x, y, size, color):
    font = pygame.font.Font('freesansbold.ttf', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

m = 1

while event_flag_2:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            event_flag_2 = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                event_flag_2 = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if back_rect.collidepoint(event.pos) and m>1:
                m -= 1
            elif next_rect.collidepoint(event.pos) and m<52:
                m += 1
    back_rect = pygame.draw.rect(screen, white, ((150, 400), (100, 50)))
    back_text = display_text('Back', 190, 420, 30, black)
    next_rect = pygame.draw.rect(screen, white, ((370, 400), (100, 50)))
    next_text = display_text('Next', 410, 420, 30, black)
    image = pygame.image.load(sevendeadlysins_index[m].card_image).convert_alpha()
    name = sevendeadlysins_index[m].name
    title = sevendeadlysins_index[m].title
    form = sevendeadlysins_index[m].form
    rank = sevendeadlysins_index[m].rank
    atk = sevendeadlysins_index[m].ATK
    hp = sevendeadlysins_index[m].HP
    dp = sevendeadlysins_index[m].DP
    sp = sevendeadlysins_index[m].SP
    iq = sevendeadlysins_index[m].IQ

    display_text((name+' - '+form), 310, 225, 30, white)
    display_text(("["+title+"]"), 310, 255, 20, white)
    display_text("rank: {}".format(rank), 208, 300, 15, white)
    display_text("ATK: {}".format(atk), 208, 335, 15, white)
    display_text("HP: {}".format(hp), 208, 370, 15, white)
    display_text("DP: {}".format(dp), 390, 300, 15, white)
    display_text("SP: {}".format(sp), 390, 335, 15, white)
    display_text("IQ: {}".format(iq), 390, 370, 15, white)
    image = pygame.transform.scale(image, (104, 150))
    screen.blit(image, [260, 50])

    pygame.display.flip()
    time.sleep(0.1)
