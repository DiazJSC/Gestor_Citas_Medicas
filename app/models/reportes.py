from abc import ABC, abstractmethod
from datetime import datetime

class Reportes(ABC):
    @abstractmethod
    def generar(self):
        pass

class Demanda(Reportes):
    def generar(self):
        fecha_actual = datetime.now()
        print(f"Fecha descarga: {fecha_actual}\nTipo reporte: Médicos con mayor demanda\nExportando reporte en formato excel...\n")

class Tendencia(Reportes):
    def generar(self):
        fecha_actual = datetime.now()
        print(f"Fecha descarga: {fecha_actual}\nTipo reporte: Tendencia de citas\nExportando reporte en formato excel...\n")

class ReporteFactory:
    def crear_reporte(self):
        while True:
            print("\nMenú Reportes - ¿Qué reporte deseas obtener hoy?\n")
            print("1. Médicos con mayor demanda")
            print("2. Tendencia de citas")
            print("3. Salir del menú")
            
            opcion = input("Indique la opción a realizar: ")

            if opcion == "1":
                return Demanda()
            elif opcion == "2":
                return Tendencia()
            elif opcion == "3":
                print("Saliendo del menú...")
                break
            else:
                print("¡La opción no se encuentra disponible, intente nuevamente!")