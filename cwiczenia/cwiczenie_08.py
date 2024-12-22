class Square(object):
    
    def __init__(self, side=1):

        self.side = side

    @property
    def side(self):
        return self._side
    

    @side.setter
    def side(self, value):
        if value < 0:
            raise ValueError("Side nie moze byc mniejszy od 0")
        self._side = value


    def __add__(self, other):
        return Square(self.side + other.side)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return Square(self.side * other.side)
        elif isinstance(other, int):
            return Square(self.side * other)
        else:
            print("XXX")
            # raise NotImplementedError("Nie zaimplementowano dla tego typu")
            return NotImplemented
        
    def __rmul__(self, other):
        return self.__mul__(other)


    def __repr__(self):
        return f"<Square({self.side})>"


"""
dodać metodę obliczajaca pole powierzni

"""

if __name__ == "__main__":

    s = Square(10)
    assert s.area == 100  # 100
    s.area = 25
    assert s.side  == 5