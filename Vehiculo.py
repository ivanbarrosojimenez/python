from datetime import date

class Vehiculo:
    def __init__(self, matricula_vehiculo, vehiculo, tipo_vehiculo, itv):
        self.matricula_vehiculo = matricula_vehiculo
        self.vehiculo = vehiculo
        self.tipo_vehiculo = tipo_vehiculo
        self.itv = itv  # This should be a date object

    def mostrar_info_vehiculo(self):
        print(f'Matrícula del Vehículo: {self.matricula_vehiculo}')
        print(f'Vehículo: {self.vehiculo}')
        print(f'Tipo de Vehículo: {self.tipo_vehiculo}')
        print(f'ITV: {self.itv}')