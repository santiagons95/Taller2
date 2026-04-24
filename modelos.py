class Paciente:
    def __init__(self, cedula, nombre, telefono, tipo_atencion, prioridad, fecha_atencion, cantidad):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.tipo_atencion = tipo_atencion
        self.prioridad = prioridad
        self.fecha_atencion = fecha_atencion
        self.cantidad = cantidad
 
    def __repr__(self):
        return (f"Cédula: {self.cedula} | Nombre: {self.nombre} | "
                f"Teléfono: {self.telefono} | "
                f"Tipo Atención: {self.tipo_atencion} | Prioridad: {self.prioridad} | "
                f"Fecha: {self.fecha_atencion} | Cantidad: {self.cantidad}")
 
 
class PilaUrgente:
    def __init__(self):
        self._pila = []
 
    def agregar(self, paciente):
        self._pila.append(paciente)
        self._pila.sort(key=lambda x: x.fecha_atencion, reverse=True)
 
    def atender(self):
        if self._pila:
            return self._pila.pop()
        return None
 
    def consultar_siguiente(self):
        if self._pila:
            return self._pila[-1] 
        return None
 
    def mostrar(self):
        if self._pila:
            print("=" * 45)
            print("       PILA DE PACIENTES URGENTES")
            print("=" * 45)
            for i, paciente in enumerate(reversed(self._pila), 1):
                print(f"  {i}. {paciente.nombre} (CC {paciente.cedula}) - {paciente.fecha_atencion} - {paciente.telefono}")
            print("=" * 45 + "\n")
        else:
            print("La pila de pacientes urgentes está vacía.\n")
 
    def hay_pacientes(self):
        return len(self._pila) > 0
 
 
class ColaPacientes:
    def __init__(self):
        self._cola = []
 
    def agregar(self, paciente):
        self._cola.append(paciente)
        self._cola.sort(key=lambda x: x.fecha_atencion)
 
    def atender(self):
        if self._cola:
            return self._cola.pop(0)
        return None
 
    def consultar_siguiente(self):
        if self._cola:
            return self._cola[0]
        return None
 
    def mostrar(self):
        if self._cola:
            print("=" * 45)
            print("       COLA DE PACIENTES REGULARES")
            print("=" * 45)
            for i, paciente in enumerate(self._cola, 1):
                print(f"  {i}. {paciente.nombre} (CC {paciente.cedula}) - {paciente.fecha_atencion} - {paciente.telefono}")
            print("=" * 45 + "\n")
        else:
            print("La cola de pacientes está vacía.\n")
 
    def hay_pacientes(self):
        return len(self._cola) > 0