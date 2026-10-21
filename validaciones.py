# Funciones de validación de los datos ingresados.

def es_numerico(cadena):
    return len(cadena) > 0 and cadena.isdigit()

def documento_valido(tipo, numero):
    tipo = tipo.upper()
    if tipo == "DNI":
        return len(numero) == 8 and es_numerico(numero)
    elif tipo == "RUC":
        return len(numero) == 11 and es_numerico(numero) and numero[:2] in ("10", "20")
    elif tipo == "CE":
        return 1 <= len(numero) <= 11 and es_numerico(numero)
    elif tipo == "PASAPORTE":
        return 1 <= len(numero) <= 15 and numero.isalnum()
    return False

def telefono_valido(telefono):
    return len(telefono) == 9 and es_numerico(telefono) and telefono.startswith("9")

def correo_valido(correo):
    if len(correo) < 6 or " " in correo or correo.count("@") != 1:
        return False
    posicion_arroba = correo.find("@")
    posicion_punto = correo.rfind(".")
    return (posicion_arroba > 0 and posicion_punto > posicion_arroba + 1
            and posicion_punto < len(correo) - 1)

def fecha_valida(fecha):
    if len(fecha) != 10 or fecha[2] != "/" or fecha[5] != "/":
        return False
    dia_texto, mes_texto, anio_texto = fecha[:2], fecha[3:5], fecha[6:10]
    if not (es_numerico(dia_texto) and es_numerico(mes_texto) and es_numerico(anio_texto)):
        return False
    dia, mes, anio = int(dia_texto), int(mes_texto), int(anio_texto)
    if not 2026 <= anio <= 2036 or not 1 <= mes <= 12:
        return False
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        dias_mes[1] = 29
    return 1 <= dia <= dias_mes[mes - 1]

def hora_valida(hora):
    if len(hora) != 5 or hora[2] != ":":
        return False
    hora_texto, minuto_texto = hora[:2], hora[3:]
    if not (es_numerico(hora_texto) and es_numerico(minuto_texto)):
        return False
    h, m = int(hora_texto), int(minuto_texto)
    return 0 <= h <= 23 and 0 <= m <= 59