#missingData.py
###########################################################


###########################################################
#When and Why Is Data Missed?
# Let us consider an online survey for a product. Many a times, people do not share all the
# information related to them.
# Few people share their experience, but not how long they are using the product;
# few people share how long they are using the
# product, their experience but not their contact information.
# Thus, in some or the other way a part of data is always missing, and
# this is very common in real time.




###########################################################
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f','h'],
#                   columns=['one', 'two', 'three'])
# df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
# print(df)
#         one       two     three
# a -0.922222  2.413065  0.308156
# b       NaN       NaN       NaN
# c  1.600694  0.096803  1.437383
# d       NaN       NaN       NaN
# e  0.040496 -0.543667 -0.621806
# f -0.776735  0.917140 -0.592696
# g       NaN       NaN       NaN
# h  0.394618 -0.234855 -1.179264






###########################################################
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f','h'])
# df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
# print(df)
#           0         1         2
# a  0.458525  1.531964  1.035289
# b       NaN       NaN       NaN
# c -0.917223  0.005637  1.201422
# d       NaN       NaN       NaN
# e  0.337383  0.032286  1.424074
# f -1.836215  0.802196  0.017694
# g       NaN       NaN       NaN
# h -1.312147  1.898662  0.116727




###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1, index=[0,2,4,6,7,9,10])
# print(df)
# print(df.reindex([1,2,3,4,5,6]))
#     marks   Age
# 0    50.0  55.0
# 2    40.0  24.0
# 4    60.0  74.0
# 6     8.0  54.0
# 7    90.0   NaN
# 9     NaN   NaN
# 10    NaN   NaN
#    marks   Age
# 1    NaN   NaN
# 2   40.0  24.0
# 3    NaN   NaN
# 4   60.0  74.0
# 5    NaN   NaN
# 6    8.0  54.0



###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1, index=[0,2,4,6,7,9,10])
# print(df)
# df.reindex([1,2,3,4,5,6])
# print(df)
#     marks   Age
# 0    50.0  55.0
# 2    40.0  24.0
# 4    60.0  74.0
# 6     8.0  54.0
# 7    90.0   NaN
# 9     NaN   NaN
# 10    NaN   NaN
#     marks   Age
# 0    50.0  55.0
# 2    40.0  24.0
# 4    60.0  74.0
# 6     8.0  54.0
# 7    90.0   NaN
# 9     NaN   NaN
# 10    NaN   NaN







###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1, index=[0,1,3,5,7,9])
# print(df)
# df.reindex([2,4,6,8,10])
# print(df['Age'].isnull())
#    marks   Age
# 0   50.0  55.0
# 1   30.0  84.0
# 3   60.0  68.0
# 5    8.0  21.0
# 7    NaN   NaN
# 9    NaN   NaN
# 0    False
# 1    False
# 3    False
# 5    False
# 7     True
# 9     True
# Name: Age, dtype: bool







###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1, index=[0,1,3,5,7,9])
# print(df)
# df.reindex([2,4,6,8,10])
# print(df)
#    marks   Age
# 0   50.0  55.0
# 1   30.0  84.0
# 3   60.0  68.0
# 5    8.0  21.0
# 7    NaN   NaN
# 9    NaN   NaN
#    marks   Age
# 0   50.0  55.0
# 1   30.0  84.0
# 3   60.0  68.0
# 5    8.0  21.0
# 7    NaN   NaN
# 9    NaN   NaN





###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1, index=[0,2,3,5,7,9])
# print(df)
# print(df.reindex([2,4,6,8,10]))
#    marks   Age
# 0   50.0  55.0
# 2   40.0  24.0
# 3   60.0  68.0
# 5    8.0  21.0
# 7    NaN   NaN
# 9    NaN   NaN
#     marks   Age
# 2    40.0  24.0
# 4     NaN   NaN
# 6     NaN   NaN
# 8     NaN   NaN
# 10    NaN   NaN









###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1, index=[0,2,3,5,7,9])
# print(df)
# print(df.reindex([2,4,6,8,10]))
#    marks   Age
# 0   50.0  55.0
# 2   40.0  24.0
# 3   60.0  68.0
# 5    8.0  21.0
# 7    NaN   NaN
# 9    NaN   NaN
#     marks   Age
# 2    40.0  24.0
# 4     NaN   NaN
# 6     NaN   NaN
# 8     NaN   NaN
# 10    NaN   NaN






###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1, index=[0,1,3,5,7,9])
# print(df)
# df.reindex([2,4,6,8,10])
# print(df['Age'].notnull())
#    marks   Age
# 0   50.0  55.0
# 1   30.0  84.0
# 3   60.0  68.0
# 5    8.0  21.0
# 7    NaN   NaN
# 9    NaN   NaN
# 0     True
# 1     True
# 3     True
# 5     True
# 7    False
# 9    False
# Name: Age, dtype: bool






###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1, index=[0,1,3,5,7,9])
# print(df)
# df.reindex([2,4,6,8,10])
# print(df)
#    marks   Age
# 0   50.0  55.0
# 1   30.0  84.0
# 3   60.0  68.0
# 5    8.0  21.0
# 7    NaN   NaN
# 9    NaN   NaN
#    marks   Age
# 0   50.0  55.0
# 1   30.0  84.0
# 3   60.0  68.0
# 5    8.0  21.0
# 7    NaN   NaN
# 9    NaN   NaN




###########################################################
# Calculations with Missing Data
# When summing data, NA will be treated as Zero
# If the data are all NA, then the result will be NA



###########################################################
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f','h'],columns=['one', 'two', 'three'])
# df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
# print(df['one'].sum())
# 1.024324388974825




###########################################################
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f','h'],
#                   columns=['one', 'two', 'three'])
# df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
# print(df)
# print(df['one'].sum())
#         one       two     three
# a  0.690118  0.276142 -1.116885
# b       NaN       NaN       NaN
# c  0.349070  1.339726 -1.131528
# d       NaN       NaN       NaN
# e -0.003865 -0.216286 -1.860152
# f  1.201844 -0.837943  1.189715
# g       NaN       NaN       NaN
# h -1.166641  2.614688  0.107510
# 1.0705264050486611




###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1, index=[0,1,3,5,7,9])
# print(df)
# df.reindex([2,4,6,8,10])
# print(df['Age'].sum())
# df["total"] = df["marks"] + df["Age"]
# print(df["total"])
# print(df)
#    marks   Age
# 0   50.0  55.0
# 1   30.0  84.0
# 3   60.0  68.0
# 5    8.0  21.0
# 7    NaN   NaN
# 9    NaN   NaN
# 228.0
# 0    105.0
# 1    114.0
# 3    128.0
# 5     29.0
# 7      NaN
# 9      NaN
# Name: total, dtype: float64
#    marks   Age  total
# 0   50.0  55.0  105.0
# 1   30.0  84.0  114.0
# 3   60.0  68.0  128.0
# 5    8.0  21.0   29.0
# 7    NaN   NaN    NaN
# 9    NaN   NaN    NaN




###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,60,70,8,90,22,33]),
#          "Age" :pd.Series([55,84,24,68,74,21,54,77,99])
#          }
# df = pd.DataFrame(data1, index=[0,1,3,5,7,9])
# print(df)
# df.reindex([2,4,6,8,10])
# df['Total']= df.iloc[:, -4:].sum(axis=1)
# print(df)
#    marks   Age
# 0   50.0  55.0
# 1   30.0  84.0
# 3   60.0  68.0
# 5    8.0  21.0
# 7   22.0  77.0
# 9    NaN   NaN
#    marks   Age  Total
# 0   50.0  55.0  105.0
# 1   30.0  84.0  114.0
# 3   60.0  68.0  128.0
# 5    8.0  21.0   29.0
# 7   22.0  77.0   99.0
# 9    NaN   NaN    0.0





###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,60,70,8,90,22,33]),
#          "Age" :pd.Series([55,84,24,68,74,21,54,77,99])
#          }
# df = pd.DataFrame(data1, index=[0,1,3,5,7,9])
# print(df)
# df.reindex([2,4,6,8,10])
# df['Total']= df.iloc[:, :].sum(axis=1)
# print(df)
#    marks   Age
# 0   50.0  55.0
# 1   30.0  84.0
# 3   60.0  68.0
# 5    8.0  21.0
# 7   22.0  77.0
# 9    NaN   NaN
#    marks   Age  Total
# 0   50.0  55.0  105.0
# 1   30.0  84.0  114.0
# 3   60.0  68.0  128.0
# 5    8.0  21.0   29.0
# 7   22.0  77.0   99.0
# 9    NaN   NaN    0.0





###########################################################
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(index=[0,1,2,3,4,5],columns=['one','two'])
# print(df['one'].sum())
# 0



###########################################################
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(index=[0,1,2,3,4,5],columns=['one','two'])
# print(df)
#    one  two
# 0  NaN  NaN
# 1  NaN  NaN
# 2  NaN  NaN
# 3  NaN  NaN
# 4  NaN  NaN
# 5  NaN  NaN




###########################################################
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(index=[0,1,2,3,4,5],columns=['one','two'])
# print(df)
#   one  two
# 0  NaN  NaN
# 1  NaN  NaN
# 2  NaN  NaN
# 3  NaN  NaN
# 4  NaN  NaN
# 5  NaN  NaN



###########################################################
# Cleaning / Filling Missing Data
# Pandas provides various methods for cleaning the missing values. The fillna function can
# “fill in” NA values with non-null data in a couple of ways, which we have illustrated in the following sections.
# Replace NaN with a Scalar Value
# The following program shows how you can replace "NaN" with "0".




###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,60,70,8,90,22,33]),
#          "Age" :pd.Series([55,84,24,68,74,21,54,77,99])
#          }
# df = pd.DataFrame(data1, index=[0,1,3,5,7,9])
# print(df)
# df.reindex([2,4,6,8,10])
# print(df.fillna(0))
#    marks   Age
# 0   50.0  55.0
# 1   30.0  84.0
# 3   60.0  68.0
# 5    8.0  21.0
# 7   22.0  77.0
# 9    NaN   NaN
#    marks   Age
# 0   50.0  55.0
# 1   30.0  84.0
# 3   60.0  68.0
# 5    8.0  21.0
# 7   22.0  77.0
# 9    0.0   0.0




###########################################################
# Fill NA Forward and Backward
# pad/fill == Fill methods Forward
# bfill/backfill == Fill methods Backward



###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,60,70,8,90,22,33]),
#          "Age" :pd.Series([55,84,24,68,74,21,54,77,99])
#          }
# df = pd.DataFrame(data1, index=[0,1,3,5,7,9])
# print(df)
# print(df.reindex([1,2,4,5,6,8,10]))
#
#    marks   Age
# 0   50.0  55.0
# 1   30.0  84.0
# 3   60.0  68.0
# 5    8.0  21.0
# 7   22.0  77.0
# 9    NaN   NaN
#     marks   Age
# 1    30.0  84.0
# 2     NaN   NaN
# 4     NaN   NaN
# 5     8.0  21.0
# 6     NaN   NaN
# 8     NaN   NaN
# 10    NaN   NaN




###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,60,70,8,90,22,33]),
#          "Age" :pd.Series([55,84,24,68,74,21,54,77,99])
#          }
# df = pd.DataFrame(data1, index=[0,1,3,5,7,9])
# print(df)
# print(df.reindex([1,2,4,5,6,8,10]))
# print(df.fillna(method="pad"))
#    marks   Age
# 0   50.0  55.0
# 1   30.0  84.0
# 3   60.0  68.0
# 5    8.0  21.0
# 7   22.0  77.0
# 9    NaN   NaN
#     marks   Age
# 1    30.0  84.0
# 2     NaN   NaN
# 4     NaN   NaN
# 5     8.0  21.0
# 6     NaN   NaN
# 8     NaN   NaN
# 10    NaN   NaN
#    marks   Age
# 0   50.0  55.0
# 1   30.0  84.0
# 3   60.0  68.0
# 5    8.0  21.0
# 7   22.0  77.0
# 9   22.0  77.0





###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,60,70,8,90,22,33]),
#          "Age" :pd.Series([55,84,24,68,74,21,54,77,99])
#          }
# df = pd.DataFrame(data1, index=[0,1,4,6,7,8,9])
# print(df)
# c = df.reindex([3,4,5,6,7,8,9])
# print(c)
# print(c.fillna(method='backfill'))
#    marks   Age
# 0   50.0  55.0
# 1   30.0  84.0
# 4   70.0  74.0
# 6   90.0  54.0
# 7   22.0  77.0
# 8   33.0  99.0
# 9    NaN   NaN
#    marks   Age
# 3    NaN   NaN
# 4   70.0  74.0
# 5    NaN   NaN
# 6   90.0  54.0
# 7   22.0  77.0
# 8   33.0  99.0
# 9    NaN   NaN
#    marks   Age
# 3   70.0  74.0
# 4   70.0  74.0
# 5   90.0  54.0
# 6   90.0  54.0
# 7   22.0  77.0
# 8   33.0  99.0
# 9    NaN   NaN




###########################################################
#Drop Missing Values
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,60,70]),
#          "Age" :pd.Series([55,84,24,68,74,21,54,77,99])
#          }
# df = pd.DataFrame(data1, index=[0,1,3,4,6,7,8,9])
# print(df)
# df = df.reindex([2,4,6,8])
# print(df)
# print(df.dropna())
#    marks   Age
# 0   50.0  55.0
# 1   30.0  84.0
# 3   60.0  68.0
# 4   70.0  74.0
# 6    NaN  54.0
# 7    NaN  77.0
# 8    NaN  99.0
# 9    NaN   NaN
#    marks   Age
# 2    NaN   NaN
# 4   70.0  74.0
# 6    NaN  54.0
# 8    NaN  99.0
#    marks   Age
# 4   70.0  74.0



###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,60,70]),
#          "Age" :pd.Series([55,84,24,68,74,21,54,77,99])
#          }
# df = pd.DataFrame(data1, index=[0,1,3,4,6,7,8,9])
# print(df)
# df = df.reindex([2,4,6,8])
# print(df)
# print(df.dropna(axis=1))
#    marks   Age
# 0   50.0  55.0
# 1   30.0  84.0
# 3   60.0  68.0
# 4   70.0  74.0
# 6    NaN  54.0
# 7    NaN  77.0
# 8    NaN  99.0
# 9    NaN   NaN
#    marks   Age
# 2    NaN   NaN
# 4   70.0  74.0
# 6    NaN  54.0
# 8    NaN  99.0
# Empty DataFrame
# Columns: []
# Index: [2, 4, 6, 8]




###########################################################
# import pandas as pd
# import numpy as np
# df = pd.DataFrame({'one':[10,20,30,40,50,2000], 'two':[1000,0,30,40,50,60]})
# print(df.replace({1000:10,2000:60}))
#    one  two
# 0   10   10
# 1   20    0
# 2   30   30
# 3   40   40
# 4   50   50
# 5   60   60





##########################################################
# import pandas as pd
# import numpy as np
# df = pd.DataFrame({'one':[10,20,30,40,50,2000], 'two':[1000,0,30,40,50,60]})
# print(df)
#     one   two
# 0    10  1000
# 1    20     0
# 2    30    30
# 3    40    40
# 4    50    50
# 5  2000    60






###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,60,70]),
#          "Age" :pd.Series([55,84,24,68,74,21,54,77,99])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.replace({55:111, 50:111, np.NaN:222}))
#    marks  Age
# 0   50.0   55
# 1   30.0   84
# 2   40.0   24
# 3   60.0   68
# 4   70.0   74
# 5    NaN   21
# 6    NaN   54
# 7    NaN   77
# 8    NaN   99
#    marks  Age
# 0  111.0  111
# 1   30.0   84
# 2   40.0   24
# 3   60.0   68
# 4   70.0   74
# 5  222.0   21
# 6  222.0   54
# 7  222.0   77
# 8  222.0   99

