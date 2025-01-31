from Persona import Persona
from Permiso import Permiso

class Profesor(Persona):
    def __init__(self, dni, nombre, primer_apellido='', segundo_apellido='', permisos=None, fecha_nacimiento=''):
        super().__init__(dni, nombre, primer_apellido, segundo_apellido, fecha_nacimiento)
        self.permisos = [permiso if isinstance(permiso, Permiso) else Permiso(**permiso) for permiso in (permisos or [])]

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
            'permisos': [permiso.to_json() for permiso in self.permisos]
        }
    def mostrar_datos(self):
        permisos_str = ', '.join([permiso.tipo_permiso for permiso in self.permisos if permiso.tipo_permiso])
        return (f'DNI: {self.dni}\n'
                f'Nombre: {self.nombre}\n'
                f'Apellido 1: {self.primer_apellido}\n'
                f'Apellido 2: {self.segundo_apellido}\n'
                f'Permisos: {permisos_str}')