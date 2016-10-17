class fraction(object):
    def __init__(self,n=None,d=None):
        self.numerator = n
        self.denominator = d

    def __str__(self):
        return "%s / %s" % (self.numerator , self.denominator)

    def numerator(self,n):
        self.numerator = n 

    def denominator(self,d):
        self.denominator = d

    def __mul__(self,rhs):
        x = self.numerator * rhs.numerator
        y = self.denominator * rhs.denominator
        return fraction(x,y)
        
    def __add__(self,rhs):
        x = (self.numerator * rhs.denominator) + (rhs.numerator * self.denominator)
        y = (self.denominator * rhs.denominator)
        return fraction(x,y)
