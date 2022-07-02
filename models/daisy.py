from models.personaje import Personaje


class Daisy(Personaje):

    def __init__(self):
        self.__hp: float = 100
        self.__atq: float = 60
        self.__def: float = 40
        self.__speed: float = 50

    def get_hp(self) -> float:
        return self.__hp

    def get_atq(self) -> float:
        return self.__atq

    def get_def(self) -> float:
        return self.__def

    def get_speed(self) -> float:
        return self.__speed

    def reduce_hp(self, damage: float):
        vida = self.__hp - damage
        if vida < 0:
            self.__hp = 0
        else:
            self.__hp = vida

    def atacar(self,  enemy_def: float) -> float:
        danio = self.__atq - enemy_def
        if danio < 0:
            danio = 0
        else:
            danio = self.__atq
        return danio

    def set_hp(self, hp: float):
        self.__hp = self.__hp + hp
        return f'Daisy tiene {self.__hp} de vida'
