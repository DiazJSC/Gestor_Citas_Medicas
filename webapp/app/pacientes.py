#Autor Juan Sebastian Diaz Campos - Cód. Estudiantil: 2116642

from .citas import Cita
from .medicos import Medico

class Paciente:
    def __init__(self, nombre, identificacion, correo, telefono, fechaNacimiento):
        self.nombre = nombre
        self.identificacion = identificacion
        self.correo = correo
        self.telefono = telefono
        self.fechaNacimiento = fechaNacimiento
        self.citas = []


    def agendarCita(self, medico, horario):
        fecha = horario['fecha']
        hora = horario['hora_inicio']
        duracion = 20  # Se establece una duración predeterminada de 20 minutos para las citas

        nueva_cita = Cita(fecha, hora, duracion)
        self.citas.append(nueva_cita)

        # Marcar el horario como "no disponible"
        horario['disponible'] = False
        print(f"Cita agendada con el Dr. {medico.nombre}, Fecha: {fecha}, Hora: {hora}")

    def cancelarCita(self, cita):
        if cita in self.citas:
            self.citas.remove(cita)
            print(f"Cita cancelada: {cita}")
        else:
            print("¡La cita no está registrada!")

    def recibirRecordatorio(self):
        if not self.citas:
            print("¡No hay citas agendadas!")
        for cita in self.citas:
            print(f"Recordatorio: {cita}")

    @staticmethod
    def registro_paciente():
        print("\n====== Registro de paciente ======")
        nombre = input("Ingrese nombre completo: ")
        identificacion = input("Ingrese número de identificación: ")
        correo = input("Ingrese correo electrónico: ")
        telefono = input("Ingrese número de teléfono: ")
        fechaNacimiento = input("Ingrese fecha de nacimiento (YYYY-MM-DD): ")

        return Paciente(nombre, identificacion, correo, telefono, fechaNacimiento)

    # Función para estructurar la interación con el menú de gestión de citas
    def menuPaciente(self):
        while True:
            print("\nMenú Citas - ¿Qué deseas realizar hoy?")
            print("1. Agendar una cita")
            print("2. Cancelar una cita")
            print("3. Recibir recordatorio de citas")
            print("4. Ver horarios de médicos")
            print("5. Salir")

            opcion = input("Indique la opción a realizar: ")

            if opcion == "1":
                self.agendar_cita()
            elif opcion == "2":
                self.cancelar_cita()
            elif opcion == "3":
                self.recibirRecordatorio()
            elif opcion == "4":
                self.verHorariosMedico()
            elif opcion == "5":
                print("Saliendo del menú...")
                break
            else:
                print("¡La opción no se encuentra disponible, intente nuevamente!")

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

    def obtenerMedico(self):
        medicos = list(Medico.lis_medicos.keys())

        print("\nMédicos disponibles:")
        for idx, nombre in enumerate(medicos):
            print(f"{idx + 1}. {nombre} ({Medico.lis_medicos[nombre]})")

        numero_medico = int(input("Seleccione un médico por su número: ")) - 1
        if 0 <= numero_medico < len(medicos):
            nombre_medico = medicos[numero_medico]
            especialidad = Medico.lis_medicos[nombre_medico]

            medico = Medico(nombre_medico, especialidad)
            return medico
        else:
            print("¡Selección inválida!")
            return None

    def agendar_cita(self):
        medico = self.obtenerMedico()
        if medico:
            medico.visualizarHorariosMedico()
            self.seleccionarHorario(medico)

    def verHorariosMedico(self):
        medico = self.obtenerMedico()
        if medico:
            print(f"Horarios disponibles para el Dr. {medico.nombre}:")
            medico.visualizarHorariosMedico()

    def seleccionarHorario(self, medico):
        horarios_disponibles = [h for h in medico.horarios.horarios if h['disponible']]

        if horarios_disponibles:
            print("\nHorarios disponibles:")
            for idx, horario in enumerate(horarios_disponibles):
                print(f"{idx + 1}. Fecha: {horario['fecha']}, Hora: {horario['hora_inicio']}")

            numero_horario = int(input("Seleccione un horario por su número: ")) - 1
            if 0 <= numero_horario < len(horarios_disponibles):
                horario_seleccionado = horarios_disponibles[numero_horario]
                self.agendarCita(medico, horario_seleccionado)
            else:
                print("¡Selección inválida!")
        else:
            print("¡No hay horarios disponibles!")