class Registro:
    def __init__(self, alumno, fecha_registro, permiso, profesor):
        self._alumno = alumno
        self._fecha_registro = fecha_registro
        self._permiso = permiso
        self._profesor = profesor

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
        self._permiso = value

    @property
    def alumno(self):
        return self._alumno

    @alumno.setter
    def alumno(self, value):
        self._alumno = value

    @property
    def profesor(self):
        return self._profesor

    @profesor.setter
    def profesor(self, value):
        self._profesor = value

    def to_string(self):
        return (f'Alumno: {self._alumno.to_string()}\n'
                f'Fecha de Registro: {self._fecha_registro}\n'
                f'Permiso: {self._permiso.to_string()}\n'
                f'Profesor: {self._profesor.to_string()}')

    def to_json(self):
        return {
            'alumno': self._alumno.to_json(),
            'fecha_registro': self._fecha_registro,
            'permiso': self._permiso.to_json(),
            'profesor': self._profesor.to_json()
        }