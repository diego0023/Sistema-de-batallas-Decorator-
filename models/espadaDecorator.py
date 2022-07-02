from models.personajeDecorator import PersonajeDecorator
from models.personaje import Personaje


class EspadaDecorator(PersonajeDecorator):
    def __init__(self, p: Personaje) -> None:
        super().__init__(p)

    def atacar(self,  enemy_def: float) -> float:
        return super().atacar(enemy_def)*2
