from src.lib.managedb import Managedb

def post_contacts(new_contact):
    md = Managedb()
    contacts = md.read_contacts()
    new_contact = new_contact.model_dump()
    
    contacts.append(new_contact)
    
    md.write_contact(contacts)
    
    return{
        "success": True,
        "message": "Added new contact"
    }