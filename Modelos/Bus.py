# python
from __future__ import annotations
from datetime import date
from typing import Optional
from pydantic import constr
from sqlmodel import SQLModel, Field
from Utils.enumeracion import Marca_Bus

class BusBase(SQLModel):
    marca: Marca_Bus = Field(..., description="Marca del bus")
    modelo: int = Field(..., description="Modelo del bus")
    placa: str = Field(..., description="Placa formato 111AAA")
    soat: int = Field(..., description="SOAT formato de 10 dígitos")
    fecha_soat: date = Field(..., description="Fecha de vencimiento del SOAT")
    tecnomecanica: int = Field(..., description="Tecnomecánica formato de 10 dígitos")
    fecha_tecnomecanica: date = Field(..., description="Fecha de vencimiento de la Tecnomecánica")


class Bus(BusBase, table=True):
    Bus_id: int = Field(default=None, primary_key=True)

class BusCreate(BusBase):
    pass

class BusUpdate(BusBase):
    pass

class BusDelete(BusBase):
    pass
