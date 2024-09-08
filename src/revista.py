from publicacion import Publicacion
class Revista(Publicacion):
    def __init__(self, titulo, anio_publicacion, numero_revista, nombre_revista):
        super().__init__(titulo, anio_publicacion)
        self.numero_revista = numero_revista
        self.nombre_revista = nombre_revista

    def mostrar_info(self):
        
        info_base = super().mostrar_info()
        
        return f"{info_base}\nNombre Revista: {self.nombre_revista}\nNumero Revista: {self.numero_revista}"
