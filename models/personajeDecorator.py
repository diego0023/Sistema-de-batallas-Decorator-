from models.personaje import Personaje


class PersonajeDecorator(Personaje):
    def __init__(self, personaje: Personaje) -> None:
        self.__personaje_decorator: Personaje = personaje

    def get_hp(self) -> float:
        return self.__personaje_decorator.get_hp()

    def get_speed(self) -> float:
        return self.__personaje_decorator.get_speed()

    def get_def(self) -> float:
        return self.__personaje_decorator.get_def()

    def get_atq(self) -> float:
        return self.__personaje_decorator.get_atq()

    def get_personaje(self) -> Personaje:
        return self.__personaje_decorator

    def defender(self):
        return "se defesndio"

    def set_hp(self, hp: float):
        self.__personaje_decorator.set_hp(hp)
        return f''

    def atacar(self,  enemy_def: float) -> float:
        danio = self.__personaje_decorator.get_atq() - enemy_def
        if danio < 0:
            danio = 0
        else:
            danio = self.__personaje_decorator.get_atq()
        return danio

    def reduce_hp(self, damage: float):
        vida = self.__personaje_decorator.get_hp() - damage
        if vida < 0:
            self.__personaje_decorator.set_hp(0)
        else:
            self.__personaje_decorator.set_hp(vida)
