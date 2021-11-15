import numpy as np

#Arrays in NumPy: NumPy’s main object is the homogeneous multidimensional array.
mdarr = np.array( [ [1, 2, 3],
                  [4, 2, 5]] )
print("Array is of type: ", type(mdarr));

print("No. of dimensions: ", mdarr.ndim);

print("Shape of array: ", mdarr.shape);

print("Size of array: ", mdarr.size);

print("Array stores elements of type: ", mdarr.dtype);




