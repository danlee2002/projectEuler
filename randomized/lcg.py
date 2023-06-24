class lcg:
    
    def __init__(self,a:int  = 131, n:int = 2 ** 32 - 1):
        """Initalizes lcg instance

        Args:
            a (int, optional): sets value of A. Defaults to 131.
            n (int, optional): sets range of randomly generated integers. Defaults to 2**32-1.
        """
        self.n = n 
        self.x = 1 
        self.a = 131
        self.b = 3
    
    def generate(self) -> int:
        """Generates randomized value 

        Returns:
            int: randomized value based on LCG 
        """
        self.x = (self.a * self.x + self.b) % self.n
        return self.x

        