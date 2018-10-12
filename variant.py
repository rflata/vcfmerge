class variant:
    def __init__(self, var):
        self.chrom = var[0]
        self.pos = var[1]
        self.id = var[2]
        self.ref = var[3]
        self.alt = var[4]
        self.qual = var[5]
        self.filter = var[6]
        self.info = var[7]
        self.gt = '0|0'
    
    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other): 
        return self.__dict__ == other.__dict__