import pygame as pg


class Main:
    def __init__(self, width, height):
        pg.init()
        self.width = width
        self.height = height
        pg.display.set_mode(self.width, self.height)
