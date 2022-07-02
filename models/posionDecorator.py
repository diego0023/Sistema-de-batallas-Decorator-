from models.personajeDecorator import PersonajeDecorator
from models.personaje import Personaje


class PosionDecorator(PersonajeDecorator):
    def __init__(self, p: Personaje) -> None:
        super().__init__(p)

    def defender(self) -> float:
        super().get_personaje().set_hp(10)
        return "Posion aumento hp"
