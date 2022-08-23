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

class Nages:

    def __init__(self):
        self.get_nages()

    def get_nages():
        path_nages = os.path.join(os.path.dirname(__file__), 'nages.json')
        var_nages = {}

        with open(path_nages) as d:
            var_nages = json.load(d)
            return var_nages

if __name__ == '__main__':
    print(Sexes.get_sexes())
    print(Nages.get_nages())