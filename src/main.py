from fastapi import FastAPI
from src.optimizer import ejecutar_optimizacion

app = FastAPI(
    title="API de Optimización de Turnos",
    description="Servicio online para generar horarios laborales mediante algoritmos genéticos.",
    version="1.0.0"
)

@app.get("/health", tags=["Monitoreo"])
def health_check():
    """Endpoint de verificación de salud requerido para producción."""
    return {"status": "ok"}

@app.post("/predict", tags=["Optimización"])
def predict_horario():
    """Ejecuta el modelo de optimización y retorna el horario libre de violaciones."""
    resultado = ejecutar_optimizacion()
    return {
        "mensaje": "Optimización completada con éxito",
        "detalles": resultado
    }