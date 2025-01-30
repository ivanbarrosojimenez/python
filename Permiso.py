class Permiso:
    def __init__(self, tipo_permiso, precio_matricula, clases_incluidas, precio_por_clase, precio_examen, precio_renovacion):
        self.tipo_permiso = tipo_permiso
        self.precio_matricula = precio_matricula
        self.clases_incluidas = clases_incluidas
        self.precio_por_clase = precio_por_clase
        self.precio_examen = precio_examen
        self.precio_renovacion = precio_renovacion

    def mostrar_info_permiso(self):
        print(f'Tipo de Permiso: {self.tipo_permiso}')
        print(f'Precio de Matrícula: {self.precio_matricula}')
        print(f'Clases Incluidas: {self.clases_incluidas}')
        print(f'Precio por Clase: {self.precio_por_clase}')
        print(f'Precio del Examen: {self.precio_examen}')
        print(f'Precio de Renovación: {self.precio_renovacion}')