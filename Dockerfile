# Utiliza la imagen oficial de Python 3.11 slim para mantener el contenedor ligero
FROM python:3.11-slim

# Instala uv utilizando la imagen oficial de astral-sh para una gestión rápida de dependencias
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de configuración de dependencias
COPY pyproject.toml uv.lock ./

# Instala solo las dependencias de producción (sin herramientas de desarrollo ni pruebas)
RUN uv sync --frozen --no-dev

# Copia el código fuente del proyecto
COPY src/ ./src/

# Expone el puerto en el que corre FastAPI
EXPOSE 8000

# Comando por defecto para ejecutar la aplicación con uvicorn
CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]