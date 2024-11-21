from app.pacientes import Paciente
from app.medicos import Medico
from app.reportes import ReporteFactory

# Lista global para guardar los pacientes registrados
pacientes_registrados = []

def menu_paciente(paciente):
    while True:
        print("\nMenú Citas - ¿Qué deseas realizar hoy?")
        print("1. Agendar una cita")
        print("2. Cancelar una cita")
        print("3. Recibir recordatorio de citas")
        print("4. Ver horarios de médicos")
        print("5. Salir")

        opcion = input("Indique la opción a realizar: ")

        if opcion == "1":
            medico = paciente.obtenerMedico()
            if medico:
                medico.visualizarHorariosMedico()
                paciente.seleccionarHorario(medico)
        elif opcion == "2":
            paciente.cancelar_cita()
        elif opcion == "3":
            paciente.recibirRecordatorio()
        elif opcion == "4":
            medico = paciente.obtenerMedico()
            if medico:
                print(f"Horarios disponibles para el Dr. {medico.nombre}:")
                medico.visualizarHorariosMedico()
        elif opcion == "5":
            print("Saliendo del menú...")
            break
        else:
            print("¡La opción no se encuentra disponible, intente nuevamente!")

def registrar_paciente():
    paciente = Paciente.registro_paciente()
    pacientes_registrados.append(paciente)
    print(f"¡Paciente {paciente.nombre} registrado exitosamente!")
    return paciente

def main():
    print("\n======= Consultorio CitaYA =======\n¡Bienvenido al lugar donde la salud es lo primero!\n")
    
    while True:
        print("1. Gestionar citas")
        print("2. Generar un reporte")
        print("3. Salir del sistema")

        opcion = input("Indique la opción a realizar: ")

        if opcion == "1":
            print("1. Registrar un nuevo paciente")
            print("2. Seleccionar un paciente registrado")

            sub_opcion = input("Indique la opción a realizar: ")
            if sub_opcion == "1":
                paciente = registrar_paciente()
                menu_paciente(paciente)
            elif sub_opcion == "2":
                if pacientes_registrados:
                    print("\nPacientes registrados:")
                    for idx, p in enumerate(pacientes_registrados):
                        print(f"{idx + 1}. {p.nombre} - ID: {p.identificacion}")
                    
                    seleccion = int(input("Seleccione un paciente por su número: ")) - 1
                    if 0 <= seleccion < len(pacientes_registrados):
                        paciente = pacientes_registrados[seleccion]
                        menu_paciente(paciente)
                    else:
                        print("¡Selección inválida!")
                else:
                    print("¡No hay pacientes registrados! Registre un nuevo paciente primero.")
            else:
                print("¡La opción no se encuentra disponible!")
        elif opcion == "2":
            reporte_factory = ReporteFactory()
            while True:
                reporte = reporte_factory.crear_reporte()
                if reporte:
                    reporte.generar()
                else:
                    break
        elif opcion == "3":
            print("Saliendo...\n¡Gracias por creer en nosotros!")
            break
        else:
            print("¡La opción no se encuentra disponible, intente nuevamente!")

if __name__ == "__main__":
    main()
