# Programa principal: menú de Mesa de Partes Digital - EsSalud.
import os
import datos
from expedientes import registrar_expediente, buscar_expediente, ordenar_y_listar
from archivos import guardar_binario, cargar_binario, guardar_plano, cargar_plano

def menu_principal():
    # Recupera los datos al iniciar, si ya existe el archivo binario.
    if os.path.exists(datos.ARCHIVO_BINARIO):
        cargar_binario()

    while True:
        print("\n================================")
        print("MESA DE PARTES DIGITAL - ESSALUD")
        print("1. Registrar expediente")
        print("2. Buscar expediente")
        print("3. Ordenar y listar expedientes")
        print("4. Guardar datos en archivo binario")
        print("5. Cargar datos desde archivo binario")
        print("6. Guardar datos en archivo plano (.txt)")
        print("7. Cargar datos desde archivo plano (.txt)")
        print("8. Contar expedientes registrados")
        print("9. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Ingrese un número válido.")
            continue

        if opcion == 1:
            registrar_expediente()
        elif opcion == 2:
            buscar_expediente()
        elif opcion == 3:
            ordenar_y_listar()
        elif opcion == 4:
            guardar_binario()
        elif opcion == 5:
            cargar_binario()
        elif opcion == 6:
            guardar_plano()
        elif opcion == 7:
            cargar_plano()
        elif opcion == 8:
            expedientes.contar_expedientes()
        elif opcion == 9:
            print("Cerrando sistema...")
            break
        else:
            print("Seleccione una opción del 1 al 8.")

if __name__ == "__main__":
    menu_principal()