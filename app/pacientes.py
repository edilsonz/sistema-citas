class PacienteService:
    def __init__(self):
        self.pacientes = []

    def registrar_paciente(self, nombre):
        if nombre in self.pacientes:
            raise ValueError("El paciente ya existe")

        self.pacientes.append(nombre)
        return True

    def obtener_pacientes(self):
        return self.pacientes