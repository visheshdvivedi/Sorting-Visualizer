import pygame
from app.base.array import BlockArray
from app.base.constants import *

class InsertionSortArray(BlockArray):
    def __init__(self):
        super().__init__()

        self.outer_counter = 1
        self.inner_counter = 0
        self.key = self.list[self.outer_counter]

        self.color_switch = False
        self.swapped = False

    def reset(self):
        super().reset()

        self.outer_counter = 1
        self.inner_counter = 0
        self.key = self.list[self.outer_counter]

        self.color_switch = False
        self.swapped = False

    def next_sort_iteration(self):
        if self.outer_counter == self.size:
            return
        
        if self.inner_counter >= 0 and self.key < self.list[self.inner_counter]:
            if not self.color_switch:
                self.colors[self.inner_counter + 1] = WHITE_COLOR
                self.colors[self.inner_counter] = WHITE_COLOR
                self.color_switch = True
            else:
                self.list[self.inner_counter + 1] = self.list[self.inner_counter]
                self.inner_counter -= 1
                self.colors[self.inner_counter + 1] = WHITE_COLOR
                self.colors[self.inner_counter] = WHITE_COLOR
                self.color_switch = False
                return
        else:

            if not self.color_switch:
                self.colors[self.inner_counter + 1] = RED_COLOR
                self.color_switch = True
            else:
                
                self.colors[self.inner_counter + 1] = WHITE_COLOR
                self.color_switch = False

                self.list[self.inner_counter + 1] = self.key
                self.outer_counter += 1

                if self.outer_counter == self.size:
                    return

                self.key = self.list[self.outer_counter]
                self.inner_counter = self.outer_counter - 1

    def draw(self, surface: pygame.Surface):
        if not self.paused:
            self.next_sort_iteration()
        super().draw(surface)