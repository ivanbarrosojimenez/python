import json
import os

import Anticipo
import Factura
import Permiso
import Vehiculo
from feedback2.Clase import Clase
from feedback2.Alumno import Alumno



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
        dni=""
        existe=False
        while existe==False:
            dni = input("Ingrese el DNI del alumno: ")
            if valida_alumno(dni):
                print(f"El alumno con DNI {dni} ya está registrado.")
            else:
                existe=True
        nombre = input("Ingrese el nombre del alumno: ")
        apellido1 = input("Ingrese el apellido 1: ")
        apellido2 = input("Ingrese el apellido 2: ")
        nuevo_alumno = Alumno(dni, nombre, apellido1, apellido2)

        alumnos.append(nuevo_alumno)
        #guardar_datos('alumnos.json', alumnos)

        #a = alumnos.pop().to_json()
        guardar_alumnos('alumnos.json', alumnos)
        print(f"Alumno {nombre} con DNI {dni} registrado.")
    except Exception as e:
        print(f"Error al registrar alumno: {e}")

def valida_alumno(dni):
    for alumno in alumnos:
        if alumno.dni == dni:
            return True
    return False

def registrar_profesor():
    try:
        dni=""
        valido=False
        while not valido:
            dni = input("Ingrese el DNI del profesor: ")
            if valida_alumno(dni):
                print(f"El profesor con DNI {dni} ya está registrado.")
                valido=False
            else: valido=True
        nombre = input("Ingrese el nombre del profesor: ")
        profesores.append({'dni': dni, 'nombre': nombre})
        guardar_datos('profesores.json', profesores)
        print(f"Profesor {nombre} con DNI {dni} registrado.")
    except Exception as e:
        print(f"Error al registrar profesor: {e}")

def registrar_clase():
    try:
        alumno=""
        existe=False
        while existe==False:
            alumno = input("Ingrese el DNI del alumno: ")
            if valida_alumno(alumno):
                print(f"El alumno con DNI {alumno} no existe.")
                existe=True
        profesor=""
        existe=False
        while existe==False:
            profesor = input("Ingrese el DNI del profesor: ")
            if valida_alumno(profesor):
                print(f"El profesor con DNI {profesor} no existe.")
                existe=True
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
        alumno=""
        existe=False
        while existe==False:
            alumno = input("Ingrese el DNI del alumno: ")
            if valida_alumno(alumno):
                print(f"El alumno con DNI {alumno} no existe.")
                existe=True
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
        alumno=""
        existe=False
        while existe==False:
            alumno = input("Ingrese el DNI del alumno: ")
            if valida_alumno(alumno):
                print(f"El alumno con DNI {alumno} no existe.")
                existe=True
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

def guardar_datos(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def guardar_alumnos(filename, alumnos):
    with open(filename, 'w') as file:
        json.dump([alumno.to_json() for alumno in alumnos], file, indent=4)


def cargar_datos(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"El archivo {filename} no existe.")
        return []

def cargar_datos_generico(filename, cls):
    try:
        if os.path.getsize(filename) == 0:
            print(f"El archivo {filename} está vacío.")
            return []
        with open(filename, 'r') as file:
            data = json.load(file)
            return [cls(**item) for item in data]
    except FileNotFoundError:
        print(f"El archivo {filename} no existe.")
        return []


permisos = cargar_datos('permisos.json')
vehiculos = cargar_datos('vehiculos.json')
alumnos = cargar_datos_generico('alumnos.json', Alumno)
profesores = cargar_datos('profesores.json')
clases = cargar_datos('clases.json')
anticipos = cargar_datos('anticipos.json')
facturas = cargar_datos('facturas.json')
for alumno in alumnos:
    print(alumno.to_string())
for profesor in profesores:
    print(f"Profesor: {profesor['nombre']}, DNI: {profesor['dni']}")
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