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