import pathlib
import json

class Managedb:
    __address_file = "{0}\\src\\db\\dbApp.json".format(pathlib.Path().absolute())
    
    def read_contacts(self):
        with open(self.__address_file, mode= "r") as data:
            return json.loads(data.read())
        
md = Managedb()

print(md.read_contacts())