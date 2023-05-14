from abc import ABC, abstractmethod

class RedesSociales(ABC):
    def __init__(self, nombre, url, usuarios):
        self.nombre = nombre
        self.url = url
        self.usuarios = usuarios

    @abstractmethod
    def descripcion(self):
        pass
