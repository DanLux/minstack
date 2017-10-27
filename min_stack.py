#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []


    def min(self):
        return self.min_stack[-1] if self.min_stack else None


    def push(self, value):
        older_min = self.min()
        current_min = min(older_min, value) if older_min else value

        self.stack.append(value)
        self.min_stack.append(current_min)


    def pop(self):
        if self.stack:
            self.min_stack.pop()
            return self.stack.pop()
        else: return None
