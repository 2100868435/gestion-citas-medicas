from citas import registrar_cita


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


def test_registrar_otra_cita():
    cita = registrar_cita(
        "Ana Torres",
        "Dr. Carlos Gómez",
        "2026-09-11",
        "14:30"
    )

    assert cita["paciente"] == "Ana Torres"
    assert cita["medico"] == "Dr. Carlos Gómez"
    assert cita["fecha"] == "2026-09-11"
    assert cita["hora"] == "14:30"


def test_cp06_aceptacion_registrar_cita():
    # CP-06: la recepcionista registra una cita médica
    cita = registrar_cita(
        "María González",
        "Dra. Ana Rodríguez",
        "2026-09-15",
        "09:30"
    )

    assert cita["paciente"] == "María González"
    assert cita["medico"] == "Dra. Ana Rodríguez"
    assert cita["fecha"] == "2026-09-15"
    assert cita["hora"] == "09:30"
