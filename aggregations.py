#aggregations.py
###########################################################anuj
# import pandas as
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age01" :pd.Series([55,84,24,68,74,21,54]),
#          "Age02" :pd.Series([11,22,33,44,55,66,77,88,99,100]),
#          "Age03" :pd.Series([55,48,92,96,47,22,4]),
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.rolling(window=2,min_periods=1))
#    marks  Age01  Age02  Age03
# 0   50.0   55.0     11   55.0
# 1   30.0   84.0     22   48.0
# 2   40.0   24.0     33   92.0
# 3   55.0   68.0     44   96.0
# 4   60.0   74.0     55   47.0
# 5   70.0   21.0     66   22.0
# 6    8.0   54.0     77    4.0
# 7   90.0    NaN     88    NaN
# 8    NaN    NaN     99    NaN
# 9    NaN    NaN    100    NaN
# Rolling [window=2,min_periods=1,center=False,axis=0]





###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age01" :pd.Series([55,84,24,68,74,21,54]),
#          "Age02" :pd.Series([11,22,33,44,55,66,77,88,99,100]),
#          "Age03" :pd.Series([55,48,92,96,47,22,4]),
#          }
# df = pd.DataFrame(data1)
# print(df)
# r = df.rolling(window=2,min_periods=1)
# print(r.aggregate(np.sum))
#    marks  Age01  Age02  Age03
# 0   50.0   55.0     11   55.0
# 1   30.0   84.0     22   48.0
# 2   40.0   24.0     33   92.0
# 3   55.0   68.0     44   96.0
# 4   60.0   74.0     55   47.0
# 5   70.0   21.0     66   22.0
# 6    8.0   54.0     77    4.0
# 7   90.0    NaN     88    NaN
# 8    NaN    NaN     99    NaN
# 9    NaN    NaN    100    NaN
#    marks  Age01  Age02  Age03
# 0   50.0   55.0   11.0   55.0
# 1   80.0  139.0   33.0  103.0
# 2   70.0  108.0   55.0  140.0
# 3   95.0   92.0   77.0  188.0
# 4  115.0  142.0   99.0  143.0
# 5  130.0   95.0  121.0   69.0
# 6   78.0   75.0  143.0   26.0
# 7   98.0   54.0  165.0    4.0
# 8   90.0    NaN  187.0    NaN
# 9    NaN    NaN  199.0    NaN







###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age01" :pd.Series([55,84,24,68,74,21,54]),
#          "Age02" :pd.Series([11,22,33,44,55,66,77,88,99,100]),
#          "Age03" :pd.Series([55,48,92,96,47,22,4]),
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.aggregate(np.sum))
#    marks  Age01  Age02  Age03
# 0   50.0   55.0     11   55.0
# 1   30.0   84.0     22   48.0
# 2   40.0   24.0     33   92.0
# 3   55.0   68.0     44   96.0
# 4   60.0   74.0     55   47.0
# 5   70.0   21.0     66   22.0
# 6    8.0   54.0     77    4.0
# 7   90.0    NaN     88    NaN
# 8    NaN    NaN     99    NaN
# 9    NaN    NaN    100    NaN
# marks    403.0
# Age01    380.0
# Age02    595.0
# Age03    364.0
# dtype: float64





#Apply Aggregation on a Single Column of a Dataframe
###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age01" :pd.Series([55,84,24,68,74,21,54]),
#          "Age02" :pd.Series([11,22,33,44,55,66,77,88,99,100]),
#          "Age03" :pd.Series([55,48,92,96,47,22,4]),
#          }
# df = pd.DataFrame(data1)
# print(df)
# r = df.rolling(window=2,min_periods=1)
# print(r["marks"].aggregate(np.sum))
#    marks  Age01  Age02  Age03
# 0   50.0   55.0     11   55.0
# 1   30.0   84.0     22   48.0
# 2   40.0   24.0     33   92.0
# 3   55.0   68.0     44   96.0
# 4   60.0   74.0     55   47.0
# 5   70.0   21.0     66   22.0
# 6    8.0   54.0     77    4.0
# 7   90.0    NaN     88    NaN
# 8    NaN    NaN     99    NaN
# 9    NaN    NaN    100    NaN
# 0     50.0
# 1     80.0
# 2     70.0
# 3     95.0
# 4    115.0
# 5    130.0
# 6     78.0
# 7     98.0
# 8     90.0
# 9      NaN
# Name: marks, dtype: float64





###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age01" :pd.Series([55,84,24,68,74,21,54]),
#          "Age02" :pd.Series([11,22,33,44,55,66,77,88,99,100]),
#          "Age03" :pd.Series([55,48,92,96,47,22,4]),
#          }
# df = pd.DataFrame(data1)
# print(df)
# r = df.rolling(window=2,min_periods=1)
# print(r["marks","Age01"].aggregate(np.sum))
#    marks  Age01  Age02  Age03
# 0   50.0   55.0     11   55.0
# 1   30.0   84.0     22   48.0
# 2   40.0   24.0     33   92.0
# 3   55.0   68.0     44   96.0
# 4   60.0   74.0     55   47.0
# 5   70.0   21.0     66   22.0
# 6    8.0   54.0     77    4.0
# 7   90.0    NaN     88    NaN
# 8    NaN    NaN     99    NaN
# 9    NaN    NaN    100    NaN
#    marks  Age01
# 0   50.0   55.0
# 1   80.0  139.0
# 2   70.0  108.0
# 3   95.0   92.0
# 4  115.0  142.0
# 5  130.0   95.0
# 6   78.0   75.0
# 7   98.0   54.0
# 8   90.0    NaN
# 9    NaN    NaN




###########################################################
#Apply Multiple Functions on Multiple Columns of a DataFrame
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(10, 4),
#    index = pd.date_range('1/1/2000', periods=10),
#    columns = ['A', 'B', 'C', 'D'])
# print(df)
# r = df.rolling(window=3,min_periods=1)
# print(r[['A','B']].aggregate([np.sum,np.mean]))
#                    A         B         C         D
# 2000-01-01  1.444651  0.043353 -0.064126 -0.154217
# 2000-01-02  0.878751  1.569930 -1.893218 -0.377505
# 2000-01-03 -0.343943  0.520199  0.377232  0.527917
# 2000-01-04 -0.625143 -1.647383  1.813154  0.039963
# 2000-01-05  1.744807 -1.638486  0.138053 -0.329546
# 2000-01-06  0.194078  0.167279  0.130328  1.661803
# 2000-01-07 -1.096271  1.096733 -0.907016  0.026001
# 2000-01-08 -0.113647  1.280304 -0.289082 -1.667080
# 2000-01-09  0.376065  0.286376 -0.933353  0.420202
# 2000-01-10  1.277080  1.030351  1.212857 -0.856444
#                    A                   B
#                  sum      mean       sum      mean
# 2000-01-01  1.444651  1.444651  0.043353  0.043353
# 2000-01-02  2.323402  1.161701  1.613283  0.806642
# 2000-01-03  1.979459  0.659820  2.133482  0.711161
# 2000-01-04 -0.090336 -0.030112  0.442747  0.147582
# 2000-01-05  0.775720  0.258573 -2.765670 -0.921890
# 2000-01-06  1.313741  0.437914 -3.118590 -1.039530
# 2000-01-07  0.842614  0.280871 -0.374474 -0.124825
# 2000-01-08 -1.015840 -0.338613  2.544316  0.848105
# 2000-01-09 -0.833853 -0.277951  2.663413  0.887804
# 2000-01-10  1.539498  0.513166  2.597031  0.865677




###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age01" :pd.Series([55,84,24,68,21,54]),
#          "Age02" :pd.Series([11,22, " ",44,55,66,77,88,99,100]),
#          "Age03" :pd.Series([55,48,92,96,47,22,4]),
#          }
# df = pd.DataFrame(data1)
# print(df)
# r = df.rolling(window=2,min_periods=1)
# print(r["marks","Age01"].aggregate([np.sum,np.mean]))
#    marks  Age01 Age02  Age03
# 0   50.0   55.0    11   55.0
# 1   30.0   84.0    22   48.0
# 2   40.0   24.0         92.0
# 3   55.0   68.0    44   96.0
# 4   60.0   21.0    55   47.0
# 5   70.0   54.0    66   22.0
# 6    8.0    NaN    77    4.0
# 7   90.0    NaN    88    NaN
# 8    NaN    NaN    99    NaN
# 9    NaN    NaN   100    NaN
#    marks        Age01
#      sum  mean    sum  mean
# 0   50.0  50.0   55.0  55.0
# 1   80.0  40.0  139.0  69.5
# 2   70.0  35.0  108.0  54.0
# 3   95.0  47.5   92.0  46.0
# 4  115.0  57.5   89.0  44.5
# 5  130.0  65.0   75.0  37.5
# 6   78.0  39.0   54.0  54.0
# 7   98.0  49.0    NaN   NaN
# 8   90.0  90.0    NaN   NaN
# 9    NaN   NaN    NaN   NaN





###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age01" :pd.Series([55,84," ",68,21,54]),
#          "Age02" :pd.Series([11,22, " ",44,55,66,77,88,99,100]),
#          "Age03" :pd.Series([55,48,92,96,47,22,4]),
#          }
# df = pd.DataFrame(data1)
# print(df)
# r = df.rolling(window=2,min_periods=1)
# print(r["marks","Age01"].aggregate([np.sum,np.mean]))
#    marks Age01 Age02  Age03
# 0   50.0    55    11   55.0
# 1   30.0    84    22   48.0
# 2   40.0               92.0
# 3   55.0    68    44   96.0
# 4   60.0    21    55   47.0
# 5   70.0    54    66   22.0
# 6    8.0   NaN    77    4.0
# 7   90.0   NaN    88    NaN
# 8    NaN   NaN    99    NaN
# 9    NaN   NaN   100    NaN
#    marks
#      sum  mean
# 0   50.0  50.0
# 1   80.0  40.0
# 2   70.0  35.0
# 3   95.0  47.5
# 4  115.0  57.5
# 5  130.0  65.0
# 6   78.0  39.0
# 7   98.0  49.0
# 8   90.0  90.0
# 9    NaN   NaN




###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age01" :pd.Series([55,84,68,21,54]),
#          "Age02" :pd.Series([11,22, " ",44,55,66,77,88,99,100]),
#          "Age03" :pd.Series([55,48,92,96,47,22,4]),
#          }
# df = pd.DataFrame(data1)
# print(df)
# r = df.rolling(window=2,min_periods=1)
# print(r.aggregate({"marks": np.sum, "Age01":np.mean}))
#    marks  Age01 Age02  Age03
# 0   50.0   55.0    11   55.0
# 1   30.0   84.0    22   48.0
# 2   40.0   68.0         92.0
# 3   55.0   21.0    44   96.0
# 4   60.0   54.0    55   47.0
# 5   70.0    NaN    66   22.0
# 6    8.0    NaN    77    4.0
# 7   90.0    NaN    88    NaN
# 8    NaN    NaN    99    NaN
# 9    NaN    NaN   100    NaN
#    marks  Age01
# 0   50.0   55.0
# 1   80.0   69.5
# 2   70.0   76.0
# 3   95.0   44.5
# 4  115.0   37.5
# 5  130.0   54.0
# 6   78.0    NaN
# 7   98.0    NaN
# 8   90.0    NaN
# 9    NaN    NaN



###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age01" :pd.Series([55,84,68,21,54]),
#          "Age02" :pd.Series([11,22,np.nan,44,55,66,77,88,99,100]),
#          "Age03" :pd.Series([55,48,92,96,47,22,4]),
#          }
# df = pd.DataFrame(data1)
# print(df)
# r = df.rolling(window=2,min_periods=1)
# print(r.aggregate({"marks": np.sum, "Age02":np.sum}))
#    marks  Age01  Age02  Age03
# 0   50.0   55.0   11.0   55.0
# 1   30.0   84.0   22.0   48.0
# 2   40.0   68.0    NaN   92.0
# 3   55.0   21.0   44.0   96.0
# 4   60.0   54.0   55.0   47.0
# 5   70.0    NaN   66.0   22.0
# 6    8.0    NaN   77.0    4.0
# 7   90.0    NaN   88.0    NaN
# 8    NaN    NaN   99.0    NaN
# 9    NaN    NaN  100.0    NaN
#    marks  Age02
# 0   50.0   11.0
# 1   80.0   33.0
# 2   70.0   22.0
# 3   95.0   44.0
# 4  115.0   99.0
# 5  130.0  121.0
# 6   78.0  143.0
# 7   98.0  165.0
# 8   90.0  187.0
# 9    NaN  199.0


