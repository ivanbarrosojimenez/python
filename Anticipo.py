class Anticipo:
    def __init__(self, alumno, fecha, concepto, cantidad):
        self.alumno = alumno
        self.fecha = fecha
        self.concepto = concepto
        self.cantidad = cantidad

    def mostrar_info_anticipo(self):
        return (f"\n----------------------------------------------\n"
                f"  |  Alumno (DNI): {self.alumno}\n"
                f"  |  Fecha: {self.fecha}\n"
                f"  |  Concepto: {self.concepto}\n"
                f"  |  Cantidad: {self.cantidad}\n"
                f"----------------------------------------------\n")
    def mostrar_info_editar_anticipo(self):
        return (f"\n----------------------------------------------\n"
                f"  |  1.  Alumno (DNI): {self.alumno}\n"
                f"  |  2.  Fecha: {self.fecha}\n"
                f"  |  3.  Concepto: {self.concepto}\n"
                f"  |  4.  Cantidad: {self.cantidad}")

    def mostrar_info_anticipo_avanzado(self, alumno):
        return (f"\n----------------------------------------------\n"
                f"|  Alumno: {alumno.nombre} {alumno.primer_apellido} {alumno.segundo_apellido}\n"
                f"|  Permiso: {alumno.permiso_opta}\n"
                f"|  Fecha: {self.fecha}\n"
                f"|  Concepto: {self.concepto}\n"
                f"|  Cantidad: {self.cantidad}\n"
                f"----------------------------------------------\n")
    def to_json(self):
        return {
            'alumno': self.alumno,
            'fecha': self.fecha,
            'concepto': self.concepto,
            'cantidad': self.cantidad
        }