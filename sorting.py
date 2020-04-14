########################################################
# There are two kinds of sorting available in Pandas. They are −
# == By label
# == By Actual Value


#Iteration PY

# The behavior of basic iteration over Pandas objects depends on the type.
# When iterating over a Series, it is regarded as array-like, and basic iteration produces the values.
# Other data structures, like DataFrame and Panel,
# follow the dict-like convention of iterating over the keys of the objects.
# In short, basic iteration (for i in object) produces −
# == Series − values
# == DataFrame − column labels
# == Panel − item labels

# iteritems() − to iterate over the (key,value) pairs
# iterrows() − iterate over the rows as (index,series) pairs
# itertuples() − iterate over the rows as namedtuples


#############################################################
# import pandas as pd
# import numpy as np
#
# N = 10
# df = pd.DataFrame({
#     'A': pd.date_range(start='2016-01-01', periods=N, freq='D'),
#     'x': np.linspace(0, stop=N - 1, num=N),
#     'y': np.random.rand(N),
#     'C': np.random.choice(['Low', 'Medium', 'High'], N).tolist(),
#     'D': np.random.normal(100, 10, size=(N)).tolist()
# })
# print(df)
#            A    x         y       C           D
# 0 2016-01-01  0.0  0.901285  Medium   79.178591
# 1 2016-01-02  1.0  0.954155     Low  108.926116
# 2 2016-01-03  2.0  0.028031    High   94.766280
# 3 2016-01-04  3.0  0.414206     Low  102.345479
# 4 2016-01-05  4.0  0.981745     Low  103.265062
# 5 2016-01-06  5.0  0.828964    High  100.159072
# 6 2016-01-07  6.0  0.383194  Medium   94.512110
# 7 2016-01-08  7.0  0.514841    High  104.424106
# 8 2016-01-09  8.0  0.033926     Low  104.183054
# 9 2016-01-10  9.0  0.853429  Medium  107.071822




#############################################################
# import pandas as pd
# import numpy as np
#
# N = 20
# df = pd.DataFrame({
#     'A': pd.date_range(start='2016-01-01', periods=N, freq='D'),
#     'x': np.linspace(0, stop=N - 1, num=N),
#     'y': np.random.rand(N),
#     'C': np.random.choice(['Low', 'Medium', 'High'], N).tolist(),
#     'D': np.random.normal(100, 10, size=(N)).tolist()
# })
#
# for col in df:
#     print(col)
#
# A
# x
# y
# C
# D




#############################################################
# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {
#    'Age':pd.Series([25,26,25,23,30,29]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20])
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df)
# for i,j in df.iteritems():
#     print(i)
#
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN
# Age
# Rating





#############################################################
# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {
#    'Age':pd.Series([25,26,25,23,30,29]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20])
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df)
# for i,j in df.iteritems():
#     print(j)
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN
# 0    25
# 1    26
# 2    25
# 3    23
# 4    30
# 5    29
# Name: Age, dtype: int64
# 0    4.23
# 1    3.24
# 2    3.98
# 3    2.56
# 4    3.20
# 5     NaN
# Name: Rating, dtype: float64




#############################################################
# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {
#    'Age':pd.Series([25,26,25,23,30,29]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20])
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df)
# for i,j in df.iteritems():
#     print(i,j)
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN
# Age 0    25
# 1    26
# 2    25
# 3    23
# 4    30
# 5    29
# Name: Age, dtype: int64
# Rating 0    4.23
# 1    3.24
# 2    3.98
# 3    2.56
# 4    3.20
# 5     NaN
# Name: Rating, dtype: float64





#############################################################
# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {
#    'Age':pd.Series([25,26,25,23,30,29]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20])
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df)
# for i,j in df.iterrows():
#     print(i)
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN
# 0
# 1
# 2
# 3
# 4
# 5



#############################################################
# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {
#    'Age':pd.Series([25,26,25,23,30,29]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20])
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df)
# for i,j in df.iterrows():
#     print(j)
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN
# Age       25.00
# Rating     4.23
# Name: 0, dtype: float64
# Age       26.00
# Rating     3.24
# Name: 1, dtype: float64
# Age       25.00
# Rating     3.98
# Name: 2, dtype: float64
# Age       23.00
# Rating     2.56
# Name: 3, dtype: float64
# Age       30.0
# Rating     3.2
# Name: 4, dtype: float64
# Age       29.0
# Rating     NaN
# Name: 5, dtype: float64




#############################################################
# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {
#    'Age':pd.Series([25,26,25,23,30,29]),
#    'Rating':pd.Series(['a','b','c','d'])
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df)
# for i,j in df.iterrows():
#     print(i)
#    Age Rating
# 0   25      a
# 1   26      b
# 2   25      c
# 3   23      d
# 4   30    NaN
# 5   29    NaN
# 0
# 1
# 2
# 3
# 4
# 5




#############################################################
# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {
#    'Age':pd.Series([25,26,25,23,30,29]),
#    'Rating':pd.Series(['a','b','c','d'])
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df)
# for i,j in df.iterrows():
#     print(j)
#    Age Rating
# 0   25      a
# 1   26      b
# 2   25      c
# 3   23      d
# 4   30    NaN
# 5   29    NaN
# Age       25
# Rating     a
# Name: 0, dtype: object
# Age       26
# Rating     b
# Name: 1, dtype: object
# Age       25
# Rating     c
# Name: 2, dtype: object
# Age       23
# Rating     d
# Name: 3, dtype: object
# Age        30
# Rating    NaN
# Name: 4, dtype: object
# Age        29
# Rating    NaN
# Name: 5, dtype: object




#############################################################
# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {
#    'Age':pd.Series([25,26,25,23,30,29]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20])
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df)
# for i,j in df.iterrows():
#     print(i,j)
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN
# 0 Age       25.00
# Rating     4.23
# Name: 0, dtype: float64
# 1 Age       26.00
# Rating     3.24
# Name: 1, dtype: float64
# 2 Age       25.00
# Rating     3.98
# Name: 2, dtype: float64
# 3 Age       23.00
# Rating     2.56
# Name: 3, dtype: float64
# 4 Age       30.0
# Rating     3.2
# Name: 4, dtype: float64
# 5 Age       29.0
# Rating     NaN
# Name: 5, dtype: float64





#############################################################
# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {
#    'Age':pd.Series([25,26,25,23,30,29]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20])
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df)
# for i in df.itertuples():
#     print(i)
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN
# Pandas(Index=0, Age=25, Rating=4.23)
# Pandas(Index=1, Age=26, Rating=3.24)
# Pandas(Index=2, Age=25, Rating=3.98)
# Pandas(Index=3, Age=23, Rating=2.56)
# Pandas(Index=4, Age=30, Rating=3.2)
# Pandas(Index=5, Age=29, Rating=nan)



#############################################################
# Note − Do not try to modify any object while iterating. Iterating is meant for
# reading and the iterator returns a copy of the original object (a view), thus the
# changes will not reflect on the original object.




#############################################################
# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {
#    'Age':pd.Series([25,26,25,23,30,29]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20])
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df)
# for i,j in df.iterrows():
#     j["Age"] = 20
# print(df)
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN




#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.sort_index())
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN




#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1, index=[1,2,4,5,9,7,4,6])
# print(df)
# print(df.sort_index())
#    marks   Age
# 1   30.0  84.0
# 2   40.0  24.0
# 4   60.0  74.0
# 5   70.0  21.0
# 9    NaN   NaN
# 7   90.0   NaN
# 4   60.0  74.0
# 6    8.0  54.0
#    marks   Age
# 1   30.0  84.0
# 2   40.0  24.0
# 4   60.0  74.0
# 4   60.0  74.0
# 5   70.0  21.0
# 6    8.0  54.0
# 7   90.0   NaN
# 9    NaN   NaN




#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.sort_index(ascending=False))
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN
#    marks   Age
# 7     90   NaN
# 6      8  54.0
# 5     70  21.0
# 4     60  74.0
# 3     55  68.0
# 2     40  24.0
# 1     30  84.0
# 0     50  55.0






#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.sort_index(ascending=True))
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN




#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.sort_index(axis=0))
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN


#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.sort_index(axis=1))
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN
#     Age  marks
# 0  55.0     50
# 1  84.0     30
# 2  24.0     40
# 3  68.0     55
# 4  74.0     60
# 5  21.0     70
# 6  54.0      8
# 7   NaN     90



#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.sort_values(by="Age"))
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN
#    marks   Age
# 5     70  21.0
# 2     40  24.0
# 6      8  54.0
# 0     50  55.0
# 3     55  68.0
# 4     60  74.0
# 1     30  84.0
# 7     90   NaN



#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54]),
#          "distance" :pd.Series([44,21,87,14,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.sort_values(by=["marks"]))
#    marks   Age  distance
# 0     50  55.0      44.0
# 1     30  84.0      21.0
# 2     40  24.0      87.0
# 3     55  68.0      14.0
# 4     60  74.0      74.0
# 5     70  21.0      21.0
# 6      8  54.0      54.0
# 7     90   NaN       NaN
#    marks   Age  distance
# 6      8  54.0      54.0
# 1     30  84.0      21.0
# 2     40  24.0      87.0
# 0     50  55.0      44.0
# 3     55  68.0      14.0
# 4     60  74.0      74.0
# 5     70  21.0      21.0
# 7     90   NaN       NaN


#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54]),
#          "distance" :pd.Series([44,21,87,14,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.sort_values(by="marks", kind="mergesort"))
#    marks   Age  distance
# 0     50  55.0      44.0
# 1     30  84.0      21.0
# 2     40  24.0      87.0
# 3     55  68.0      14.0
# 4     60  74.0      74.0
# 5     70  21.0      21.0
# 6      8  54.0      54.0
# 7     90   NaN       NaN
#    marks   Age  distance
# 6      8  54.0      54.0
# 1     30  84.0      21.0
# 2     40  24.0      87.0
# 0     50  55.0      44.0
# 3     55  68.0      14.0
# 4     60  74.0      74.0
# 5     70  21.0      21.0
# 7     90   NaN       NaN



#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54]),
#          "distance" :pd.Series([44,21,87,14,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.sort_values(by="Age", kind="heapsort"))
#    marks   Age  distance
# 0     50  55.0      44.0
# 1     30  84.0      21.0
# 2     40  24.0      87.0
# 3     55  68.0      14.0
# 4     60  74.0      74.0
# 5     70  21.0      21.0
# 6      8  54.0      54.0
# 7     90   NaN       NaN
#    marks   Age  distance
# 5     70  21.0      21.0
# 2     40  24.0      87.0
# 6      8  54.0      54.0
# 0     50  55.0      44.0
# 3     55  68.0      14.0
# 4     60  74.0      74.0
# 1     30  84.0      21.0
# 7     90   NaN       NaN




#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54]),
#          "distance" :pd.Series([44,21,87,14,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.sort_values(by="distance", kind="quicksort"))
#    marks   Age  distance
# 0     50  55.0      44.0
# 1     30  84.0      21.0
# 2     40  24.0      87.0
# 3     55  68.0      14.0
# 4     60  74.0      74.0
# 5     70  21.0      21.0
# 6      8  54.0      54.0
# 7     90   NaN       NaN
#    marks   Age  distance
# 3     55  68.0      14.0
# 1     30  84.0      21.0
# 5     70  21.0      21.0
# 0     50  55.0      44.0
# 6      8  54.0      54.0
# 4     60  74.0      74.0
# 2     40  24.0      87.0
# 7     90   NaN       NaN



#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54]),
#          "distance" :pd.Series([44,21,87,14,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.sort_values(by="distance", kind="quicksort"))
# print(df.reset_index(drop=True))
#    marks   Age  distance
# 0     50  55.0      44.0
# 1     30  84.0      21.0
# 2     40  24.0      87.0
# 3     55  68.0      14.0
# 4     60  74.0      74.0
# 5     70  21.0      21.0
# 6      8  54.0      54.0
# 7     90   NaN       NaN
#    marks   Age  distance
# 3     55  68.0      14.0
# 1     30  84.0      21.0
# 5     70  21.0      21.0
# 0     50  55.0      44.0
# 6      8  54.0      54.0
# 4     60  74.0      74.0
# 2     40  24.0      87.0
# 7     90   NaN       NaN
#    marks   Age  distance
# 0     50  55.0      44.0
# 1     30  84.0      21.0
# 2     40  24.0      87.0
# 3     55  68.0      14.0
# 4     60  74.0      74.0
# 5     70  21.0      21.0
# 6      8  54.0      54.0
# 7     90   NaN       NaN





