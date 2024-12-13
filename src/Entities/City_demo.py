class City:
    def __init__(self, code = "", name = ""):
        self.code = code
        self.name = name
    
    def from_tuple(self, data):
        self.code = data[1]
        self.name = data[2]