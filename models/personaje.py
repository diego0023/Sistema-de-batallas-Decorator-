from abc import ABC, abstractmethod


class Personaje(ABC):
    @abstractmethod
    def get_hp(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def get_atq(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def get_def(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def get_speed(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def reduce_hp(self, damage: float):
        raise NotImplementedError

    @abstractmethod
    def atacar(self, enemy_def: float) -> float:
        raise NotImplementedError

    @abstractmethod
    def set_hp(self, htp: float):
        raise NotImplementedError
