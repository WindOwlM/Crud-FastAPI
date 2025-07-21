from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4 as uudi
from src.router.get_contacts import get_contacts
from src.router.get_contact import get_contact
from src.router.post_contacts import post_contacts
from src.router.put_contacts import put_contacts
from src.router.delete_contact import delete_contact

class Contact_model(BaseModel):
    id: str = str(uudi())
    name: str
    phone: str

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hi Im Maicol"}

@app.get("/api/contacts")
def get_all_contacts():
    return get_contacts()

@app.get("/api/contacts/{id_contact}")
def get_single_contact(id_contact:str):
    return get_contact(id_contact)
    

@app.post("/api/contacts")
def add_contact(new_contact: Contact_model):
    return post_contacts(new_contact)
    
@app.put("/api/contacts/{id_contact}")
def update_contact(id_contact:str, new_contact:Contact_model):
    return put_contacts(id_contact,new_contact)

@app.delete("/api/contacts/{id_contact}")
def remove_contact(id_contact:str):
    return delete_contact(id_contact)