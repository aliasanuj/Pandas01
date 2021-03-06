######################################################3
#Function Application
# Table wise Function Application: pipe()
# Row or Column Wise Function Application: apply()
# Element wise Function Application: applymap()

######################################################3
#Table-wise Function Application
######################################################3




######################################################3
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
# def adder(ele1,ele2):
#    return ele1+ele2
# print(df.pipe(adder,5))
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN
#    Age  Rating
# 0   30    9.23
# 1   31    8.24
# 2   30    8.98
# 3   28    7.56
# 4   35    8.20
# 5   34     NaN




######################################################3
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
# def adder(ele1,ele2):
#    return ele1+ele2
# print(df.pipe(adder,5, axis=1))
# TypeError: adder() got an unexpected keyword argument 'axis'





######################################################3
# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {
#    'Age':pd.Series([25,26,25,23,30,29]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20]),
#    'Rating1':pd.Series([1,2,3.98,2.56,3.20]),
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df)
# def adder(ele1,ele2):
#    return ele1+ele2
# print(df.pipe(adder,5))
#    Age  Rating  Rating1
# 0   25    4.23     1.00
# 1   26    3.24     2.00
# 2   25    3.98     3.98
# 3   23    2.56     2.56
# 4   30    3.20     3.20
# 5   29     NaN      NaN
#    Age  Rating  Rating1
# 0   30    9.23     6.00
# 1   31    8.24     7.00
# 2   30    8.98     8.98
# 3   28    7.56     7.56
# 4   35    8.20     8.20
# 5   34     NaN      NaN






######################################################3
# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {
#    'Age': [25,26,25,23,30,29],
#    'Rating': [4.23,3.24,3.98,2.56,3.20]
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df)
# def adder(ele1,ele2):
#    return ele1+ele2
# print(df.pipe(adder,5))
# ValueError: arrays must all be same length




######################################################3
# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {
#    'Age': [25,26,25,23,30],
#    'Rating': [4.23,3.24,3.98,2.56,3.20]
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df)
# def adder(ele1,ele2):
#    return ele1+ele2
# print(df.pipe(adder,5))
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
#    Age  Rating
# 0   30    9.23
# 1   31    8.24
# 2   30    8.98
# 3   28    7.56
# 4   35    8.20




######################################################3
# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {
#    'Age': [25,26,25,23,30],
#    'Rating': [4.23,3.24,3.98,2.56,3.20]
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df)
# def adder(ele1,ele2):
#    return ele1+ele2
# print(df.apply(adder,5))
# ValueError: No axis named 5 for object type <class 'pandas.core.frame.DataFrame'>






######################################################3
# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {
#    'Age':pd.Series([25,26,25,23,30,29]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20]),
#    'Name':pd.Series(["anuj","bbbb","cc","dd","ee","ss"])
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df)
# print(df.apply(np.mean))
# TypeError: Could not convert anujbbbbccddeess to numeric








######################################################3
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
# print(df.apply(np.mean,axis=1))
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN
# 0    14.615
# 1    14.620
# 2    14.490
# 3    12.780
# 4    16.600
# 5    29.000
# dtype: float64






######################################################3
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
# print(df.apply(np.mean))
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN
# Age       26.333333
# Rating     3.442000
# dtype: float64




######################################################3
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
# print(df.apply(np.mean,axis=1))
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN
# 0    14.615
# 1    14.620
# 2    14.490
# 3    12.780
# 4    16.600
# 5    29.000
# dtype: float64



######################################################3
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
# print(df.applymap(lambda x:x*100))
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN
#     Age  Rating
# 0  2500   423.0
# 1  2600   324.0
# 2  2500   398.0
# 3  2300   256.0
# 4  3000   320.0
# 5  2900     NaN



######################################################3
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
# def mul(a1,b1):
#     return a1*b1
# print(df.pipe(mul,100))
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN
#     Age  Rating
# 0  2500   423.0
# 1  2600   324.0
# 2  2500   398.0
# 3  2300   256.0
# 4  3000   320.0
# 5  2900     NaN



######################################################3
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
# print(df['Age'].applymap(lambda x:x*100))
# AttributeError: 'Series' object has no attribute 'applymap'






######################################################3
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
# print(df["Age"].map(lambda x:x*10))
# print(df)
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN
# 0    250
# 1    260
# 2    250
# 3    230
# 4    300
# 5    290
# Name: Age, dtype: int64
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN
# 4



######################################################3
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
# print(df.apply(lambda x : x.max() - x.min()))
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN
# Age       7.00
# Rating    1.67
# dtype: float64





######################################################3
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
# print(df.apply(lambda x : x.max() - x.min(), axis=1))
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN
# 0    20.77
# 1    22.76
# 2    21.02
# 3    20.44
# 4    26.80
# 5     0.00
# dtype: float64




######################################################3
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
# print(df.map(lambda x : x.max() - x.min()))
# AttributeError: 'DataFrame' object has no attribute 'map'




######################################################3
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
# print(df.apply(lambda x : x.max() - x.min()))
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN
# Age       7.00
# Rating    1.67
# dtype: float64
