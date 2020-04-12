#series:
# axes == Returns a list of the row axis labels
# dtype == Returns the dtype of the object.
# empty == Returns True if series is empty.
# ndim == Returns the number of dimensions of the underlying data, by definition 1.
# size == Returns the number of elements in the underlying data.
# values == Returns the Series as ndarray.
# head() == Returns the first n rows.
# tail() == Returns the last n rows.


########################################################
# import pandas as pd
# import numpy as np
# #Create a series with 100 random numbers
# s = pd.Series(np.random.randn(5))
# print(s)
# 0    3.003758
# 1   -1.625125
# 2   -0.395299
# 3    0.781908
# 4   -0.247127
# dtype: float64




########################################################
# import pandas as pd
# import numpy as np
# #Create a series with 100 random numbers
# s = pd.Series(np.random.randn(5))
# print(s.dtype)
# float64



########################################################
# import pandas as pd
# import numpy as np
# #Create a series with 100 random numbers
# s = pd.Series(np.random.randn(5))
# print(s.axes)
# [RangeIndex(start=0, stop=5, step=1)]



########################################################
# import pandas as pd
# import numpy as np
# #Create a series with 100 random numbers
# s = pd.Series(np.random.randn(4))
# print ("Is the Object empty?")
# print(s.empty)
# Is the Object empty?
# False



########################################################
# import pandas as pd
# import numpy as np
# #Create a series with 4 random numbers
# s = pd.Series(np.random.randn(4))
# print(s)
# print ("The dimensions of the object:")
# print(s.ndim)
# 0   -0.417240
# 1   -1.376671
# 2   -0.646602
# 3   -0.149123
# dtype: float64
# The dimensions of the object:
# 1




########################################################
# import pandas as pd
# import numpy as np
# #Create a series with 4 random numbers
# s = pd.Series(np.random.randn(2))
# print(s)
# print ("The size of the object:")
# print(s.size)
# 0    1.112680
# 1   -0.913148
# dtype: float64
# The size of the object:
# 2





########################################################
# import pandas as pd
# import numpy as np
# #Create a series with 4 random numbers
# s = pd.Series(np.random.randn(4))
# print(s)
# print ("The actual data series is:")
# print(s.values)
# 0    0.883875
# 1    2.141409
# 2    0.028212
# 3    1.741619
# dtype: float64
# The actual data series is:
# [0.8838754  2.14140934 0.02821167 1.74161896]







########################################################
# import pandas as pd
# import numpy as np
# #Create a series with 4 random numbers
# s = pd.Series(np.random.randn(4))
# print ("The original series is:")
# print(s)
# print ("The first two rows of the data series:")
# print(s.head(2))
# The original series is:
# 0    0.687686
# 1    0.176362
# 2   -1.556395
# 3    0.583936
# dtype: float64
# The first two rows of the data series:
# 0    0.687686
# 1    0.176362
# dtype: float64





########################################################
# import pandas as pd
# import numpy as np
# #Create a series with 4 random numbers
# s = pd.Series(np.random.randn(4))
# print ("The original series is:")
# print (s)
# print ("The last two rows of the data series:")
# print(s.tail(2))
# The original series is:
# 0    0.951026
# 1   -0.157518
# 2   -0.040028
# 3    1.253546
# dtype: float64
# The last two rows of the data series:
# 2   -0.040028
# 3    1.253546
# dtype: float64




########################################################
# DataFrame:
# T == Transposes rows and columns.
# axes == Returns a list with the row axis labels and column axis labels as the only members.
# dtypes == Returns the dtypes in this object.
# empty == True if NDFrame is entirely empty [no items]; if any of the axes are of length 0.
# ndim == Number of axes / array dimensions.
# shape == Returns a tuple representing the dimensionality of the DataFrame.
# size == Number of elements in the NDFrame.
# values == Numpy representation of NDFrame.
# head() == Returns the first n rows.
# tail() == Returns last n rows.
########################################################







########################################################
# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
#    'Age':pd.Series([25,26,25,23,30,29,23]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,14])}
# #Create a DataFrame
# df = pd.DataFrame(d)
# print ("Our data series is:")
# print (df)
# Our data series is:
#     Name   Age  Rating
# 0    Tom  25.0    4.23
# 1  James  26.0    3.24
# 2  Ricky  25.0    3.98
# 3    Vin  23.0    2.56
# 4  Steve  30.0    3.20
# 5  Smith  29.0    4.60
# 6   Jack  23.0    3.80
# 7    NaN   NaN   14.00




########################################################
# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
#    'Age':pd.Series([25,26,25,23,30,29,23]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,14])}
# #Create a DataFrame
# df = pd.DataFrame(d)
# print ("Our data series is:")
# print (df.T)
# Our data series is:
#            0      1      2     3      4      5     6    7
# Name     Tom  James  Ricky   Vin  Steve  Smith  Jack  NaN
# Age       25     26     25    23     30     29    23  NaN
# Rating  4.23   3.24   3.98  2.56    3.2    4.6   3.8   14





########################################################
# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
#    'Age':pd.Series([25,26,25,23,30,29,23]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
# #Create a DataFrame
# df = pd.DataFrame(d)
# print ("Row axis labels and column axis labels are:")
# print(df.axes)
# Row axis labels and column axis labels are:
# [RangeIndex(start=0, stop=7, step=1), Index(['Name', 'Age', 'Rating'], dtype='object')]
#




########################################################
# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
#    'Age':pd.Series([25,26,25,23,30,29,23]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
# #Create a DataFrame
# df = pd.DataFrame(d)
# print ("The data types of each column are:")
# print(df.dtypes)
# The data types of each column are:
# Name       object
# Age         int64
# Rating    float64
# dtype: object




########################################################
# import pandas as pd
# import numpy as np
# # Create a Dictionary of series
# d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
#      'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
#      'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8])}
# # Create a DataFrame
# df = pd.DataFrame(d)
# print("Is the object empty?")
# print(df.empty)
# Is the object empty?
# False



########################################################
# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
#    'Age':pd.Series([25,26,25,23,30,29,23]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
# #Create a DataFrame
# df = pd.DataFrame(d)
# print ("Our object is:")
# print(df)
# print ("The dimension of the object is:")
# print(df.ndim)
# Our object is:
#     Name  Age  Rating
# 0    Tom   25    4.23
# 1  James   26    3.24
# 2  Ricky   25    3.98
# 3    Vin   23    2.56
# 4  Steve   30    3.20
# 5  Smith   29    4.60
# 6   Jack   23    3.80
# The dimension of the object is:
# 2



########################################################
# import pandas as pd
# import numpy as np
# # Create a Dictionary of series
# d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
#      'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
#      'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8])}
# # Create a DataFrame
# df = pd.DataFrame(d)
# print("Our object is:")
# print(df)
# print("The shape of the object is:")
# print(df.shape)
# Our object is:
#     Name  Age  Rating
# 0    Tom   25    4.23
# 1  James   26    3.24
# 2  Ricky   25    3.98
# 3    Vin   23    2.56
# 4  Steve   30    3.20
# 5  Smith   29    4.60
# 6   Jack   23    3.80
# The shape of the object is:
# (7, 3)



########################################################
# import pandas as pd
# import numpy as np
# # Create a Dictionary of series
# d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
#      'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
#      'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8])}
# # Create a DataFrame
# df = pd.DataFrame(d)
# print("Our object is:")
# print(df)
# print("The total number of elements in our object is:")
# print(df.size)
# Our object is:
#     Name  Age  Rating
# 0    Tom   25    4.23
# 1  James   26    3.24
# 2  Ricky   25    3.98
# 3    Vin   23    2.56
# 4  Steve   30    3.20
# 5  Smith   29    4.60
# 6   Jack   23    3.80
# The total number of elements in our object is:
# 21




########################################################
# import pandas as pd
# import numpy as np
# # Create a Dictionary of series
# d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
#      'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
#      'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8])}
# # Create a DataFrame
# df = pd.DataFrame(d)
# print("Our object is:")
# print(df)
# print("The actual data in our data frame is:")
# print(df.values)
# Our object is:
#     Name  Age  Rating
# 0    Tom   25    4.23
# 1  James   26    3.24
# 2  Ricky   25    3.98
# 3    Vin   23    2.56
# 4  Steve   30    3.20
# 5  Smith   29    4.60
# 6   Jack   23    3.80
# The actual data in our data frame is:
# [['Tom' 25 4.23]
#  ['James' 26 3.24]
#  ['Ricky' 25 3.98]
#  ['Vin' 23 2.56]
#  ['Steve' 30 3.2]
#  ['Smith' 29 4.6]
#  ['Jack' 23 3.8]]
#
#
#





########################################################
# import pandas as pd
# import numpy as np
# # Create a Dictionary of series
# d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
#      'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
#      'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8])}
#
# # Create a DataFrame
# df = pd.DataFrame(d)
# print("Our data frame is:")
# print(df)
# print("The first two rows of the data frame is:")
# print(df.head(2))
# Our data frame is:
#     Name  Age  Rating
# 0    Tom   25    4.23
# 1  James   26    3.24
# 2  Ricky   25    3.98
# 3    Vin   23    2.56
# 4  Steve   30    3.20
# 5  Smith   29    4.60
# 6   Jack   23    3.80
# The first two rows of the data frame is:
#     Name  Age  Rating
# 0    Tom   25    4.23
# 1  James   26    3.24




########################################################
# import pandas as pd
# import numpy as np
# # Create a Dictionary of series
# d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
#      'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
#      'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8])}
# # Create a DataFrame
# df = pd.DataFrame(d)
# print("Our data frame is:")
# print(df)
# print("The last two rows of the data frame is:")
# print(df.tail(2))
# Our data frame is:
#     Name  Age  Rating
# 0    Tom   25    4.23
# 1  James   26    3.24
# 2  Ricky   25    3.98
# 3    Vin   23    2.56
# 4  Steve   30    3.20
# 5  Smith   29    4.60
# 6   Jack   23    3.80
# The last two rows of the data frame is:
#     Name  Age  Rating
# 5  Smith   29     4.6
# 6   Jack   23     3.8



