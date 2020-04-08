series:
axes == Returns a list of the row axis labels
dtype == Returns the dtype of the object.
empty == Returns True if series is empty.
ndim == Returns the number of dimensions of the underlying data, by definition 1.
size == Returns the number of elements in the underlying data.
values == Returns the Series as ndarray.
head() == Returns the first n rows.
tail() == Returns the last n rows.
============================================================
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




# import pandas as pd
# import numpy as np
# #Create a series with 100 random numbers
# s = pd.Series(np.random.randn(5))
# print(s.axes)
# [RangeIndex(start=0, stop=5, step=1)]


# import pandas as pd
# import numpy as np
# #Create a series with 100 random numbers
# s = pd.Series(np.random.randn(4))
# print ("Is the Object empty?")
# print(s.empty)
# Is the Object empty?
# False


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

=================================================

DataFrame:
T == Transposes rows and columns.
axes == Returns a list with the row axis labels and column axis labels as the only members.
dtypes == Returns the dtypes in this object.
empty == True if NDFrame is entirely empty [no items]; if any of the axes are of length 0.
ndim == Number of axes / array dimensions.
shape == Returns a tuple representing the dimensionality of the DataFrame.
size == Number of elements in the NDFrame.
values == Numpy representation of NDFrame.
head() == Returns the first n rows.
tail() == Returns last n rows.

