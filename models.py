import json 
import os

class Sexes:

    def __init__(self):
        self.get_sexes()

    def get_sexes():
        path_sexes = os.path.join(os.path.dirname(__file__), 'sexes.json')
        var_sexes = {}

        with open(path_sexes) as d:
            var_sexes = json.load(d)
            return var_sexes

if __name__ == '__main__':
    print(Sexes.get_sexes())