from libro import Libro
from publicacion import Publicacion
from revista import Revista

if __name__ == '__main__':
    # TODO: Aquí va el código que inicializa tu aplicación.
    libro1 = Libro("Changua", 2022, "Punisher", 250)
    print(libro1.mostrar_info())

    revista1 = Revista("Mondongo", 2024, 10, "Punisher Magazine")
    print(revista1.mostrar_info())

    revs = Revista("Mondongo", 2024, 10, "Punisher Magazine")
    print(revs.mostrar_info())