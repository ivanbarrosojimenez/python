# Clase base Persona
class Persona:
    def __init__(self, dni, nombre, apellido_1, apellido_2):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido_1 = apellido_1
        self.__apellido_2 = apellido_2

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, value):
        self.__dni = value

    @property
    def apellido_1(self):
        return self.__apellido_1

    @apellido_1.setter
    def apellido_1(self, value):
        self.__apellido_1 = value

    @property
    def apellido_2(self):
        return self.__apellido_2

    @apellido_2.setter
    def apellido_2(self, value):
        self.__apellido_2 = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    def to_string(self):
        return (f"DNI: {self.dni}, Nombre: {self.nombre}, Apellido 1: {self.apellido_1}, "
                f"Apellido 2: {self.apellido_2}")