class Matrix:
    def __init__(self,rows,cols,fill_value=0):
        self.rows=rows
        self.cols=cols
        self.data=[[fill_value for _ in range(cols)] for _ in range(rows)]
    def __getitem__(self, key):
        row,col=key
        if row>=self.rows or col >=self.cols:
            raise IndexError("Index out of range")
        return  self.data[row][col]
    def __setitem__(self, key, value):
        row,col=key
        if row>=self.rows or col>=self.cols:
            raise IndexError("Index out of range")
        self.data[row][col]=value
        

matrix = Matrix(2, 3)

matrix[0,0]=4
matrix[0,1]=3
matrix[0,2]=2
matrix[1,0]=5
matrix[1,1]=6
matrix[1,2]=7

print(matrix[0,0])
print(matrix[0,1])
print(matrix[1,0])
print(matrix[1,1])
print(matrix[1,2])


print(matrix.data)