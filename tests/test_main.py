from fastapi.testclient import TestClient
from src.main import app
from src.optimizer import ejecutar_optimizacion

client = TestClient(app)

def test_health_check():
    """Valida que el endpoint de salud responda correctamente."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_predict_endpoint():
    """Valida que el endpoint de optimización retorne un estado exitoso y la estructura esperada."""
    response = client.post("/predict")
    assert response.status_code == 200
    data = response.json()
    assert data["mensaje"] == "Optimización completada con éxito"
    assert "detalles" in data

def test_optimizer_direct_execution():
    """Valida que la función de optimización interna ejecute y retorne un fitness válido."""
    resultado = ejecutar_optimizacion()
    assert isinstance(resultado, dict)
    assert "fitness" in resultado
    assert "horario" in resultado
    assert len(resultado["horario"]) == 42  # 42 asignaciones totales (7 personas x 6 turnos)