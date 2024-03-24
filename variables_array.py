variables_array=[1,2,3,4,5,6,7,8,8]

# 1. Variables unidimensionales de enteros
int_array1 = np.array([1, 2, 3, 4, 5, 6])

# 2. Variables unidimensionales de flotantes
float_array1 = np.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6])

# 3. Variables unidimensionales de texto
str_array1 = np.array(['a', 'b', 'c', 'd', 'e', 'f'])

# 4. Variables unidimensionales de enteros, flotantes y texto
mixed_array1 = np.array([1, 2.2, 'c', 4, 5.5, 'f'])

# 5. Variables bidimensionales de enteros
int_array2x3 = np.array([[1, 2, 3], [4, 5, 6]])
int_array5x5 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
int_array3x6 = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]])

# 6. Variables bidimensionales de flotantes
float_array2x3 = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])
float_array5x5 = np.array([[1.1, 2.2, 3.3, 4.4, 5.5], [6.6, 7.7, 8.8, 9.9, 10.1], [11.11, 12.12, 13.13, 14.14, 15.15], [16.16, 17.17, 18.18, 19.19, 20.20], [21.21, 22.22, 23.23, 24.24, 25.25]])
float_array3x6 = np.array([[1.1, 2.2, 3.3, 4.4, 5.5, 6.6], [7.7, 8.8, 9.9, 10.1, 11.11, 12.12], [13.13, 14.14, 15.15, 16.16, 17.17, 18.18]])

# 7. Variables bidimensionales de texto
str_array2x3 = np.array([['a', 'b', 'c'], ['d', 'e', 'f']])
str_array5x5 = np.array([['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']])
str_array3x6 = np.array([['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p', 'q', 'r']])

# 8. Variables bidimensionales de enteros, flotantes y texto
mixed_array2x3 = np.array([[1, 2.2, 'c'], [4, 5.5, 'f']])
mixed_array5x5 = np.array([[1, 2.2, 'c', 4, 5.5], [6, 7.7, 'h', 9, 10.1], [11, 12.12, 'm', 14, 15.15], [16, 17.17, 'r', 19, 20.20], [21, 22.22, 'w', 24, 25.25]])
mixed_array3x6 = np.array([[1, 2.2, 'c', 4, 5.5, 'f'], [7, 8.8, 'i', 10.1, 11.11, 'l'], [13, 14.14, 'o', 16, 17.17, 'r']])

# 9. Variables tridimensionales de enteros
int_array2x3x2 = np.array([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]])
int_array5x5x5 = np.array([[[i+j+k for i in range(5)] for j in range(5)] for k in range(5)])
int_array3x6x2 = np.array([[[i+j for i in range(3)] for j in range(6)] for _ in range(2)])

# 10. Variables tridimensionales de flotantes
float_array2x3x1 = np.array([[[1.1], [2.2], [3.3]], [[4.4], [5.5], [6.6]]])
float_array5x5x2 = np.array([[[i+j for i in range(5)] for j in range(5)] for _ in range(2)])
float_array3x6x5 = np.array([[[i+j*0.1 for i in range(3)] for j in range(6)] for _ in range(5)])

# 11. Variables tridimensionales de texto
str_array2x3x3 = np.array([[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']], [['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r']]])
str_array5x5x4 = np.array([[[chr(97+i*5+j*25+k) for i in range(5)] for j in range(5)] for k in range(4)])
str_array3x6x1 = np.array([[[chr(97+i+j*3) for i in range(3)] for _ in range(6)] for j in range(1)])

# 12. Variables tridimensionales de enteros, flotantes y texto
mixed_array2x3x2 = np.array([[[1,