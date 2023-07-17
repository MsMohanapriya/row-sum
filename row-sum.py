import numpy as np
def RowSum(matrix):
    
    row_sum_array=[]
    for i in range(row):
        sum=0
        for j in range(column):
            sum+=matrix[i][j]
        row_sum_array.append(sum)
    return row_sum_array
    
    
row =int(input("Enter row count: "))
column=int(input("enter column count:"))
array=list(map(int,input("enter matrix values: ").split()))
matrix=np.array(array).reshape(row,column)
print(RowSum(matrix))