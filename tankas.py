
class Tankas:
    def __init__(self):
        self._x = 0
        self._y = 0
        self._kryptis = "Š"
        self._suviai = [0, 0, 0, 0]

    def info(self):
        print(f"Koordinatės: x: {self._x}, y: {self._y}, kryptis: {self._kryptis}")
        print(f"Šūviai: {sum(self._suviai)}, kryptys: {self._suviai}")

    def siaure(self):
        self._y += 1
        self._kryptis = "Š"
        self.info()

    def pietus(self):
        self._y -= 1
        self._kryptis = "P"
        self.info()

    def vakarai(self):
        self._x -= 1
        self._kryptis = "V"
        self.info()

    def rytai(self):
        self._x += 1
        self._kryptis = "R"
        self.info()

    def sauti(self):
        if self._kryptis == "Š":
            self._suviai[0] += 1
        if self._kryptis == "P":
            self._suviai[1] += 1
        if self._kryptis == "V":
            self._suviai[2] += 1
        if self._kryptis == "R":
            self._suviai[3] += 1
        self.info()



