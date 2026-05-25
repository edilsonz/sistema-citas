import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.pacientes import PacienteService


def test_registrar_paciente_correctamente():
    servicio = PacienteService()

    resultado = servicio.registrar_paciente("Juan")

    assert resultado is True
    assert "Juan" in servicio.obtener_pacientes()


def test_no_permitir_pacientes_duplicados():
    servicio = PacienteService()

    servicio.registrar_paciente("Juan")

    with pytest.raises(ValueError):
        servicio.registrar_paciente("Juan")