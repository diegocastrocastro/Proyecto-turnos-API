# Proyecto de Optimización de Turnos con Algoritmos Genéticos y FastAPI

Servicio backend desarrollado en **FastAPI** que implementa un modelo de optimización basado en **Algoritmos Genéticos** (`PyGAD`) para la asignación y programación automatizada de turnos de trabajo.

---

## 📂 Estructura del Proyecto

El repositorio está organizado bajo estándares profesionales de desarrollo en Python:

```text
Proyecto-turnos/
├── .python-version      # Versión de Python definida para el entorno
├── pyproject.toml       # Configuración y dependencias del proyecto
├── src/
│   ├── __init__.py      # Paquete fuente
│   ├── main.py          # Aplicación principal de FastAPI y endpoints
│   └── optimizer.py     # Lógica central del algoritmo genético
└── tests/
    ├── __init__.py      # Paquete de pruebas
    └── test_main.py     # Pruebas unitarias con pytest