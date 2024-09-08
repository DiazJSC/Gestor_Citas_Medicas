class Horarios:
    def __init__(self):
        # Inicializar los horarios predefinidos
        self.horarios = []  
        self.cargarHorariosPredefinidos()

    def cargarHorariosPredefinidos(self):
        # Horarios predefinidos para mañana y tarde
        dias = [
            {'fecha': '2024-09-09', 'hora_inicio': '08:00', 'hora_fin': '08:20', 'disponible': True},
            {'fecha': '2024-09-09', 'hora_inicio': '09:20', 'hora_fin': '09:40', 'disponible': True},
            {'fecha': '2024-09-09', 'hora_inicio': '10:40', 'hora_fin': '11:00', 'disponible': True},
            {'fecha': '2024-09-10', 'hora_inicio': '08:00', 'hora_fin': '08:20', 'disponible': True},
            {'fecha': '2024-09-10', 'hora_inicio': '09:20', 'hora_fin': '09:40', 'disponible': True},
            {'fecha': '2024-09-10', 'hora_inicio': '10:40', 'hora_fin': '11:00', 'disponible': True},
            {'fecha': '2024-09-11', 'hora_inicio': '08:00', 'hora_fin': '08:20', 'disponible': True},
            {'fecha': '2024-09-11', 'hora_inicio': '09:20', 'hora_fin': '09:40', 'disponible': True},
            {'fecha': '2024-09-11', 'hora_inicio': '10:40', 'hora_fin': '11:00', 'disponible': True},
        ]

        tardes = [
            {'fecha': '2024-09-09', 'hora_inicio': '13:20', 'hora_fin': '13:40', 'disponible': True},
            {'fecha': '2024-09-09', 'hora_inicio': '15:00', 'hora_fin': '15:20', 'disponible': True},
            {'fecha': '2024-09-09', 'hora_inicio': '16:40', 'hora_fin': '17:00', 'disponible': True},
            {'fecha': '2024-09-10', 'hora_inicio': '13:20', 'hora_fin': '13:40', 'disponible': True},
            {'fecha': '2024-09-10', 'hora_inicio': '15:00', 'hora_fin': '15:20', 'disponible': True},
            {'fecha': '2024-09-10', 'hora_inicio': '16:40', 'hora_fin': '17:00', 'disponible': True},
            {'fecha': '2024-09-11', 'hora_inicio': '13:20', 'hora_fin': '13:40', 'disponible': True},
            {'fecha': '2024-09-11', 'hora_inicio': '15:00', 'hora_fin': '15:20', 'disponible': True},
            {'fecha': '2024-09-11', 'hora_inicio': '16:40', 'hora_fin': '17:00', 'disponible': True},
        ]

        # Agregar todos los horarios de mañana y tarde a la lista
        self.horarios.extend(dias + tardes)

    def marcarDisponibilidad(self):
        if not self.horarios:
            print("¡No hay horarios registrados!")
            return

        print("\nHorarios registrados:")
        for idx, horario in enumerate(self.horarios):
            estado = "Disponible" if horario['disponible'] else "No disponible"
            print(f"{idx + 1}. Fecha: {horario['fecha']}, Inicio: {horario['hora_inicio']}, Fin: {horario['hora_fin']}, Estado: {estado}")

        numero_horario = int(input("\n¿Qué horario desea marcar como No Disponible? (Ingrese el número de horario): ")) - 1
        if 0 <= numero_horario < len(self.horarios):
            self.horarios[numero_horario]['disponible'] = False
            print("¡La fecha ha sido marcado como No Disponible!")
        else:
            print("¡El número de horario no existe!")

    def visualizarHorarios(self):
        if not self.horarios:
            print("¡No hay horarios registrados!")
            return

        print("\nHorarios del médico:")
        for idx, horario in enumerate(self.horarios):
            estado = "Disponible" if horario['disponible'] else "No Disponible"
            print(f"{idx + 1}. Fecha: {horario['fecha']}, Inicio: {horario['hora_inicio']}, Fin: {horario['hora_fin']}, Estado: {estado}")