#Autor Juan Sebastian Diaz Campos - Cód. Estudiantil: 2116642

class Cita:
    def __init__(self, fecha, hora, duracion):
        self.fecha = fecha
        self.hora = hora
        self.duracion = duracion

    def __str__(self):
        return f"Tienes una cita el día {self.fecha} a las {self.hora} - Duración aproximada {self.duracion} mins"