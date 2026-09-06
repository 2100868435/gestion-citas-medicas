# Módulo de gestión de citas médicas
# Sistema: SaludPlus

def registrar_cita(paciente, medico, fecha, hora):
    cita = {
        "paciente": paciente,
        "medico": medico,
        "fecha": fecha,
        "hora": hora
    }

    return cita
