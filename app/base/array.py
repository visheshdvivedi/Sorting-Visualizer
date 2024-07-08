import pygame
import random
from app.base.constants import *

class BlockArray:
    def __init__(self):
        self.width = 5
        self.paused = True
        self.size = SORT_BOX_WIDTH // self.width
        print(f"Array Size: {self.size}")

        self.max_val = SORT_BOX_HEIGHT - self.width
        self.min_val = self.width

        self.blocks = []
        self.list = []
        self.colors = []

        for i in range(self.size):
            height = random.randint(self.min_val, self.max_val)
            x = SORT_BOX_LEFT + (i*self.width)
            y = SORT_BOX_TOP + SORT_BOX_HEIGHT - height

            rect = pygame.Rect(x, y, self.width, height)
            self.list.append(height)
            self.blocks.append(rect)
            self.colors.append(WHITE_COLOR)

    def reset(self):
        self.paused = True

        self.blocks = []
        self.list = []
        self.colors = []

        for i in range(self.size):
            height = random.randint(self.min_val, self.max_val)
            x = SORT_BOX_LEFT + (i*self.width)
            y = SORT_BOX_TOP + SORT_BOX_HEIGHT - height

            rect = pygame.Rect(x, y, self.width, height)
            self.list.append(height)
            self.blocks.append(rect)
            self.colors.append(WHITE_COLOR)

    def toggle_pause(self):
        self.paused = not self.paused

    def draw(self, surface: pygame.Surface):
        pygame.time.wait(50)
        for i in range(self.size):
            self.blocks[i].y = SORT_BOX_TOP + SORT_BOX_HEIGHT - self.list[i]
            self.blocks[i].height = self.list[i]

            pygame.draw.rect(surface, self.colors[i], self.blocks[i])
        pygame.display.flip()