import pygame
import os
import tempterminal05

pygame.init()

big_window_size = (960, 560)
small_window_size = (360, 500)
main_file_directory = os.getcwd()
clock = pygame.time.Clock()

#variables
fps = 60

tempterminal05.login_page(big_window_size, small_window_size, main_file_directory)

pygame.quit()