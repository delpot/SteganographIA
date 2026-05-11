"""
SteganographIA — Backend API

Point d'entrée principal de l'application FastAPI.
"""

from fastapi import FastAPI

app = FastAPI(
    title="SteganographIA API",
    description="API de protection des œuvres d'art par stéganographie, IA et blockchain.",
    version="0.1.0",
)


@app.get("/")
def read_root() -> dict[str, str]:
    """Endpoint de bienvenue, utile pour vérifier que l'API tourne."""
    return {
        "name": "SteganographIA API",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    """Endpoint de health check pour le monitoring."""
    return {"status": "ok"}