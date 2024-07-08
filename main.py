import random
from argparse import ArgumentParser

import pygame
import pygame_menu as pm

pygame.init()

from app.base.constants import *
from app.algorithms.bubble import BubbleSortArray
from app.algorithms.selection import SeletionSortArray
from app.algorithms.insertion import InsertionSortArray
from app.algorithms.merge import MergeSortArray

parser = ArgumentParser(
    prog = "python3 main.py",
    description = "GUI sorting visualizer using Pygame",
    epilog = "created by @visheshdvivedi"
)

parser.add_argument('--print-algo', action='store_true', help="Display all supported algorithms")
parser.add_argument("--algo", nargs="?", default=SORTING_ALGORITHMS[0], const=SORTING_ALGORITHMS[0], help="Sorting algorithm to use (default 'selection')")
parser.add_argument("--speed", nargs="?", const=0.5, help="Sorter speed (default 0.5)")
args = parser.parse_args()

if (args.print_algo):
    print("Supported algorithms: ")
    for algo in SORTING_ALGORITHMS:
        print(f"- {algo}")
    exit(0)


def main():

    display = pygame.display.set_mode(( SCREEN_WIDTH, SCREEN_HEIGHT ))
    pygame.display.set_caption("Sorting Visualizer")

    title_text = TITLE_FONT.render("Sorting Visualizer", True, WHITE_COLOR, BLACK_COLOR)
    title_text_rect = title_text.get_rect()
    title_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 20)

    content_text = CONTENT_FONT.render(args.algo.capitalize() + " Sort", True, WHITE_COLOR, BLACK_COLOR)
    content_text_rect = content_text.get_rect()
    content_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 9)

    help_text = SUBTEXT_FONT.render("Click 'Space' to pause/unpause", True, WHITE_COLOR, BLACK_COLOR)
    help_text_rect = help_text.get_rect()
    help_text_rect.center = (SCREEN_WIDTH // 6, SCREEN_WIDTH // 20)

    help_text_2 = SUBTEXT_FONT.render("Click 'R' to reset", True, WHITE_COLOR, BLACK_COLOR)
    help_text_rect_2 = help_text_2.get_rect()
    help_text_rect_2.center = (SCREEN_WIDTH * 5 // 6, SCREEN_WIDTH // 20)

    if args.algo == SORTING_ALGORITHMS[0]:
        array = SeletionSortArray()
    elif args.algo == SORTING_ALGORITHMS[1]:
        array = BubbleSortArray()
    elif args.algo == SORTING_ALGORITHMS[2]:
        array = InsertionSortArray()
    elif args.algo == SORTING_ALGORITHMS[3]:
        array = MergeSortArray()

    while True:

        # get events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    array.toggle_pause()
                elif event.key == pygame.K_r:
                    array.reset()

        # display
        display.fill(BLACK_COLOR)
        display.blit(title_text, title_text_rect)
        display.blit(content_text, content_text_rect)
        display.blit(help_text, help_text_rect)
        display.blit(help_text_2, help_text_rect_2)
        array.draw(display)

        # update game window
        pygame.display.update()

if __name__ == "__main__":
    main()