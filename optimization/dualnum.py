import numpy as np
from numbers import Number 
from math import log
class DualNum:
    """
    Initializes Dual Number where Dual Number is of form real number + epsilon
    real: real portion of Dual
    epsilon: epsilon portion of Dual
    """
    def __init__(self, real: int, epsilon: int):
        self.real = real
        self.epsilon = epsilon

    """
    Returns string representation of DualNumbers
    returns Real and Epsilon component of string
    """
    def __str__(self):
        return f'{self.real} + {self.epsilon}\u03B5'
    
    """
    Sums DualNumber together
    other: DualNumber to be added
    returns: elementwise summation of DualNumbers
    """
    def _add(self, other):
        if isinstance(other, DualNum):
            return DualNum(self.real + other.real, self.epsilon + other.epsilon)
        if isinstance(other, Number):
            return DualNum(self.real + Number, self.epsilon)
        else:
            raise TypeError("Unsupported type for add")
        
    """
    Addition operator for Dual Numbers 
    returns: elementwise summation of DualNumbers
    """
    def __add__(self,other):
        return self._add(other)
    
    """
    Addition operator for Dual Numbers where one number has no dual part
    returns: elementwise summation of DualNumbers
    """
    def __radd__(self, other):
        return self._add(other) 
    


    """
    Subtraction operator for DualNumbers
    first: denotes position with subtraction operator
    returns: elementwise difference of DualNumbers 
    """
    def _sub(self, other, first=True):
        if first and isinstance(other, DualNum):
            return DualNum(self.real - other.real, self.epsilon - other.epsilon)
        elif first and isinstance(other, Number):
            return DualNum(self.real - other, self.epsilon)
        elif not first and isinstance(other, Number):
            return DualNum(other - self.real, -1 * self.epsilon)
        else:
            raise TypeError("Unsupported Type for __sub__")
        
    """
    Generic subtraction operator for DualNumber operator 
    """
    def __sub__(self, other):
        return self._sub(other)
    
    """
    Subtraction operator for DualNumber with Real Number
    """
    def __rsub__(self, other):
        return self._sub(other, self_first=False)
    
    """
    Multiplication operator for DualNumbers 
    """
    def _mul(self, other):
        if isinstance(other, DualNum):
            return DualNum(self.real * other.real, self.real * other.epsilon + self.epsilon * other.real)
        elif isinstance(other, Number):
            return DualNum(self.real * other, self.epsilon * other)
        else:
            raise TypeError("Unsupported Type for __mul__")


    """
    Overloads the mult operator for dual numbers
    """
    def __mul__(self, other):
       
        return self._mul(other)
    """
    Overloads the reverese multoperator for dual numbers
     """
    def __rmul__(self, other):
       
        return self._mul(other)


        
    """
    Division operator for dual numbers
    self_numerator: flag for order in operator 
    returns: Quotient of Dual Division
    """
    def _div(self, other, self_numerator=True):
   
        if self_numerator and isinstance(other, DualNum):
            if other.real == 0:
                raise ZeroDivisionError("Attempting to divide by a zero")
            else:
                div_real = self.real / other.real
                div_dual = -1 * (self.real * other.complex- self.complex * other.real) / other.real ** 2
                return DualNum(div_real, div_dual)
        elif self_numerator and isinstance(other, Number):
            if other == 0:
                raise ZeroDivisionError("Attempting to divide by a zero")
            else:
                return DualNum(self.real / other, self.epsilon / other)
        elif not self_numerator and isinstance(other, Number):
            if self.real == 0:
                raise ZeroDivisionError("Attempting to divide by a zero")
            else:
                return DualNum(other / self.real, -1 * (other * self.epsilon) / self.real ** 2)
        else:
            raise TypeError("Unsupported Type for __div__")
        
    def __truediv__(self, other):
        
        return self._div(other)

    def __rtruediv__(self, other):
       
        return self._div(other, self_numerator=False)

    def __div__(self, other):
        
        return self._div(other)

    def __rdiv__(self, other):
        return self._div(other, self_numerator=False)

    """
    Power operator for Dual Numbers
    self_base: flag to determine if number is base or not
    """
    def _pow(self, other, self_base=True):
       
        if self_base and isinstance(other, Number):
            return DualNum(self.real ** other, self.epsilon * other * (self.real ** (other - 1)))
        elif self_base and isinstance(other, DualNum):
            new_real = self.real ** other.real
            new_dual = (self.real ** (other.real - 1)) * (self.real * other.epsilon * log(self.real) + other.real * self.epsilon)
            return DualNum(new_real, new_dual)
        elif not self_base and isinstance(other, Number):
            return DualNum(other ** self.real, (other ** self.real) * self.epsilon * log(other))
        else:
            raise TypeError("Unsupported Type for __pow__")
  
    def __pow__(self, other):
        return self._pow(other)

    def __rpow__(self, other):
        
        return self._pow(other, self_base=False)

    def __cmp__(self, other):
        if isinstance(other, DualNum):
            return self.real - other.real
        elif isinstance(other, Number):
            return self.real - other
        else:
            raise TypeError("Unsupported Type for __cmp__")

