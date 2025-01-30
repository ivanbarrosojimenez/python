
import json
import os

import Anticipo
import Factura
import Vehiculo
from feedback2.Clase import Clase
from feedback2.Alumno import Alumno
from feedback2.Registro import Registro
from feedback2.Permiso import Permiso
from feedback2.Profesor import Profesor


def mostrar_submenu_alumnos():
    print("Gestión de Alumnos")
    print("1. Registrar Alumno")
    print("2. Editar Alumno")
    print("3. Consultar Alumno")
    print("4. Listar todos los Alumnos")
    print("5. Volver al Menú Principal")

def gestionar_alumnos():
    while True:
        mostrar_submenu_alumnos()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_alumno()
        elif opcion == "2":
            editar_alumno()
        elif opcion == "3":
            consultar_alumno()
        elif opcion == "4":
            listar_alumnos()
        elif opcion == "5":
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

def registrar_alumno():
    try:
        dni=""
        existe=False
        while not existe:
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
        guardar_datos_generico('alumnos.json', alumnos)
        print(f"Alumno {nombre} con DNI {dni} registrado.")
    except Exception as e:
        print(f"Error al registrar alumno: {e}")

def editar_alumno():
    dni = input("Ingrese el DNI del alumno a editar: ")
    alumno = buscar_alumno(dni)
    if alumno:
        print(f"Alumno encontrado: {alumno.to_string()}")
        while True:
            mostrar_submenu_editar_alumno()
            opcion = input("Seleccione el dato a editar: ")
            if opcion == "1":
                nuevo_nombre = input("Ingrese el nuevo nombre del alumno: ")
                alumno.nombre = nuevo_nombre
            elif opcion == "2":
                nuevo_apellido1 = input("Ingrese el nuevo primer apellido del alumno: ")
                alumno.apellido_1 = nuevo_apellido1
            elif opcion == "3":
                nuevo_apellido2 = input("Ingrese el nuevo segundo apellido del alumno: ")
                alumno.apellido_2 = nuevo_apellido2
            elif opcion == "4":
                nuevo_curso = input("Ingrese el nuevo curso del alumno: ")
                alumno.curso = nuevo_curso
            elif opcion == "5":
                nueva_fecha_matriculacion = input("Ingrese la nueva fecha de matriculación del alumno: ")
                alumno.fecha_matriculacion = nueva_fecha_matriculacion
            elif opcion == "6":
                nuevo_domicilio = input("Ingrese el nuevo domicilio del alumno: ")
                alumno.domicilio = nuevo_domicilio
            elif opcion == "7":
                nuevo_municipio = input("Ingrese el nuevo municipio del alumno: ")
                alumno.municipio = nuevo_municipio
            elif opcion == "8":
                nueva_provincia = input("Ingrese la nueva provincia del alumno: ")
                alumno.provincia = nueva_provincia
            elif opcion == "9":
                nuevo_telefono1 = input("Ingrese el nuevo teléfono 1 del alumno: ")
                alumno.telefono1 = nuevo_telefono1
            elif opcion == "10":
                nuevo_telefono2 = input("Ingrese el nuevo teléfono 2 del alumno: ")
                alumno.telefono2 = nuevo_telefono2
            elif opcion == "11":
                nuevo_correo = input("Ingrese el nuevo correo del alumno: ")
                alumno.correo = nuevo_correo
            elif opcion == "12":
                print("Volviendo al menú anterior...")
                break
            else:
                print("Opción no válida, por favor intente de nuevo.")
            guardar_datos_generico('alumnos.json', alumnos)
            print("Alumno actualizado correctamente.")
    else:
        print(f"No se encontró un alumno con DNI {dni}.")

def mostrar_submenu_editar_alumno():
    print("Editar Alumno")
    print("1. Editar Nombre")
    print("2. Editar Primer Apellido")
    print("3. Editar Segundo Apellido")
    print("4. Editar Curso")
    print("5. Editar Fecha de Matriculación")
    print("6. Editar Domicilio")
    print("7. Editar Municipio")
    print("8. Editar Provincia")
    print("9. Editar Teléfono 1")
    print("10. Editar Teléfono 2")
    print("11. Editar Correo")
    print("12. Volver al Menú Anterior")

def buscar_alumno(dni):
    for alumno in alumnos:
        if alumno.dni == dni:
            return alumno
    return None

def consultar_alumno():
    dni = input("Ingrese el DNI del alumno a consultar: ")
    alumno = buscar_alumno(dni)
    if alumno:
        print(f"Alumno encontrado: {alumno.to_string()}")
    else:
        print(f"No se encontró un alumno con DNI {dni}.")

def listar_alumnos():
    for alumno in alumnos:
        print(alumno.to_string())

def valida_alumno(dni):
    for alumno in alumnos:
        if alumno.dni == dni:
            return True
    return False

def registrar_profesor():
    try:
        dni = ""
        valido = False
        while not valido:
            dni = input("Ingrese el DNI del profesor: ")
            if valida_alumno(dni):
                print(f"El profesor con DNI {dni} ya está registrado.")
                valido = False
            else:
                valido = True
        nombre = input("Ingrese el nombre del profesor: ")
        nuevo_profesor = Profesor(dni, nombre)
        profesores.append(nuevo_profesor)
        guardar_datos_generico('profesores.json', profesores)
        print(f"Profesor {nombre} con DNI {dni} registrado.")
    except Exception as e:
        print(f"Error al registrar profesor: {e}")

def registrar_clase():
    try:
        alumno=""
        existe=False
        while not existe:
            alumno = input("Ingrese el DNI del alumno: ")
            if not valida_alumno(alumno):
                print(f"El alumno con DNI {alumno} no existe.")
            else:
                existe=True
        profesor=""
        existe=False
        while not existe:
            profesor = input("Ingrese el DNI del profesor: ")
            if not valida_alumno(profesor):
                print(f"El profesor con DNI {profesor} no existe.")
            else:
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
        while not existe:
            alumno = input("Ingrese el DNI del alumno: ")
            if not valida_alumno(alumno):
                print(f"El alumno con DNI {alumno} no existe.")
            else:
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
        while not existe:
            alumno = input("Ingrese el DNI del alumno: ")
            if not valida_alumno(alumno):
                print(f"El alumno con DNI {alumno} no existe.")
            else:
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

def guardar_datos_generico(filename, datos):
    with open(filename, 'w') as file:
        json.dump([dato.to_json() for dato in datos], file, indent=4)

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


registros = cargar_datos_generico('registros.json', Registro)
alumnos = cargar_datos_generico('alumnos.json', Alumno)
permisos = cargar_datos_generico('permisos.json', Permiso)
profesores = cargar_datos_generico('profesores.json', Profesor)
vehiculos = cargar_datos('vehiculos.json')
clases = cargar_datos('clases.json')
anticipos = cargar_datos('anticipos.json')
facturas = cargar_datos('facturas.json')

for alumno in alumnos:
    print(alumno.to_string())
for profesor in profesores:
    print(profesor.to_string())

def mostrar_submenu_registros():
    print("Gestión de Registros")
    print("1. Alta Registro")
    print("2. Editar Registro")
    print("3. Consultar Registro")
    print("4. Listar todos los registros")
    print("5. Volver al Menú Principal")

def gestionar_registros():
    while True:
        mostrar_submenu_registros()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            alta_registro()
        elif opcion == "2":
            editar_registro()
        elif opcion == "3":
            consultar_registro()
        elif opcion == "4":
            listar_registros()
        elif opcion == "5":
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
def buscar_permiso(tipo_permiso):
    for permiso in permisos:
        if permiso.tipo_permiso == tipo_permiso:
            return permiso
    return None

def alta_registro():
    try:
        alumno_dni = input("Ingrese el DNI del alumno: ")
        alumno = buscar_alumno(alumno_dni)
        if not alumno:
            print(f"No se encontró un alumno con DNI {alumno_dni}.")
            return
        fecha_registro = input("Ingrese la fecha de registro: ")
        tipo_permiso = input("Ingrese el tipo de permiso: ")
        permiso = buscar_permiso(tipo_permiso)
        if not permiso:
            print(f"No se encontró un permiso de tipo {tipo_permiso}.")
            return
        profesor_dni = input("Ingrese el DNI del profesor: ")
        profesor = buscar_profesor(profesor_dni)
        if not profesor:
            print(f"No se encontró un profesor con DNI {profesor_dni}.")
            return
        nuevo_registro = Registro(alumno, fecha_registro, permiso, profesor)
        registros.append(nuevo_registro)
        guardar_datos_generico('registros.json', registros)
        print("Registro añadido correctamente.")
    except Exception as e:
        print(f"Error al añadir registro: {e}")

def editar_registro():
    try:
        alumno_dni = input("Ingrese el DNI del alumno del registro a editar: ")
        registro = buscar_registro(alumno_dni)
        if not registro:
            print(f"No se encontró un registro para el alumno con DNI {alumno_dni}.")
            return
        print(f"Registro encontrado: {registro.to_string()}")
        fecha_registro = input("Ingrese la nueva fecha de registro: ")
        permiso = input("Ingrese el nuevo permiso: ")
        profesor_dni = input("Ingrese el nuevo DNI del profesor: ")
        profesor = buscar_profesor(profesor_dni)
        if not profesor:
            print(f"No se encontró un profesor con DNI {profesor_dni}.")
            return
        registro.fecha_registro = fecha_registro
        registro.permiso = permiso
        registro.profesor = profesor
        guardar_datos_generico('registros.json', registros)
        print("Registro actualizado correctamente.")
    except Exception as e:
        print(f"Error al editar registro: {e}")

def consultar_registro():
    alumno_dni = input("Ingrese el DNI del alumno del registro a consultar: ")
    registro = buscar_registro(alumno_dni)
    if registro:
        print(f"Registro encontrado: {registro.to_string()}")
    else:
        print(f"No se encontró un registro para el alumno con DNI {alumno_dni}.")

def listar_registros():
    for registro in registros:
        print(registro.to_string())

def buscar_registro(alumno_dni):
    for registro in registros:
        if registro.alumno.dni == alumno_dni:
            return registro
    return None

def buscar_profesor(dni):
    for profesor in profesores:
        if profesor.dni == dni:
            return profesor
    return None

def mostrar_menu():
    print("Menú Principal")
    print("1. Gestionar Registros")
    print("2. Gestionar Alumnos")
    print("3. Registrar Profesor")
    print("4. Registrar Clase")
    print("5. Registrar Anticipo")
    print("6. Generar Factura")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            gestionar_registros()
        elif opcion == "2":
            gestionar_alumnos()
        elif opcion == "3":
            registrar_profesor()
        elif opcion == "4":
            registrar_clase()
        elif opcion == "5":
            registrar_anticipo()
        elif opcion == "6":
            generar_factura()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()