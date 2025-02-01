
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

#Gestion principal:
def mostrar_menu():
    #TODO Añadir info básica

    imprime_formato_menu("Menú Principal" )
    imprime_formato_menu("1. Gestionar Registros")
    imprime_formato_menu("2. Gestionar Alumnos")
    imprime_formato_menu("3. Gestionar Profesores")
    imprime_formato_menu("4. Registrar Clase")
    imprime_formato_menu("5. Registrar Anticipo")
    imprime_formato_menu("6. Generar Factura")
    imprime_formato_menu("0. Salir")
    print(f"")



#Gestion de registros:
def mostrar_submenu_registros():
    imprime_formato_menu("Gestión de Registros", 1)
    imprime_formato_menu("1. Alta Registro", 1)
    imprime_formato_menu("2. Editar Registro", 1)
    imprime_formato_menu("3. Consultar Registro", 1)
    imprime_formato_menu("4. Listar todos los registros", 1)
    imprime_formato_menu("0. Volver al Menú Principal", 1)
    print(f"")

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
        elif opcion == "0":
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

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



        #persona = Persona(alumno_dni, nombre, primer_apellido, segundo_apellido,fecha_nacimiento)

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
            print(f"No hay Registros disponibles, crea uno primero.")
            return
        imprime_lista(ids_registros)
        indice_registro = obtener_indice_respuesta("Seleccione el registro: ", ids_registros)

        registro = alumnos[int(indice_registro) - 1]


        print(f"{registro.mostrar_datos_editar()}")


        while True:
            print(f"{registro.mostrar_datos_editar()}")
            opcion = input("Número de dato a editar (0 para salir): ")

            if opcion == "0":
                print("Saliendo de la edición...")
                break
            elif opcion == "1":
                fecha_registro = validar_fecha("Ingrese la nueva fecha de registro (DD/MM/AAAA): ")
                registro.fecha_registro = fecha_registro
                year = fecha_registro.split('/')[2]
                num_registro = f"{year}/{int(indice_registro):04d}"
                registro.num_registro = num_registro
            elif opcion == "2":
                permisos_disponibles = [permiso.tipo_permiso for permiso in permisos]
                print(f"Tipos de permiso disponibles:{permisos_disponibles}")
                permiso = solicitar_tipo_permiso()
                registro.permiso_opta = permiso.tipo_permiso
            elif opcion == "3":
                nuevo_nombre = input("Ingrese el nuevo nombre del alumno: ")
                registro.nombre = nuevo_nombre
            elif opcion == "4":
                nuevo_apellido1 = input("Ingrese el nuevo primer apellido del alumno: ")
                registro.primer_apellido = nuevo_apellido1
            elif opcion == "5":
                nuevo_apellido2 = input("Ingrese el nuevo segundo apellido del alumno: ")
                registro.segundo_apellido = nuevo_apellido2
            elif opcion == "6":
                nuevo_dni = solicitar_dni("Ingrese el nuevo DNI del alumno: ")
                registro.dni = nuevo_dni
            elif opcion == "7":
                nueva_fecha_nacimiento = validar_fecha("Ingrese la nueva fecha de nacimiento del alumno: ")
                registro.fecha_nacimiento = nueva_fecha_nacimiento
            else:
                print("Opción no válida, por favor intente de nuevo.")

            guardar_datos_generico('registros.json', alumnos)
            print("Registro actualizado correctamente.")
    except Exception as e:
        print(f"Error al editar registro: {e}")












    '''    fecha_registro = input("Número de dato a editar: ")


        year = fecha_registro.split('/')[2]
        num_registro = f"{year}/{int(indice_registro):04d}"

        permisos_disponibles = [permiso.tipo_permiso for permiso in permisos]
        print(f"Tipos de permiso disponibles:{permisos_disponibles}")
        permiso = solicitar_tipo_permiso()
        permiso_opta = permiso.tipo_permiso

        ''' '''
        profesor_dni = input("Ingrese el nuevo DNI del profesor (vacío para no modificar): ")
        profesor = buscar_profesor(profesor_dni)
        if not profesor:
            print(f"No se encontró un profesor con DNI {profesor_dni}.")
            return
        registro.profesor = profesor

        ''' '''
        registro.fecha_registro = fecha_registro
        registro.permiso_opta = permiso_opta
        registro.num_registro = num_registro
        guardar_datos_generico('registros.json', alumnos)
        print("Registro actualizado correctamente.")
    except Exception as e:
        print(f"Error al editar registro: {e}")
    '''
def consultar_registro():
    ids_registros = buscar_id_registros()
    if not ids_registros:
        print(f"No hay Registros disponibles, crea uno primero.")
        return
    imprime_lista(ids_registros)
    indice_registro = obtener_indice_respuesta("Seleccione el registro: ", ids_registros)

    registro = alumnos[int(indice_registro) - 1]


    print(f"{registro.mostrar_datos_basicos()}")

def listar_registros():
    for alumno in alumnos:
        print(alumno.mostrar_datos_basicos())

#Gestion de alumnos:


def imprime_formato_menu(texto, subnivel=0, ancho=50,):
    espacios = ' '*(subnivel*2)
    texto_formateado = f"{espacios}[  {texto:<{ancho - 4}}]"
    print(texto_formateado)

def mostrar_submenu_alumnos():
    imprime_formato_menu("Gestión de Alumnos")
    imprime_formato_menu("1. Editar Alumno")
    imprime_formato_menu("2. Consultar Alumno")
    imprime_formato_menu("3. Listar todos los Alumnos")
    imprime_formato_menu("0. Volver al Menú Principal")

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


def mostrar_info_personas(registros):
    for i, persona in enumerate(registros, start=1):
        print(f"{i}. {persona.dni} - {persona.nombre} {persona.primer_apellido} {persona.segundo_apellido}")
    if not registros:
        print("No hay alumnos registrados.")

def mostrar_info_gastos_combustible_profesor(profesor):
    for i, (fecha, coste) in enumerate(profesor.gastos_combustible.items(), start=1):
        print(f"{i}. {fecha}: {coste}€")
    if not profesor.gastos_combustible:
        print("No hay gastos registrados.")


def editar_alumno():
    alumnos_disponibles= buscar_registros()
    mostrar_info_personas(registro for registro in alumnos_disponibles)
    indice_alumno = obtener_indice_respuesta("Ingrese el número de Alumno a editar: ", alumnos_disponibles)
    alumno = alumnos[int(indice_alumno) - 1]


    #print(f"-----------------")
    #print(f"Editando Alumno: {alumno.dni} - {alumno.nombre} {alumno.primer_apellido} {alumno.segundo_apellido}")

    while True:
        print(f"{alumno.mostrar_datos_editar_avanzado()}")
        print(f"|  0. Volver al menú Principal  \n")
        opcion = input("Seleccione el dato a editar: ")
        if opcion == "1":
            nuevo_domicilio = input("Ingrese el nuevo domicilio del alumno: ")
            alumno.domicilio = nuevo_domicilio
        elif opcion == "2":
            nuevo_municipio = input("Ingrese el nuevo municipio del alumno: ")
            alumno.municipio = nuevo_municipio
        elif opcion == "3":
            nueva_provincia = input("Ingrese la nueva provincia del alumno: ")
            alumno.provincia = nueva_provincia
        elif opcion == "4":
            nuevo_telefono1 = input("Ingrese el nuevo teléfono 1 del alumno: ")
            alumno.telefono1 = nuevo_telefono1
        elif opcion == "5":
            nuevo_telefono2 = input("Ingrese el nuevo teléfono 2 del alumno: ")
            alumno.telefono2 = nuevo_telefono2
        elif opcion == "6":
            nuevo_correo = input("Ingrese el nuevo correo del alumno: ")
            alumno.correo = nuevo_correo
        elif opcion == "7":
            nuevo_num_clases = solicitar_entero("Ingrese el nuevo número de clases del alumno: ")
            alumno.num_clases = nuevo_num_clases
        elif opcion == "8":
            if not profesores:
                print(f"No hay profesores disponibles, da de alta primero un profesor para ese permiso")
                return
            imprime_disponibles(profesores)
            indice_profesor = obtener_indice_respuesta("Seleccione el profesor: ", profesores)
            profesor = profesores[int(indice_profesor) - 1]
            alumno.profesor = profesor.dni
        elif opcion == "9":
            #TODO IMPLEMENTAR
            break
        elif opcion == "10":
            #TODO IMPLEMENTAR
            break
        elif opcion == "11":
            #TODO IMPLEMENTAR
            break
        elif opcion == "0":
            print("Volviendo al menú anterior...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
        guardar_datos_generico('registros.json', alumnos)
        print("Alumno actualizado correctamente.")





'----------------- Bloque para gestion de profesores -----------------'
#Gestion profesores:

def mostrar_submenu_profesores():
    imprime_formato_menu("Gestión de Profesores",1)
    imprime_formato_menu("1. Registrar Profesor",1)
    imprime_formato_menu("2. Editar Profesor",1)
    imprime_formato_menu("3. Consultar Profesor",1)
    imprime_formato_menu("4. Listar todos los Profesores",1)
    imprime_formato_menu("0. Volver al Menú Principal",1)

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
        elif opcion == "0":
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

def registrar_profesor():
    try:

        profesor_dni = ''
        valido = False
        while not valido:
            profesor_dni = solicitar_dni("Ingrese el DNI del profesor: ")
            if existe_profesor(profesor_dni):
                print(f"El profesor con DNI {profesor_dni} ya está registrado.")
            else:
                valido = True
        nombre = input("Ingrese el nombre del profesor: ")
        apellido_1 = input("Ingrese el primer apellido del profesor: ")
        apellido_2 = input("Ingrese el segundo apellido del profesor: ")
        nuevo_profesor = Profesor(nombre, apellido_1, apellido_2, profesor_dni)
        profesores.append(nuevo_profesor)
        guardar_datos_generico('profesores.json', profesores)
        print(f"Profesor {nombre} con DNI {profesor_dni} registrado.")
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
    if not profesores:
        print(f"No hay profesores disponibles, da de alta primero un profesor para ese permiso")
        return
    imprime_disponibles(profesores)
    indice_profesor = obtener_indice_respuesta("Seleccione el profesor: ", profesores)
    profesor = profesores[int(indice_profesor) - 1]


    while True:
        print(f"{profesor.mostrar_info_editar_profesor()}")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            profesor_dni = ''
            valido = False
            while not valido:
                profesor_dni = solicitar_dni("Ingrese el DNI del profesor: ")
                if existe_profesor(profesor_dni):
                    print(f"El profesor con DNI {profesor_dni} ya está registrado.")
                else:
                    valido = True
            profesor.dni = profesor_dni
        elif opcion == "2":
            nombre = input("Ingrese el nombre del profesor: ")
            profesor.nombre = nombre
        elif opcion == "3":
            apellido_1 = input("Ingrese el primer apellido del profesor: ")
            profesor.primer_apellido = apellido_1
        elif opcion == "4":
            apellido_2 = input("Ingrese el segundo apellido del profesor: ")
            profesor.segundo_apellido = apellido_2
        elif opcion == "5":
            vehiculo = input("Ingrese el vehículo del profesor: ")
            profesor.vehiculo = vehiculo
        elif opcion == "6":
            tipo_vehiculo = input("Ingrese el tipo de vehículo del profesor: ")
            profesor.tipo_vehiculo = tipo_vehiculo
        elif opcion == "7":
            itv = validar_fecha("Ingrese la fecha de la ITV del vehículo del profesor: ")
            profesor.itv = itv
        elif opcion == "8":
            if not profesor.gastos_combustible:
                print("No hay gastos de combustible registrados.")
                continue
            mostrar_info_gastos_combustible_profesor(profesor)
            seleccion_combustible = obtener_indice_respuesta("Seleccione el gasto de combustible a editar: ", profesor.gastos_combustible)

            nueva_fecha = validar_fecha("Ingrese la nueva fecha del gasto de combustible: ")
            nuevo_coste = validar_float("Ingrese el nuevo coste del gasto de combustible: ")
            profesor.gastos_combustible.pop(list(profesor.gastos_combustible.keys())[int(seleccion_combustible) - 1])
            profesor.gastos_combustible[nueva_fecha] = nuevo_coste
        elif opcion == "9":
            nueva_fecha = validar_fecha("Ingrese la fecha del nuevo gasto de combustible: ")
            nuevo_coste = validar_float("Ingrese el coste del nuevo gasto de combustible: ")
            profesor.registrar_gasto_combustible(nueva_fecha, nuevo_coste)
        elif opcion == "0":
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
        guardar_datos_generico('profesores.json', profesores)
        print("Profesor actualizado correctamente.")

def consultar_profesor():
    if not profesores:
        print(f"No hay profesores disponibles, da de alta primero un profesor para ese permiso")
        return
    imprime_disponibles(profesores)
    indice_profesor = obtener_indice_respuesta("Seleccione el profesor: ", profesores)
    profesor = profesores[int(indice_profesor) - 1]

    print(f"{profesor.mostrar_info_profesor()}")

def listar_profesores():
    for profesor in profesores:
        print(profesor.mostrar_info_profesor())

def existe_profesor(dni):
    for profesor in profesores:
        if profesor.dni == dni:
            return True
    return False













def validar_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número decimal (separado por punto).")



def buscar_alumno(dni):
    for alumno in alumnos:
        if alumno.dni == dni:
            return alumno
    return None

def solicitar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

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
        print(alumno.mostrar_info_profesor())

def valida_alumno(dni):
    for alumno in alumnos:
        if alumno.dni == dni:
            return True
    return False

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

def buscar_profesores():
    return [profesor for profesor in profesores]


def buscar_alumnos():
    return [registro.persona for registro in alumnos]

def buscar_registros():
    return [registro for registro in alumnos]


def imprime_disponibles(profesores_disponibles):
    for i, p in enumerate(profesores_disponibles, start=1):
        print(f"{i}. {p.dni} {p.nombre} {p.primer_apellido} {p.segundo_apellido}")
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


def obtener_indice_respuesta(param, lista):
    while True:
        indice_profesor = input(param)
        if indice_profesor.isdigit() and 1 <= int(indice_profesor) <= len(lista):
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


alumnos = cargar_datos_generico('registros.json', Alumno)
#alumnos = cargar_datos_generico('alumnos.json', Alumno)
permisos = cargar_datos_generico('permisos.json', Permiso)
profesores = cargar_datos_generico('profesores.json', Profesor)
vehiculos = cargar_datos('vehiculos.json')
clases = cargar_datos('clases.json')
anticipos = cargar_datos('anticipos.json')
facturas = cargar_datos('facturas.json')


for profesor in profesores:
    print(profesor.mostrar_info_profesor())

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