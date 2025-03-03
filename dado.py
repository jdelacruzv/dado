"""
    Author: José De La Cruz
    Created: 2020-04-15
    Modified: 2021-08-26 - Cambio de librería de playsound a pygame
"""
from random import randint
import pygame as pg


class Dado:
    """Class that works as the application model"""
    @staticmethod
    def __throw_dado():
        """Random integer between 1 and 6"""
        value = randint(1, 6)
        return value


    def print_value(self):
        """Returns the random number stored in value"""
        return self.__throw_dado()


    @property
    def play_sound(self):
        """Returns sound in wav format"""
        pg.init()
        pg.mixer.init()

        sonido = pg.mixer.Sound('res/dados.wav')   
        pg.mixer.Sound.play(sonido)
