import pygame
from app.base.array import BlockArray
from app.base.constants import *

class SeletionSortArray(BlockArray):
    def __init__(self):
        super().__init__()

        self.sort_counter = 0
        self.color_switch = False

    def reset(self):
        super().reset()
        self.sort_counter = 0
        self.color_switch = False

    def next_sort_iteration(self):
        if (self.sort_counter == self.size - 1):
            return

        min_index = self.sort_counter
        for i in range(self.sort_counter+1, len(self.list)):
            if self.list[i] < self.list[min_index]:
                min_index = i

        if not self.color_switch:
            self.list[min_index], self.list[self.sort_counter] = self.list[self.sort_counter], self.list[min_index]
            self.colors[min_index] = WHITE_COLOR
            self.colors[self.sort_counter] = WHITE_COLOR
        
            self.colors[self.sort_counter] = WHITE_COLOR
            self.sort_counter += 1
            self.colors[self.sort_counter] = BLUE_COLOR
        else:
            self.colors[min_index] = GREEN_COLOR
            self.colors[self.sort_counter] = RED_COLOR

        self.color_switch = not self.color_switch

    def draw(self, surface: pygame.Surface):
        if not self.paused:
            self.next_sort_iteration()
        super().draw(surface)