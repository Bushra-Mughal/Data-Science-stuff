# pip install numpy
# Note: 
# DONOT name your file 'numpy'. Python tries to import your file instead of the actual NumPy library, causing a circular import. 

import numpy as np
# Array creation using numpy functions:
array1=np.array([1,3] , dtype='i')  # 1D ---> NEED 1 INDEX TO ACCESS AN ELEMENT
array2=np.array([['1','3'],['3','4']])  # 1d+1d = 2D ---> NEED 2 INDICES TO ACCESS AN ELEMENT
array3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])  # 2d+2d = 3D ---> NEED 3 INDICES TO ACCESS AN ELEMENT
a=np.zeros(5,dtype='i')
b=np.arange(1,100,2)
c=np.random.rand(10) #---> WHAT DOES IT DO? IT HAS '3.1232e-01' THEN HOW COME IT IS 'BETWEEN 1 AND 0'
d=b.reshape(2,5,5)


# Array properties:
print(array1.ndim)
print(array2.ndim)
print(array3.ndim)
print(array1.dtype)
print(array2.dtype)
print(array3.dtype)
print(a.dtype)
print(array1.shape)
print(array2.shape)  #--> (2,2) is order of 2X2 matrix , are 2 one dimention arrays having 2 elements
print(array3.shape)
print(array1.size)
print(array2.size)
print(array3.size)
print(array2.nbytes)
print(a.nbytes)


## Slicing an array:  (one way of accesing numpy array)
# 1 D:
A = np.random.rand(20)
B = A[1:5]
B[0] = 1200
print(A)
# 2 D:
a=np.random.rand(4,2)
print(a[1,1:]) #--> WILL RETURN SECOND ROW ELEMENT INDEX 1 TILL END
print(a[1:3])  #---> WILL RETURN ROW 1 , 2
# 3 D:
b = np.random.rand(2,2,2)
print(b[0,0,1:]) #--> WILL RETURN FIRST 2D ARRAY'S FIRST 1D ARRAY'S ALL ELEMENTS 



## Sorting:
# 1D:
mat1 = np.random.rand(10)
mat1.sort(axis=0)      #WILL SORT ELEMENTS IN ROWS
print(mat1)
# 2D:
mat2 = np.random.rand(2,2)
mat2.sort(axis=0)     #--->WILL SORT ELEMENTS COLUMN WISE
print(mat2)
mat2.sort(axis=1)     #--->WILL SORT ELEMENTS ROWS WISE
print(mat2)


# Linear Algebra module:
import numpy.linalg as la
inv = np.linalg.inv(np.random.rand(2,2))  #---> INVERSE CANT BE ON 1D array
print(inv)



#Numpy Indexing and Masking:  (another way of accesing numpy array)  (gives copy of the array)
a = np.arange(4).reshape(2,2)   #---> a 2D array
print(a[1])
print( a[ [True,False]  ] )  #---> MASKING (accessing elements using boolean expression) 3D array , ACCESSING 1st and 3rd 2D array
print( (a>1) )               #---> return elements in form of True False
print( a(a>0) & (a<3) )       #---> return elements in form of True False


#BROADCASTING:  (numpy allows you to add an integer/coloumn with the matrix) (numpy adjusts the dimention for you)
a = np.random.rand(2,2)
print(a)
a = a + 100
print(a)
a += np.array([ 1 , 2 ])
print(a)
a += np.array( [[1],[2]])
print(a)
a -= np.array( [[1],[2]])
print(a)
a *= np.array( [[1],[2]])
print(a)
a /= np.array( [[1],[2]])
print(a)
a = a+(np.arange(2))
print(a)
a = a+(np.arange(2).reshape(2,1))
print(a)


##Random permutation:    (IN MATH---> 10! ways to arrange for 10 elements)
A = np.arange(9)                    #---> 0,1,2,3...
print( A )
array = np.random.permutation( A )  #---> 3,7,1...
print(array)
array.sort()                        #---> 0,1,2,3...
print(array)


#Numpy( hstack , vstack , sort(axis=0) ):   (universal funtions , for concatenation and sorting)
A = np.array( [ [1,2],[2,5] ])
B = np.arange(4).reshape(2,2)
C = np.hstack( (A,B))
D = np.vstack( (A,B))
print( C ,"\n",D)




#### NOTES:
##IF:
# a=np.array([[1],[1,2]])
##THEN:
# print(a.ndim)         #---> error , AS THERE IS NON-HOMOGENOUS DIMENTION

##AS:
# array=np.array([[[[1],[2]],[[1],[2]],[[1],[2]]],[[[3],[4]],[[3],[4]],[[3],[4]]]])
##THEREFORE:
# print(array.ndim)     #---> 4 , here 'n' is 'number of dimention'
# print(type(array))    #---> this is an object of class 'numpy.ndarray'

##TO FIND INDEX OF AN ELEMENT:
# array=np.array([[1,23,34],[23,5,6])
# index = np.argwhere( array==23 )[0][0]

##WHAT DOES ' a[::2 , :]' MEANS?
# c = np.array([[1,2],[3,4]])    #---> 2D array
# s=c[::2,:]           #---> SLICING ON 2D array
# print(s)

##SLICING (VIEW OF SAME MEMORY) V/S INDEXING (COPY OF MEMORY):
# c = np.arange(1,10)   #--> a 1D array
# b = c[3:6]            #---> b is a pointer
# b[1]=100
# print(c)
# b = c[5]              #---> b is another variable (copy)
# b = c[True]
# b = 2333
# print(c)

###USE OF ROUND OFF IN RAND ARRAY:
# array_1 = np.random.rand(2,2)
# array_2 = 10*(array_1)      #---> WILL SHIFT POINT TO RIGHT SIDE
# array_3 = np.round(array_2)
# print(array_1)
# print(array_2)
# print(array_3)


##OPERATORS MASKING:
##FOR ARRAYS       FOR NON-ARRAY
# &                     and
# |                      or
# ~                     not

