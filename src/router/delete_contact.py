from src.lib.managedb import Managedb
from fastapi import HTTPException

def delete_contact(id_contact):
    md = Managedb()
    contacts = md.read_contacts()
    
    for index, contact in enumerate(contacts):
        if contact["id"] == id_contact:
            contacts.pop(index)
            
            md.write_contact(contacts)
            
            return{
                "success": True,
                "message": "Deleted complete"
            }
            
    raise HTTPException(status_code=404, detail="Contact not found")