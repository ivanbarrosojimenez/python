# Proyecto de Gestión de Auto Escuela

Este proyecto es una aplicación de gestión de una autoescuela desarrollada en Python. Permite registrar alumnos, profesores, clases, permisos, anticipos y generar facturas en formato PDF.

## Autor

Iván Barroso Jiménez

## Repositorio

El código fuente del proyecto está disponible en GitHub en la siguiente URL: [https://github.com/ivanbarrosojimenez/python.git](https://github.com/ivanbarrosojimenez/python.git)

## Funcionalidades

- Gestión de registros de alumnos
- Gestión de profesores
- Gestión de clases
- Gestión de permisos
- Gestión de anticipos
- Generación de facturas en formato PDF

## Requisitos

- Python 3.x
- Librerías: `fpdf`, `os`, `json`, `re`

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/ivanbarrosojimenez/python.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd python
    ```
3. Instala las dependencias:
    ```bash
    pip install fpdf
    ```

## Uso

Para ejecutar la aplicación, simplemente ejecuta el archivo `Main.py`:
```bash
python Main.py
```

## Estructura del Proyecto

- `Main.py`: Archivo principal que contiene la lógica de la aplicación.
- `Clase.py`, `Alumno.py`, `Factura.py`, `GeneradorPDF.py`, `Permiso.py`, `Profesor.py`, `Anticipo.py`, `Vehiculo.py`: Archivos que contienen las clases utilizadas en el proyecto.
- `json/`: Carpeta donde se almacenan los archivos JSON con los datos de la aplicación.
- `pdf/`: Carpeta donde se almacenan los archivos PDF generados

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request en el repositorio de GitHub.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.