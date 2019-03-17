# import numpy
import numpy as np

# --------- EXC01 : Create an array of 10 zeros
print(np.zeros(10))

# --------- EXC02 : Create an array of 10 ones
print(np.ones(10))

# --------- EXC03 : Create an array of 10 fives
print(np.ones(10)*5)

# --------- EXC04 : Create an array of the integers from 10 to 50
print(np.arange(10, 51, 1))

# --------- EXC05 : Create an array of all the even integers from 10 to 50
print(np.arange(10, 51, 2))

# --------- EXC06 : Create a 3x3 matrix with values ranging from 0 to 8
print(np.reshape(np.arange(0, 9), [3,3]))

# --------- EXC07 : Create a 3x3 identity matrix
print(np.identity(3))

# --------- EXC08 : Use NumPy to generate a random number between 0 and 1
print(np.random.random())

# --------- EXC09 : Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
print(np.random.randn(25))

# --------- EXC10 : Create the following matrix
print(np.arange(1, 101, 1).reshape(10,10)/100)

# --------- EXC11 : Create an array of 20 linearly spaced points between 0 and 1
print(np.linspace(0, 1, 20))

# --------- EXC12 :
# Replicate de following results in the given the matrix
# array([[ 1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10],
#        [11, 12, 13, 14, 15],
#        [16, 17, 18, 19, 20],
#        [21, 22, 23, 24, 25]])
mat = np.arange(1,26).reshape(5,5)
print(mat)

# array([[12, 13, 14, 15],
#        [17, 18, 19, 20],
#        [22, 23, 24, 25]])
print(mat[2:, 1:])

# --------- EXC13 :
# 20
print(mat[3][4])

# --------- EXC14 :
# array([[ 2],
#        [ 7],
#        [12]])
print(mat[0:3, 1].reshape(3,1))

# --------- EXC15 :
# array([21, 22, 23, 24, 25])
print(mat[-1:, :])

# --------- EXC16 :
# array([[16, 17, 18, 19, 20],
#        [21, 22, 23, 24, 25]])
print(mat[-2:, :])

# --------- EXC17 : Get the sum of all the values in mat
print(np.sum(mat))

# --------- EXC18 : Get the standard deviation of the values in mat
print(np.std(mat))

# --------- EXC19 : Get the sum of all the columns in mat
print(np.sum(mat, axis=0))


