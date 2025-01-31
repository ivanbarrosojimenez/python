# feedback2/Registro.py
from feedback2.Persona import Persona

class Registro(Persona):
    def __init__(self, nombre='', primer_apellido='', segundo_apellido='', dni='', fecha_nacimiento='', fecha_registro=None, num_registro=None, permiso_opta=None):
        super().__init__(nombre, primer_apellido, segundo_apellido, dni, fecha_nacimiento)
        self._num_registro = num_registro
        self._fecha_registro = fecha_registro
        self._permiso_opta = permiso_opta

    @property
    def permiso_opta(self):
        return self._permiso_opta

    @permiso_opta.setter
    def permiso_opta(self, value):
        self._permiso_opta = value

    @property
    def fecha_registro(self):
        return self._fecha_registro

    @fecha_registro.setter
    def fecha_registro(self, value):
        self._fecha_registro = value

    @property
    def num_registro(self):
        return self._num_registro

    @num_registro.setter
    def num_registro(self, value):
        self._num_registro = value

    def to_json(self):
        return {
            'nombre': self.nombre,
            'primer_apellido': self.primer_apellido,
            'segundo_apellido': self.segundo_apellido,
            'dni': self.dni,
            'fecha_nacimiento': self.fecha_nacimiento,
            'num_registro': self._num_registro,
            'fecha_registro': self._fecha_registro,
            'permiso_opta': self._permiso_opta
        }

    def mostrar_datos(self):
        return (f"Nombre: {self.nombre}, Primer Apellido: {self.primer_apellido}, "
                f"Segundo Apellido: {self.segundo_apellido}, DNI: {self.dni}, "
                f"Fecha de Nacimiento: {self.fecha_nacimiento}, Número de Registro: {self._num_registro}, "
                f"Fecha de Registro: {self._fecha_registro}, Permiso Opta: {self._permiso_opta}")