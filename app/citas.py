class CitaService:
    def __init__(self):
        self.citas = {}

    def reservar_cita(self, horario, paciente):
        if horario in self.citas:
            raise ValueError("Horario no disponible")

        self.citas[horario] = paciente
        return True

    def cancelar_cita(self, horario):
        if horario not in self.citas:
            raise ValueError("La cita no existe")

        del self.citas[horario]
        return True

    def verificar_disponibilidad(self, horario):
        return horario not in self.citas