from app.core.event_handler import startup_event, shutdown_event
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router as api_router
from fastapi import FastAPI

app = FastAPI(
    title="AI-Driven Cyber Attack Simulation and Response Tool",
    description="Cyber attack simulation, AI-based detection, and reporting.",
    version="0.1.0"
)

app.add_event_handler("startup", startup_event)
app.add_event_handler("shutdown", shutdown_event)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

app.include_router(api_router)

