class GaussJordanRow():
    data=[]

    def __init__(self,arr):
        self.data=arr
    
    def write_row(self,row,new_row):
        row=new_row

    def __lshift__(self,other):
        self.write_row(other,self)
        
    def __rshift__(self,other):
        self.write_row(self,other)
        
    def __mul__(self,other):
        '''
        La función __mul__ multiplica un renglón de la matriz por una constante
        >>> r1=GaussJordanRow([1,2,3])
        >>> (r1*3).data
        [3, 6, 9]
        >>> r2=GaussJordanRow([2,5,8])
        >>> (r2*5).data
        [10, 25, 40]
        >>> r3=GaussJordanRow([4,8,10])
        >>> (r3*9).data
        [36, 72, 90]
        '''
        product=[]
        for i in self.data:
            product.append(i*other)
        return GaussJordanRow(product)

    def show_row(self):
        for col in self.data:
            print(str(col)+",",end="")
        print("")
    
    def __add__(self, other):
        new_row = []
        row_actually = self.data
        row_to_plus = self.other
        if len(row_actually) == len(row_to_plus):
            for i in range(len(row_actually)):
                new_row.append(row_actually[i] + other[i])
            return  GaussJordanRow(new_row)
        else:
            print("Los elementos son distintos")
        


class GaussJordanMatrix():

    rows=[]
    def __init__(self, arr):
        for row in arr:
            self.rows.append(GaussJordanRow(row))
    def show_matrix(self):
        for row in self.rows:
            for col in row.data:
                print(str(col)+",",end="")
            print()
        

mat=GaussJordanMatrix([[1,2,3],[4,5,6],[7,8,9]])
newrow=mat.rows[0]*5
print((newrow).data)
# newrow=mat.rows[0]+mat.rows[1]
# newrow.show_row()
# mat.show_matrix()



