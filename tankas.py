
class Tankas:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.kryptis = "Š"
        self.suviai = [0, 0, 0, 0]

    def info(self):
        print(f"Koordinatės: x: {self.x}, y: {self.y}, kryptis: {self.kryptis}")

    def siaure(self):
        self.y += 1
        self.kryptis = "Š"
        self.info()

    def pietus(self):
        self.y -= 1
        self.kryptis = "P"
        self.info()

    def vakarai(self):
        self.x -= 1
        self.kryptis = "V"
        self.info()

    def rytai(self):
        self.x += 1
        self.kryptis = "R"
        self.info()