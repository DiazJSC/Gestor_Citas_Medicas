from .horarios import Horarios

class Medico:
    lis_medicos = {
        "Pablo Arias": "Cardiología",
        "Ricardo Molano": "Pediatría",
        "Monica Zuñiga": "Ginecología"
    }

    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.horarios = Horarios()  # Instancia de la clase Horarios para gestionar los horarios del médico

    def registrarMedico(self):
        print(f"Se registró al Médico: {self.nombre}, con la Especialidad: {self.especialidad}")

    def marcarDisponibilidadMedico(self):
        print(f"\nMarcando disponibilidad para el Dr. {self.nombre}")
        self.horarios.marcarDisponibilidad()

    def visualizarHorariosMedico(self):
        print(f"\nVisualizando horarios del Dr. {self.nombre}")
        self.horarios.visualizarHorarios()

    def menuMedico(self):
        while True:
            print(f"\nMenú del Dr. {self.nombre} - Especialidad: {self.especialidad}")
            print("1. Marcar disponibilidad")
            print("2. Visualizar horarios")
            print("3. Salir")
            
            opcion = input("Indique la opción a realizar: \n")

            if opcion == "1":
                self.marcarDisponibilidadMedico()
            elif opcion == "2":
                self.visualizarHorariosMedico()
            elif opcion == "3":
                print(f"Saliendo del menú del Dr. {self.nombre}...")
                break
            else:
                print("¡La opción no se encuentra disponible, intente nuevamente!")

    @classmethod
    def iniciar_sistema_medico(cls):
        # Mostrar lista de médicos predeterminados
        print("\nLista de médicos disponibles:")
        for idx, (nombre, especialidad) in enumerate(cls.lis_medicos.items()):
            print(f"{idx + 1}. {nombre} - Especialidad: {especialidad}")
        
        # Seleccionar médico de la lista
        seleccion = int(input("Seleccione el médico (ingrese el número): ")) - 1
        if 0 <= seleccion < len(cls.lis_medicos):
            nombre_medico = list(cls.lis_medicos.keys())[seleccion]
            especialidad_medico = cls.lis_medicos[nombre_medico]
            
            # Crear una instancia del médico seleccionado
            medico = cls(nombre_medico, especialidad_medico)
            medico.registrarMedico()

            # Iniciar el menú para el médico seleccionado
            medico.menuMedico()
        else:
            print("¡Selección inválida!")