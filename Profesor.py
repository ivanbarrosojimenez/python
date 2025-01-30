from Persona import Persona
from Permiso import Permiso

class Profesor(Persona):
    def __init__(self, dni, nombre, apellido_1='', apellido_2='', permisos=None):
        super().__init__(dni, nombre, apellido_1, apellido_2)
        self.permisos = permisos if permisos is not None else []

    def agregar_permiso(self, permiso):
        self.permisos.append(permiso)

    def mostrar_info_completa(self):
        self.mostrar_info()
        print(f'Permisos: {[permiso.to_json() for permiso in self.permisos]}')

    def to_json(self):
        return {
            'dni': self.dni,
            'nombre': self.nombre,
            'apellido_1': self.apellido_1,
            'apellido_2': self.apellido_2,
            'permisos': [permiso.to_json() for permiso in self.permisos]
        }