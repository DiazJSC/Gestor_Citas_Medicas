from abc import ABC, abstractmethod
from datetime import datetime

class Reportes(ABC):
    def generar(self):
        pass

class Demanda(Reportes):
    def generar(self):
        fecha_actual = datetime.now()
        print(f"Fecha descarga: {fecha_actual}\nTipo reporte: Médicos con mayor demanda
              \nExportando reporte en formato excel...")

class Tendencia(Reportes):
    def generar(self):
        fecha_actual = datetime.now()
        print(f"Fecha descarga: {fecha_actual}\nTipo reporte: Tendencia de citas
              \nExportando reporte en formato excel...")

class ReporteFactory:
    def crear_reporte(self, tipo_reporte):
        if tipo_reporte == 1:
            return Demanda()
        elif tipo_reporte == 2:
            return Tendencia()
        else:
            return None
        
reporte_factory = ReporteFactory()
excel_demanda = reporte_factory.crear_reporte(1)
excel_demanda.generar()

excel_tendencia = reporte_factory.crear_reporte(2)
excel_tendencia.generar()