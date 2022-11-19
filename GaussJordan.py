class GaussJordanRow():
    data = []

    def __init__(self, arr):
        self.data = arr

    def write_row(self, row, new_row):
        row.data = new_row.data
        '''
        Esta funciona con el operador mágico Bitwise Right Shift permitiendo el cambio de filas
        >>> mat=GaussJordanMatrix([[1,2,3],[4,5,6],[7,8,9]])
        >>> mat.rows[0] << (mat.rows[0]*10)
        >>> mat.rows[0] 
        [10, 20, 30]
        
        >>> mat.rows[2] << mat.rows[1]
        >>> mat.rows[2] 
        [4, 5, 6]
        
        >>> mat.rows[1] << (mat.rows[1]*2)
        >>> mat.rows[1] 
        [8, 10, 12]

        '''

    def __lshift__(self, other):
        self.write_row(self, other)

    def __rshift__(self, other):
        self.write_row(other, self)

    def __mul__(self, other):
        '''
        La función __mul__ multiplica un renglón de la matriz por una constante
        >>> r=GaussJordanRow([1,2,3])
        >>> r*3
        [3,6,9]
        '''
        product = []
        for i in self.data:
            product.append(i*other)
        return GaussJordanRow(product)

    def show_row(self):
        for col in self.data:
            print(str(col)+",", end="")
        print("")

    def __add__(self, other):
        """ 
        >>> m1 = GaussJordanRow([1,2,3])
        >>> m2 = GaussJordanRow([2,3,1])
        >>> m3 = GaussJordanRow([3,4,5])
        >>> result1 = m1 + m2
        >>> result1.data
        [3, 5, 4]
        >>> result2 = m2 + m3
        >>> result2.data
        [5, 7, 6]
        >>> result3 = m1 + m3
        >>> result3.data
        [4, 6, 8]
        """
        new_row = []
        row_actually = self.data
        row_to_plus = other.data
        if len(row_actually) == len(row_to_plus):
            for i in range(len(row_actually)):
                new_row.append(row_actually[i] + row_to_plus[i])
            return GaussJordanRow(new_row)
        else:
            print("Los elementos son distintos")


class GaussJordanMatrix():

    rows = []

    def __init__(self, arr):
        for row in arr:
            self.rows.append(GaussJordanRow(row))

    def show_matrix(self):
        for row in self.rows:
            for col in row.data:
                print(str(col)+",", end="")
            print()

    def elimination(self, arr):
        # '''
        # Debe tomar la matrix con una lista de resultados y halla el valor de cada variable
        # >>> GaussJordanMatrix([[1,0],[1,1]]).elimination([1,0])
        # [{'name':'entrada', 'data':[[1,0,1],[1,1,0]]},{'name':'paso 1', 'data':[[1,0,1],[0,1,-1]]}]

        # >>> GaussJordanMatrix([[2,0],[1,1]],[1,0])
        # [{'name':'entrada', 'data':[[2,0,1],[1,1,0]]},{'name':'paso 1', 'data':[[1,0,0.5],[1,1,0]]},{'name':'paso 2', 'data':[[1,0,0.5],[0,1,-0.5]]}]

        # >>> GaussJordanMatrix([[0,2],[1,1]],[1,0])
        # [{'name':'entrada', 'data':[[0,2,1],[1,1,0]]},{'name':'paso 1', 'data':[[1,1,0],[0,2,1]]},{'name':'paso 2', 'data':[[1,1,0],[0,1,0.5]]},{'name':'paso 3', 'data':[[1,0,-0.5],[0,1,0.5]]}]

        # '''
        result=GaussJordanRow(self.rows)
        for i in range(len(self.rows)):
            self.rows[i].data.append(arr[i])

        for i in range(len(self.rows)):
            if self.rows[i].data[i] == 0:
                temp = GaussJordanRow([])
                temp << self.rows[i]
                self.rows[i] << self.rows[i+1]
                self.rows[i+1] << temp
            self.rows[i] << self.rows[i]*(1/self.rows[i].data[i])
            for j,rows in enumerate(self.rows):
                if rows.data[i] != 0 and i!=j:
                    rows << ((rows*(1/rows.data[i])) + (self.rows[i]*-1))

        for i in range(len(self.rows)):
            self.rows[i] << self.rows[i]*(1/self.rows[i].data[i])
            
        for row in self.rows:
            new_data=[]
            for el in row.data:
                new_data.append(round(el))
            row.data = new_data

        self.show_matrix()


mat = GaussJordanMatrix([[2, 4,6], [4, 5,6],[3, 1,-2]])
# newrow=mat.rows[0]*5
# newrow.show_row()
# newrow=mat.rows[0]+mat.rows[1]
# newrow.show_row()
# mat.rows[0] << mat.rows[0]*10
# mat.rows[0].show_row()
# mat.show_matrix()
mat.elimination([18, 24,4])
# mat.show_matrix()
