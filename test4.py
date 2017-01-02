#!/usr/bin/env python3

from yaz.task import task
from yaz.main import main
from yaz.plugin import Plugin

class Dummy(Plugin):
    """Plugin without tasks"""
    def __init__(self):
        print("SHOULD BE CALLED ONCE")

class Food(Plugin):
    def __init__(self, dummy: Dummy):
        self.dummy = dummy

if __name__ == "__main__":
    def food():
        food = Food()
        print(food, food.dummy)

    food()
    food()
    food()
