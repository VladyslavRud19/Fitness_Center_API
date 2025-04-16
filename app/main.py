import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from typing import List, Optional
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fitness Center API", debug=True)

# API ендпоінти для клієнтів
@app.post("/clients/", response_model=schemas.Client, tags=["Clients"])
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    db_client = crud.get_client_by_email(db, email=client.email)
    if db_client:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_client(db=db, client=client)


@app.get("/clients/", response_model=List[schemas.Client], tags=["Clients"])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clients = crud.get_clients(db, skip=skip, limit=limit)
    return clients


@app.get("/clients/{client_id}", response_model=schemas.Client, tags=["Clients"])
def read_client(client_id: int, db: Session = Depends(get_db)):
    db_client = crud.get_client(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client


@app.put("/clients/{client_id}", response_model=schemas.Client, tags=["Clients"])
def update_client(client_id: int, client: schemas.ClientUpdate, db: Session = Depends(get_db)):
    db_client = crud.update_client(db, client_id=client_id, client=client)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client


@app.delete("/clients/{client_id}", response_model=schemas.Client, tags=["Clients"])
def delete_client(client_id: int, db: Session = Depends(get_db)):
    db_client = crud.delete_client(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client


@app.post("/trainers/", response_model=schemas.Trainer, tags=["Trainers"])
def create_trainer(trainer: schemas.TrainerCreate, db: Session = Depends(get_db)):
    db_trainer = crud.get_trainer_by_email(db, email=trainer.email)
    if db_trainer:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_trainer(db=db, trainer=trainer)


@app.get("/trainers/", response_model=List[schemas.Trainer], tags=["Trainers"])
def read_trainers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    trainers = crud.get_trainers(db, skip=skip, limit=limit)
    return trainers


@app.get("/trainers/{trainer_id}", response_model=schemas.Trainer, tags=["Trainers"])
def read_trainer(trainer_id: int, db: Session = Depends(get_db)):
    db_trainer = crud.get_trainer(db, trainer_id=trainer_id)
    if db_trainer is None:
        raise HTTPException(status_code=404, detail="Trainer not found")
    return db_trainer


@app.put("/trainers/{trainer_id}", response_model=schemas.Trainer, tags=["Trainers"])
def update_trainer(trainer_id: int, trainer: schemas.TrainerUpdate, db: Session = Depends(get_db)):
    db_trainer = crud.update_trainer(db, trainer_id=trainer_id, trainer=trainer)
    if db_trainer is None:
        raise HTTPException(status_code=404, detail="Trainer not found")
    return db_trainer


@app.delete("/trainers/{trainer_id}", response_model=schemas.Trainer, tags=["Trainers"])
def delete_trainer(trainer_id: int, db: Session = Depends(get_db)):
    db_trainer = crud.delete_trainer(db, trainer_id=trainer_id)
    if db_trainer is None:
        raise HTTPException(status_code=404, detail="Trainer not found")
    return db_trainer


# API ендпоінти для абонементів
@app.post("/subscriptions/", response_model=schemas.Subscription, tags=["Subscriptions"])
def create_subscription(subscription: schemas.SubscriptionCreate, db: Session = Depends(get_db)):
    return crud.create_subscription(db=db, subscription=subscription)


@app.get("/subscriptions/", response_model=List[schemas.Subscription], tags=["Subscriptions"])
def read_subscriptions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    subscriptions = crud.get_subscriptions(db, skip=skip, limit=limit)
    return subscriptions


@app.get("/subscriptions/{subscription_id}", response_model=schemas.Subscription, tags=["Subscriptions"])
def read_subscription(subscription_id: int, db: Session = Depends(get_db)):
    db_subscription = crud.get_subscription(db, subscription_id=subscription_id)
    if db_subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return db_subscription


@app.put("/subscriptions/{subscription_id}", response_model=schemas.Subscription, tags=["Subscriptions"])
def update_subscription(subscription_id: int, subscription: schemas.SubscriptionUpdate, db: Session = Depends(get_db)):
    db_subscription = crud.update_subscription(db, subscription_id=subscription_id, subscription=subscription)
    if db_subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return db_subscription


@app.delete("/subscriptions/{subscription_id}", response_model=schemas.Subscription, tags=["Subscriptions"])
def delete_subscription(subscription_id: int, db: Session = Depends(get_db)):
    db_subscription = crud.delete_subscription(db, subscription_id=subscription_id)
    if db_subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return db_subscription


@app.post("/workouts/", response_model=schemas.Workout, tags=["Workouts"])
def create_workout(workout: schemas.WorkoutCreate, db: Session = Depends(get_db)):
    return crud.create_workout(db=db, workout=workout)


@app.get("/workouts/", response_model=List[schemas.Workout], tags=["Workouts"])
def read_workouts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    workouts = crud.get_workouts(db, skip=skip, limit=limit)
    return workouts


@app.get("/workouts/{workout_id}", response_model=schemas.Workout, tags=["Workouts"])
def read_workout(workout_id: int, db: Session = Depends(get_db)):
    db_workout = crud.get_workout(db, workout_id=workout_id)
    if db_workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return db_workout


@app.put("/workouts/{workout_id}", response_model=schemas.Workout, tags=["Workouts"])
def update_workout(workout_id: int, workout: schemas.WorkoutUpdate, db: Session = Depends(get_db)):
    db_workout = crud.update_workout(db, workout_id=workout_id, workout=workout)
    if db_workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return db_workout


@app.delete("/workouts/{workout_id}", response_model=schemas.Workout, tags=["Workouts"])
def delete_workout(workout_id: int, db: Session = Depends(get_db)):
    db_workout = crud.delete_workout(db, workout_id=workout_id)
    if db_workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return db_workout


@app.get("/clients/{client_id}/subscriptions/", response_model=List[schemas.Subscription], tags=["Clients"])
def read_client_subscriptions(client_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_client = crud.get_client(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    subscriptions = crud.get_client_subscriptions(db, client_id=client_id, skip=skip, limit=limit)
    return subscriptions


@app.get("/trainers/{trainer_id}/workouts/", response_model=List[schemas.Workout], tags=["Trainers"])
def read_trainer_workouts(trainer_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_trainer = crud.get_trainer(db, trainer_id=trainer_id)
    if db_trainer is None:
        raise HTTPException(status_code=404, detail="Trainer not found")
    workouts = crud.get_trainer_workouts(db, trainer_id=trainer_id, skip=skip, limit=limit)
    return workouts


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)
