class Vector:

    """Represent a vector in a multidimensional space """

    def __init__(self, d):
        """Create d dimensional vector of zeros"""
        self._coords = [0]*d

    def len(self):
        """Return the dimension of the vector"""
        return len(self._coords)

    def get_item(self, j):
        """Return jth coordinate of the vector"""
        return self._coords[j]

    def set_item(self, j, val):
        """Set jth coordinate of the vector to the given value"""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors"""
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """"Return True if vectors have same coordinate as other"""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differ from other"""
        return not self == other

    def __str__(self):
        """Produce a string representation of vector"""
        return '<' + str(self._coords)[1:-1] + '>'
