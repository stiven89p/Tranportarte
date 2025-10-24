from typing import List
from fastapi import APIRouter, HTTPException
from Modelos.Bus import Bus, BusCreate, BusUpdate, BusDelete
from Utils.enumeracion import Marca_Bus as MarcaBus
from datetime import date
from fastapi import Form
from db import SessionDep


router = APIRouter(prefix="/Bus", tags=["buses"])


@router.post("/", response_model=Bus)
def create_bus(session: SessionDep,
               marca: MarcaBus = Form(...),
                modelo: int = Form(...),
                placa: str = Form(...),
                soat: int = Form(...),
                fecha_soat: date = Form(...),
                tecnomecanica: int = Form(...),
                fecha_tecnomecanica: date = Form(...),
               ):
    new_bus = Bus(
        marca=marca,
        modelo=modelo,
        placa=placa,
        soat=soat,
        fecha_soat=fecha_soat,
        tecnomecanica=tecnomecanica,
        fecha_tecnomecanica=fecha_tecnomecanica
    )

    session.add(new_bus)
    session.commit()
    session.refresh(new_bus)
    return new_bus

@router.get("/", response_model=List[Bus])
def get_buses(session: SessionDep):
    buses = session.query(Bus).all()
    return buses

@router.put("/{bus_id}", response_model=Bus)
def update_bus(bus_id: int, bus_update: BusUpdate, session: SessionDep):
    db_bus = session.get(Bus, bus_id)
    if not db_bus:
        raise HTTPException(status_code=404, detail="Bus not found")

    bus_data = bus_update.model_dump(exclude_unset=True)
    for key, value in bus_data.items():
        setattr(db_bus, key, value)

    session.add(db_bus)
    session.commit()
    session.refresh(db_bus)
    return db_bus

@router.delete("/{bus_id}", response_model=Bus)
def delete_bus(bus_id: int, session: SessionDep):
    db_bus = session.get(Bus, bus_id)
    if not db_bus:
        raise HTTPException(status_code=404, detail="Bus not found")

    session.delete(db_bus)
    session.commit()
    return db_bus
