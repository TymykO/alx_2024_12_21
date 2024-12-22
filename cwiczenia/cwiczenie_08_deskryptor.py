class PositiveSide:
    """Ta klasa to tzw deskryptor"""
    def __init__(self):
        self.name = None

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, obj, owner=None):
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        # if value < 0:
        #     raise ValueError("Side nie moze byc ujemny")
        setattr(obj, self.name, value)

class Square(object):

    side = PositiveSide()
    
    def __init__(self, side=1):

        self.side = side

    @property
    def area(self):
        return self.side ** 2
    
    @area.setter
    def area(self, value):
        self.side = value ** 0.5


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