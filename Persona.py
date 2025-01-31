# feedback2/Persona.py
class Persona:
    def __init__(self, nombre='', primer_apellido='', segundo_apellido=''
                 , dni='', fecha_nacimiento=''):
        self._nombre = nombre
        self._primer_apellido = primer_apellido
        self._segundo_apellido = segundo_apellido
        self._dni = dni
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def primer_apellido(self):
        return self._primer_apellido

    @primer_apellido.setter
    def primer_apellido(self, value):
        self._primer_apellido = value

    @property
    def segundo_apellido(self):
        return self._segundo_apellido

    @segundo_apellido.setter
    def segundo_apellido(self, value):
        self._segundo_apellido = value

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, value):
        self._dni = value

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value):
        self._fecha_nacimiento = value

    def to_json(self):
        return {
            'nombre': self._nombre,
            'primer_apellido': self._primer_apellido,
            'segundo_apellido': self._segundo_apellido,
            'dni': self._dni,
            'fecha_nacimiento': self._fecha_nacimiento
        }

    def mostrar_datos(self):
        return (f"Nombre: {self._nombre}, Primer Apellido: {self._primer_apellido}, "
                f"Segundo Apellido: {self._segundo_apellido}, DNI: {self._dni}, "
                f"Fecha de Nacimiento: {self._fecha_nacimiento}")