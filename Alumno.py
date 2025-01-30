# feedback2/Alumno.py
from Persona import Persona

class Alumno(Persona):
    def __init__(self, dni, nombre, apellido_1, apellido_2, curso='', fecha_matriculacion='', domicilio='', municipio='', provincia='', telefono1='', telefono2='', correo='', num_clases=0, examenes_teoricos=None, examenes_circulacion=None, total_anticipos=0.0):
        super().__init__(dni, nombre, apellido_1, apellido_2)
        self.curso = curso
        self.fecha_matriculacion = fecha_matriculacion
        self.domicilio = domicilio
        self.municipio = municipio
        self.provincia = provincia
        self.telefono1 = telefono1
        self.telefono2 = telefono2
        self.correo = correo
        self.num_clases = num_clases
        self.examenes_teoricos = examenes_teoricos if examenes_teoricos is not None else []
        self.examenes_circulacion = examenes_circulacion if examenes_circulacion is not None else []
        self.total_anticipos = total_anticipos

    def agregar_examen_teorico(self, fecha_hora):
        self.examenes_teoricos.append(fecha_hora)

    def agregar_examen_circulacion(self, fecha_hora):
        self.examenes_circulacion.append(fecha_hora)

    def agregar_clases(self, num):
        self.num_clases += num

    def to_json(self):
        return {
            'dni': self.dni,
            'nombre': self.nombre,
            'apellido_1': self.apellido_1,
            'apellido_2': self.apellido_2,
            'curso': self.curso,
            'fecha_matriculacion': self.fecha_matriculacion,
            'domicilio': self.domicilio,
            'municipio': self.municipio,
            'provincia': self.provincia,
            'telefono1': self.telefono1,
            'telefono2': self.telefono2,
            'correo': self.correo,
            'num_clases': self.num_clases,
            'examenes_teoricos': self.examenes_teoricos,
            'examenes_circulacion': self.examenes_circulacion,
            'total_anticipos': self.total_anticipos
        }

    def to_string(self):
        return (f"DNI: {self.dni}, Nombre: {self.nombre}, Apellido 1: {self.apellido_1}, "
                f"Apellido 2: {self.apellido_2}, Curso: {self.curso}, Fecha de Matriculación: {self.fecha_matriculacion}, "
                f"Domicilio: {self.domicilio}, Municipio: {self.municipio}, Provincia: {self.provincia}, "
                f"Teléfono 1: {self.telefono1}, Teléfono 2: {self.telefono2}, Correo: {self.correo}, "
                f"Número de Clases: {self.num_clases}, "
                f"Exámenes Teóricos: {self.examenes_teoricos}, Exámenes de Circulación: {self.examenes_circulacion}, "
                f"Total Anticipos: {self.total_anticipos}")