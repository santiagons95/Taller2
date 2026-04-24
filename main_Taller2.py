from datetime import datetime
import unicodedata
from modelos import Paciente, PilaUrgente, ColaPacientes

pila = PilaUrgente()
cola = ColaPacientes()

def normalizar(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    ).lower()

def ingresar_info_paciente():
    while True:
        try:
            cedula = int(input("Ingrese el número de cédula del paciente: ").strip())
            if cedula <= 0:
                print("La cédula debe ser un número positivo. Intente nuevamente.")
                continue
            else:
                break
        except ValueError:
            print("Entrada no válida. Por favor ingrese un número de cédula válido.")

    while True:
        nombre = input("Ingrese el nombre del paciente: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío. Intente nuevamente.")
            continue
        elif not nombre.replace(" ", "").isalpha():
            print("El nombre solo puede contener letras y espacios. Intente nuevamente.")
            continue
        else:
            break

    while True:
        telefono = input("Ingrese el número de teléfono del paciente: ").strip()
        if not telefono:
            print("El número de teléfono no puede estar vacío. Intente nuevamente.")
            continue
        elif not telefono.isdigit():
            print("El número de teléfono solo puede contener dígitos. Intente nuevamente.")
            continue
        else:
            break

    while True:
        tipo_raw = input("Ingrese el tipo de atención (L=Limpieza, C=Calzas, E=Extracción, D=Diagnostico): ").strip()
        match = next((k for k in ["Limpieza", "Calzas", "Extracción", "Diagnostico"] if normalizar(k)[0] == normalizar(tipo_raw)), None)
        if not match:
            print("Tipo de atención no válido. Intente nuevamente.")
            continue
        else:
            tipo_atencion = match
            break

    if tipo_atencion in ("Limpieza", "Diagnostico"):
        cantidad = 1
    else:
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad de " + tipo_atencion + ": ").strip())
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número entero.")
                continue
            else:
                if cantidad > 0:
                    break
                print("La cantidad debe ser mayor a cero. Intente nuevamente.")

    while True:
        tipo_raw = input("Ingrese el tipo de prioridad (N=Normal, U=Urgente): ").strip()
        match = next((k for k in ["Normal", "Urgente"] if normalizar(k)[0] == normalizar(tipo_raw)), None)
        if not match:
            print("Tipo de prioridad no válido. Intente nuevamente.")
            continue
        else:
            prioridad = match
            break

    while True:
        fecha_atencion = input("Ingrese la fecha de atención (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(fecha_atencion, "%Y-%m-%d")
            break
        except ValueError:
            print("Fecha no válida. Use el formato YYYY-MM-DD. Intente nuevamente.")

    paciente = Paciente(cedula, nombre, telefono, tipo_atencion, prioridad, fecha_atencion, cantidad)

    if tipo_atencion == "Extracción" and prioridad == "Urgente":
        pila.agregar(paciente)
    else:
        cola.agregar(paciente)

    print(f"\n✔ Paciente registrado: {paciente}\n")


def menu_urgentes():
    while True:
        opcion = input(
            "Pacientes urgentes:\n"
            "1. Atender siguiente paciente urgente\n"
            "2. Consultar siguiente paciente urgente\n"
            "3. Revisar pila completa\n"
            "4. Volver\n"
            "Ingrese su opción: "
        ).strip()

        if opcion == "1":
            paciente = pila.atender()
            if paciente:
                print("=" * 45)
                print("  ATENDIENDO PACIENTE URGENTE")
                print("=" * 45)
                print(f"  {paciente}")
                print("=" * 45 + "\n")
            else:
                print("No hay pacientes urgentes en la pila.\n")

        elif opcion == "2":
            paciente = pila.consultar_siguiente()
            if paciente:
                print(f"\nSiguiente paciente urgente: {paciente}\n")
            else:
                print("No hay pacientes urgentes en la pila.\n")

        elif opcion == "3":
            pila.mostrar()

        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.\n")


def menu_cola():
    while True:
        opcion = input(
            "Pacientes en cola:\n"
            "1. Atender siguiente paciente en cola\n"
            "2. Consultar siguiente paciente en cola\n"
            "3. Revisar cola completa\n"
            "4. Volver\n"
            "Ingrese su opción: "
        ).strip()

        if opcion == "1":
            paciente = cola.atender()
            if paciente:
                print("=" * 45)
                print("  ATENDIENDO PACIENTE REGULAR")
                print("=" * 45)
                print(f"  {paciente}")
                print("=" * 45 + "\n")
            else:
                print("No hay pacientes en la cola.\n")

        elif opcion == "2":
            paciente = cola.consultar_siguiente()
            if paciente:
                print(f"\nSiguiente paciente en cola: {paciente}\n")
            else:
                print("No hay pacientes en la cola.\n")

        elif opcion == "3":
            cola.mostrar()

        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.\n")


def menu_atencion():
    while True:
        opcion = input(
            "Elija la opción que desea realizar:\n"
            "1. Pacientes urgentes\n"
            "2. Pacientes en cola de llegada\n"
            "3. Salir\n"
            "Ingrese su opción: "
        ).strip()

        if opcion == "1":
            if pila.hay_pacientes():
                menu_urgentes()
            else:
                print("No hay pacientes urgentes registrados.\n")

        elif opcion == "2":
            if cola.hay_pacientes():
                menu_cola()
            else:
                print("No hay pacientes en cola registrados.\n")

        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.\n")


def main():
    while True:
        tipo_raw = input(
            "Bienvenido al sistema de gestión de pacientes de la clínica dental.\n"
            "¿Desea registrar un paciente? (S/N): "
        ).strip()
        match = next((k for k in ["s", "n"] if k == normalizar(tipo_raw)), None)

        if not match:
            print("Opción no válida. Por favor ingrese 'S' para sí o 'N' para no.\n")
            continue

        if match == "s":
            ingresar_info_paciente()

        elif match == "n":
            if pila.hay_pacientes() or cola.hay_pacientes():
                menu_atencion()
            else:
                print("No se han registrado pacientes. Saliendo del programa.")
                break


if __name__ == "__main__":
    main()