import json

class Alumno:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre

class Profesor:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre

class Clase:
    def __init__(self, alumno, profesor, matricula_vehiculo, fecha_hora):
        self.alumno = alumno
        self.profesor = profesor
        self.matricula_vehiculo = matricula_vehiculo
        self.fecha_hora = fecha_hora

    def mostrar_info_clase(self):
        print(f'Alumno (DNI): {self.alumno}')
        print(f'Profesor (DNI): {self.profesor}')
        print(f'Matrícula del Vehículo: {self.matricula_vehiculo}')
        print(f'Fecha y Hora: {self.fecha_hora}')

class Anticipo:
    def __init__(self, alumno, fecha, concepto, cantidad):
        self.alumno = alumno
        self.fecha = fecha
        self.concepto = concepto
        self.cantidad = cantidad

    def mostrar_info_anticipo(self):
        print(f'Alumno (DNI): {self.alumno}')
        print(f'Fecha: {self.fecha}')
        print(f'Concepto: {self.concepto}')
        print(f'Cantidad: {self.cantidad}')

class Factura:
    def __init__(self, alumno, precio_matricula, num_clases_incluidas, num_clases_dadas, precio_clase, num_examenes, precio_examen, num_renovaciones, precio_renovacion, anticipos):
        self.alumno = alumno
        self.precio_matricula = precio_matricula
        self.num_clases_incluidas = num_clases_incluidas
        self.num_clases_dadas = num_clases_dadas
        self.precio_clase = precio_clase
        self.num_examenes = num_examenes
        self.precio_examen = precio_examen
        self.num_renovaciones = num_renovaciones
        self.precio_renovacion = precio_renovacion
        self.anticipos = anticipos

    def calcular_total(self):
        total_clases = max(0, self.num_clases_dadas - self.num_clases_incluidas) * self.precio_clase
        total_examenes = self.num_examenes * self.precio_examen
        total_renovaciones = self.num_renovaciones * self.precio_renovacion
        total = self.precio_matricula + total_clases + total_examenes + total_renovaciones
        return total

    def calcular_iva(self):
        total = self.calcular_total()
        iva = total * 0.21
        return iva

    def calcular_total_con_iva(self):
        total = self.calcular_total()
        iva = self.calcular_iva()
        total_con_iva = total + iva
        return total_con_iva

    def calcular_saldo_pendiente(self):
        total_con_iva = self.calcular_total_con_iva()
        saldo_pendiente = total_con_iva - self.anticipos
        return saldo_pendiente

    def generar_factura(self):
        total = self.calcular_total()
        iva = self.calcular_iva()
        total_con_iva = self.calcular_total_con_iva()
        saldo_pendiente = self.calcular_saldo_pendiente()

        factura_str = (
            f'Factura para el alumno (DNI): {self.alumno}\n'
            f'Precio Matrícula: {self.precio_matricula}\n'
            f'Número de Clases Incluidas: {self.num_clases_incluidas}\n'
            f'Número de Clases Dadas: {self.num_clases_dadas}\n'
            f'Precio por Clase: {self.precio_clase}\n'
            f'Número de Exámenes: {self.num_examenes}\n'
            f'Precio por Examen: {self.precio_examen}\n'
            f'Número de Renovaciones: {self.num_renovaciones}\n'
            f'Precio por Renovación: {self.precio_renovacion}\n'
            f'Anticipos: {self.anticipos}\n'
            f'Total: {total}\n'
            f'IVA (21%): {iva}\n'
            f'Total con IVA: {total_con_iva}\n'
            f'Saldo Pendiente: {saldo_pendiente}\n'
        )
        print(factura_str)
        with open(f'factura_{self.alumno}.txt', 'w') as file:
            file.write(factura_str)

def guardar_datos(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def cargar_datos(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

alumnos = cargar_datos('alumnos.json')
profesores = cargar_datos('profesores.json')
clases = cargar_datos('clases.json')
anticipos = cargar_datos('anticipos.json')
facturas = cargar_datos('facturas.json')

def mostrar_menu():
    print("Menú Principal")
    print("1. Registrar Alumno")
    print("2. Registrar Profesor")
    print("3. Registrar Clase")
    print("4. Registrar Anticipo")
    print("5. Generar Factura")
    print("6. Salir")

def registrar_alumno():
    try:
        dni = input("Ingrese el DNI del alumno: ")
        nombre = input("Ingrese el nombre del alumno: ")
        alumnos.append({'dni': dni, 'nombre': nombre})
        guardar_datos('alumnos.json', alumnos)
        print(f"Alumno {nombre} con DNI {dni} registrado.")
    except Exception as e:
        print(f"Error al registrar alumno: {e}")

def registrar_profesor():
    try:
        dni = input("Ingrese el DNI del profesor: ")
        nombre = input("Ingrese el nombre del profesor: ")
        profesores.append({'dni': dni, 'nombre': nombre})
        guardar_datos('profesores.json', profesores)
        print(f"Profesor {nombre} con DNI {dni} registrado.")
    except Exception as e:
        print(f"Error al registrar profesor: {e}")

def registrar_clase():
    try:
        alumno = input("Ingrese el DNI del alumno: ")
        profesor = input("Ingrese el DNI del profesor: ")
        matricula_vehiculo = input("Ingrese la matrícula del vehículo: ")
        fecha_hora = input("Ingrese la fecha y hora de la clase: ")
        clase = Clase(alumno, profesor, matricula_vehiculo, fecha_hora)
        clases.append({'alumno': alumno, 'profesor': profesor, 'matricula_vehiculo': matricula_vehiculo, 'fecha_hora': fecha_hora})
        guardar_datos('clases.json', clases)
        clase.mostrar_info_clase()
    except Exception as e:
        print(f"Error al registrar clase: {e}")

def registrar_anticipo():
    try:
        alumno = input("Ingrese el DNI del alumno: ")
        fecha = input("Ingrese la fecha del anticipo: ")
        concepto = input("Ingrese el concepto del anticipo: ")
        cantidad = float(input("Ingrese la cantidad del anticipo: "))
        anticipo = Anticipo(alumno, fecha, concepto, cantidad)
        anticipos.append({'alumno': alumno, 'fecha': fecha, 'concepto': concepto, 'cantidad': cantidad})
        guardar_datos('anticipos.json', anticipos)
        anticipo.mostrar_info_anticipo()
    except Exception as e:
        print(f"Error al registrar anticipo: {e}")

def generar_factura():
    try:
        alumno = input("Ingrese el DNI del alumno: ")
        precio_matricula = float(input("Ingrese el precio de la matrícula: "))
        num_clases_incluidas = int(input("Ingrese el número de clases incluidas: "))
        num_clases_dadas = int(input("Ingrese el número de clases dadas: "))
        precio_clase = float(input("Ingrese el precio por clase: "))
        num_examenes = int(input("Ingrese el número de exámenes: "))
        precio_examen = float(input("Ingrese el precio por examen: "))
        num_renovaciones = int(input("Ingrese el número de renovaciones: "))
        precio_renovacion = float(input("Ingrese el precio por renovación: "))
        anticipos = float(input("Ingrese el total de anticipos: "))
        factura = Factura(alumno, precio_matricula, num_clases_incluidas, num_clases_dadas, precio_clase, num_examenes, precio_examen, num_renovaciones, precio_renovacion, anticipos)
        facturas.append({'alumno': alumno, 'precio_matricula': precio_matricula, 'num_clases_incluidas': num_clases_incluidas, 'num_clases_dadas': num_clases_dadas, 'precio_clase': precio_clase, 'num_examenes': num_examenes, 'precio_examen': precio_examen, 'num_renovaciones': num_renovaciones, 'precio_renovacion': precio_renovacion, 'anticipos': anticipos})
        guardar_datos('facturas.json', facturas)
        factura.generar_factura()
    except Exception as e:
        print(f"Error al generar factura: {e}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_alumno()
        elif opcion == "2":
            registrar_profesor()
        elif opcion == "3":
            registrar_clase()
        elif opcion == "4":
            registrar_anticipo()
        elif opcion == "5":
            generar_factura()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()