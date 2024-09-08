from publicacion import Publicacion

class Libro(Publicacion):
    def __init__(self, titulo, anio_publicacion, autor, numero_paginas):
        super().__init__(titulo, anio_publicacion)
        self.autor = autor
        self.numero_paginas = numero_paginas

    def mostrar_info(self):
        
        info_base = super().mostrar_info()
        
        return f"{info_base}\nautor: {self.autor}\nNumero de paginas: {self.numero_paginas}"
