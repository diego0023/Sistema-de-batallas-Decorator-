import abc


class Personaje(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_hp(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def get_atq(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def get_def(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def get_speed(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def reduce_hp(self, damage: float):
        raise NotImplementedError

    @abc.abstractmethod
    def is_active(self) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def off_active(self):
        raise NotImplementedError

    @abc.abstractmethod
    def atacar(self, enemy_activo: bool, enemy_def: float) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def defender(self):
        raise NotImplementedError
