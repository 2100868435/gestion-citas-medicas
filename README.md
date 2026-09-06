# Gestión de Citas Médicas

## Sistema

Salud Integral

## Módulo

Gestión de Citas Médicas

## Descripción

Este proyecto implementa un módulo básico para registrar citas médicas, almacenando información del paciente, médico, fecha y hora de la cita.

## Tecnologías utilizadas

* Python 3.12
* Pytest
* GitHub
* GitHub Actions

## Estructura del proyecto

* `src/`: contiene el código fuente del módulo.
* `tests/`: contiene las pruebas automatizadas.
* `.github/workflows/`: contiene la configuración del pipeline de Integración Continua.
* `.gitignore`: contiene archivos y elementos que no deben incluirse en el repositorio.
* `pytest.ini`: configura la ejecución de las pruebas con Pytest.

## Flujo de ramas

Se utiliza un flujo basado en GitHub Flow:

* `main`: rama principal y estable del proyecto.
* `feature/registrar-cita`: rama utilizada para desarrollar la funcionalidad de registro de citas.

Los cambios se desarrollan en ramas de trabajo y posteriormente se integran a `main` mediante un Pull Request.

## Integración Continua

El proyecto utiliza GitHub Actions para ejecutar automáticamente las pruebas cada vez que se realizan cambios en el repositorio. El pipeline ejecuta Pytest y verifica que las pruebas finalicen correctamente.

## Pruebas

Actualmente el módulo cuenta con pruebas automatizadas para verificar el registro correcto de citas médicas.
