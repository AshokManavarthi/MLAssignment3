# Python Program illustrating
# numpy.reshape() method

import numpy as geek

# array = geek.arrange(6)
# The 'numpy' module has no attribute 'arrange'
array1 = geek.arange(6)
print("Original array : \n", array1)

# shape array with 3 rows and 2 columns
array2 = geek.arange(6).reshape(3, 2)
print("\narray reshaped with 3 rows and 2 columns : \n",
	array2)

# shape array with 2 rows and 3 columns
array3 = geek.arange(6).reshape(2, 3)
print("\narray reshaped with 2 rows and 3 columns : \n",
	array3)

