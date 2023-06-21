from dualnum import DualNum
import math 
def sin(x):
    if isinstance(x, DualNum):
        return DualNum(math.sin(x.real), math.cos(x.real) * x.epsilon)
    else:
        return math.sin(x)
