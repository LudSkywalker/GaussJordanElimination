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

    def elimination(self,arr):
        '''
        Debe tomar la matrix con una lista de resultados y halla el valor de cada variable
        >>> GaussJordanMatrix([[1,0],[1,1]]).elimination([1,0])
        [{'name':'entrada', 'data':[[1,0,1],[1,1,0]]},{'name':'paso 1', 'data':[[1,0,1],[0,1,-1]]}]

        >>> GaussJordanMatrix([[2,0],[1,1]],[1,0])
        [{'name':'entrada', 'data':[[2,0,1],[1,1,0]]},{'name':'paso 1', 'data':[[1,0,0.5],[1,1,0]]},{'name':'paso 2', 'data':[[1,0,0.5],[0,1,-0.5]]}]

        >>> GaussJordanMatrix([[0,2],[1,1]],[1,0])
        [{'name':'entrada', 'data':[[0,2,1],[1,1,0]]},{'name':'paso 1', 'data':[[1,1,0],[0,2,1]]},{'name':'paso 2', 'data':[[1,1,0],[0,1,0.5]]},{'name':'paso 3', 'data':[[1,0,-0.5],[0,1,0.5]]}]

        '''
        pass
        
        

mat=GaussJordanMatrix([[1,2,3],[4,5,6],[7,8,9]])
# newrow=mat.rows[0]*5
# newrow.show_row()

# newrow=mat.rows[0]+mat.rows[1]
# newrow.show_row()
# mat.rows[0] << mat.rows[0]*5
# mat.rows[0].show_row()
# mat.show_matrix()
