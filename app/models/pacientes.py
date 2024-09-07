from datetime import datetime
from citas import Cita

class Paciente:
    # Función para configurar los atributos después de la creación de la instancia
    def __init__(self, nombre, identificacion, correo, telefono, fechaNacimiento):
        self.nombre = nombre
        self.identificacion = identificacion
        self.correo = correo
        self.telefono = telefono
        self.fechaNacimiento = fechaNacimiento
        self.citas = []

    # Función para agendar la cita establecida por el paciente
    def agendarCita(self, fecha, hora, doctor):
        nueva_cita = Cita(fecha, hora, doctor)
        self.citas.append(nueva_cita)
        print(f"Cita agendada: {nueva_cita}")

    # Función para cancelar la(s) cita(s) establecida(s) por el paciente
    def cancelarCita(self, cita):
        if cita in self.citas:
            self.citas.remove(cita)
            print(f"Cita cancelada: {cita}")
        else:
            print("¡La cita no esta registrada!")

    # Función para generar recordatorio de la cita programada por el paciente
    def recibirRecordatorio(self):
        if not self.citas:
            print("¡No hay citas agendadas!")
        for cita in self.citas:
            print(f"Recordatorio: {cita}")

    # Método para crear un paciente sin tener que instanciar primero la clase
    @staticmethod
    # Función para obtener los datos del paciente que registra la cita
    def registro_paciente():
        print("====== Registro de paciente ======")
        nombre = input("Ingrese nombre completo: ")
        identificacion = input("Ingrese número de identificación: ")
        correo = input("Ingrese correo electrónico: ")
        telefono = input("Ingrese número de teléfono: ")
        fechaNacimiento = input("Ingrese fecha de nacimiento (YYYY-MM-DD): ")

        return Paciente(nombre, identificacion, correo, telefono, fechaNacimiento)

    # Función donde se construye el menú interactivo para la clase 'Pacientes'
    def menuPaciente(self):
        while True:
            print("\nMenú Paciente - ¿Qué deseas realizar hoy?")
            print("1. Agendar una cita")
            print("2. Cancelar una cita")
            print("3. Recibir recordatorio de citas")
            print("4. Salir")
            
            opcion = input("Indique la opción a realizar: ")

            if opcion == "1":
                self.agendar_cita()
            elif opcion == "2":
                self.cancelar_cita()
            elif opcion == "3":
                self.recibirRecordatorio()
            elif opcion == "4":
                print("Saliendo del menú...")
                break
            else:
                print("¡La opción no se encuentra disponible, intente nuevamente!")

    def agendar_cita(self):
        fecha = input("Ingrese la fecha de la cita (YYYY-MM-DD): ")
        hora = input("Ingrese la hora de la cita (HH:MM): ")
        doctor = input("Ingrese el nombre del doctor: ")
        self.agendarCita(fecha, hora, doctor)

    def cancelar_cita(self):
        if self.citas:
            print("Citas agendadas:")
            for idx, cita in enumerate(self.citas):
                print(f"{idx + 1}. {cita}")
            numero_cita = int(input("¿Qué cita desea cancelar? (Ingrese número de cita): ")) - 1
            if 0 <= numero_cita < len(self.citas):
                self.cancelarCita(self.citas[numero_cita])
            else:
                print("¡El número de cita no es correcto!")
        else:
            print("¡No hay citas agendadas para cancelar!")

# Inicialización de las clases
paciente = Paciente.registro_paciente()
paciente.menuPaciente()