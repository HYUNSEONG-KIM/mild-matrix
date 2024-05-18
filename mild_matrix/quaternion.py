class Quaternion:
    def __init__(self, o=0, i=0, j=0, k=0):
        self.o = o
        self.i = i
        self.j = j
        self.k = k
    @property
    def arr(self):
        return [self.o, self.i, self.j, self.k]
    def __str__(self):
        oper = [("+" if a>0 else "-") for a in self.arr]
        return f"{self.o}{oper[1]}{self.i}{oper[2]}{self.j}{oper[3]}{self.k}"
    def __repr__(self):
        return "Quaternion({},{},{},{})".format(*self.arr)
    def __add__(self, other):
        su = [
            self.o + other.o,
            self.i + other.i,
            self.j + other.j,
            self.k + other.k
        ]
        return Quaternion(*su)
    def __sub__(self,other):
        su = [
            self.o - other.o,
            self.i - other.i,
            self.j - other.j,
            self.k - other.k
        ]
        return Quaternion(*su)
    def __mul__(self, other):
        a0, a1, a2, a3 = self.o, self.i, self.j, self.k
        b0, b1, b2, b3 = other.o, other.i, other.j, other.k
        r0 = a0*b0 - a1*b1 - a2*b2 - a3*b3
        r1 = a0*b1 + a1*b0 + a2*b3 - a3*b2  
        r2 = a0*b2 - a1*b3 + a2*b0 + a3*b1  
        r3 = a0*b3 + a1*b2 - a2*b1 + a3*b0  
        return Quaternion(r0, r1, r2, r3)