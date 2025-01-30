from Persona import Persona
from Permiso import Permiso

class Profesor(Persona):
    def __init__(self, dni, nombre, apellido_1='', apellido_2='', permisos=None):
        super().__init__(dni, nombre, apellido_1, apellido_2)
        self.permisos = [permiso if isinstance(permiso, Permiso) else Permiso(**permiso) for permiso in (permisos or [])]

    def agregar_permiso(self, permiso):
        #if not isinstance(permiso, Permiso):
        #    permiso = Permiso(**permiso)
        self.permisos.append(permiso)


    def to_json(self):
        return {
            'dni': self.dni,
            'nombre': self.nombre,
            'apellido_1': self.apellido_1,
            'apellido_2': self.apellido_2,
            'permisos': [permiso.to_json() for permiso in self.permisos]
        }
    def to_string(self):
        permisos_str = ', '.join([permiso.tipo_permiso for permiso in self.permisos if permiso.tipo_permiso])
        return (f'DNI: {self.dni}\n'
                f'Nombre: {self.nombre}\n'
                f'Apellido 1: {self.apellido_1}\n'
                f'Apellido 2: {self.apellido_2}\n'
                f'Permisos: {permisos_str}')