class Permiso:
    def __init__(self, tipo_permiso, precio_matricula, clases_incluidas, precio_por_clase, precio_examen, precio_renovacion):
        self.tipo_permiso = tipo_permiso
        self.precio_matricula = precio_matricula
        self.clases_incluidas = clases_incluidas
        self.precio_por_clase = precio_por_clase
        self.precio_examen = precio_examen
        self.precio_renovacion = precio_renovacion

    def to_json(self):
        return {
            'tipo_permiso': self.tipo_permiso,
            'precio_matricula': self.precio_matricula,
            'clases_incluidas': self.clases_incluidas,
            'precio_por_clase': self.precio_por_clase,
            'precio_examen': self.precio_examen,
            'precio_renovacion': self.precio_renovacion
        }


    def mostrar_datos(self):
        return (f"Tipo Permiso: {self.tipo_permiso}, Precio Matrícula: {self.precio_matricula}, "
                f"Clases Incluidas: {self.clases_incluidas}, Precio por Clase: {self.precio_por_clase}, "
                f"Precio Examen: {self.precio_examen}, Precio Renovación: {self.precio_renovacion}")