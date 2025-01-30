class Clase:
    def __init__(self, alumno, profesor, matricula_vehiculo, fecha_hora):
        self.alumno = alumno
        self.profesor = profesor
        self.matricula_vehiculo = matricula_vehiculo
        self.fecha_hora = fecha_hora

    def mostrar_info_clase(self):
        print(f'Alumno (DNI): {self.alumno}')
        print(f'Profesor (DNI): {self.profesor}')
        print(f'Matrícula del Vehículo: {self.matricula_vehiculo}')
        print(f'Fecha y Hora: {self.fecha_hora}')