import pandas as pd

## Slicing the Data Frame
## Convert a dictionary into a pandas Data Frame along with index to the left
XYZ_web= {'Day':[1,2,3,4,5,6], "Visitors":[1000, 700,6000,1000,400,350], "Bounce_Rate":[20,20, 23,15,10,34]}
df= pd.DataFrame(XYZ_web)
print(df)
print('*' * 40)
## First 2 rows of data
print("THE FIRST TWO ROWS OF DATA : ")
print(df.head(2))
## Last 2 rows of data
print("THE LAST TWO ROWS OF DATA : ")
print(df.tail(2))

## Merging and Joining
import pandas as pd

df1= pd.DataFrame({ "HPI":[80,90,70,60],"Int_Rate":[2,1,2,3],"IND_GDP":[50,45,45,67]}, index=[2001, 2002,2003,2004])

df2=pd.DataFrame({ "HPI":[80,90,70,60],"Int_Rate":[2,1,2,3],"IND_GDP":[50,45,45,67]}, index=[2005, 2006,2007,2008])

merged= pd.merge(df1,df2)

print(merged)



