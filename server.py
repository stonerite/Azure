"""
Azure Buddy AI - Production-grade FastAPI Server.
Modular architecture with separated core, knowledge, repository, and api layers.
"""

from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from core.config import settings
from api.routes import router as api_router

BASE_DIR = settings.base_dir
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description="Unofficial AZ-900 Study Assistant with East African analogies and AI intelligence."
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount API routes
app.include_router(api_router)

# Mount Static UI assets
if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

@app.get("/", response_class=HTMLResponse)
async def serve_index():
    """Serve the single-page AI study interface."""
    index_file = STATIC_DIR / "index.html"
    if not index_file.exists():
        index_file = BASE_DIR / "index.html"
    if index_file.exists():
        with open(index_file, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Azure Buddy AI Server is running. UI assets not found.</h1>"

if __name__ == "__main__":
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=settings.port,
        reload=False
    )
