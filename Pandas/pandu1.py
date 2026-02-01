from pandas import *
from numpy import *
s = Series(random.randn(10))
print(s)
print("Row axis Label of the series: ",s.axes)
print("datatype of series is:",s.dtype)
print ("Is the Object empty?: ", s.empty)
print("no of dimension are: ", s.ndim)
print("No of elements in this series are: ", s.size)
print("Series elements in the form of array are:", s.values)
print("First three rows of series are: ",s.head(3))
print("Last four rows of series are",s.tail(4))