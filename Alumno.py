# feedback2/Alumno.py
from feedback2.Registro import Registro

class Alumno(Registro):
    def __init__(self, nombre='', primer_apellido='', segundo_apellido='', dni='', fecha_nacimiento='',
                 fecha_registro='', num_registro='', permiso_opta='', domicilio='', municipio='', provincia='',
                 telefono1='', telefono2='', correo='', num_clases=0, profesor='', examenes_teoricos='', examenes_circulacion='', total_anticipos=0.0):
        super().__init__(nombre, primer_apellido, segundo_apellido, dni, fecha_nacimiento, fecha_registro, num_registro, permiso_opta)
        self._domicilio = domicilio
        self._municipio = municipio
        self._provincia = provincia
        self._telefono1 = telefono1
        self._telefono2 = telefono2
        self._correo = correo
        self._num_clases = num_clases
        self._profesor = profesor
        self._examenes_teoricos = examenes_teoricos if examenes_teoricos is not None else []
        self._examenes_circulacion = examenes_circulacion if examenes_circulacion is not None else []
        self._total_anticipos = total_anticipos

    @property
    def profesor(self):
        return self._profesor if self._profesor is not None else ""

    @profesor.setter
    def profesor(self, value):
        self._profesor = value

    @property
    def examenes_teoricos(self):
        return self._examenes_teoricos

    @examenes_teoricos.setter
    def examenes_teoricos(self, value):
        self._examenes_teoricos = value

    @property
    def domicilio(self):
        return self._domicilio

    @domicilio.setter
    def domicilio(self, value):
        self._domicilio = value

    @property
    def total_anticipos(self):
        return self._total_anticipos

    @total_anticipos.setter
    def total_anticipos(self, value):
        self._total_anticipos = value

    @property
    def municipio(self):
        return self._municipio

    @municipio.setter
    def municipio(self, value):
        self._municipio = value

    @property
    def num_clases(self):
        return self._num_clases

    @num_clases.setter
    def num_clases(self, value):
        self._num_clases = value

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, value):
        self._correo = value

    @property
    def telefono1(self):
        return self._telefono1

    @telefono1.setter
    def telefono1(self, value):
        self._telefono1 = value

    @property
    def examenes_circulacion(self):
        return self._examenes_circulacion

    @examenes_circulacion.setter
    def examenes_circulacion(self, value):
        self._examenes_circulacion = value

    @property
    def telefono2(self):
        return self._telefono2

    @telefono2.setter
    def telefono2(self, value):
        self._telefono2 = value

    @property
    def provincia(self):
        return self._provincia

    @provincia.setter
    def provincia(self, value):
        self._provincia = value

    def agregar_examen_teorico(self, fecha_hora):
        self._examenes_teoricos.append(fecha_hora)

    def agregar_examen_circulacion(self, fecha_hora):
        self._examenes_circulacion.append(fecha_hora)

    def agregar_clases(self, num):
        self._num_clases += num

    def to_json(self):
        return {
            'nombre': self.nombre,
            'primer_apellido': self.primer_apellido,
            'segundo_apellido': self.segundo_apellido,
            'dni': self.dni,
            'fecha_nacimiento': self.fecha_nacimiento,
            'num_registro': self._num_registro,
            'fecha_registro': self._fecha_registro,
            'permiso_opta': self._permiso_opta,
            'domicilio': self._domicilio,
            'municipio': self._municipio,
            'provincia': self._provincia,
            'telefono1': self._telefono1,
            'telefono2': self._telefono2,
            'correo': self._correo,
            'num_clases': self._num_clases,
            'profesor': self._profesor,
            'examenes_teoricos': self._examenes_teoricos,
            'examenes_circulacion': self._examenes_circulacion,
            'total_anticipos': self._total_anticipos,
            'permiso_opta': self.permiso_opta
        }


    def mostrar_info(self):
        return (f"----------------------------------------------\n"
                f"| Número de Registro: {self._num_registro}\n"
                f"|  Fecha de Registro: {self._fecha_registro}\n"
                f"|  Permiso Opta: {self._permiso_opta}\n"
                f"|  ---------\n"
                f"|  |  Nombre: {self.nombre}\n"
                f"|  |  Primer Apellido: {self.primer_apellido}\n"
                f"|  |  Segundo Apellido: {self.segundo_apellido}\n"
                f"|  |  DNI: {self.dni}\n"
                f"|  |  Fecha de Nacimiento: {self.fecha_nacimiento}\n"
                f"|  |---------\n"
                f"|  |  Domicilio: {self._domicilio}\n"
                f"|  |  Municipio: {self._municipio}\n"
                f"|  |  Provincia: {self._provincia}\n"
                f"|  |  Teléfono 1: {self._telefono1}\n"
                f"|  |  Teléfono 2: {self._telefono2}\n"
                f"|  |  Correo: {self._correo}\n"
                f"|  |  Número de Clases: {self._num_clases}\n"
                f"|  |  Profesor: {self.profesor}\n"
                f"|  |  Exámenes Teóricos: {self._examenes_teoricos}\n"
                f"|  |  Exámenes de Circulación: {self._examenes_circulacion}\n"
                f"|  |  Total Anticipos: {self._total_anticipos}\n"
                f"----------------------------------------------\n")

    def mostrar_datos_basicos(self):
        return (f"----------------------------------------------\n"
                f"| Número de Registro: {self._num_registro}\n"
                f"|  Fecha de Registro: {self._fecha_registro}\n"
                f"|  Permiso Opta: {self._permiso_opta}\n"
                f"|  ---------\n"
                f"|  |  Nombre: {self.nombre}\n"
                f"|  |  Primer Apellido: {self.primer_apellido}\n"
                f"|  |  Segundo Apellido: {self.segundo_apellido}\n"
                f"|  |  DNI: {self.dni}\n"
                f"|  |  Fecha de Nacimiento: {self.fecha_nacimiento}\n"
                f"----------------------------------------------\n")

    def mostrar_datos_editar(self):
        return (f"\n----------------------------------------------\n"
                f"|  Número de Registro: {self._num_registro} (no editable)\n"
                f"|  1. Fecha de Registro: {self._fecha_registro}\n"
                f"|  2. Permiso Opta: {self._permiso_opta}\n"
                f"|  3.  Nombre: {self.nombre}\n"
                f"|  4.  Primer Apellido: {self.primer_apellido}\n"
                f"|  5.  Segundo Apellido: {self.segundo_apellido}\n"
                f"|  6.  DNI: {self.dni}\n"
                f"|  7.  Fecha de Nacimiento: {self.fecha_nacimiento}\n"
                f"----------------------------------------------\n")
    def mostrar_datos_editar_avanzado(self):
        return (f"\n----------------------------------------------\n"
                f"|  Número de Registro: {self._num_registro}\n"
                f"|  Fecha de Registro: {self._fecha_registro}\n"
                f"|  Permiso Opta: {self._permiso_opta}\n"
                f"|  Nombre: {self.nombre}\n"
                f"|  Primer Apellido: {self.primer_apellido}\n"
                f"|  Segundo Apellido: {self.segundo_apellido}\n"
                f"|  DNI: {self.dni}\n"
                f"|  Fecha de Nacimiento: {self.fecha_nacimiento}\n"
                f"----------------------------------------------\n"
                f"|  1.  Domicilio: {self._domicilio}\n"
                f"|  2.  Municipio: {self._municipio}\n"
                f"|  3.  Provincia: {self._provincia}\n"
                f"|  4.  Teléfono 1: {self._telefono1}\n"
                f"|  5.  Teléfono 2: {self._telefono2}\n"
                f"|  6.  Correo: {self._correo}\n"
                f"|  7.  Número de Clases: {self._num_clases}\n"
                f"|  8.  Profesor: {self.profesor}\n"
                f"|  9.  Exámenes Teóricos: {self._examenes_teoricos}\n"
                f"|  10.  Exámenes de Circulación: {self._examenes_circulacion}\n"
                f"|  11.  Total Anticipos: {self._total_anticipos}")