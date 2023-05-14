from contenidocodigo.clases.RRSS import RedesSociales

class Twitter(RedesSociales):
    def __init__(self, nombre, url, usuarios, hashtags):
        super().__init__(nombre, url, usuarios)
        self.hashtags = hashtags

    def descripcion(self):
        return f"{self.nombre} es una red social con {self.usuarios} usuarios, que se encuentra en {self.url}. Además, cuenta con los hashtags {self.hashtags}."
