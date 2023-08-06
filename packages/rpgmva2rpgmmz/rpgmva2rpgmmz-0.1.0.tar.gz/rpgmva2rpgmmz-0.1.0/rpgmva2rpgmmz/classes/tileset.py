from struct import *
import json

from rubymarshal.classes import RubyObject, UserDef, registry

class Tileset(RubyObject):
    ruby_class_name = "RPG::Tileset"

    def tojson(self):

        #Convert from rubmarshalstr to str
        tilesetNames = []
        
        for i in self.attributes["@tileset_names"]:
            if i == b'':
                tilesetNames.append("")
            else:
                tilesetNames.append(str(i))

        if self.attributes["@name"] == b'':
            self.attributes["@name"] = ""

        if self.attributes["@note"] == b'':
            self.attributes["@note"] = ""
        

        todump = {
            "id": self.attributes["@id"],
            "flags": self.attributes["@flags"].flags,
            "mode": self.attributes["@mode"],
            "name": str(self.attributes["@name"]),
            "note": str(self.attributes["@note"]),
            "tilesetNames": tilesetNames
        }

        return todump

class Table(UserDef):
    ruby_class_name = "Table"
    flags = []
    
    def _load(self, private_data):
        self.flags = list(unpack("@8192H", private_data[0x14:]))
        return

registry.register(Table)
registry.register(Tileset)