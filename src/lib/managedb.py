import pathlib
import json
from pathlib import Path

class Managedb:
    BASE_DIR = Path(__file__).resolve().parent.parent  # apunta a "src"
    ADDRESS_FILE = BASE_DIR / "db" / "dbApp.json"
    
    def read_contacts(self):
        with open(self.ADDRESS_FILE, mode= "r") as data:
            return json.loads(data.read())

    def write_contact(self,new_data):
        with open(self.ADDRESS_FILE, "w") as data:
            data.write(json.dumps(new_data))
