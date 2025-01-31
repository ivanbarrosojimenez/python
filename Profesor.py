from Persona import Persona
from Permiso import Permiso

class Profesor(Persona):
    def __init__(self, dni, nombre, primer_apellido='', segundo_apellido='', fecha_nacimiento='', vehiculo=None, tipo_vehiculo=None, itv=None, gastos_combustible=None, permisos=None):
        super().__init__(dni, nombre, primer_apellido, segundo_apellido, fecha_nacimiento)
        self.permisos = [permiso if isinstance(permiso, Permiso) else Permiso(**permiso) for permiso in (permisos or [])]
        self.vehiculo = vehiculo
        self.tipo_vehiculo = tipo_vehiculo
        self.itv = itv
        self.gastos_combustible = gastos_combustible

    def agregar_permiso(self, permiso):
        #if not isinstance(permiso, Permiso):
        #    permiso = Permiso(**permiso)
        self.permisos.append(permiso)


    def to_json(self):
        return {
            'dni': self.dni,
            'nombre': self.nombre,
            'primer_apellido': self.primer_apellido,
            'segundo_apellido': self.segundo_apellido,
            'permisos': [permiso.to_json() for permiso in self.permisos],
            'vehiculo': self.vehiculo,
            'tipo_vehiculo': self.tipo_vehiculo,
            'itv': self.itv,
            'gastos_combustible': self.gastos_combustible
        }
    def mostrar_datos(self):
        permisos_str = ', '.join([permiso.tipo_permiso for permiso in self.permisos if permiso.tipo_permiso])
        return (f'DNI: {self.dni}\n'
                f'Nombre: {self.nombre}\n'
                f'Apellido 1: {self.primer_apellido}\n'
                f'Apellido 2: {self.segundo_apellido}\n'
                f'Permisos: {permisos_str}\n'
                f'Vehículo: {self.vehiculo}\n'
                f'Tipo de vehículo: {self.tipo_vehiculo}\n'
                f'ITV: {self.itv}\n'
                f'Gastos de combustible: {self.gastos_combustible}\n')
