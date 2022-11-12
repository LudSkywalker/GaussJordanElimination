class GaussJordanRow():
    
    def write_row(self,row,new_row):
        pass

    def __lshift__(self,other):
        self.write_row(other,self)
        
    def __rshift__(self,other):
        self.write_row(self,other)
        
    def __mul__(self,other):
        product=[]
        for i in self:
            product.append(self.data[i]*other)

class GaussJordanMatrix():

    rows=[]
    def __init__(self, arr):

        for i in range(len(arr)):
            self.rows.append(GaussJordanRow)