
# Python program to demonstrate 
# unary operators in numpy 
import numpy as np 
  
arr = np.array([[1, 5, 6], 
                [4, 7, 2], 
                [3, 1, 9]]) 
  
# maximum element of array 
print ("Largest element is:", arr.max()) 
print ("Row-wise maximum elements:", arr.max(axis = 1)) 
  
# minimum element of array 
print ("Column-wise minimum elements:", arr.min(axis = 0)) 
  
# sum of array elements 
print ("Sum of all array elements:", arr.sum()) 
  
# cumulative sum along each row 
print ("Cumulative sum along each row:\n",arr.cumsum(axis = 1)) 

a = np.array([[1, 2], 
            [3, 4]]) 
b = np.array([[4, 3], 
            [2, 1]]) 
  
# add arrays 
print ("Array sum:\n", a + b) 
  
# multiply arrays (elementwise multiplication) 
print ("Array multiplication:\n", a*b) 
  
# matrix multiplication 
print ("Matrix multiplication:\n", a.dot(b)) 


