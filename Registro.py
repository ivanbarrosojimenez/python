from feedback2.Alumno import Alumno
from feedback2.Permiso import Permiso
from feedback2.Profesor import Profesor

class Registro:
    def __init__(self, alumno, fecha_registro, permiso, profesor):
        self._alumno = alumno if isinstance(alumno, Alumno) else Alumno(**alumno)
        self._fecha_registro = fecha_registro
        self._permiso = permiso if isinstance(permiso, Permiso) else Permiso(**permiso)
        self._profesor = profesor if isinstance(profesor, Profesor) else Profesor(**profesor)

    @property
    def fecha_registro(self):
        return self._fecha_registro

    @fecha_registro.setter
    def fecha_registro(self, value):
        self._fecha_registro = value

    @property
    def permiso(self):
        return self._permiso

    @permiso.setter
    def permiso(self, value):
        self._permiso = value if isinstance(value, Permiso) else Permiso(**value)

    @property
    def alumno(self):
        return self._alumno

    @alumno.setter
    def alumno(self, value):
        self._alumno = value if isinstance(value, Alumno) else Alumno(**value)

    @property
    def profesor(self):
        return self._profesor

    @profesor.setter
    def profesor(self, value):
        self._profesor = value if isinstance(value, Profesor) else Profesor(**value)

    def to_string(self):
        alumno_str = self._alumno.to_string() if isinstance(self._alumno, Alumno) else str(self._alumno)
        permiso_str = self._permiso.to_string() if isinstance(self._permiso, Permiso) else str(self._permiso)
        profesor_str = self._profesor.to_string() if isinstance(self._profesor, Profesor) else str(self._profesor)

        return (f'Alumno: {alumno_str}\n'
                f'Fecha de Registro: {self._fecha_registro}\n'
                f'Permiso: {permiso_str}\n'
                f'Profesor: {profesor_str}')

    def to_json(self):
        return {
            'alumno': self._alumno.to_json(),
            'fecha_registro': self._fecha_registro,
            'permiso': self._permiso.to_json(),
            'profesor': self._profesor.to_json()
        }