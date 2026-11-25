# Registro, visualización, búsqueda y ordenamiento de expedientes.
import datos
from datetime import datetime, timedelta
from validaciones import (
    documento_valido,
    telefono_valido,
    correo_valido,
    fecha_valida,
    hora_valida,
    nombre_valido,
    formatear_nombres
)

# Solicita y valida los datos necesarios para registrar un expediente.
def registrar_expediente():

    # Verificar que no se haya alcanzado el límite de registros.
    if datos.contador >= datos.LIMITE:
        print("Límite de expedientes alcanzado.")
        return

    while True:
        tipo_doc = input("Tipo de documento (DNI, RUC, CE, PASAPORTE): ").strip().upper()
        if tipo_doc in ("DNI", "RUC", "CE", "PASAPORTE"):
            break
        print("Tipo de documento no válido.")

    while True:
        num_doc = input("Número de documento: ").strip()
        if documento_valido(tipo_doc, num_doc):
            break
        print("Número de documento no válido.")

    while True:
        nombres = input("Ingrese nombres y apellidos: ").strip()

        if nombre_valido(nombres):
            nombres = formatear_nombres(nombres)
            break

        print("Nombre no válido.")
        print("Ingrese únicamente letras y espacios.")
        print("Debe contener como mínimo 3 letras.")
                    
    while True:
        telefono = input("Teléfono (9 dígitos, empieza con 9): ").strip()
        if telefono_valido(telefono):
            break
        print("Teléfono no válido.")

    while True:
        correo = input("Correo electrónico: ").strip()
        if correo_valido(correo):
            break
        print("Correo no válido.")

    # Opciones disponibles para el tipo de trámite.
    tipos_tramite = [
        "TUPA",
        "NO TUPA",
        "Descanso Médico",
        "Reclamo"
    ]

    # Mostrar las opciones disponibles y permitir seleccionar una.
    print("\nSeleccione el tipo de trámite:")
    for i, tipo in enumerate(tipos_tramite, 1):
        print(f"{i}. {tipo}")

    while True:
        try:
            opcion = int(input("Ingrese una opción: "))

            if 1 <= opcion <= len(tipos_tramite):
                tipo_tramite = tipos_tramite[opcion - 1]
                break

            print("Opción no válida. Intente nuevamente.")

        except ValueError:
            print("Debe ingresar un número.")

    # Validar que el asunto no esté vacío y tenga un máximo de 100 caracteres.
    while True:
        asunto = input("Asunto (máximo 100 caracteres): ").strip()

        if not asunto:
            print("El asunto no puede estar vacío.")
        elif len(asunto) > 100:
            print("El asunto no puede superar los 100 caracteres.")
        else:
            break

    while True:
        try:
            folios = int(input("Número de folios: "))
            if folios > 0:
                break
            print("Debe ingresar un número mayor que cero.")
        except ValueError:
            print("Ingrese un número entero válido.")

   
    # Opciones disponibles para el área de destino.
    areas_destino = [
        "Admisión",
        "Jefatura Médica",
        "Trámite Documentario"
    ]

    # Mostrar las opciones disponibles y permitir seleccionar una.
    print("\nSeleccione el área de destino:")
    for i, area in enumerate(areas_destino, 1):
        print(f"{i}. {area}")

    while True:
        try:
            opcion_area = int(input("Ingrese una opción: "))

            if 1 <= opcion_area <= len(areas_destino):
                area_destino = areas_destino[opcion_area - 1]
                break

            print("Opción no válida. Intente nuevamente.")

        except ValueError:
            print("Debe ingresar un número.")

    while True:
        fecha = input("Fecha de ingreso (DD/MM/AAAA): ").strip()
        if fecha_valida(fecha):
            break
        print("Fecha no válida.")

    while True:
        hora = input("Hora de ingreso (HH:MM): ").strip()
        if hora_valida(hora):
            break
        print("Hora no válida.")

    # Incrementar el contador y generar un código para el expediente.
    datos.contador += 1
    codigo = f"EXP-2026-{datos.contador:03d}"

    # Avisar si el registro se realiza después de las 17:00.
    if hora > "17:00":
        print("Aviso: registro posterior a las 17:00.")

        # Calcula la fecha del siguiente día hábil.
        siguiente_dia = datetime.strptime(fecha, "%d/%m/%Y") + timedelta(days=1)

        # Omite los sábados y domingos.
        while siguiente_dia.weekday() >= 5:
            siguiente_dia += timedelta(days=1)

        # Muestra la fecha en formato DD/MM/AAAA.
        print("Siguiente día hábil:", siguiente_dia.strftime("%d/%m/%Y"))
        
    # Registrar el expediente con estado inicial pendiente.
    datos.estados.append("Pendiente")

    # Almacenar los datos del expediente en sus listas correspondientes.
    datos.codigos.append(codigo)
    datos.tiposDoc.append(tipo_doc)
    datos.numerosDoc.append(num_doc)
    datos.nombresExp.append(nombres)
    datos.correos.append(correo)
    datos.telefonos.append(telefono)
    datos.tiposTramite.append(tipo_tramite)
    datos.asuntos.append(asunto)
    datos.areasDestino.append(area_destino)
    datos.fechas.append(fecha)
    datos.horas.append(hora)
    datos.foliosExp.append(folios)

    print("\nExpediente registrado correctamente.")
    mostrar_expediente(datos.contador - 1)

# Muestra toda la información de un expediente según su posición.
def mostrar_expediente(i):
    print("================================")
    print("Código:", datos.codigos[i])
    print("Solicitante:", datos.nombresExp[i])
    print("Documento:", datos.tiposDoc[i], datos.numerosDoc[i])
    print("Correo:", datos.correos[i])
    print("Teléfono:", datos.telefonos[i])
    print("Trámite:", datos.tiposTramite[i])
    print("Asunto:", datos.asuntos[i])
    print("Folios:", datos.foliosExp[i])
    print("Área:", datos.areasDestino[i])
    print("Fecha:", datos.fechas[i])
    print("Hora:", datos.horas[i])
    print("Estado:", datos.estados[i])

# Busca expedientes mediante su código o número de documento.
def buscar_expediente():
    if datos.contador == 0:
        print("No existen expedientes registrados.")
        return
        
    parametro = input("Ingrese código o número de documento: ").strip()
    cantidad = 0
    
    for i in range(datos.contador):
        if datos.codigos[i] == parametro or datos.numerosDoc[i] == parametro:
            mostrar_expediente(i)
            cantidad += 1
            
    if cantidad == 0:
        print("No se encontró el expediente.")
    else:
        print("================================")
        print(f"Se encontraron {cantidad} expediente(s).")

# Ordena los expedientes por código y muestra el listado.
def ordenar_y_listar():
    if datos.contador == 0:
        print("No hay expedientes para listar.")
        return
        
    arreglos = [
        datos.codigos,
        datos.tiposDoc,
        datos.numerosDoc,
        datos.nombresExp,
        datos.correos,
        datos.telefonos,
        datos.tiposTramite,
        datos.asuntos,
        datos.areasDestino,
        datos.fechas,
        datos.horas,
        datos.estados,
        datos.foliosExp
    ]

    # Intercambiar los elementos de todas las listas para mantener la correspondencia de los datos de cada expediente.
    for i in range(datos.contador - 1):
        for j in range(i + 1, datos.contador):
            if datos.codigos[i] > datos.codigos[j]:
                for arreglo in arreglos:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
                    
    print("\nLISTADO ORDENADO POR CÓDIGO")
    
    for i in range(datos.contador):
        print(
            datos.codigos[i], "|",
            datos.nombresExp[i], "|",
            datos.numerosDoc[i], "|",
            datos.fechas[i], "|",
            datos.estados[i]
        )
        
    print("Total:", datos.contador)

# Muestra la cantidad total de expedientes y su distribución por estado.
def contar_expedientes():
    total = len(datos.codigos)

    print("\n--- TOTAL DE EXPEDIENTES ---")
    print("Cantidad de expedientes registrados:", total)

    pendientes = datos.estados.count("Pendiente")
    atendidos = datos.estados.count("Atendido")
    observados = datos.estados.count("Observado")

    print("Pendientes:", pendientes)
    print("Atendidos:", atendidos)
    print("Observados:", observados)

# Filtra y muestra los expedientes según el estado seleccionado.
def filtrar_por_estado():
    print("\n--- FILTRAR POR ESTADO ---")
    print("1. Pendiente")
    print("2. Atendido")
    print("3. Observado")

    opcion = input("Selecciona el estado: ").strip()

    estados_opciones = {
        "1": "Pendiente",
        "2": "Atendido",
        "3": "Observado"
    }

    if opcion not in estados_opciones:
        print("Opción no válida.")
        return

    estado_buscado = estados_opciones[opcion]
    encontrados = 0

    for i in range(len(datos.estados)):
        if datos.estados[i] == estado_buscado:
            print(
                f"Código: {datos.codigos[i]} | "
                f"Nombre: {datos.nombresExp[i]} | "
                f"Estado: {datos.estados[i]}"
            )
            encontrados += 1

    if encontrados == 0:
        print("No hay expedientes con ese estado.")
    else:
        print("Total encontrados:", encontrados)

# Permite modificar el estado de un expediente mediante su código.
def actualizar_estado():
    print("\n--- ACTUALIZAR ESTADO ---")

    codigo = input("Código del expediente: ").strip().upper()

    if codigo not in datos.codigos:
        print("No se encontró el expediente.")
        return

    posicion = datos.codigos.index(codigo)

    print("Estado actual:", datos.estados[posicion])
    print("1. Pendiente")
    print("2. Atendido")
    print("3. Observado")

    opcion = input("Selecciona el nuevo estado: ").strip()

    nuevos_estados = {
        "1": "Pendiente",
        "2": "Atendido",
        "3": "Observado"
    }

    if opcion not in nuevos_estados:
        print("Opción no válida. No se modificó el estado.")
        return

    datos.estados[posicion] = nuevos_estados[opcion]

    print("Estado actualizado correctamente.")
    mostrar_expediente(posicion)
