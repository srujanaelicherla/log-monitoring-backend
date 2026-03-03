from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import uuid

from app.database import SessionLocal, engine
from app import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/logs", response_model=schemas.LogResponse)
def create_log(log: schemas.LogCreate, db: Session = Depends(get_db)):
    new_log = models.LogDB(
        id=str(uuid.uuid4()),
        level=log.level,
        message=log.message
    )
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log

@app.get("/logs")
def get_logs(db: Session = Depends(get_db)):
    return db.query(models.LogDB).all()


@app.get("/alert")
def check_alert(db: Session = Depends(get_db)):
    error_count = db.query(models.LogDB).filter(models.LogDB.level == "error").count()
    
    if error_count > 3:
        return {"alert": "Too many ERROR logs!"}
    
    return {"alert": "System stable"}