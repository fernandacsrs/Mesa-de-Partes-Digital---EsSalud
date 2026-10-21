# Registro, visualización, búsqueda y ordenamiento de expedientes.
import datos
from validaciones import documento_valido, telefono_valido, correo_valido, fecha_valida, hora_valida

def registrar_expediente():
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
        nombres = input("Nombres o razón social: ").strip()
        if nombres:
            break
        print("El nombre no puede estar vacío.")

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

    while True:
        tipo_tramite = input("Tipo de trámite: ").strip()
        if tipo_tramite:
            break
        print("El tipo de trámite no puede estar vacío.")

    while True:
        asunto = input("Asunto: ").strip()
        if asunto:
            break
        print("El asunto no puede estar vacío.")

    while True:
        try:
            folios = int(input("Número de folios: "))
            if folios > 0:
                break
            print("Debe ingresar un número mayor que cero.")
        except ValueError:
            print("Ingrese un número entero válido.")

    while True:
        area_destino = input("Área de destino: ").strip()
        if area_destino:
            break
        print("El área no puede estar vacía.")

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

    datos.contador += 1
    codigo = f"EXP-2026-{datos.contador:03d}"
    if hora > "17:00":
        print("Aviso: registro posterior a las 17:00.")

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
    datos.estados.append("REGISTRADO")
    datos.foliosExp.append(folios)

    print("\nExpediente registrado correctamente.")
    mostrar_expediente(datos.contador - 1)

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

def ordenar_y_listar():
    if datos.contador == 0:
        print("No hay expedientes para listar.")
        return
    arreglos = [datos.codigos, datos.tiposDoc, datos.numerosDoc, datos.nombresExp,
                datos.correos, datos.telefonos, datos.tiposTramite, datos.asuntos,
                datos.areasDestino, datos.fechas, datos.horas, datos.estados, datos.foliosExp]
    for i in range(datos.contador - 1):
        for j in range(i + 1, datos.contador):
            if datos.codigos[i] > datos.codigos[j]:
                for arreglo in arreglos:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
    print("\nLISTADO ORDENADO POR CÓDIGO")
    for i in range(datos.contador):
        print(datos.codigos[i], "|", datos.nombresExp[i], "|", datos.numerosDoc[i],
              "|", datos.fechas[i], "|", datos.estados[i])
    print("Total:", datos.contador)