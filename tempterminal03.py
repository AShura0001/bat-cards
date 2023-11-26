import pygame

pygame.init()
screen = pygame.display.set_mode([640, 480])

event_flag = True
event_flag_2 = False

while event_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            event_flag = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                event_flag = False
            if event.key == pygame.K_SPACE:
                event_flag_2 = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    while event_flag_2:
        screen_2 = pygame.display.set_mode([100, 200])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                event_flag_2 = False
                screen = pygame.display.set_mode([640, 480])
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    event_flag_2 = False
                    screen = pygame.display.set_mode([640, 480])
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)

            screen_2.fill([0, 0, 0])
            pygame.display.flip()
    screen.fill([255, 255, 255])
    pygame.display.flip()

pygame.quit()