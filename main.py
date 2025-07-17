from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hi Im Maicol"}

@app.get("/api/contacts")
def get_all_contacts():
    