# Guardado y carga de datos en archivos binarios y archivos de texto.
import json
import os
import pickle
import datos

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

def aplicar_datos(informacion):
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
    datos.contador = informacion.get("contador", len(datos.codigos))

def guardar_binario():
    try:
        with open(datos.ARCHIVO_BINARIO, "wb") as archivo:
            pickle.dump(obtener_datos(), archivo)
        print(f"Datos guardados correctamente en '{datos.ARCHIVO_BINARIO}'.")
    except OSError as error:
        print("No se pudieron guardar los datos:", error)

def cargar_binario():
    if not os.path.exists(datos.ARCHIVO_BINARIO):
        print(f"No existe el archivo '{datos.ARCHIVO_BINARIO}'.")
        return
    try:
        with open(datos.ARCHIVO_BINARIO, "rb") as archivo:
            informacion = pickle.load(archivo)
        aplicar_datos(informacion)
        print(f"Se cargaron {datos.contador} expediente(s) desde el archivo binario.")
    except (OSError, pickle.PickleError, EOFError, AttributeError, ValueError, TypeError) as error:
        print("No se pudieron cargar los datos binarios:", error)

def guardar_plano():
    try:
        with open(datos.ARCHIVO_PLANO, "w", encoding="utf-8") as archivo:
            json.dump(obtener_datos(), archivo, ensure_ascii=False, indent=4)
        print(f"Datos guardados correctamente en '{datos.ARCHIVO_PLANO}'.")
    except OSError as error:
        print("No se pudieron guardar los datos:", error)

def cargar_plano():
    if not os.path.exists(datos.ARCHIVO_PLANO):
        print(f"No existe el archivo '{datos.ARCHIVO_PLANO}'.")
        return
    try:
        with open(datos.ARCHIVO_PLANO, "r", encoding="utf-8") as archivo:
            informacion = json.load(archivo)
        aplicar_datos(informacion)
        print(f"Se cargaron {datos.contador} expediente(s) desde el archivo plano.")
    except (OSError, json.JSONDecodeError, TypeError, ValueError) as error:
        print("No se pudieron cargar los datos del archivo plano:", error)