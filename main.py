# Autor Juan Sebastian Diaz Campos - Cód. Estudiantil: 2116642

from app.pacientes import Paciente
from app.reportes import ReporteFactory

class Consultorio:
    _instancia = None

    # Creador del Singleton para solo trabajar con una instancia con relación a la clase 'Consultorio'
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super(Consultorio, cls).__new__(cls, *args, **kwargs)
        return cls._instancia

    # Función para estructurar el menú iterativo con el usuario
    def sistemaConsultorio(self):
        while True:
            print("\n======= Consultorio CitaYA =======\n¡Bienvenido al lugar donde la salud es lo primero!\n")
            print("1. Gestionar citas")
            print("2. Generar un reporte")
            print("3. Salir del sistema")

            opcion = input("Indique la opción a realizar: ")

            if opcion == "1":
                self.ObtenerPacientes()
            elif opcion == "2":
                self.obtenerReportes()
            elif opcion == "3":
                print("Saliendo...\n¡Gracias por creer en nosotros!")
                break
            else:
                print("¡La opción no se encuentra disponible, intente nuevamente!")

    # Función para obtener datos de inicialización de la clase 'Reporte'
    def obtenerReportes(self):
        reporte_factory = ReporteFactory()
        while True:
            reporte = reporte_factory.crear_reporte()
            if reporte:
                reporte.generar()
            else:
                break

    # Función para obtener datos de inicialización de la clase 'Paciente'
    def ObtenerPacientes(self):
        paciente = Paciente.registro_paciente()
        paciente.menuPaciente()

# Iniciar clase 'Consultorio'
consultorio = Consultorio()
consultorio.sistemaConsultorio()
