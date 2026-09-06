from src.citas import registrar_cita


def test_registrar_cita():
    cita = registrar_cita(
        "Juan Pérez",
        "Dra. María López",
        "2026-09-10",
        "10:00"
    )

    assert cita["paciente"] == "Juan Pérez"
    assert cita["medico"] == "Dra. María López"
    assert cita["fecha"] == "2026-09-10"
    assert cita["hora"] == "10:00"
