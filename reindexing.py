#Reindexing.py


# Reindexing changes the row labels and column labels of a DataFrame. To reindex means to conform the data to match a given set
# of labels along a particular axis.
# Multiple operations can be accomplished through indexing like −
#
# Reorder the existing data to match a new set of labels.
# Insert missing value (NA) markers in label locations where no data for the label existed.


# import pandas as pd
# import numpy as np
# N=20
# df = pd.DataFrame({
#    'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
#    'x': np.linspace(0,stop=N-1,num=N),
#    'y': np.random.rand(N),
#    'C': np.random.choice(['Low','Medium','High'],N).tolist(),
#    'D': np.random.normal(100, 10, size=(N)).tolist()
# })
# #reindex the DataFrame
# df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])
# print (df_reindexed)
#            A       C   B
# 0 2016-01-01  Medium NaN
# 2 2016-01-03  Medium NaN
# 5 2016-01-06     Low NaN


# import pandas as pd
# import numpy as np
# N=20
# df = pd.DataFrame({
#    'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
#    'x': np.linspace(0,stop=N-1,num=N),
#    'y': np.random.rand(N),
#    'C': np.random.choice(['Low','Medium','High'],N).tolist(),
#    'D': np.random.normal(100, 10, size=(N)).tolist()
# })
# #reindex the DataFrame
# df_reindexed = df.reindex(index=[10,11,12], columns=['A', 'C', 'B','x','y','D'])
# print (df_reindexed)
#             A       C   B     x         y           D
# 10 2016-01-11  Medium NaN  10.0  0.829307  105.164361
# 11 2016-01-12  Medium NaN  11.0  0.096326  100.285934
# 12 2016-01-13  Medium NaN  12.0  0.496484   93.860558





# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d1 = {
#    'Age':pd.Series([25,26,25,23,30,29]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20])
# }
# d2 = {
#    'Age':pd.Series([10,20,30,40,50]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20])
# }
# #Create a DataFrame
# df1 = pd.DataFrame(d1)
# df2 = pd.DataFrame(d2)
# print(df1)
# print(df2)
# df1 = df1.reindex_like(df2)
# print(df1)
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN
#    Age  Rating
# 0   10    4.23
# 1   20    3.24
# 2   30    3.98
# 3   40    2.56
# 4   50    3.20
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20




# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d1 = {
#    'Age':pd.Series([25,26,25,23,30,29]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20])
# }
# d2 = {
#    'Age':pd.Series([10,20,30,40,50]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20])
# }
# #Create a DataFrame
# df1 = pd.DataFrame(d1)
# df2 = pd.DataFrame(d2)
# print(df1)
# print(df2)
# df2 = df2.reindex_like(df1)
# print(df2)
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN
#    Age  Rating
# 0   10    4.23
# 1   20    3.24
# 2   30    3.98
# 3   40    2.56
# 4   50    3.20
#     Age  Rating
# 0  10.0    4.23
# 1  20.0    3.24
# 2  30.0    3.98
# 3  40.0    2.56
# 4  50.0    3.20
# 5   NaN     NaN



# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d1 = {
#    'Age':pd.Series([25,26,25,23,30,29]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20])
# }
# d2 = {
#    'Age':pd.Series([10,20,30,40,50]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20])
# }
# #Create a DataFrame
# df1 = pd.DataFrame(d1)
# df2 = pd.DataFrame(d2)
# print(df1)
# print(df2)
# df3 = df2.reindex_like(df1)
# print(df3)
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN
#    Age  Rating
# 0   10    4.23
# 1   20    3.24
# 2   30    3.98
# 3   40    2.56
# 4   50    3.20
#     Age  Rating
# 0  10.0    4.23
# 1  20.0    3.24
# 2  30.0    3.98
# 3  40.0    2.56
# 4  50.0    3.20
# 5   NaN     NaN

# Filling while ReIndexing
# reindex() takes an optional parameter method which is a filling method with values as follows −
#
# pad/ffill − Fill values forward
# bfill/backfill − Fill values backward
# nearest − Fill from the nearest index values


# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d1 = {
#    'Age':pd.Series([25,26,25]),
#    'Rating':pd.Series([4.23,3.24,3.98])
# }
# d2 = {
#    'Age':pd.Series([10,20,30,40]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56])
# }
# #Create a DataFrame
# df1 = pd.DataFrame(d1)
# df2 = pd.DataFrame(d2)
# print(df1)
# print(df2)
# print(df1.reindex_like(df2))
# print(df1.reindex_like(df2,method="ffill")) #pad
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
#    Age  Rating
# 0   10    4.23
# 1   20    3.24
# 2   30    3.98
# 3   40    2.56
#     Age  Rating
# 0  25.0    4.23
# 1  26.0    3.24
# 2  25.0    3.98
# 3   NaN     NaN
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   25    3.98




# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d1 = {
#    'Age':pd.Series([25,26,25]),
#    'Rating':pd.Series([4.23,3.24,3.98])
# }
# d2 = {
#    'Age':pd.Series([10,20,30,40]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56])
# }
# #Create a DataFrame
# df1 = pd.DataFrame(d1)
# df2 = pd.DataFrame(d2)
# print(df1)
# print(df2)
# print(df1.reindex_like(df2))
# print(df1.reindex_like(df2,method="bfill")) #pad
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
#    Age  Rating
# 0   10    4.23
# 1   20    3.24
# 2   30    3.98
# 3   40    2.56
#     Age  Rating
# 0  25.0    4.23
# 1  26.0    3.24
# 2  25.0    3.98
# 3   NaN     NaN
#     Age  Rating
# 0  25.0    4.23
# 1  26.0    3.24
# 2  25.0    3.98
# 3   NaN     NaN


# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d1 = {
#    'Age':pd.Series([25,26,25]),
#    'Rating':pd.Series([4.23,3.24,3.98])
# }
# d2 = {
#    'Age':pd.Series([10,20,30,40]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56])
# }
# #Create a DataFrame
# df1 = pd.DataFrame(d1)
# df2 = pd.DataFrame(d2)
# print(df1)
# print(df2)
# print(df1.reindex_like(df2))
# print(df1.reindex_like(df2,method="nearest")) #pad
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
#    Age  Rating
# 0   10    4.23
# 1   20    3.24
# 2   30    3.98
# 3   40    2.56
#     Age  Rating
# 0  25.0    4.23
# 1  26.0    3.24
# 2  25.0    3.98
# 3   NaN     NaN
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   25    3.98




# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d1 = {
#    'Age':pd.Series([25,26,25]),
#    'Rating':pd.Series([4.23,3.24,3.98])
# }
# d2 = {
#    'Age':pd.Series([10,20,30,40,50,55]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,4.1,5.4])
# }
# #Create a DataFrame
# df1 = pd.DataFrame(d1)
# df2 = pd.DataFrame(d2)
# print(df1)
# print(df2)
# print(df1.reindex_like(df2))
# print(df1.reindex_like(df2,method="ffill", limit=1)) #pad
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
#    Age  Rating
# 0   10    4.23
# 1   20    3.24
# 2   30    3.98
# 3   40    2.56
# 4   50    4.10
# 5   55    5.40
#     Age  Rating
# 0  25.0    4.23
# 1  26.0    3.24
# 2  25.0    3.98
# 3   NaN     NaN
# 4   NaN     NaN
# 5   NaN     NaN
#     Age  Rating
# 0  25.0    4.23
# 1  26.0    3.24
# 2  25.0    3.98
# 3  25.0    3.98
# 4   NaN     NaN
# 5   NaN     NaN



# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d1 = {
#    'Age':pd.Series([25,26,25,30,54,48]),
#    'Rating':pd.Series([4.23,3.24,3.98,5.12,3.47,6.42])
# }
# #Create a DataFrame
# df = pd.DataFrame(d1)
# print(df)
# print(df.rename(columns={"a":"col1","b":"col2","c":"col3"}, index ={0:"apple",1:"banana",2:"papaya"} ))
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   30    5.12
# 4   54    3.47
# 5   48    6.42
#         Age  Rating
# apple    25    4.23
# banana   26    3.24
# papaya   25    3.98
# 3        30    5.12
# 4        54    3.47
# 5        48    6.42
