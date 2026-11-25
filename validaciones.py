# Funciones de validación de los datos ingresados.

def es_numerico(cadena):
    """
    Comprueba que una cadena contenga únicamente números.
    """
    return len(cadena) > 0 and cadena.isdigit()

def nombre_valido(nombre):
    """
    Verifica que el nombre contenga únicamente letras
    y espacios, y que tenga como mínimo 3 letras.
    """
    nombre = nombre.strip()

    # Evita nombres vacíos.
    if not nombre:
        return False
    # Separa las palabras y elimina espacios repetidos.
    palabras = nombre.split()

    # Comprueba que todas las palabras tengan solo letras.
    if not all(palabra.isalpha() for palabra in palabras):
        return False

    # Comprueba que existan al menos 3 letras.
    cantidad_letras = sum(len(palabra) for palabra in palabras)

    return cantidad_letras >= 3

def formatear_nombres(nombre):
    """
    Organiza los nombres colocando la primera letra
    de cada palabra en mayúscula.
    """
    return " ".join(
        palabra.capitalize()
        for palabra in nombre.split()
    )

# Valida el número de documento según el tipo seleccionado.
def documento_valido(tipo, numero):
    tipo = tipo.upper()

    # Cada tipo de documento tiene diferentes requisitos de longitud y formato.
    if tipo == "DNI":
        return len(numero) == 8 and es_numerico(numero)
    elif tipo == "RUC":
        return len(numero) == 11 and es_numerico(numero) and numero[:2] in ("10", "20")
    elif tipo == "CE":
        return 1 <= len(numero) <= 11 and es_numerico(numero)
    elif tipo == "PASAPORTE":
        return 1 <= len(numero) <= 15 and numero.isalnum()

    # Rechaza los tipos de documento no reconocidos.
    return False

# Comprueba que el teléfono tenga 9 dígitos y comience con 9.
def telefono_valido(telefono):
    return len(telefono) == 9 and es_numerico(telefono) and telefono.startswith("9")

# Comprueba que el correo electrónico tenga un formato básico válido.
def correo_valido(correo):

    # Rechaza correos demasiado cortos, con espacios o con una cantidad incorrecta de arrobas.
    if len(correo) < 6 or " " in correo or correo.count("@") != 1:
        return False

    # Identifica la posición de la arroba y del último punto.
    posicion_arroba = correo.find("@")
    posicion_punto = correo.rfind(".")

    # Verifica que los elementos del correo estén ubicados correctamente.
    return (posicion_arroba > 0 and posicion_punto > posicion_arroba + 1
            and posicion_punto < len(correo) - 1)

# Valida el formato y los valores de una fecha de ingreso.
def fecha_valida(fecha):

    # Comprueba que la fecha respete el formato DD/MM/AAAA.
    if len(fecha) != 10 or fecha[2] != "/" or fecha[5] != "/":
        return False

    # Separa el día, el mes y el año.
    dia_texto, mes_texto, anio_texto = fecha[:2], fecha[3:5], fecha[6:10]

    # Verifica que los componentes de la fecha sean numéricos.
    if not (es_numerico(dia_texto) and es_numerico(mes_texto) and es_numerico(anio_texto)):
        return False

    dia, mes, anio = int(dia_texto), int(mes_texto), int(anio_texto)

    # Comprueba que el año y el mes estén dentro del rango permitido.
    if not 2026 <= anio <= 2036 or not 1 <= mes <= 12:
        return False

    # Establece la cantidad de días correspondiente a cada mes.
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Ajusta febrero a 29 días cuando el año es bisiesto.
    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        dias_mes[1] = 29

    # Verifica que el día exista dentro del mes indicado.
    return 1 <= dia <= dias_mes[mes - 1]

# Valida que la hora ingresada respete el formato de 24 horas.
def hora_valida(hora):

    # Comprueba que la hora tenga el formato HH:MM.
    if len(hora) != 5 or hora[2] != ":":
        return False

    # Separa las horas de los minutos.
    hora_texto, minuto_texto = hora[:2], hora[3:]

    # Verifica que ambos componentes sean numéricos.
    if not (es_numerico(hora_texto) and es_numerico(minuto_texto)):
        return False

    h, m = int(hora_texto), int(minuto_texto)

    # Comprueba que las horas y los minutos estén en rangos válidos.
    return 0 <= h <= 23 and 0 <= m <= 59