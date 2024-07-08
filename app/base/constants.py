import pygame

SORTING_ALGORITHMS = [
    'selection',
    'bubble',
    'insertion',
    'merge'
]

# constants
WHITE_COLOR = 255, 255, 255
BLACK_COLOR = 0, 0, 0
BLUE_COLOR = 0, 125, 255
GREEN_COLOR = 0, 255, 0
RED_COLOR = 255, 0, 0

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SORT_BOX_LEFT = SCREEN_WIDTH // 20
SORT_BOX_TOP = (SCREEN_HEIGHT // 20) + 50
SORT_BOX_WIDTH = 725
SORT_BOX_HEIGHT = 500

TITLE_FONT = pygame.font.Font('open-sans/OpenSans-Bold.ttf', 32)
CONTENT_FONT = pygame.font.Font('open-sans/OpenSans-Regular.ttf', 19)
SUBTEXT_FONT = pygame.font.Font('open-sans/OpenSans-Regular.ttf', 14)
