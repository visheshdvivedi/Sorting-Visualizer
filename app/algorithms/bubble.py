import pygame
from app.base.array import BlockArray
from app.base.constants import *

class BubbleSortArray(BlockArray):
    def __init__(self):
        super().__init__()

        self.outer_counter = 0
        self.inner_counter = 0

        self.color_switch = False
        self.swapped = False

    def reset(self):
        super().reset()
        self.outer_counter = 0
        self.inner_counter = 0

        self.color_switch = False
        self.swapped = False

    def next_sort_iteration(self):
        if self.outer_counter == self.size:
            return
        
        if self.inner_counter == self.size - self.outer_counter - 1:
            self.outer_counter += 1
            self.inner_counter = 0
            return
        

        if self.list[self.inner_counter] > self.list[self.inner_counter + 1]:
            if not self.color_switch:
                self.color_switch = True
                self.colors[self.outer_counter] = BLUE_COLOR
                self.colors[self.inner_counter] = RED_COLOR
                self.colors[self.inner_counter + 1] = GREEN_COLOR
                return
            else:
                self.list[self.inner_counter], self.list[self.inner_counter + 1] = self.list[self.inner_counter + 1], self.list[self.inner_counter]
                self.color_switch = False
                self.colors[self.outer_counter] = WHITE_COLOR
                self.colors[self.inner_counter] = WHITE_COLOR
                self.colors[self.inner_counter + 1] = WHITE_COLOR

        self.inner_counter += 1

    def draw(self, surface: pygame.Surface):
        if not self.paused:
            self.next_sort_iteration()
        super().draw(surface)