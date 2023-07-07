"""
Clase abstracta que define los métodos básicos que debe implementar un vehículo
"""
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass
class Vehiculo(metaclass=ABCMeta):
    _tipo: str
    _modelo: str
    _año: int
    _marca: str
    _color: str
    _cilindros: int
    _kilometros: int = 0

    @abstractmethod
    def recorrer(self, kilometros):
        pass

    @abstractmethod
    def tipo(self):
        pass

    @abstractmethod
    def modelo(self):
        pass

    @abstractmethod
    def año(self):
        pass

    @abstractmethod
    def marca(self):
        pass

    @abstractmethod
    def color(self):
        pass

    @abstractmethod
    def cilindros(self):
        pass

    @abstractmethod
    def kilometros(self):
        pass


class Motocicleta(Vehiculo):
    def __init__(self, modelo, año, marca, color, cilindros):
        super().__init__("Motocicleta", modelo, año, marca, color, cilindros)

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @tipo.deleter
    def tipo(self):
        del self._tipo

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @modelo.deleter
    def modelo(self):
        del self._modelo

    @property
    def año(self):
        return self._año

    @año.setter
    def año(self, año):
        self._año = año

    @año.deleter
    def año(self):
        del self._año

    @property
    def cilindros(self):
        return self._cilindros

    @cilindros.setter
    def cilindros(self, cilindros):
        self._cilindros = cilindros

    @cilindros.deleter
    def cilindros(self):
        del self._cilindros

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @color.deleter
    def color(self):
        del self._color

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @marca.deleter
    def marca(self):
        del self._marca

    @property
    def kilometros(self):
        return self._kilometros

    def __agregar_kilometraje(self, kilometros):
        self._kilometros += kilometros

    def recorrer(self, kilometros):
        self.__agregar_kilometraje(kilometros)

    def __str__(self):
        return (f"Tipo: {self.tipo}\nMarca: {self.marca}\nModelo: \
{self.modelo}\nAño: {self.año}\nColor: {self.color}\nCilindros: \
{self.cilindros}\nKilometraje: {self.kilometros}")


if __name__ == '__main__':
    moto = Motocicleta('R3', 2018, 'Yamaha', 'Negro con blanco', 2)
    print(moto)
    print("***********************************")
    moto.recorrer(10)
    print(moto)
