import numpy as np


def compute_strassen_multiplication(matrix_1,matrix_2):
    # print(matrix_1,'\n',matrix_2)
    new_array = np.zeros(matrix_1.shape)
    row_shape,column_shape = matrix_1.shape
    # print(row_shape,column_shape)

    for common_count in range(row_shape):
        for row in range(row_shape):
            for column in range(column_shape):
                # print("Before :",new_array[row,column],matrix_1[row,common_count],matrix_2[common_count,column])
                new_array[row,column]+= matrix_1[row,common_count]*matrix_2[common_count,column]
                # print("After :",new_array[row,column],matrix_1[row,common_count],matrix_2[common_count,column])

    print(new_array)
mat_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
mat_2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

compute_strassen_multiplication(mat_1,mat_2)
print(np.dot(mat_1,mat_2))