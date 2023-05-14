from contenidocodigo.clases.RRSS import RedesSociales

class Instagram(RedesSociales):
    def __init__(self, nombre, url, usuarios, filtros):
        super().__init__(nombre, url, usuarios)
        self.filtros = filtros

    def descripcion(self):
        return f"{self.nombre} es una red social con {self.usuarios} usuarios, que se encuentra en {self.url}. Además, cuenta con los filtros {self.filtros}."