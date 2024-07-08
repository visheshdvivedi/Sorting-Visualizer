import pygame
from app.base.array import BlockArray
from app.base.constants import *

class MergeSortArray(BlockArray):
    def __init__(self):
        super().__init__()

        self.start = 0
        self.end = self.size - 1

        self.color_switch = False

    def reset(self):
        super().reset()
        self.color_switch = False

    def merge(self, start, mid, end):
        left = self.list[start:mid + 1]
        right = self.list[mid + 1: end + 1]
        left_index = right_index = 0

        for arr_index in range(start, end + 1):
            if left_index < len(left) and (right_index >= len(right) or left[left_index] <= right[right_index]):
                self.list[arr_index] = left[left_index]
                left_index += 1
            else:
                self.list[arr_index] = right[right_index]
                right_index += 1

    def next_sort_iteration(self, start, end):
        if start >= end:
            return
        
        mid = (start + end) // 2
        self.next_sort_iteration(start, mid)
        self.next_sort_iteration(mid + 1, end)
        self.merge(start, mid, end)

    def draw(self, surface: pygame.Surface):
        if not self.paused:
            self.next_sort_iteration(0, self.size - 1)
        super().draw(surface)
