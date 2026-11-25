# Guardado y carga de datos en archivos binarios y archivos de texto.

# Importación de módulos para gestionar archivos y datos del sistema.
import json
import os
import pickle
import datos

# Reúne los datos de los expedientes en un diccionario para su almacenamiento.
def obtener_datos():
    return {
        "codigos": datos.codigos, "tiposDoc": datos.tiposDoc,
        "numerosDoc": datos.numerosDoc, "nombresExp": datos.nombresExp,
        "correos": datos.correos, "telefonos": datos.telefonos,
        "tiposTramite": datos.tiposTramite, "asuntos": datos.asuntos,
        "areasDestino": datos.areasDestino, "fechas": datos.fechas,
        "horas": datos.horas, "estados": datos.estados,
        "foliosExp": datos.foliosExp, "contador": datos.contador
    }

# Restaura la información recuperada de un archivo en las variables del sistema.
def aplicar_datos(informacion):

    # Utiliza listas vacías como valores predeterminados si faltan datos.
    datos.codigos = informacion.get("codigos", [])
    datos.tiposDoc = informacion.get("tiposDoc", [])
    datos.numerosDoc = informacion.get("numerosDoc", [])
    datos.nombresExp = informacion.get("nombresExp", [])
    datos.correos = informacion.get("correos", [])
    datos.telefonos = informacion.get("telefonos", [])
    datos.tiposTramite = informacion.get("tiposTramite", [])
    datos.asuntos = informacion.get("asuntos", [])
    datos.areasDestino = informacion.get("areasDestino", [])
    datos.fechas = informacion.get("fechas", [])
    datos.horas = informacion.get("horas", [])
    datos.estados = informacion.get("estados", [])
    datos.foliosExp = informacion.get("foliosExp", [])

    # Recupera el contador o utiliza la cantidad de códigos registrados.
    datos.contador = informacion.get("contador", len(datos.codigos))

# Guarda los datos del sistema en un archivo binario mediante pickle.
def guardar_binario():
    try:
        # Abre el archivo en modo de escritura binaria.
        with open(datos.ARCHIVO_BINARIO, "wb") as archivo:
            pickle.dump(obtener_datos(), archivo)
        print(f"Datos guardados correctamente en '{datos.ARCHIVO_BINARIO}'.")

    # Controla posibles errores durante el guardado.
    except OSError as error:
        print("No se pudieron guardar los datos:", error)

# Recupera los expedientes almacenados en el archivo binario.
def cargar_binario():

    # Verifica que el archivo exista antes de intentar abrirlo.
    if not os.path.exists(datos.ARCHIVO_BINARIO):
        print(f"No existe el archivo '{datos.ARCHIVO_BINARIO}'.")
        return
    try:
        # Lee y recupera la información del archivo binario.
        with open(datos.ARCHIVO_BINARIO, "rb") as archivo:
            informacion = pickle.load(archivo)

        # Restaura los datos recuperados en las variables del sistema.
        aplicar_datos(informacion)
        print(f"Se cargaron {datos.contador} expediente(s) desde el archivo binario.")

    # Controla posibles errores de lectura o recuperación de datos.
    except (OSError, pickle.PickleError, EOFError, AttributeError, ValueError, TypeError) as error:
        print("No se pudieron cargar los datos binarios:", error)

# Guarda los expedientes en un archivo de texto con formato JSON.
def guardar_plano():
    try:
        # Utiliza UTF-8 para conservar los caracteres especiales y las tildes.
        with open(datos.ARCHIVO_PLANO, "w", encoding="utf-8") as archivo:
            json.dump(obtener_datos(), archivo, ensure_ascii=False, indent=4)
        print(f"Datos guardados correctamente en '{datos.ARCHIVO_PLANO}'.")

    # Controla posibles errores durante la escritura del archivo.
    except OSError as error:
        print("No se pudieron guardar los datos:", error)

# Recupera los expedientes almacenados en el archivo de texto.
def cargar_plano():

    # Comprueba la existencia del archivo antes de realizar la lectura.
    if not os.path.exists(datos.ARCHIVO_PLANO):
        print(f"No existe el archivo '{datos.ARCHIVO_PLANO}'.")
        return
    try:
        # Lee el contenido del archivo y lo convierte en datos de Python.
        with open(datos.ARCHIVO_PLANO, "r", encoding="utf-8") as archivo:
            informacion = json.load(archivo)

        # Actualiza las variables del sistema con la información recuperada.
        aplicar_datos(informacion)
        print(f"Se cargaron {datos.contador} expediente(s) desde el archivo plano.")

    # Controla errores de lectura, formato JSON o tipos de datos.
    except (OSError, json.JSONDecodeError, TypeError, ValueError) as error:
        print("No se pudieron cargar los datos del archivo plano:", error)
