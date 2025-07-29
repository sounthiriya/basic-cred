from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/test")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/xyz")
def sys_page():
    return {"text": "Happy Monday!","addon": "Monday Blues!"}
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)