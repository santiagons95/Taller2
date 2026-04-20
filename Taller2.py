from datetime import datetime
import unicodedata

def normalizar(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    ).lower()

lista_clientes = []

def ingresar_info_cliente():
    while True:
        try:
            cedula = int(input("Ingrese el número de cédula del cliente:").strip())
            if cedula <= 0:
                print("La cédula debe ser un número positivo y no puede estar vacía. Intente nuevamente.")
                continue
            else:
                break
        except ValueError:
            print("Entrada no válida. Por favor ingrese un número de cédula válido.")
                
    while True:
        nombre = str(input("Ingrese el nombre del cliente:").strip())
        if not nombre:
            print("El nombre no puede estar vacío. Intente nuevamente.")
            continue
        elif not nombre.replace(" ", "").isalpha():
            print("El nombre debe contener solo letras y espacios. Intente nuevamente.")
            continue
        else:
            break

    while True:
        telefono = input("Ingrese el número de teléfono del cliente:").strip()
        if not telefono:
            print("El número de teléfono no puede estar vacío. Intente nuevamente.")
            continue
        elif not telefono.isdigit():
            print("El número de teléfono solo puede contener dígitos. Intente nuevamente.")
            continue
        else:    
            break

    while True:
        tipo_raw = input("Ingrese el tipo de cliente (Particular, EPS, Prepagada): ").strip()
        match = next((k for k in ["Particular", "EPS", "Prepagada"] if normalizar(k) == normalizar(tipo_raw)), None)
        if not match:
            print("Tipo de cliente no válido. Intente nuevamente.")
            continue
        else:
            tipo_cliente = match
            break
            
    while True:
        tipo_raw = input("Ingrese el tipo de atención (Limpieza, Calzas, Extracción, Diagnostico): ").strip()
        match = next((k for k in ["Limpieza", "Calzas", "Extracción", "Diagnostico"] if normalizar(k) == normalizar(tipo_raw)), None)
        if not match:
            print("Tipo de atención no válido. Intente nuevamente.")
            continue
        else:
            tipo_atencion = match
            break
    if tipo_atencion == "Limpieza" or tipo_atencion == "Diagnostico":
        cantidad = 1
    else:
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad de " + tipo_atencion + ":").strip())
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número entero.")
            else:
                if cantidad > 0:
                    break
                print("La cantidad debe ser mayor a cero. Intente nuevamente.")
                continue
    while True:
        tipo_raw = input("Ingrese el tipo de prioridad (Normal, Urgente): ").strip()
        match = next((k for k in ["Normal", "Urgente"] if normalizar(k) == normalizar(tipo_raw)), None)
        if not match:
            print("Tipo de prioridad no válido. Intente nuevamente.")
            continue
        else:
            tipo_prioridad = match
            break

    while True:
       fecha_atencion = input("Ingrese la fecha de atención (formato YYYY-MM-DD): ").strip()
       try:
            datetime.strptime(fecha_atencion, "%Y-%m-%d")
            break
       except ValueError:
            print("Fecha no válida. Asegúrese de usar el formato YYYY-MM-DD. Intente nuevamente.")
            continue

    cliente_info = {
    "Cédula": cedula,
    "Nombre": nombre,
    "Teléfono": telefono,
    "Tipo Cliente": tipo_cliente,
    "Tipo Atención": tipo_atencion,
    "Prioridad": tipo_prioridad,
    "Fecha Atención": fecha_atencion,
    "Cantidad": cantidad
    }

    lista_clientes.append(cliente_info)
    print(f"\n Cliente registrado: {cliente_info}\n")


def clientes_urgentes():
    pila_clientes = [cliente for cliente in lista_clientes if cliente["Tipo Atención"] == "Extracción" and cliente["Prioridad"] == "Urgente"]
    pila_clientes.sort(key=lambda x: x["Fecha Atención"], reverse=True)
    while pila_clientes:
        cliente_urgente = pila_clientes.pop()
        print("=" * 45)
        print("           ATENCIÓN DE CLIENTE CON EXTRACCIÓN URGENTE")
        print("=" * 45)
        print(f"  Cliente por atender : {cliente_urgente['Nombre']} Tel: {cliente_urgente['Teléfono']} (Cédula: {cliente_urgente['Cédula']})")
        print("=" * 45 + "\n")        
    print("Todos los clientes de la pila han sido atendidos.")
    
def cola_atencion():
    cola_atención = [cliente for cliente in lista_clientes if cliente["Tipo Atención"] != "Extracción" or cliente["Prioridad"] != "Urgente"]
    cola_atención.sort(key=lambda x: x["Fecha Atención"])
    while cola_atención:
        cliente_atencion = cola_atención.pop(0)
        print("=" * 45)
        print("           ATENCIÓN DE CLIENTE REGULAR")
        print("=" * 45)
        print(f"  Cliente por atender : {cliente_atencion['Nombre']} (Cédula: {cliente_atencion['Cédula']})")
        print("=" * 45 + "\n")        
    print("Todos los clientes de la cola han sido atendidos.")

def main():
    while True:
        print("Bienvenido al sistema de gestión de clientes de la clínica dental.\n Elija la opción que desea realizar:")
        print("1. Agregar cliente")
        print("2. Atender clientes urgentes")
        print("3. Atender clientes en cola")
        print("4. Salir")

        opcion = input("Ingrese la opción deseada: ").strip()
        if opcion == "1":
            ingresar_info_cliente()
        elif opcion == "2":
            if lista_clientes:
                clientes_urgentes()
            else:
                print("No se han registrado clientes.")
        elif opcion == "3":
            if lista_clientes:
                cola_atencion()
            else:
                print("No se han registrado clientes.")
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()