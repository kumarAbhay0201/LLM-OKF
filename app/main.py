from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.routes.query import router as knowledge_router
from app.routes.knowledge import router as graph_router


FRONTEND_DIR = Path(__file__).resolve().parents[1] / "frontend"


app = FastAPI(
    title="LLM OKF",
    description=(
        "A persistent LLM knowledge system "
        "using Open Knowledge Format."
    ),
    version="0.1.0",
)


app.include_router(knowledge_router)
app.include_router(graph_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return FileResponse(FRONTEND_DIR / "index.html")


@app.get("/health")
def health():

    return {
        "status": "healthy",
    }


app.mount(
    "/",
    StaticFiles(directory=FRONTEND_DIR),
    name="frontend",
)