class Publicacion:
    def __init__(self, titulo, anio_publicacion):
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion

    def mostrar_info(self):
        return f"Titulo: {self.titulo}\nAño publicacion: {self.anio_publicacion}"
