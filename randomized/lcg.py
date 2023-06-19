class lcg:
    """
    n: Range to generate for [0, n - 1]
    a: selects a 
    b: selects b
    """
    def __init__(self,a:int  = 131, n:int = 2 ** 32 - 1):
        self.n = n 
        self.x = 1 
        self.a = 131
        self.b = 3
    """
    Generates value from [0, n-1]
    """
    def generate(self) -> int: 
        self.x = (self.a * self.x + self.b) % self.n
        return self.x

        