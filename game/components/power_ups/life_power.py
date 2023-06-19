from game.components.power_ups.power_up import PowerUp
from game.utils.constants import LIFE, LIFE_TYPE, SPACESHIP


class LifePower(PowerUp):
    def __init__(self):
        super().__init__(LIFE, LIFE_TYPE)