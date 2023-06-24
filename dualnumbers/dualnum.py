import numpy as np
from numbers import Number 
from math import log
class DualNum:

    def __init__(self, real: int, epsilon: int):
        """Initializes DualNum

        Args:
            real (int): real portion of Dual Number
            epsilon (int):epsilon portion of Dual Number
        """
        self.real = real
        self.epsilon = epsilon

    def __str__(self):
        
        """Gets string representation of DualNum

        Returns:
            str: String representation of DualNum
        """
        return f'{self.real} + {self.epsilon}\u03B5' 

    def _add(self, other):
        """Overloads + operator for Dual Number

        Args:
            other (DualNum): DualNum to be added

        Raises:
            TypeError: Value must be DualNum or Number

        Returns:
            DualNum: Summation of Dual Numbers
        """
       
        if isinstance(other, DualNum):
            return DualNum(self.real + other.real, self.epsilon + other.epsilon)
        if isinstance(other, Number):
            return DualNum(self.real + Number, self.epsilon)
        else:
            raise TypeError("Unsupported type for add")
        
    def __add__(self,other):
        """Overloads + operator for Dual Number

        Args:
            other (DualNum): DualNum to be added

        Raises:
            TypeError: Value must be DualNum or Number

        Returns:
            DualNum: Summation of Dual Numbers
        """
        return self._add(other)
    
    def __radd__(self, other):
        """Overloads reverse + operator for Dual Number

        Args:
            other (DualNum): DualNum to be added

        Raises:
            TypeError: Value must be DualNum or Number

        Returns:
            DualNum: Summation of Dual Numbers
        """
        return self._add(other) 
    
    def _sub(self, other, first=True):
        """Overloads - operator for Dual Number

        Args:
            other (DualNum): value to be subtracted
            first (bool, optional): Flag for order in relation to operator. Defaults to True.

        Raises:
            TypeError: Value must be DualNum or Number

        Returns:
            DualNum: Difference between Dual Numbers
        """
        if first and isinstance(other, DualNum):
            return DualNum(self.real - other.real, self.epsilon - other.epsilon)
        elif first and isinstance(other, Number):
            return DualNum(self.real - other, self.epsilon)
        elif not first and isinstance(other, Number):
            return DualNum(other - self.real, -1 * self.epsilon)
        else:
            raise TypeError("Unsupported Type for __sub__")
        
    def __sub__(self, other):
        """Overloads - operator for Dual Number

        Args:
            other (DualNum): value to be subtracted

        Raises:
            TypeError: Value must be DualNum or Number

        Returns:
            DualNum: Difference between Dual Numbers
        """
        return self._sub(other)
    
    def __rsub__(self, other):
        """Overloads reverse - operator for Dual Number

        Args:
            other (DualNum): value to be subtracted
            first (bool, optional): Flag for order in relation to operator. Defaults to True.

        Raises:
            TypeError: Value must be DualNum or Number

        Returns:
            DualNum: Difference between Dual Numbers
        """
        return self._sub(other, self_first=False)
    
    def _mul(self, other):
        """Overloads * operator for DualNumbers 

        Args:
            other (DualNum): value to be multiplied

        Raises:
            TypeError: value must be DualNum or Number

        Returns:
            DualNum: returns product of Dual Numbers
        """
        if isinstance(other, DualNum):
            return DualNum(self.real * other.real, self.real * other.epsilon + self.epsilon * other.real)
        elif isinstance(other, Number):
            return DualNum(self.real * other, self.epsilon * other)
        else:
            raise TypeError("Unsupported Type for __mul__")
   
    def __mul__(self, other):
        """Overloads * operator for DualNumbers 

        Args:
            other (DualNum): value to be multiplied

        Raises:
            TypeError: value must be DualNum or Number

        Returns:
            DualNum: returns product of Dual Numbers
        """
        return self._mul(other)
    
    def __rmul__(self, other):
        """Overloads reverse * operator for DualNumbers 

        Args:
            other (DualNum): value to be multiplied

        Raises:
            TypeError: value must be DualNum or Number

        Returns:
            DualNum: returns product of Dual Numbers
        """
        return self._mul(other)
    
    def _div(self, other, self_numerator=True):
        """Overloads / operator for Dual 
        Args:
            other (DualNum): value to divide by 
            self_numerator (bool, optional): flag to tell if value is numerator or not. Defaults to True.

        Raises:
            ZeroDivisionError: Cannot divide by 0
            ZeroDivisionError: Cannot divide by 0
            ZeroDivisionError: Cannot divide by 0
            TypeError: Value must be DualNum or Number

        Returns:
            DualNum: difference between DualNum
        """
        if self_numerator and isinstance(other, DualNum):
            if other.real == 0:
                raise ZeroDivisionError("Attempting to divide by a zero")
            else:
                div_real = self.real / other.real
                div_dual = -1 * (self.real * other.epsilon- self.epsilon * other.real) / other.real ** 2
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
        """
        Overloads reverse / operator for Dual Numbers
        self_numerator: Flag for if value is numerator
        other: Dual Number to be divided
        returns: Quotient of Dual Division
        """
        return self._div(other, self_numerator=False)

    def __div__(self, other):
        """Overloads / operator for Dual 
        Args:
            other (DualNum): value to divide by 

        Raises:
            ZeroDivisionError: Cannot divide by 0
            ZeroDivisionError: Cannot divide by 0
            ZeroDivisionError: Cannot divide by 0
            TypeError: Value must be DualNum or Number

        Returns:
            DualNum: difference between DualNum
        """
        return self._div(other)

    def __rdiv__(self, other):
        """Overloads reverse / operator for Dual 
        Args:
            other (DualNum): value to divide by 

        Raises:
            ZeroDivisionError: Cannot divide by 0
            ZeroDivisionError: Cannot divide by 0
            ZeroDivisionError: Cannot divide by 0
            TypeError: Value must be DualNum or Number

        Returns:
            DualNum: difference between DualNum
        """ 
        return self._div(other, self_numerator=False)

    def _pow(self, other, self_base=True):
        """Overloads ** operator 

        Args:
            other (DualNum): DualNum
            self_base (bool, optional): flag to declare order in relation to operator Defaults to True.

        Raises:
            TypeError: Value must be DualNum or Number

        Returns:
            DualNum: DualNum raised to power
        """
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
        """Overloads ** operator

        Args:
            other (DualNum): DualNum Power

        Returns:
            DualNum: expontiated DualNum
        """
        return self._pow(other)

    def __rpow__(self, other):
        """Overloads reverse ** operator

        Args:
            other (DualNum): DualNum Base

        Returns:
            DualNum: exponentiated DualNum
        """
        return self._pow(other, self_base=False)

    def __cmp__(self, other):
        """
        Args:
            other (DualNum): Value to be compared to 

        Raises:
            TypeError: Value must be DualNum or number

        Returns:
            DualNum: Comparison Value 
        """
        if isinstance(other, DualNum):
            return self.real - other.real
        elif isinstance(other, Number):
            return self.real - other
        else:
            raise TypeError("Unsupported Type for __cmp__")
