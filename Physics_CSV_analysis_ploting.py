import pandas as pd                         #-->for data processing
import numpy as np                          #-->for array operations
from sklearn.impute import SimpleImputer    # for missing value imputation
from matplotlib import pyplot as pp


##import a local csv dataset:
csv = pd.read_csv(r"H:\WORK Python\NUMPY PANDAS\physics_particles.csv")   # Prefix your string with r to make it a "raw string". This tells Python to treat backslashes as literal characters, not escape sequences.

#print(csv):
print(csv.head(10))

#Editing the dataset:
csv.rename(columns={'pdg_name' : 'Symbol','name':'Name' , 'quarks' : 'QUARKS'},inplace=True)
csv.drop(['pdg_id','rank','width_lower','width_upper','mass_lower','mass_upper'],axis=1,inplace=True)
print(csv.head())

#FOR CONVERTING THE DATE/TIME to PANDAS FORMAT
csv['date']=csv.to_datetime(csv['date'])  

# TO GET DATASET DETAIL:
print( csv.describe() )
print( csv.info() ) 

#HANDLE NULL VALUES:
csv.fillna('NA',inplace=True)
print(csv.head(10) )
# OR:
imputer = SimpleImputer( strategy='constant')
csv = pd.DataFrame(imputer.fit_transform( csv ), columns= csv.columns)
print( csv )


##GROUPING THE RECORDS:
print( csv.groupby('charge')[ ['charge','name']].sum() )    #---> reset_index() is not working here
print( csv.groupby(['charge','name'])[ ['charge','name']].sum() )    #--->will collect values by same charge and then by same name
print( csv[ csv['charge']>-1 ])    #-->WILL GIVE ALL ROWS HAVING CHARGE > -1

###PLOTING THE DATA:  (matplotlib)

#PLOTING REAL DATA:
pp.plot( csv['mass_lower'] , csv['mass_upper'])

x = np.linspace(0,10,100)
y = np.sin(x)
#Graph:
pp.plot( x , y , )
pp.xlabel('Independant')
pp.ylabel('Dependant')
pp.title('A graph')

#Scatter graph/plot:
pp.scatter( x , y, colorizer='red')

#Types of graphs:
pp.plot(x , x**2+1 , ':r')
pp.plot(x , x**3+2 , ':.k')
pp.plot(x , x**4+3 , '--c')
pp.show()

#Violin plot:
pp.violinplot(x)
pp.show()



