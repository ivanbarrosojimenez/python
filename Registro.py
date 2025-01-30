class Registro:
    def __init__(self, num_registro, nombre, primer_apellido, segundo_apellido, dni, fecha_nacimiento, fecha_registro, permiso_opta):
        self.num_registro = num_registro
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_registro = fecha_registro
        self.permiso_opta = permiso_opta

    def mostrar_datos(self):
        print(f'Número de Registro: {self.num_registro}')
        print(f'Nombre: {self.nombre}')
        print(f'Primer Apellido: {self.primer_apellido}')
        print(f'Segundo Apellido: {self.segundo_apellido}')
        print(f'DNI: {self.dni}')
        print(f'Fecha de Nacimiento: {self.fecha_nacimiento}')
        print(f'Fecha de Registro: {self.fecha_registro}')
        print(f'Permiso Opta: {self.permiso_opta}')