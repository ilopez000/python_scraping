import os


class Pagina:
    def __init__(self, titulo, descripcion, subtitulos, contenido):
        self.titulo = titulo
        self.descripcion = descripcion
        self.subtitulos = subtitulos
        self.contenido = contenido

    def mostrar_pagina(self):
        print(f"Titulo: {self.titulo}")
        print(f"Descripcion: {self.descripcion}")
        print("Subtitulos:")
        for i, subtitulo in enumerate(self.subtitulos):
            print(f"{i + 1}. {subtitulo}")
        print("Contenido:")
        print(self.contenido)


    def imprimir_pagina_a_fichero(self, nombre_fichero, ruta):
        ruta_completa = os.path.join(ruta, nombre_fichero)
        with open(ruta_completa, "w", encoding="utf-8") as archivo:
            archivo.write(f"Titulo: {self.titulo}\n")
            archivo.write(f"Descripcion: {self.descripcion}\n")
            archivo.write("Subtitulos:\n")
            for i, subtitulo in enumerate(self.subtitulos):
                archivo.write(f"{i + 1}. {subtitulo}\n")
            archivo.write("Contenido:\n")
            archivo.write(self.contenido)