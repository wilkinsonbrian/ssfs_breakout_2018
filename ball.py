import pygame

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight, radius):
        # initialize sprite super class

        # finish setting the class variables to the parameters
        self.color = color

        # Create a surface, get the rect coordinates, fill the surface with a white color (or whatever color the
        # background of your breakout game will be.
        self.image =
        self.rect =

        # Add a circle to represent the ball to the surface just created.

    def move(self):
        pass
