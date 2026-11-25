# Mesa de Partes Digital - EsSalud

Prototipo de consola en Python. Permite registrar, buscar y ordenar expedientes, además de guardar y cargar información desde un archivo binario y un archivo de texto.

## Archivos del proyecto

- `main.py`: menú principal y navegación.
- `datos.py`: arreglos paralelos, contador y nombres de archivos.
- `validaciones.py`: validación de documento, teléfono, correo, fecha y hora.
- `expedientes.py`: registro, visualización, búsqueda y ordenamiento.
- `archivos.py`: carga y guardado de los datos.

### Instalación de dependencias

Antes de ejecutar el proyecto, instala las dependencias necesarias.

1. Abre una terminal en la carpeta principal del proyecto.
2. Ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```

Este comando instala automáticamente las bibliotecas especificadas en el archivo `requirements.txt`.

## Ejecución

Con Python instalado, abre una terminal y ejecuta:

```bash
python main.py
```

En Windows también puedes utilizar `py main.py`.

### Pruebas automáticas

El archivo `test_validaciones.py` contiene pruebas automatizadas desarrolladas con la biblioteca `unittest` de Python. Su propósito es comprobar el correcto funcionamiento de las funciones de validación de datos, como nombres, documentos, teléfonos, correos electrónicos, fechas y horas.

Para ejecutar las pruebas, utiliza el siguiente comando desde la carpeta principal del proyecto:

```bash
python -m unittest -v test_validaciones.py
```

El resultado permite identificar si las validaciones funcionan correctamente o si existen errores que deben corregirse.

Los archivos `expedientes.dat` y `expedientes.txt` se crean cuando se guardan datos. No se incluyen en el repositorio porque contienen información de los registros de prueba.