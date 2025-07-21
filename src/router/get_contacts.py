from src.lib.managedb import Managedb

def get_contacts():
    md = Managedb()
    return md.read_contacts()