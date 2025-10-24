from fastapi import FastAPI
import Routers.Bus

from db import create_tables

app = FastAPI(lifespan=create_tables, title="API de Gestión de Buses", version="1.0.0")

app.include_router(Routers.Bus.router)