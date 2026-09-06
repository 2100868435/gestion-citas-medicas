# Módulo de gestión de citas médicas
# Sistema: SaludPlus

def registrar_cita():
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


# Ejemplo de uso
cita = registrar_cita(
    "Juan Pérez",
    "Dra. María López",
    "2026-09-10",
    "10:00"
)

print("Cita registrada correctamente:")
print(cita)
