from fastapi import FastAPI, Request, Form, Depends, status
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import models
from database import engine, SessionLocal

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def form_home(request: Request, db: Session = Depends(get_db)):
    favorites = db.query(models.Favorite).all()
    return templates.TemplateResponse("form.html", {"request": request, "favorites": favorites})

@app.post("/add", response_class=HTMLResponse)
async def add_favorite(username: str = Form(...), favorite_show: str = Form(...), db: Session = Depends(get_db)):
    new_entry = models.Favorite(username=username, favorite_show=favorite_show)
    db.add(new_entry)
    db.commit()
    return RedirectResponse("/", status_code=303)

@app.post("/update", response_class=HTMLResponse)
async def update_favorite(id: int = Form(...), favorite_show: str = Form(...), db: Session = Depends(get_db)):
    entry = db.query(models.Favorite).filter(models.Favorite.id == id).first()
    if entry:
        entry.favorite_show = favorite_show
        db.commit()
    return RedirectResponse("/", status_code=303)

@app.get("/delete/{id}", response_class=HTMLResponse)
async def delete_favorite(id: int, db: Session = Depends(get_db)):
    entry = db.query(models.Favorite).filter(models.Favorite.id == id).first()
    if entry:
        db.delete(entry)
        db.commit()
    return RedirectResponse("/", status_code=303)