import os

class Analyzer(object):

    def __init__(self, model_path):
        if os.path.isdir(model_path):
            self.model_path = model_path
        else:
            self.model_path = None

    def get_model_path(self):
        return self.model_path

if __name__ == "__main__":
    a = Analyzer("../scad")
    print(a.get_model_path())
