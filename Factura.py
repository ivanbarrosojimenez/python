class Factura:
    def __init__(self, alumno, precio_matricula, num_clases_incluidas, num_clases_dadas,
                 precio_clase, num_examenes, precio_examen, num_renovaciones, precio_renovacion,
                 anticipos, permiso):
        self.alumno = alumno
        self.precio_matricula = precio_matricula
        self.num_clases_incluidas = num_clases_incluidas
        self.num_clases_dadas = num_clases_dadas
        self.precio_clase = precio_clase
        self.num_examenes = num_examenes
        self.precio_examen = precio_examen
        self.num_renovaciones = num_renovaciones
        self.precio_renovacion = precio_renovacion
        self.anticipos = anticipos
        self.permiso = permiso

    def calcular_total(self):
        total_precio_clases = max(0, self.num_clases_dadas - self.num_clases_incluidas) * self.precio_clase
        total_precio_examenes = self.num_examenes * self.precio_examen
        total_precio_renovaciones = self.num_renovaciones * self.precio_renovacion
        total = self.precio_matricula + total_precio_clases + total_precio_examenes + total_precio_renovaciones
        return total

    def calcular_iva(self):
        total = self.calcular_total()
        iva = total * 0.21
        return iva

    def calcular_total_con_iva(self):
        total = self.calcular_total()
        iva = self.calcular_iva()
        total_con_iva = total + iva
        return total_con_iva

    def calcular_saldo_pendiente(self):
        total_con_iva = self.calcular_total_con_iva()
        saldo_pendiente = total_con_iva - self.anticipos
        return saldo_pendiente

    def generar_factura(self):
        total = self.calcular_total()
        iva = self.calcular_iva()
        total_con_iva = self.calcular_total_con_iva()
        saldo_pendiente = self.calcular_saldo_pendiente()

        return (f"\n----------------------------------------------\n"
                f"|  Factura para el alumno (DNI): {self.alumno}\n"
                f"|  Precio Matrícula: {self.precio_matricula}\n"
                f"|  Número de Clases Incluidas: {self.num_clases_incluidas}\n"
                f"|  Número de Clases Dadas: {self.num_clases_dadas}\n"
                f"|  Precio por Clase: {self.precio_clase}\n"
                f"|  Número de Exámenes: {self.num_examenes}\n"
                f"|  Precio por Examen: {self.precio_examen}\n"
                f"|  Número de Renovaciones: {self.num_renovaciones}\n"
                f"|  Precio por Renovación: {self.precio_renovacion}\n"
                f"|  Anticipos: {self.anticipos}\n"
                f"|  Total: {total}\n"
                f"|  IVA (21%): {iva}\n"
                f"|  Total con IVA: {total_con_iva}\n"
                f"|  Saldo Pendiente: {saldo_pendiente}\n"
                f"----------------------------------------------\n")

    def to_json(self):
        return {
            'alumno': self.alumno,
            'precio_matricula': self.precio_matricula,
            'num_clases_incluidas': self.num_clases_incluidas,
            'num_clases_dadas': self.num_clases_dadas,
            'precio_clase': self.precio_clase,
            'num_examenes': self.num_examenes,
            'precio_examen': self.precio_examen,
            'num_renovaciones': self.num_renovaciones,
            'precio_renovacion': self.precio_renovacion,
            'anticipos': self.anticipos,
            'permiso': self.permiso
        }