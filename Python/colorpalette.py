import json 
import random

class ColorPalette:
    # TODO determine how to dynamically instantiate this class from a json file
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.json = self.load_json()
        
        try: 
            self.name = self.json['name']
        except KeyError:
            self.name = 'unnamed'

        try:
            self.description = self.json['description']
        except KeyError:
            self.description = 'no description'

        try:    
            self.colors = self.json['colors']
        except KeyError:
            e = Exception('No colors found in json file')
            raise e

    def load_json(self):
        with open(self.filepath, 'r') as f:
            return json.load(f)

    def random_color_hex(self)->str:
        return random.choice(self.colors)['hex']
