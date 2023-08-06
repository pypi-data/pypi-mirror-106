import os
import json
import sys
from pathlib import Path

HOMEDIR = str(Path.home())

class FavoritesManager():
    def __init__(self, name=None):
        if name is None:
            configs_path = os.path.join(HOMEDIR, ".config", "marker")
            if not os.path.exists(configs_path):
                os.makedirs(configs_path, exist_ok=True)
            name = os.path.join(configs_path, "favorites.json")
        
        self.fname = name
        try:
            with open(name) as handle:
                self.data = json.load(handle)
        except FileNotFoundError:
            self.data = []
    
    def addFavorite(self, path):
        abspath = os.path.abspath(path)
        if abspath not in self.data:
            self.data.append(os.path.abspath(path))
            with open(self.fname, "w") as handle:
                json.dump(self.data, handle, indent=2)

    def removeFavorite(self, path):
        abspath = os.path.abspath(path)
        if abspath in self.data:
            self.data.remove(abspath)
            with open(self.fname, "w") as handle:
                json.dump(self.data, handle, indent=2)

    def getFavorites(self):
        response = []
        for path in self.data:
            response.append({'path': path, 'name': os.path.basename(path)})
        return response
