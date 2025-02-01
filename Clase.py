class Clase:
    def __init__(self, alumno, profesor, matricula_vehiculo, fecha_hora):
        self.alumno = alumno
        self.profesor = profesor
        self.matricula_vehiculo = matricula_vehiculo
        self.fecha_hora = fecha_hora

    def mostrar_info_clase(self):
        return (f"  ----------------------------------------------\n"
                f"  | Alumno (DNI): {self.alumno}\n"
                f"  | Profesor (DNI): {self.profesor}\n"
                f"  | Matrícula del vehículo: {self.matricula_vehiculo}\n"
                f"  | Fecha y hora: {self.fecha_hora}\n"
                f"  ----------------------------------------------\n")

    def to_json(self):
        return {
            'alumno': self.alumno,
            'profesor': self.profesor,
            'matricula_vehiculo': self.matricula_vehiculo,
            'fecha_hora': self.fecha_hora
        }
    def mostrar_info_editar_clase(self):
        return (f"  ----------------------------------------------\n"
                f"  1. Alumno (DNI): {self.alumno}\n"
                f"  2. Profesor (DNI): {self.profesor}\n"
                f"  3. Fecha y hora: {self.fecha_hora}\n"
                f"     Matrícula del vehículo (de Profesor): {self.matricula_vehiculo}")