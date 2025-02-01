
import json
import os
import re

from feedback2.Clase import Clase
from feedback2.Alumno import Alumno
from feedback2.Factura import Factura
from feedback2.GeneradorPDF import GeneradorPDF

from feedback2.Permiso import Permiso
from feedback2.Profesor import Profesor
from feedback2.Anticipo import Anticipo
from feedback2.Vehiculo import Vehiculo


#Gestion principal:
def mostrar_menu():
    print(f"Información básica: Las fechas son en formato DD/MM/AAAAA")
    print(f"")
    imprime_formato_menu("Menú Principal" )
    imprime_formato_menu("1. Gestionar Registros")
    imprime_formato_menu("2. Gestionar Alumnos")
    imprime_formato_menu("3. Gestionar Profesores")
    imprime_formato_menu("4. Gestionar Clases")
    imprime_formato_menu("5. Gestionar Permisos")
    imprime_formato_menu("6. Gestionar Anticipos")
    imprime_formato_menu("7. Generar Factura")
    imprime_formato_menu("0. Salir")
    print(f"")



#Gestion de registros:
def mostrar_submenu_registros():
    print(f"")
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

        alumno_existente = buscar_alumno_por_dni_y_permiso(alumno_dni, permiso_opta)
        if alumno_existente:
            print(f"Ese Alumno ya está dado de alta para ese dni y tipo de permiso en el registro {alumno_existente.num_registro}")
            return


        nombre = input("Ingrese el nombre del Alumno: ")
        primer_apellido = input("Ingrese el primer apellido del Alumno: ")
        segundo_apellido = input("Ingrese el segundo apellido del Alumno: ")
        fecha_nacimiento = validar_fecha("Ingrese fecha nacimiento del Alumno: ")

        fecha_registro = validar_fecha("Ingrese la fecha de registro (DD/MM/AAAA): ")

        year = fecha_registro.split('/')[2]
        num_registro = f"{year}/{len(alumnos) + 1:04d}"

        nuevo_registro = Alumno(nombre, primer_apellido, segundo_apellido, alumno_dni, fecha_nacimiento, fecha_registro, num_registro, permiso_opta)
        alumnos.append(nuevo_registro)
        guardar_datos_generico('json/registros.json', alumnos)
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

            guardar_datos_generico('json/registros.json', alumnos)
            print("Registro actualizado correctamente.")
    except Exception as e:
        print(f"Error al editar registro: {e}")


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

def mostrar_clase_con_indice(clases):
    for i, clase in enumerate(clases, start=1):
        print(f"\n  | Clase {i}.\n {clase.mostrar_info_clase()}")
    if not clase:
        print("No hay alumnos registrados.")

def mostrar_persona_con_indice(registros):
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
    mostrar_persona_con_indice(registro for registro in alumnos_disponibles)
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
            nuevo_examen = validar_fecha("Introduce fecha:")
            alumno.examenes_teoricos.append(nuevo_examen);
            print(f"Añadido correctamente.")
        elif opcion == "10":
            nuevo_examen = validar_fecha("Introduce fecha:")
            alumno.examenes_circulacion.append(nuevo_examen)
            print(f"Añadido correctamente.")
        elif opcion == "0":
            print("Volviendo al menú anterior...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
        guardar_datos_generico('json/registros.json', alumnos)
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
        guardar_datos_generico('json/profesores.json', profesores)
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
        guardar_datos_generico('json/profesores.json', profesores)
        print("Profesor actualizado correctamente.")

def consultar_profesor():
    if not profesores:
        print(f"No hay profesores disponibles, da de alta primero un profesor para ese permiso")
        return
    imprime_disponibles(profesores)
    indice_profesor = obtener_indice_respuesta("Seleccione el profesor: ", profesores)
    profesor = profesores[int(indice_profesor) - 1]

    print(f"{profesor.mostrar_info()}")

def listar_profesores():
    for profesor in profesores:
        print(profesor.mostrar_info())

def existe_profesor(dni):
    for profesor in profesores:
        if profesor.dni == dni:
            return True
    return False

''' ------------ Bloque para gestion de clases ---------------'''


def mostrar_submenu_clases():
    imprime_formato_menu("Gestión de Clases", 1)
    imprime_formato_menu("1. Registrar Clase", 1)
    imprime_formato_menu("2. Editar Clase", 1)
    imprime_formato_menu("3. Consultar Clases", 1)
    imprime_formato_menu("4. Listar Clases", 1)
    imprime_formato_menu("0. Volver al Menú Principal", 1)


def buscar_clases():
    for i in range(len(clases)):
        print(f"{i+1}. {clases[i].mostrar_info_clase()}")


def mostrar_clases(clases_disponibles):
    for i in range(len(clases_disponibles)):
        print(f"{i+1}. {clases_disponibles[i].mostrar_info_clase()}")


def editar_clase():
    mostrar_clase_con_indice(clases)
    indice_clase = obtener_indice_respuesta("Seleccione la clase a editar: ", clases)
    clase = clases[int(indice_clase) - 1]

    while True:
        print(f"{clase.mostrar_info_editar_clase()}")
        print(f"  0. Volver al menú anterior")
        print(f"  ----------------------------------------------\n")
        opcion = input("Seleccione el dato a editar: ")
        if opcion == "1":
            alumnos_disponibles = buscar_registros()
            mostrar_persona_con_indice(alumnos_disponibles)
            indice_alumno = obtener_indice_respuesta("Ingrese el número de Alumno para añadir a Clase: ", alumnos_disponibles)
            alumno = alumnos[int(indice_alumno) - 1]
            clase.alumno = alumno.dni
        elif opcion == "2":
            if not profesores:
                print(f"No hay profesores disponibles, da de alta primero un profesor para ese permiso")
                return
            imprime_disponibles(profesores)
            indice_profesor = obtener_indice_respuesta("Seleccione el profesor: ", profesores)
            profesor = profesores[int(indice_profesor) - 1]
            clase.profesor = profesor.dni
        elif opcion == "3":
            fecha = validar_fecha("Ingrese la fecha de la clase (DD/MM/AAAA): ")
            hora = validar_hora("Ingrese la hora de la clase (HH:MM): ")
            fecha_hora = f"{fecha} {hora}"
            clase.fecha_hora = fecha_hora
        elif opcion == "0":
            print("Volviendo al menú anterior...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
        guardar_datos_generico('json/clases.json', clases)
        print("Clase actualizada correctamente.")


def consultar_clase():
    while True:
        print("\n----------------------------------------------")
        print("|  Consultar Clases")
        print("|  1. Por Profesor (DNI)")
        print("|  2. Por Alumno (DNI)")
        print("|  3. Por Fecha")
        print("|  0. Volver al Menú Anterior")
        print("----------------------------------------------\n")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            profesores_disponibles = buscar_profesores()
            imprime_disponibles(profesores_disponibles)
            indice_profesor = obtener_indice_respuesta("Seleccione el profesor: ", profesores_disponibles)
            profesor = profesores_disponibles[int(indice_profesor) - 1]

            dni_profesor = profesor.dni
            clases_profesor = [clase for clase in clases if clase.profesor == dni_profesor]
            if(not clases_profesor):
                print(f"\nNo hay clases para ese profesor.\n")
                return
            print(f"\nClases del profesor {profesor.nombre} {profesor.primer_apellido} {profesor.segundo_apellido} [{profesor.dni}]:")
            mostrar_clases(clases_profesor)
        elif opcion == "2":
            alumnos_disponibles = buscar_registros()
            mostrar_persona_con_indice(alumnos_disponibles)
            indice_alumno = obtener_indice_respuesta("Seleccione el alumno: ", alumnos_disponibles)
            alumno = alumnos_disponibles[int(indice_alumno) - 1]

            dni_alumno = alumno.dni
            clases_alumno = [clase for clase in clases if clase.alumno == dni_alumno]
            if(not clases_alumno):
                print(f"\nNo hay clases para ese alumno.\n")
                return
            print(f"\nClases del alumno {alumno.nombre} {alumno.primer_apellido} {alumno.segundo_apellido} [{alumno.dni}]:")
            mostrar_clases(clases_alumno)

        elif opcion == "3":
            fecha = input("Ingrese la fecha (DD/MM/AAAA): ")
            clases_fecha = [clase for clase in clases if clase.fecha_hora.startswith(fecha)]
            if(not clases_fecha):
                print(f"\nNo hay clases para esa fecha.\n")
                return
            mostrar_clases(clases_fecha)
        elif opcion == "0":
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")


def listar_clases():
    for clase in clases:
        print(clase.mostrar_info_clase())


def gestionar_clases():
    while True:
        mostrar_submenu_clases()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_clase()
        elif opcion == "2":
            editar_clase()
        elif opcion == "3":
            consultar_clase()
        elif opcion == "4":
            listar_clases()
        elif opcion == "0":
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")


def validar_hora(param):
    while True:
        hora = input(param)
        if re.match(r"([01]?[0-9]|2[0-3]):[0-5][0-9]", hora):
            return hora
        print("Hora no válida. Por favor, introduzca una hora en formato HH:MM.")


def registrar_clase():
    try:
        alumnos_disponibles= buscar_registros()
        mostrar_persona_con_indice(registro for registro in alumnos_disponibles)
        indice_alumno = obtener_indice_respuesta("Ingrese el número de Alumno para añadir a Clase: ", alumnos_disponibles)
        alumno = alumnos[int(indice_alumno) - 1]

        if not profesores:
            print(f"No hay profesores disponibles, da de alta primero un profesor para ese permiso")
            return
        imprime_disponibles(profesores)
        indice_profesor = obtener_indice_respuesta("Seleccione el profesor: ", profesores)
        profesor = profesores[int(indice_profesor) - 1]

        fecha = validar_fecha("Ingrese la fecha de la clase (DD/MM/AAAA): ")
        hora = validar_hora("Ingrese la hora de la clase (HH:MM): ")

        dni_profesor = profesor.dni
        matricula_vehiculo = profesor.vehiculo
        fecha_hora = f"{fecha} {hora}"
        dni_alumno = alumno.dni

        clase = Clase(dni_alumno, dni_profesor, matricula_vehiculo, fecha_hora)

        clases.append(clase)
        guardar_datos_generico('json/clases.json', clases)
        clase.mostrar_info_clase()
    except Exception as e:
        print(f"Error al registrar clase: {e}")





''' ------------ Bloque para gestion de permisos ---------------'''


def mostrar_submenu_permisos():
    print(f"")
    imprime_formato_menu("Gestión de Permisos", 1)
    imprime_formato_menu("1. Registrar Permiso", 1)
    imprime_formato_menu("2. Editar Permiso", 1)
    imprime_formato_menu("3. Consultar Permiso", 1)
    imprime_formato_menu("4. Listar Permisos", 1)
    imprime_formato_menu("0. Volver al Menú Principal", 1)
    print(f"")


def existe_permiso(tipo_permiso):
    for permiso in permisos:
        if permiso.tipo_permiso == tipo_permiso:
            return True
    return False


def registrar_permiso():
    try:
        tipo_permiso = input("Ingrese el tipo de permiso: ")
        if existe_permiso(tipo_permiso):
            print(f"\nEl permiso {tipo_permiso} ya está registrado.\n")
            return
        precio_matricula = validar_float("Ingrese el precio de la matrícula: ")
        clases_incluidas = solicitar_entero("Ingrese el número de clases incluidas: ")
        precio_clase = validar_float("Ingrese el precio por clase: ")
        precio_examnen = validar_float("Ingrese el precio por examen: ")
        precio_renovacion = validar_float("Ingrese el precio por renovación: ")

        permiso = Permiso(tipo_permiso, precio_matricula, clases_incluidas, precio_clase, precio_examnen, precio_renovacion)

        permisos.append(permiso)
        guardar_datos_generico('json/permisos.json', permisos)
        print(f"Permiso {tipo_permiso} registrado.")
    except Exception as e:
        print(f"Error al registrar permiso: {e}")


def mostrar_permiso_con_indice(permisos):
    for i, permiso in enumerate(permisos, start=1):
        print(f"{i}. {permiso.tipo_permiso}")
    if not permisos:
        print("No hay permisos registrados.")


def editar_permiso():
    mostrar_permiso_con_indice(permisos)
    indice_permiso = obtener_indice_respuesta("Seleccione el permiso a editar: ", permisos)
    permiso = permisos[int(indice_permiso) - 1]

    while True:
        print(f"{permiso.mostrar_info_editar_permiso()}")
        print(f"  |  0. Volver al menú anterior")
        print(f"  ----------------------------------------------\n")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nuevo_tipo_permiso = input("Ingrese el nuevo tipo de permiso: ")
            if existe_permiso(nuevo_tipo_permiso):
                print(f"\nEl permiso {nuevo_tipo_permiso} ya está registrado.\n")
                return
            permiso.tipo_permiso = nuevo_tipo_permiso
        elif opcion == "2":
            nuevo_precio_matricula = validar_float("Ingrese el nuevo precio de la matrícula: ")
            permiso.precio_matricula = nuevo_precio_matricula
        elif opcion == "3":
            nuevo_clases_incluidas = solicitar_entero("Ingrese el nuevo número de clases incluidas: ")
            permiso.clases_incluidas = nuevo_clases_incluidas
        elif opcion == "4":
            nuevo_precio_clase = validar_float("Ingrese el nuevo precio por clase: ")
            permiso.precio_por_clase = nuevo_precio_clase
        elif opcion == "5":
            nuevo_precio_examen = validar_float("Ingrese el nuevo precio por examen: ")
            permiso.precio_examen = nuevo_precio_examen
        elif opcion == "6":
            nuevo_precio_renovacion = validar_float("Ingrese el nuevo precio por renovación: ")
            permiso.precio_renovacion = nuevo_precio_renovacion
        elif opcion == "0":
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
        guardar_datos_generico('json/permisos.json', permisos)


def consultar_permiso():
    mostrar_permiso_con_indice(permisos)
    indice_permiso = obtener_indice_respuesta("Seleccione el permiso a consultar: ", permisos)
    permiso = permisos[int(indice_permiso) - 1]

    print(f"{permiso.mostrar_info_permiso()}")


def listar_permisos():
    for permiso in permisos:
        print(permiso.mostrar_info_permiso())


def gestionar_permisos():
    while True:
        mostrar_submenu_permisos()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_permiso()
        elif opcion == "2":
            editar_permiso()
        elif opcion == "3":
            consultar_permiso()
        elif opcion == "4":
            listar_permisos()
        elif opcion == "0":
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")


''' ------------ Bloque para gestion de facturas ---------------'''


def mostrar_submenu_facturas():
    imprime_formato_menu("Gestión de Facturas", 1)
    imprime_formato_menu("1. Generar Factura", 1)
    imprime_formato_menu("2. Consultar Factura", 1)
    imprime_formato_menu("3. Listar Facturas", 1)
    imprime_formato_menu("4. Imprimir Factura", 1)
    imprime_formato_menu("0. Volver al Menú Principal", 1)


def obtener_precio_matricula(permiso_opta):
    for permiso in permisos:
        if permiso.tipo_permiso == permiso_opta:
            return permiso.precio_matricula
    return 0


def obtener_numero_clases_incluidas(permiso_opta):
    for permiso in permisos:
        if permiso.tipo_permiso == permiso_opta:
            return permiso.clases_incluidas
    return 0

def obtener_permiso_por_tipo(tipo_permiso):
    for permiso in permisos:
        if permiso.tipo_permiso == tipo_permiso:
            return permiso
    return None


def obtener_total_anticipos(dni):
    total_anticipos = 0
    for anticipo in anticipos:
        if anticipo.alumno == dni:
            total_anticipos += anticipo.cantidad
    return total_anticipos


def contar_clases_por_alumno(alumno_dni):
    num_clases = 0
    for clase in clases:
        if clase.alumno == alumno_dni:
            num_clases += 1
    return num_clases

def calcular_numero_renovaciones(examenes_teoricos, examenes_practicos):
    total_examenes = examenes_teoricos + examenes_practicos
    renovaciones = max(0, (total_examenes - 3) // 3)
    return renovaciones


def obtener_factura(dni, permiso_opta):
    for factura in facturas:
        if factura.alumno == dni and factura.permiso == permiso_opta:
            return factura
    return False


def registrar_factura():

    alumnos_disponibles = buscar_registros()
    mostrar_persona_con_indice(alumnos_disponibles)
    indice_alumno = obtener_indice_respuesta("Seleccione el alumno: ", alumnos_disponibles)
    alumno = alumnos_disponibles[int(indice_alumno) - 1]

    permiso = obtener_permiso_por_tipo(alumno.permiso_opta)

    factura = obtener_factura(alumno.dni, alumno.permiso_opta)
    if (factura):
        print(f"\nYa existe una factura para el alumno {alumno.nombre} {alumno.primer_apellido} {alumno.segundo_apellido}"
              f" y el permiso {alumno.permiso_opta}. Se va a actualizar la factura con los datos actuales.\n")
        facturas.remove(factura)

    alumno_dni = alumno.dni
    precio_matricula = permiso.precio_matricula
    num_clases_incluidas = permiso.clases_incluidas
    num_clases_dadas = contar_clases_por_alumno(alumno_dni)
    precio_clase = permiso.precio_por_clase
    numero_examenes = len(alumno.examenes_teoricos) + len(alumno._examenes_circulacion)
    precio_examen = permiso.precio_examen
    num_renovaciones = calcular_numero_renovaciones(len(alumno.examenes_teoricos), len(alumno._examenes_circulacion))
    precio_renovacion = permiso.precio_renovacion
    anticipos = obtener_total_anticipos(alumno.dni)

    factura = Factura(alumno_dni, precio_matricula, num_clases_incluidas, num_clases_dadas,precio_clase,numero_examenes,
                      precio_examen, num_renovaciones, precio_renovacion, anticipos, permiso.tipo_permiso)
    facturas.append(factura)
    guardar_datos_generico('json/facturas.json', facturas)

    print("\nFactura registrada correctamente.\n")
    print(f"{factura.generar_factura()}")


def mostrar_factura_con_indice(facturas):
    for i, factura in enumerate(facturas, start=1):
        print(f"{i}. {factura.alumno} { factura.permiso} {factura.calcular_total_con_iva()}€")
    if not facturas:
        print("No hay facturas registradas.")


def consutar_factura():
    mostrar_factura_con_indice(facturas)
    indice_factura = obtener_indice_respuesta("Seleccione la factura a consultar: ", facturas)
    factura = facturas[int(indice_factura) - 1]
    alumno = buscar_alumno(factura.alumno)

    print(f"{factura.generar_factura()}")


def listar_facturas():
    for factura in facturas:
        print(f"{factura.generar_factura()}")
    if not facturas:
        print("No hay facturas registradas.")


def obtener_clases_por_alumno(dni):
    clases_alumno = [clase for clase in clases if clase.alumno == dni]
    return clases_alumno

def imprimir_factura():
    mostrar_factura_con_indice(facturas)
    indice_factura = obtener_indice_respuesta("Seleccione la factura a imprimir: ", facturas)
    factura = facturas[int(indice_factura) - 1]
    alumno = buscar_alumno(factura.alumno)

    print(f"{factura.generar_factura()}")
    clases_alumno = obtener_clases_por_alumno(alumno.dni)
    # Ejemplo de uso:
    filename = f"{alumno.dni}_Permiso_{alumno.permiso_opta}.pdf"
    pdf_gen = GeneradorPDF(filename)
    pdf_gen.generar_factura(factura, alumno, clases_alumno)
1

def gestionar_facturas():
    while True:
        mostrar_submenu_facturas()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_factura()
        elif opcion == "2":
            consutar_factura()
        elif opcion == "3":
            listar_facturas()
        elif opcion == "4":
            imprimir_factura()
        elif opcion == "0":
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")



''' ------------ Bloque para gestion de anticipos ---------------'''


def mostrar_submenu_anticipos():
    imprime_formato_menu("Gestión de Anticipos", 1)
    imprime_formato_menu("1. Registrar Anticipo", 1)
    imprime_formato_menu("2. Editar Anticipo", 1)
    imprime_formato_menu("3. Consultar Anticipo", 1)
    imprime_formato_menu("4. Listar Anticipos", 1)
    imprime_formato_menu("0. Volver al Menú Principal", 1)


def listar_anticipos():
    for anticipo in anticipos:
        print(anticipo.mostrar_info_anticipo())
    if not anticipos:
        print("\nNo hay anticipos registrados.\n")

def registrar_anticipo():
    try:
        alumnos_disponibles = buscar_registros()
        mostrar_persona_con_indice(alumnos_disponibles)
        indice_alumno = obtener_indice_respuesta("Seleccione el alumno: ", alumnos_disponibles)
        alumno = alumnos_disponibles[int(indice_alumno) - 1]
        fecha = validar_fecha("Ingrese la fecha del anticipo (DD/MM/AAAA): ")
        concepto = input("Ingrese el concepto del anticipo: ")
        cantidad = validar_float("Ingrese la cantidad del anticipo: ")

        anticipo = Anticipo(alumno.dni, fecha, concepto, cantidad)
        anticipos.append(anticipo)
        guardar_datos_generico('json/anticipos.json', anticipos)

        print("Anticipo registrado correctamente.")
    except Exception as e:
        print(f"Error al registrar anticipo: {e}")


def mostrar_anticipo_con_indice(anticipos):
    for i, anticipo in enumerate(anticipos, start=1):
        print(f"{i}. {anticipo.mostrar_info_anticipo()}")
    if not anticipos:
        print("No hay anticipos registrados.")


def consultar_anticipo():
    mostrar_anticipo_con_indice(anticipos)
    indice_anticipo = obtener_indice_respuesta("Seleccione el anticipo a consultar: ", anticipos)
    anticipo = anticipos[int(indice_anticipo) - 1]
    alumno = buscar_alumno(anticipo.alumno)

    print(f"{anticipo.mostrar_info_anticipo_avanzado(alumno)}")


def editar_anticipo():
    mostrar_anticipo_con_indice(anticipos)
    indice_anticipo = obtener_indice_respuesta("Seleccione el anticipo a consultar: ", anticipos)
    anticipo = anticipos[int(indice_anticipo) - 1]

    while True:
        print(f"{anticipo.mostrar_info_editar_anticipo()}")
        print(f"  |  0. Volver al menú anterior")
        print(f"  ----------------------------------------------\n")
        opcion = input("Seleccione el dato a editar: ")
        if opcion == "1":
            alumnos_disponibles = buscar_registros()
            mostrar_persona_con_indice(alumnos_disponibles)
            indice_alumno = obtener_indice_respuesta("Seleccione el alumno: ", alumnos_disponibles)
            alumno = alumnos_disponibles[int(indice_alumno) - 1]
            anticipo.alumno = alumno.dni
        elif opcion == "2":
            nueva_fecha = validar_fecha("Ingrese la nueva fecha del anticipo (DD/MM/AAAA): ")
            anticipo.fecha = nueva_fecha
        elif opcion == "3":
            nuevo_concepto = input("Ingrese el nuevo concepto del anticipo: ")
            anticipo.concepto = nuevo_concepto
        elif opcion == "4":
            nueva_cantidad = validar_float("Ingrese la nueva cantidad del anticipo: ")
            anticipo.cantidad = nueva_cantidad
        elif opcion == "0":
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
        guardar_datos_generico('json/anticipos.json', anticipos)
        print("Anticipo actualizado correctamente.")


def gestionar_anticipos():
    while True:
        mostrar_submenu_anticipos()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_anticipo()
        elif opcion == "2":
            editar_anticipo()
        elif opcion == "3":
            consultar_anticipo()
        elif opcion == "4":
            listar_anticipos()
        elif opcion == "0":
            break



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

def buscar_alumno_por_dni_y_permiso(dni, tipo_permiso):
    for registro in alumnos:
        if registro.dni == dni and registro.tipo_permiso == tipo_permiso:
            return registro
    return None

def consultar_alumno():
    alumnos_disponibles= buscar_registros()
    mostrar_persona_con_indice(registro for registro in alumnos_disponibles)
    indice_alumno = obtener_indice_respuesta("Ingrese el número de Alumno a editar: ", alumnos_disponibles)
    alumno = alumnos[int(indice_alumno) - 1]

    print(f"{alumno.mostrar_datos_editar_avanzado()}")


def listar_alumnos():
    for alumno in alumnos:
        print(alumno.mostrar_info())

def valida_alumno(dni):
    for alumno in alumnos:
        if alumno.dni == dni:
            return True
    return False





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
        guardar_datos('json/facturas.json', facturas)
        factura.generar_factura()
    except Exception as e:
        print(f"Error al generar factura: {e}")

def guardar_datos(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def guardar_datos_generico(filename, datos):
    if not os.path.exists('json'):
        os.makedirs('json')

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
    if not os.path.exists('json'):
        os.makedirs('json')
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

'''Carga inicial de datos, si no existe nada no da error'''
alumnos = cargar_datos_generico('json/registros.json', Alumno)
permisos = cargar_datos_generico('json/permisos.json', Permiso)
profesores = cargar_datos_generico('json/profesores.json', Profesor)
vehiculos = cargar_datos_generico('json/vehiculos.json', Vehiculo)
clases = cargar_datos_generico('json/clases.json', Clase)
anticipos = cargar_datos_generico('json/anticipos.json', Anticipo)
facturas = cargar_datos_generico('json/facturas.json', Factura)


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
            gestionar_clases()
        elif opcion == "5":
            gestionar_permisos()
        elif opcion == "6":
            gestionar_anticipos()
        elif opcion == "7":
            gestionar_facturas()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()