import pytest
from app.citas import CitaService


def test_reservar_cita_correctamente():
    servicio = CitaService()

    resultado = servicio.reservar_cita("10:00", "Juan")

    assert resultado is True


def test_no_permitir_doble_reserva():
    servicio = CitaService()

    servicio.reservar_cita("10:00", "Juan")

    with pytest.raises(ValueError):
        servicio.reservar_cita("10:00", "Pedro")


def test_cancelar_cita():
    servicio = CitaService()

    servicio.reservar_cita("10:00", "Juan")

    resultado = servicio.cancelar_cita("10:00")

    assert resultado is True


def test_verificar_disponibilidad():
    servicio = CitaService()

    disponible = servicio.verificar_disponibilidad("11:00")

    assert disponible is True