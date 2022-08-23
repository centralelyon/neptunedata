import json 
import os

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
    print(Nages.get_nages())