class cube():
    
    def __init__(self, L=1.0):
        self.L = L

    def set_L(self, L):
        self.L = L

    def get_volume(self):
        return self.L**3

    def get_area(self):
        return 6.0*self.L**2
