
import pygame
import os
from defines import *

class Image:
    def __init__(self, image_name):
        pic = pygame.image.load(image_name)
        self.surface = pic.convert()
        self.surface.set_colorkey(pic.get_palette_at(ALPHA_NUM))

        self.imagename = image_name.split(os.sep)[-1].split(".")[0]

