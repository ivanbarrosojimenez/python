
import json
import os
import re

import Anticipo
import Factura
import Vehiculo
from feedback2.Clase import Clase
from feedback2.Alumno import Alumno
from feedback2.PDFGenerator import PDFGenerator
from feedback2.Persona import Persona
from feedback2.Registro import Registro
from feedback2.Permiso import Permiso
from feedback2.Profesor import Profesor


def mostrar_submenu_alumnos():
    print("Gestión de Alumnos")
    print("1. Editar Alumno")
    print("2. Consultar Alumno")
    print("3. Listar todos los Alumnos")
    print("0. Volver al Menú Principal")

def gestionar_alumnos():
    while True:
        mostrar_submenu_alumnos()
        print(f"-----------------")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            editar_alumno()
        elif opcion == "2":
            consultar_alumno()
        elif opcion == "3":
            listar_alumnos()
        elif opcion == "0":
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


def mostrar_info_personas(personas):
    for i, persona in enumerate(personas, start=1):
        print(f"{i}. {persona.dni} - {persona.nombre} {persona.primer_apellido} {persona.segundo_apellido}")
    if not personas:
        print("No hay alumnos registrados.")


def editar_alumno():
    alumnos_disponibles= buscar_registros()
    mostrar_info_personas(registro.persona for registro in alumnos_disponibles)
    indice_alumno = obtener_indice_respuesta("Ingrese el número de Alumno a editar: ", alumnos_disponibles)
    alumno = alumnos[int(indice_alumno) - 1]


    print(f"-----------------")
    print(f"Editando Alumno: {alumno.persona.dni} - {alumno.persona.nombre} {alumno.persona.primer_apellido} {alumno.persona.segundo_apellido}")
    while True:
        mostrar_submenu_editar_alumno()
        opcion = input("Seleccione el dato a editar: ")
        if opcion == "1":
            nuevo_nombre = input("Ingrese el nuevo nombre del alumno: ")
            alumno.persona.nombre = nuevo_nombre
        elif opcion == "2":
            nuevo_apellido1 = input("Ingrese el nuevo primer apellido del alumno: ")
            alumno.persona.primer_apellido = nuevo_apellido1
        elif opcion == "3":
            nuevo_apellido2 = input("Ingrese el nuevo segundo apellido del alumno: ")
            alumno.persona.segundo_apellido = nuevo_apellido2
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
        guardar_datos_generico('registros.json', alumnos)
        print("Alumno actualizado correctamente.")

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

def buscar_alumno(dni, tipo_permiso):
    for registro in alumnos:
        if registro.dni == dni and registro.tipo_permiso == tipo_permiso:
            return registro
    return None

def consultar_alumno():
    dni = input("Ingrese el DNI del alumno a consultar: ")
    alumno = buscar_alumno(dni)
    if alumno:
        print(f"Alumno encontrado: {alumno.to_string()}")
        # Ejemplo de uso:
        filename = f"{alumno.dni}_{alumno.nombre}.pdf"
        pdf_gen = PDFGenerator(filename)
        pdf_gen.generate_pdf(alumno.to_string())
    else:
        print(f"No se encontró un alumno con DNI {dni}.")

def listar_alumnos():
    for alumno in alumnos:
        print(alumno.mostrar_datos())

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

def validar_fecha(mensaje):
    while True:
        fecha_registro = input(mensaje)
        if re.match(r'^\d{2}/\d{2}/\d{4}$', fecha_registro):
            try:
                day, month, year = map(int, fecha_registro.split('/'))
                if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
                    return fecha_registro
                else:
                    print("Fecha no válida. Asegúrese de que el día, mes y año sean correctos.")
            except ValueError:
                print("Fecha no válida. Asegúrese de que el día, mes y año sean correctos.")
        else:
            print("Formato de fecha no válido. Use DD/MM/AAAA.")


def buscar_profesores(tipo_permiso):
    return [profesor for profesor in profesores if tipo_permiso in [permiso.tipo_permiso for permiso in profesor.permisos]]


def buscar_alumnos():
    return [registro.persona for registro in alumnos]

def buscar_registros():
    return [registro for registro in alumnos]


def imprime_disponibles(profesores_disponibles):
    for i, p in enumerate(profesores_disponibles, start=1):
        print(f"{i}. {p.nombre}")
def imprime_lista(profesores_disponibles):
    for i, p in enumerate(profesores_disponibles, start=1):
        print(f"{i}. {p}")


def solicitar_dni(mensaje):
    while True:
        dni = input(mensaje)
        if re.match(r'^\d{8}[A-Z]$', dni):
            return dni
        else:
            print("DNI o NIF no válido. Debe tener 8 dígitos seguidos de una letra mayúscula.")


def obtener_indice_respuesta(param, profesores_disponibles):
    while True:
        indice_profesor = input(param)
        if indice_profesor.isdigit() and 1 <= int(indice_profesor) <= len(profesores_disponibles):
            return indice_profesor
        else:
            print("Índice no válido. Introduzca un número válido.")


def solicitar_tipo_permiso():
    while True:
        tipo_permiso = input("Ingrese el tipo de permiso: ")
        permiso = buscar_permiso(tipo_permiso)
        if permiso:
            return permiso
        else:
            print(f"No se encontró un permiso de tipo {tipo_permiso}.")

def alta_registro():
    try:
        #persona = Persona("nombre", "primer_apellido", "segundo_apellido", "dni", "fecha_nacimiento")
        #registro = Registro("nombre", "primer_apellido", "segundo_apellido", "dni", "fecha_nacimiento", "fecha_registro", "num_registro", "permiso_opta")
        #alumno = Alumno("nombre", "primer_apellido", "segundo_apellido", "dni", "fecha_nacimiento", "fecha_registro", "num_registro", "permiso_opta", "domicilio", "municipio", "provincia", "telefono1", "telefono2", "correo", "num_clases", "examenes_teoricos", "examenes_circulacion", "total_anticipos")
        #registros.append(alumno)

        #guardar_datos_generico('registros.json', registros)

        permisos_disponibles = [permiso.tipo_permiso for permiso in permisos]
        print(f"Tipos de permiso disponibles:{permisos_disponibles}")
        permiso = solicitar_tipo_permiso()
        permiso_opta = permiso.tipo_permiso


        '''profesores_disponibles = buscar_profesores(permiso_opta)
        if not profesores_disponibles:
            print(f"No hay profesores disponibles para el permiso {permiso_opta}, da de alta primero un profesor para ese permiso")
            return
        imprime_disponibles(profesores_disponibles)
        indice_profesor = obtener_indice_respuesta("Seleccione el profesor: ", profesores_disponibles)
        profesor = profesores_disponibles[int(indice_profesor) - 1]
        '''
        alumno_dni = solicitar_dni("Ingrese el DNI del alumno: ")

        alumno_existente = buscar_alumno(alumno_dni, permiso_opta)
        if alumno_existente:
            print(f"Ese Alumno ya está dado de alta para ese dni y tipo de permiso en el registro {alumno_existente.num_registro}")
            return


        nombre = input("Ingrese el nombre del Alumno: ")
        primer_apellido = input("Ingrese el primer apellido del Alumno: ")
        segundo_apellido = input("Ingrese el segundo apellido del Alumno: ")
        fecha_nacimiento = validar_fecha("Ingrese fecha nacimiento del Alumno: ")

        fecha_registro = validar_fecha("Ingrese la fecha de registro (DD/MM/AAAA): ")



        persona = Persona(alumno_dni, nombre, primer_apellido, segundo_apellido,fecha_nacimiento)

        year = fecha_registro.split('/')[2]
        num_registro = f"{year}/{len(alumnos) + 1:04d}"

        nuevo_registro = Alumno(nombre, primer_apellido, segundo_apellido, alumno_dni, fecha_nacimiento, fecha_registro, num_registro, permiso_opta)
        alumnos.append(nuevo_registro)
        guardar_datos_generico('registros.json', alumnos)
        print("Registro añadido correctamente.")
    except Exception as e:
        print(f"Error al añadir nuevo registro: {e}")


def buscar_id_registros():
    return [registro.num_registro for registro in alumnos]


def editar_registro():
    try:
        ids_registros = buscar_id_registros()
        if not ids_registros:
            print(f"No hay profesores registros disponibles, crea uno primero.")
            return
        imprime_lista(ids_registros)
        indice_registro = obtener_indice_respuesta("Seleccione el registro: ", ids_registros)

        registro = alumnos[int(indice_registro) - 1]


        print(f"Editando registro: {registro.mostrar_datos_basicos()}")

        fecha_registro = input("Ingrese la nueva fecha de registro (vacío para no modificar): ")
        year = fecha_registro.split('/')[2]
        num_registro = f"{year}/{int(indice_registro):04d}"

        permisos_disponibles = [permiso.tipo_permiso for permiso in permisos]
        print(f"Tipos de permiso disponibles:{permisos_disponibles}")
        permiso = solicitar_tipo_permiso()
        permiso_opta = permiso.tipo_permiso

        '''profesor_dni = input("Ingrese el nuevo DNI del profesor (vacío para no modificar): ")
        profesor = buscar_profesor(profesor_dni)
        if not profesor:
            print(f"No se encontró un profesor con DNI {profesor_dni}.")
            return
        registro.profesor = profesor

        '''
        registro.fecha_registro = fecha_registro
        registro.permiso_opta = permiso_opta
        registro.num_registro = num_registro
        guardar_datos_generico('registros.json', alumnos)
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
    for alumno in alumnos:
        print(alumno.mostrar_datos_basicos())

def buscar_registro(alumno_dni):
    for registro in alumnos:
        if registro.persona.dni == alumno_dni:
            return registro
    return None

def buscar_profesor(dni):
    for profesor in profesores:
        if profesor.dni == dni:
            return profesor
    return None

def mostrar_submenu_profesores():
    print("Gestión de Profesores")
    print("1. Registrar Profesor")
    print("2. Editar Profesor")
    print("3. Consultar Profesor")
    print("4. Listar todos los Profesores")
    print("5. Volver al Menú Principal")

def gestionar_profesores():
    while True:
        mostrar_submenu_profesores()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_profesor()
        elif opcion == "2":
            editar_profesor()
        elif opcion == "3":
            consultar_profesor()
        elif opcion == "4":
            listar_profesores()
        elif opcion == "5":
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

def registrar_profesor():
    try:
        dni = ""
        valido = False
        while not valido:
            dni = input("Ingrese el DNI del profesor: ")
            if valida_profesor(dni):
                print(f"El profesor con DNI {dni} ya está registrado.")
            else:
                valido = True
        nombre = input("Ingrese el nombre del profesor: ")
        apellido_1 = input("Ingrese el primer apellido del profesor: ")
        apellido_2 = input("Ingrese el segundo apellido del profesor: ")
        nuevo_profesor = Profesor(dni, nombre, apellido_1, apellido_2)
        profesores.append(nuevo_profesor)
        guardar_datos_generico('profesores.json', profesores)
        print(f"Profesor {nombre} con DNI {dni} registrado.")
    except Exception as e:
        print(f"Error al registrar profesor: {e}")

def mostrar_submenu_editar_profesor():
    print("Editar Profesor")
    print("1. Editar Nombre")
    print("2. Editar Primer Apellido")
    print("3. Editar Segundo Apellido")
    print("4. Añadir Permiso")
    print("0. Volver al Menú Anterior")

def editar_profesor():
    dni = input("Ingrese el DNI del profesor a editar: ")
    profesor = buscar_profesor(dni)
    if profesor:
        print(f"Profesor encontrado: {profesor.to_string()}")
        while True:
            mostrar_submenu_editar_profesor()
            opcion = input("Seleccione el dato a editar: ")
            if opcion == "1":
                nuevo_nombre = input("Ingrese el nuevo nombre del profesor: ")
                profesor.nombre = nuevo_nombre
            elif opcion == "2":
                nuevo_apellido1 = input("Ingrese el nuevo primer apellido del profesor: ")
                profesor.apellido_1 = nuevo_apellido1
            elif opcion == "3":
                nuevo_apellido2 = input("Ingrese el nuevo segundo apellido del profesor: ")
                profesor.apellido_2 = nuevo_apellido2
            elif opcion == "4":
                while True:
                    tipo_permiso = input("Ingrese el tipo de permiso (o 0 para volver): ")
                    if tipo_permiso == "0":
                        break
                    permiso = buscar_permiso(tipo_permiso)
                    if permiso:
                        profesor.agregar_permiso(permiso)
                        print(f"Permiso {tipo_permiso} añadido al profesor.")
                    else:
                        print(f"No se encontró un permiso de tipo {tipo_permiso}.")
            elif opcion == "0":
                print("Volviendo al menú anterior...")
                break
            else:
                print("Opción no válida, por favor intente de nuevo.")
            guardar_datos_generico('profesores.json', profesores)
            print("Profesor actualizado correctamente.")
    else:
        print(f"No se encontró un profesor con DNI {dni}.")

def consultar_profesor():
    dni = input("Ingrese el DNI del profesor a consultar: ")
    profesor = buscar_profesor(dni)
    if profesor:
        print(f"Profesor encontrado: {profesor.to_string()}")
    else:
        print(f"No se encontró un profesor con DNI {dni}.")

def listar_profesores():
    for profesor in profesores:
        print(profesor.mostrar_datos())

def valida_profesor(dni):
    for profesor in profesores:
        if profesor.dni == dni:
            return True
    return False

def mostrar_menu():
    print("Menú Principal")
    print("1. Gestionar Registros")
    print("2. Gestionar Alumnos")
    print("3. Gestionar Profesores")
    print("4. Registrar Clase")
    print("5. Registrar Anticipo")
    print("6. Generar Factura")
    print("0. Salir")


alumnos = cargar_datos_generico('registros.json', Alumno)
#alumnos = cargar_datos_generico('alumnos.json', Alumno)
permisos = cargar_datos_generico('permisos.json', Permiso)
profesores = cargar_datos_generico('profesores.json', Profesor)
vehiculos = cargar_datos('vehiculos.json')
clases = cargar_datos('clases.json')
anticipos = cargar_datos('anticipos.json')
facturas = cargar_datos('facturas.json')


for profesor in profesores:
    print(profesor.mostrar_datos())

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            gestionar_registros()
        elif opcion == "2":
            gestionar_alumnos()
        elif opcion == "3":
            gestionar_profesores()
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