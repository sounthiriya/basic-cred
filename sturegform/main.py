from fastapi import FastAPI, HTTPException, Depends, status, Request, Form
from pydantic import BaseModel
from typing import Annotated
import models
from sqlalchemy import text
from database import engine, SessionLocal, Base
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")

class PostBase(BaseModel):
    title: str
    content: str
    user_id: int

class UserBase(BaseModel):
    username: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/posts/", status_code=status.HTTP_201_CREATED)
async def create_post(post: PostBase, db: db_dependency):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    return {"message": "Post created successfully"}

@app.get("/posts/{post_id}", status_code=status.HTTP_200_OK)
async def read_post(post_id: int, db: db_dependency):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post is None:
        HTTPException(status_code=404, detail = "Post not foun")
    return post

@app.delete("/posts/{post_id}", status_code=status.HTTP_200_OK)
async def delete_post(post_id: int, db: db_dependency):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    print(db_post)
    if db_post is None:
        raise HTTPException(status_code=404, detail='post not found')
    db.delete(db_post)
    db.commit()
    return {"message": "Post deleted successfully"}
    


@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(username: str = Form(...),id: int = Form(...), db: Session = Depends(get_db)):
    db_user = models.User(username=username, id =id)
    db.add(db_user)
    db.commit()
    return RedirectResponse(url="/", status_code=303)


#@app.post("/users/", status_code=status.HTTP_201_CREATED)
#async def create_user(user: UserBase, db: db_dependency):
#    query = text("INSERT INTO users (username) VALUES (:username)")
#    db.execute(query, {"username": user.username})
#    db.commit()
#    return {"message": "User created successfully"}

# @app.get("/get-users", status_code=status.HTTP_200_OK)
# async def read_user(request: Request, user_id: int = None, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == user_id).first()
#     if user:
#         return templates.TemplateResponse("form.html", {"request": request, "username": user.username})
#     else:
#         return templates.TemplateResponse("form.html", {"request": request, "error": "User not found"})
    
@app.get("/get-user", response_class=HTMLResponse)
async def get_user_form(request: Request, user_id: int = None, db: Session = Depends(get_db)):
    print("Received user_id:", user_id)  # 🔍 Debug line
    user = db.query(models.User).filter(models.User.id == user_id).first()
    print("DB Query Result:", user)
    if user:
        return templates.TemplateResponse("form.html", {"request": request, "username": user.username})
    else:
        return templates.TemplateResponse("form.html", {"request": request, "error": "User not found"})
    
@app.post("/update-user", response_class=HTMLResponse)
async def update_user(
    request: Request,
    user_id: int = Form(...),
    new_username: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.username = new_username
        db.commit()
        return templates.TemplateResponse("form.html", {"request": request, "update_success": f"User ID {user_id} updated to '{new_username}'"})
    else:
        return templates.TemplateResponse("form.html", {"request": request, "update_error": "user Not found"})

@app.post("/delete-user", response_class=HTMLResponse)
async def delete_user(
    request: Request,
    delete_user_id: int = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.id == delete_user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return templates.TemplateResponse("form.html", {
            "request": request,
            "delete_success": f"User ID {delete_user_id} has been deleted."
        })
    else:
        return templates.TemplateResponse("form.html", {
            "request": request,
            "delete_error": "User not found"
        })
    
@app.get("/test-all-users")
def test_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return [{"id": u.id, "username": u.username} for u in users]
        

@app.get("/", response_class=HTMLResponse)
async def form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})



