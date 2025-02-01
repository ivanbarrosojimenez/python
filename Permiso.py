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


    def mostrar_info_editar_permiso(self):
        return (f"\n  ----------------------------------------------\n"
                f"  |  1. Tipo Permiso: {self.tipo_permiso}\n"
                f"  |  2. Precio Matrícula: {self.precio_matricula}\n"
                f"  |  3. Clases Incluidas: {self.clases_incluidas}\n"
                f"  |  4. Precio por Clase: {self.precio_por_clase}\n"
                f"  |  5. Precio Examen: {self.precio_examen}\n"
                f"  |  6. Precio Renovación: {self.precio_renovacion}")

    def mostrar_info_permiso(self):
        return (f"\n  ----------------------------------------------\n"
                f"  |  Tipo Permiso: {self.tipo_permiso}\n"
                f"  |  Precio Matrícula: {self.precio_matricula}\n"
                f"  |  Clases Incluidas: {self.clases_incluidas}\n"
                f"  |  Precio por Clase: {self.precio_por_clase}\n"
                f"  |  Precio Examen: {self.precio_examen}\n"
                f"  |  Precio Renovación: {self.precio_renovacion}\n"
                f"  ----------------------------------------------\n")