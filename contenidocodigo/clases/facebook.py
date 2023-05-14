from contenidocodigo.clases.RRSS import RedesSociales

class Facebook(RedesSociales):
    def __init__(self, nombre, url, usuarios, grupos):
        super().__init__(nombre, url, usuarios)
        self.grupos = grupos

    def descripcion(self):
        return f"{self.nombre} es una red social con {self.usuarios} usuarios, que se encuentra en {self.url}. Además, cuenta con {self.grupos} grupos."
