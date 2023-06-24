from dualnum import DualNum
import math 

def sin(x):
    """Performs sin operator on DualNum

    Args:
        x (DualNum): DualNum 

    Returns:
        DualNum or Number: Resultant value of sin operator on DualNum 
    """
    if isinstance(x, DualNum):
        return DualNum(math.sin(x.real), math.cos(x.real) * x.epsilon)
    else:
        return math.sin(x)

def cos(x):
    """Performs cos operator on DualNum

    Args:
        x (DualNum): DualNum

    Returns:
        DualNum or Number: Resultant value of cos operator on DualNum 
    """
    if isinstance(x,DualNum):
        return DualNum(math.cos(x.real), -math.sin(x.real) * x.epsilon)
    else:
        return math.cos(x)
        
def tan(x):
    """Performs tan operator on DualNum 

    Args:
        x (DualNum): DualNum

    Returns:
        DualNum or Number: Resultant value of tan operator on DualNum 
    """
    if isinstance(x, DualNum):
        return DualNum(math.tan(x), math.sec(x.real)**2 * x.epsilon)
    else:
        return math.sec(x)**2

def ln(x):
    """Performs ln operator on DualNum

    Args:
        x (DualNum): DualNum

    Returns:
        DualNum or Number: Resultant value of ln operator on DualNum
    """
    if isinstance(x,DualNum):
        return DualNum(math.ln(x.real), (1/x.real) * x.epsilon)
    else:
        return math.ln(x)
def log(x):
    """Performs log operator on DualNum

    Args:
        x (DualNum): DualNum

    Returns:
        DualNum or Number: Resultant value of log operator on DualNum
    """
    if isinstance(x, DualNum):
        return DualNum(log(x.real), x.epsilon/x.real)
    else:
        return log(x)
def sqrt(x):
    """Performs sqrt operator on DualNum

    Args:
        x (DualNum): DualNum

    Returns:
        DualNum: Resultant value of sqrt operator on DualNum
    """
    if isinstance(x, DualNum): 
       return DualNum(math.sqrt(x.real), (0.5 / math.sqrt(x.real)) * x.real) 
    else:
        return sqrt(x)
 
