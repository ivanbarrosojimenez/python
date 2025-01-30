class Anticipo:
    def __init__(self, alumno, fecha, concepto, cantidad):
        self.alumno = alumno
        self.fecha = fecha
        self.concepto = concepto
        self.cantidad = cantidad

    def mostrar_info_anticipo(self):
        print(f'Alumno (DNI): {self.alumno}')
        print(f'Fecha: {self.fecha}')
        print(f'Concepto: {self.concepto}')
        print(f'Cantidad: {self.cantidad}')