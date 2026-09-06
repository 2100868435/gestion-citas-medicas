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
