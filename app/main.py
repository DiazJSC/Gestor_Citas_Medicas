from models.pacientes import Paciente
from models.reportes import ReporteFactory

class Consultorio:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super(Consultorio, cls).__new__(cls, *args, **kwargs)
        return cls._instancia

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

    def obtenerReportes(self):
        reporte_factory = ReporteFactory()
        while True:
            reporte = reporte_factory.crear_reporte()
            if reporte:
                reporte.generar()
            else:
                break

    def ObtenerPacientes(self):
        paciente = Paciente.registro_paciente()
        paciente.menuPaciente()

# Inicializar sistema
consultorio = Consultorio()
consultorio.sistemaConsultorio()
