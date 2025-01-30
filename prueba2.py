import json

# Clase Registro
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
        print(f"Registro: {self.num_registro}\nNombre: {self.nombre} {self.primer_apellido} {self.segundo_apellido}\nDNI: {self.dni}\nFecha de nacimiento: {self.fecha_nacimiento}\nFecha de registro: {self.fecha_registro}\nPermiso: {self.permiso_opta}\n")

# Clase Alumno (hereda de Registro)
class Alumno(Registro):
    def __init__(self, num_registro, nombre, primer_apellido, segundo_apellido, dni, fecha_nacimiento, fecha_registro, permiso_opta, domicilio, municipio, provincia, telefono1, telefono2, correo, num_clases, profesor):
        super().__init__(num_registro, nombre, primer_apellido, segundo_apellido, dni, fecha_nacimiento, fecha_registro, permiso_opta)
        self.domicilio = domicilio
        self.municipio = municipio
        self.provincia = provincia
        self.telefono1 = telefono1
        self.telefono2 = telefono2
        self.correo = correo
        self.num_clases = num_clases
        self.profesor = profesor
        self.examenes_teoricos = []
        self.examenes_circulacion = []
        self.total_anticipos = 0.0

    def agregar_examen_teorico(self, fecha):
        self.examenes_teoricos.append(fecha)

    def agregar_examen_circulacion(self, fecha):
        self.examenes_circulacion.append(fecha)

    def agregar_clases(self, num):
        self.num_clases += num

    def mostrar_info_completa(self):
        self.mostrar_datos()
        print(f"Domicilio: {self.domicilio}, {self.municipio}, {self.provincia}\nTeléfonos: {self.telefono1}, {self.telefono2}\nCorreo: {self.correo}\nClases realizadas: {self.num_clases}\nProfesor: {self.profesor}\nTotal anticipos: {self.total_anticipos}\n")

# Clase Profesor
class Profesor:
    def __init__(self, nombre, primer_apellido, segundo_apellido, vehiculo, tipo_vehiculo, itv):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.vehiculo = vehiculo
        self.tipo_vehiculo = tipo_vehiculo
        self.itv = itv
        self.gastos_combustible = {}

    def registrar_gasto_combustible(self, fecha, costo):
        self.gastos_combustible[fecha] = costo

    def mostrar_gastos_combustible(self):
        print("Gastos de combustible:")
        for fecha, costo in self.gastos_combustible.items():
            print(f"{fecha}: {costo:.2f}€")

    def mostrar_info_profesor(self):
        print(f"Profesor: {self.nombre} {self.primer_apellido} {self.segundo_apellido}\nVehículo: {self.vehiculo} ({self.tipo_vehiculo})\nITV: {self.itv}\n")

# Menú interactivo
def menu():
    alumnos = []
    profesores = []

    while True:
        print("\n--- Menú de Gestión de Autoescuela ---")
        print("1. Registrar Alumno")
        print("2. Registrar Profesor")
        print("3. Mostrar Alumnos")
        print("4. Mostrar Profesores")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("--- Registrar Alumno ---")
            try:
                num_registro = input("Número de registro: ")
                nombre = input("Nombre: ")
                primer_apellido = input("Primer apellido: ")
                segundo_apellido = input("Segundo apellido: ")
                dni = input("DNI: ")
                fecha_nacimiento = input("Fecha de nacimiento (DD-MM-AAAA): ")
                fecha_registro = input("Fecha de registro (DD-MM-AAAA): ")
                permiso_opta = input("Permiso al que opta: ")
                domicilio = input("Domicilio: ")
                municipio = input("Municipio: ")
                provincia = input("Provincia: ")
                telefono1 = input("Teléfono 1: ")
                telefono2 = input("Teléfono 2 (opcional): ")
                correo = input("Correo: ")
                num_clases = int(input("Número de clases realizadas: "))
                profesor = input("Profesor asignado: ")

                nuevo_alumno = Alumno(num_registro, nombre, primer_apellido, segundo_apellido, dni, fecha_nacimiento, fecha_registro, permiso_opta, domicilio, municipio, provincia, telefono1, telefono2, correo, num_clases, profesor)
                alumnos.append(nuevo_alumno)
                print("Alumno registrado con éxito.")
            except ValueError as e:
                print(f"Error en la entrada de datos: {e}")

        elif opcion == "2":
            print("--- Registrar Profesor ---")
            try:
                nombre = input("Nombre: ")
                primer_apellido = input("Primer apellido: ")
                segundo_apellido = input("Segundo apellido: ")
                vehiculo = input("Vehículo (matrícula): ")
                tipo_vehiculo = input("Tipo de vehículo: ")
                itv = input("Fecha de caducidad de la ITV: ")

                nuevo_profesor = Profesor(nombre, primer_apellido, segundo_apellido, vehiculo, tipo_vehiculo, itv)
                profesores.append(nuevo_profesor)
                print("Profesor registrado con éxito.")
            except ValueError as e:
                print(f"Error en la entrada de datos: {e}")

        elif opcion == "3":
            print("--- Lista de Alumnos ---")
            if alumnos:
                for alumno in alumnos:
                    alumno.mostrar_info_completa()
            else:
                print("No hay alumnos registrados.")

        elif opcion == "4":
            print("--- Lista de Profesores ---")
            if profesores:
                for profesor in profesores:
                    profesor.mostrar_info_profesor()
            else:
                print("No hay profesores registrados.")

        elif opcion == "5":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
