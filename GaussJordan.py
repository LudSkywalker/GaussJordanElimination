class GaussJordanRow():

    data=[]

    def __init__(self,arr):
        self.data=arr
    
    def write_row(self,row,new_row):
        pass

    def __lshift__(self,other):
        self.write_row(other,self)
        
    def __rshift__(self,other):
        self.write_row(self,other)
        
    def __mul__(self,other):
        '''
        La función __mul__ multiplica un renglón de la matriz por una constante
        >>> r=GaussJordanRow([1,2,3])
        >>> r*3
        [3,6,9]
        '''
        product=[]
        for i in self.data:
            product.append(i*other)
        return GaussJordanRow(product)

class GaussJordanMatrix():

    rows=[]
    def __init__(self, arr):
        for row in arr:
            self.rows.append(GaussJordanRow(row))

        



