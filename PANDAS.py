import pandas as pd

#TO GET PANDAS VERSION:
print(pd.__version__)

## (1) Creating a pandas series:

data = pd.Series([ 1,3,5 ],index=['a','b','c'])

print(data)          
print(type(data))           #--->a pandas object 
print(data.values)  
print(type(data.values))    #--->a 1D numpy array (numpy object)
print(data.index)
print(data.index.values)
print(type(data.index))    #---->a pandas object attached to series , In pandas/NumPy, text data (strings) is stored using the object dtype by default.

### (2) Creating a pandas series:
marks_sys_dic = { 'A+': 85 , 'A': 79 ,'B+': 75 ,'B': 69 ,'F': 20}  #-->key=index , values=values
gpa_sys_dic = { 'A+': 4 , 'A': 3.5 ,'B+': 3 ,'B': 2.5 ,'F': 1 }
marks_series = pd.Series( marks_sys_dic )
print(marks_series)

### Accessing series elements using their index: (think of it as a list)
print(data['a'])
## Slicing:
print( data[0:2])       #--->  explicit indexes are used

### Creating pandas dataframes:  (2D array,3D etc)  extention of series datastructure
marks = [12 , 23 , 34 , 45]
gpa =   [4 , 3.5 , 3 , 2.5]
# data = pd.DataFrame( [marks , gpa] , index=['A','B','C','D'])             #-->error AS 'INDEX' HERE IS 'COLUMN'
data = pd.DataFrame( {'MARKS':marks , 'GPA':gpa} , index=['A','B','C','D'])
print(data)


marks_sys_dic = { 'A+': 85 , 'A': 79 ,'B+': 75 ,'B': 69 ,'F': 20 }  #-->key=index , values=values
gpa_sys_dic   = { 'A+': 4 , 'A': 3.5 ,'B+': 3 ,'B': 2.5 ,'F': 1 }
grading_system = pd.DataFrame( {"Marks" : marks_sys_dic ,"GPA" : gpa_sys_dic} )
print( grading_system )
print( grading_system.T )    #-->transpose

## NOW , TAKE IT AS A DICTIONARY:
grading_system['percentage']=(grading_system['Marks']/100)*100
print( grading_system )
del grading_system['percentage']
print( grading_system )

## YOU CAN DO MASKING AS WELL , to filterate dataframe:  (just as you did in numpy)
print(  grading_system['Marks'] > 70)
print(  grading_system['Marks'] > 70)
print( grading_system[ (grading_system['GPA'] > 2) & (grading_system['GPA'] < 3.5) ] )

## MISSING VALUE PROBLEM:  pandas(NaN)
# B = pd.Series([12,34,45],index=['a','b','c','d'])  #--->NaN VALUES CAN'T BE IN SERIES

A = pd.DataFrame({ "A": {'a' : 2 , 'b' : 5 } ,"B": {'b' : 3 , 'c': 6} })  #-->rows are in a dic
A = pd.DataFrame([ {'a' : 2 , 'b' : 5 } , {'b' : 3 , 'c': 6} ])          #--->rows are in a list
print(A)
A = A.fillna(0)  #--> we can't use A.=fillna(0) AS METHODS CAN'T BE WITH A '='
print(A)

## INDEXING: (using iloc() loc() then same as SLICING in numpy)
A = pd.DataFrame({ "A": {'a' : 2 , 'b' : 5 , 'd' : 78} ,"B": {'b' : 3 , 'c': 6} })
print(A)
print()
B = pd.Series( [12,23,34] )
print(B)

print( A.iloc[:,1:3].fillna(0) )   #--->same as numpy, WILL ACCESS ALL ROWS and 1 , 2 COLUMN
print( A.iloc[1:3] )          #---> WILL ACCESS 1,2 COLUMN
# print( A.loc[1:3] )    #--> error as 'A' and 'B' are defining 'columns' in A
print( B.loc[1:3] )

 