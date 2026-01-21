from random import randint
import pygame as pg


class Dice:
    """
    Manages the logic related to dice throwing and sound playing.
    """
    def __init__(self):
        # Initialize pygame mixer only once
        pg.init()
        pg.mixer.init()
        # Load sound only once
        self._sound = pg.mixer.Sound('res/dados.wav')

    @staticmethod
    def __throw_dice():
        """
        Random integer between 1 and 6.
        """
        value = randint(1, 6)
        return value

    def get_throw_value(self):
        """
        Returns a random number for a dice face.
        """
        return self.__throw_dice()
    
    def play_sound(self):
        """
        Plays the dice sound.
        """
        pg.mixer.Sound.play(self._sound)
