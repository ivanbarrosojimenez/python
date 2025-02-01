from Persona import Persona
from Permiso import Permiso

class Profesor(Persona):
    def __init__(self, nombre='', primer_apellido='', segundo_apellido='', dni='', fecha_nacimiento='',
                 vehiculo='', tipo_vehiculo='', itv='', gastos_combustible=None):
        super().__init__(nombre, primer_apellido, segundo_apellido, dni, fecha_nacimiento)
        self.vehiculo = vehiculo
        self.tipo_vehiculo = tipo_vehiculo
        self.itv = itv
        self.gastos_combustible = gastos_combustible if gastos_combustible is not None else {}

    def registrar_gasto_combustible(self, fecha, coste):
        self.gastos_combustible[fecha] = coste

    def mostrar_gastos_combustible(self):
        gastos_combustible_str = "\n".join([f"| {fecha}: {coste}€" for fecha, coste in self.gastos_combustible.items()])
        return gastos_combustible_str

    def to_json(self):
        return {
            'dni': self.dni,
            'nombre': self.nombre,
            'primer_apellido': self.primer_apellido,
            'segundo_apellido': self.segundo_apellido,
            'vehiculo': self.vehiculo,
            'tipo_vehiculo': self.tipo_vehiculo,
            'itv': self.itv,
            'gastos_combustible': self.gastos_combustible
        }

    def mostrar_info_editar_profesor(self):
        gastos_combustible_str = "  ".join([f"\n  |    - {fecha}: {coste}€" for fecha, coste in self.gastos_combustible.items()])
        return (f"  ----------------------------------------------\n"
                f"  |  1 DNI: {self.dni}\n"
                f"  |  2 Nombre: {self.nombre}\n"
                f"  |  3 Primer Apellido: {self.primer_apellido}\n"
                f"  |  4 Segundo Apellido: {self.segundo_apellido}\n"
                f"  |  5 Vehículo: {self.vehiculo}\n"
                f"  |  6 Tipo de vehículo: {self.tipo_vehiculo}\n"
                f"  |  7 ITV: {self.itv}\n"
                f"  |  8 Editar gastos de combustible:{gastos_combustible_str}\n"
                f"  |  9 Añadir gastos de combustible.\n"
                f"  |  0 Salir. \n"
                f"  |----------------------------------------------\n"
                )

    def mostrar_info_profesor(self):
        gastos_combustible_str = "\n".join([f"| {fecha}: {coste}€" for fecha, coste in self.gastos_combustible.items()])
        return (f"----------------------------------------------\n"
                f"| DNI: {self.dni}\n"
                f"| Nombre: {self.nombre}\n"
                f"| Primer Apellido: {self.primer_apellido}\n"
                f"| Segundo Apellido: {self.segundo_apellido}\n"
                f"| Vehículo: {self.vehiculo}\n"
                f"| Tipo de vehículo: {self.tipo_vehiculo}\n"
                f"| ITV: {self.itv}\n"
                f"| Gastos de combustible:\n{gastos_combustible_str}\n"
                f"----------------------------------------------\n")