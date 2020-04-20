#Reindexing.py
# Reindexing changes the row labels and column labels of a DataFrame.
# To reindex means to conform the data to match a given set
# of labels along a particular axis.
# Multiple operations can be accomplished through indexing like −
#
# Reorder the existing data to match a new set of labels.
# Insert missing value (NA) markers in label locations where no data for the label existed.




####################################################
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




####################################################
#import pandas as pd
# import numpy as np
# N=10
# df = pd.DataFrame({
#    'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
#    'x': np.linspace(0,stop=N-1,num=N),
#    'y': np.random.rand(N),
#    'C': np.random.choice(['Low','Medium','High'],N).tolist(),
#    'D': np.random.normal(100, 10, size=(N)).tolist()
# })
# #reindex the DataFrame
# df_reindexed = df.reindex( columns=['A', 'C', 'B','x','y','D'])
# print (df_reindexed)
#            A       C   B    x         y           D
# 0 2016-01-01  Medium NaN  0.0  0.054955   89.880366
# 1 2016-01-02     Low NaN  1.0  0.225084   91.136564
# 2 2016-01-03  Medium NaN  2.0  0.785177  101.509903
# 3 2016-01-04  Medium NaN  3.0  0.797814   96.810798
# 4 2016-01-05  Medium NaN  4.0  0.627216   91.003887
# 5 2016-01-06     Low NaN  5.0  0.138994   89.019475
# 6 2016-01-07     Low NaN  6.0  0.251904   79.783493
# 7 2016-01-08  Medium NaN  7.0  0.252319   77.054143
# 8 2016-01-09  Medium NaN  8.0  0.160999  105.777183
# 9 2016-01-10    High NaN  9.0  0.493546   83.811737






####################################################
# import pandas as pd
# import numpy as np
# N=10
# df = pd.DataFrame({
#    'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
#    'x': np.linspace(0,stop=N-1,num=N),
#    'y': np.random.rand(N),
#    'C': np.random.choice(['Low','Medium','High'],N).tolist(),
#    'D': np.random.normal(100, 10, size=(N)).tolist()
# })
# #reindex the DataFrame
# df_reindexed = df.reindex( columns=['A'=="aaa", 'C', 'B','x','y','D'])
# print (df_reindexed)
#    False       C   B    x         y           D
# 0    NaN  Medium NaN  0.0  0.825334   88.096696
# 1    NaN    High NaN  1.0  0.001130   94.009703
# 2    NaN  Medium NaN  2.0  0.350420   95.428639
# 3    NaN  Medium NaN  3.0  0.655367  102.580654
# 4    NaN    High NaN  4.0  0.155374   94.012758
# 5    NaN    High NaN  5.0  0.200422  109.217233
# 6    NaN    High NaN  6.0  0.358569   83.727063
# 7    NaN  Medium NaN  7.0  0.756036   97.455632
# 8    NaN     Low NaN  8.0  0.922705  113.800482
# 9    NaN    High NaN  9.0  0.240952  111.302060





####################################################
# import pandas as pd
# import numpy as np
# N=10
# df01 = [{
#    'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
#    'x': np.linspace(0,stop=N-1,num=N),
#    'y': np.random.rand(N),
#    'C': np.random.choice(['Low','Medium','High'],N).tolist(),
#    'D': np.random.normal(100, 10, size=(N)).tolist()
# }]
# df = pd.DataFrame(df01)
# print(df)
#                                                    A  ...                                                  D
# 0  DatetimeIndex(['2016-01-01', '2016-01-02', '20...  ...  [109.30386478190103, 102.96302047047448, 105.7...
#
# [1 rows x 5 columns]




####################################################
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





####################################################
# import pandas as pd
# import numpy as np
# N=5
# df = pd.DataFrame({
#    'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
#    'x': np.linspace(0,stop=N-1,num=N),
#    'y': np.random.rand(N),
#    'C': np.random.choice(['Low','Medium','High'],N).tolist(),
#    'D': np.random.normal(100, 10, size=(N)).tolist()
# })
# #reindex the DataFrame
# df_reindexed = df.reindex()
# print (df_reindexed)
#            A    x         y       C           D
# 0 2016-01-01  0.0  0.790207  Medium  103.529159
# 1 2016-01-02  1.0  0.918490    High   97.555297
# 2 2016-01-03  2.0  0.156254  Medium   98.344424
# 3 2016-01-04  3.0  0.116510  Medium  104.254247
# 4 2016-01-05  4.0  0.950653  Medium  110.808148





####################################################
# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d1 = {
#    'Age':pd.Series([25,26,25,23,30,29]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20])
# }
# d2 = {
#    'Age':pd.Series([11,22,33,44,55]),
#    'Rating':pd.Series([1.1,2.2,3.3,4.4,5.5])
# }
# #Create a DataFrame
# df1 = pd.DataFrame(d1)
# df2 = pd.DataFrame(d2)
# print(df1)
# print(df2)
# df1 = df1.reindex_like(df2)
# print(df1)
# print(df2)
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
# 5   29     NaN
#    Age  Rating
# 0   11     1.1
# 1   22     2.2
# 2   33     3.3
# 3   44     4.4
# 4   55     5.5
#    Age  Rating
# 0   25    4.23
# 1   26    3.24
# 2   25    3.98
# 3   23    2.56
# 4   30    3.20
#    Age  Rating
# 0   11     1.1
# 1   22     2.2
# 2   33     3.3
# 3   44     4.4
# 4   55     5.5





####################################################
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





####################################################
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





####################################################
# Filling while ReIndexing
# reindex() takes an optional parameter method which is a filling method with values as follows −
#
# pad/ffill − Fill values forward
# bfill/backfill − Fill values backward
# nearest − Fill from the nearest index values




####################################################
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






####################################################
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
# print(df1.reindex_like(df2,method="bfill"))
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





####################################################
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
# print(df1.reindex_like(df2,method="nearest"))
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



####################################################
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
# print(df1.reindex_like(df2,method="ffill", limit=1))
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




####################################################
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
# print(df1.reindex_like(df2,method="ffill", limit=2))
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
# 4  25.0    3.98
# 5   NaN     NaN




####################################################
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
#assignong col name wont work here






####################################################
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
# print(df.rename( index ={0:"apple",1:"banana",2:"papaya"} ))
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
