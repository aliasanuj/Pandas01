#statical_function.py

# Percent_change
# Series, DatFrames and Panel, all have the function pct_change().
# This function compares every element with
# its prior element and computes the change percentage.

###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.pct_change())
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN
#        marks       Age
# 0        NaN       NaN
# 1  -0.400000  0.527273
# 2   0.333333 -0.714286
# 3   0.375000  1.833333
# 4   0.090909  0.088235
# 5   0.166667 -0.716216
# 6  -0.885714  1.571429
# 7  10.250000  0.000000




###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.pct_change(axis=0))
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN
#        marks       Age
# 0        NaN       NaN
# 1  -0.400000  0.527273
# 2   0.333333 -0.714286
# 3   0.375000  1.833333
# 4   0.090909  0.088235
# 5   0.166667 -0.716216
# 6  -0.885714  1.571429
# 7  10.250000  0.000000





###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.pct_change(axis=1))
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN
#    marks       Age
# 0    NaN  0.100000
# 1    NaN  1.800000
# 2    NaN -0.400000
# 3    NaN  0.236364
# 4    NaN  0.233333
# 5    NaN -0.700000
# 6    NaN  5.750000
# 7    NaN  0.000000





###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([5,10,15,30,60,120,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.pct_change(axis=1))
#    marks    Age
# 0     50    5.0
# 1     30   10.0
# 2     40   15.0
# 3     55   30.0
# 4     60   60.0
# 5     70  120.0
# 6      8   54.0
# 7     90    NaN
#    marks       Age
# 0    NaN -0.900000
# 1    NaN -0.666667
# 2    NaN -0.625000
# 3    NaN -0.454545
# 4    NaN  0.000000
# 5    NaN  0.714286
# 6    NaN  5.750000
# 7    NaN  0.000000




###########################################################
# Covariance
# Covariance is applied on series data. The Series object has a method cov to
# compute covariance between series objects. NA will be excluded automatically.




###########################################################
# import pandas as pd
# import numpy as np
# data1 = pd.Series([50,30,40,55,60,70,8,90])
# data2 = pd.Series([50,30,40,55,60,70,8,90])
# print(data1)
# print(data2)
# print(data1.cov(data2))
# 0    50
# 1    30
# 2    40
# 3    55
# 4    60
# 5    70
# 6     8
# 7    90
# dtype: int64
# 0    50
# 1    30
# 2    40
# 3    55
# 4    60
# 5    70
# 6     8
# 7    90
# dtype: int64
# 626.8392857142857




###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54]),
#          "speed" :pd.Series([20,87,24,100,74,44,54]),
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df["marks"].cov(df["Age"]))
# print(df.cov())
#    marks   Age  speed
# 0     50  55.0   20.0
# 1     30  84.0   87.0
# 2     40  24.0   24.0
# 3     55  68.0  100.0
# 4     60  74.0   74.0
# 5     70  21.0   44.0
# 6      8  54.0   54.0
# 7     90   NaN    NaN
# -113.23809523809524
#             marks         Age       speed
# marks  626.839286 -113.238095    0.357143
# Age   -113.238095  580.904762  537.142857
# speed    0.357143  537.142857  945.285714




###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54]),
#          "speed" :pd.Series([20,87,24,100,74,44,54]),
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df["marks"].corr(df["Age"]))
# print(df.corr())
#    marks   Age  speed
# 0     50  55.0   20.0
# 1     30  84.0   87.0
# 2     40  24.0   24.0
# 3     55  68.0  100.0
# 4     60  74.0   74.0
# 5     70  21.0   44.0
# 6      8  54.0   54.0
# 7     90   NaN    NaN
# -0.2259844554913825
#           marks       Age     speed
# marks  1.000000 -0.225984  0.000559
# Age   -0.225984  1.000000  0.724863
# speed  0.000559  0.724863  1.000000








###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54]),
#          "speed" :pd.Series([20,87,24,100,74,44,54]),
#          }
# df = pd.DataFrame(data1)
# print(df)
# df["marks"] = (df["Age"])
# print(df.rank())
#    marks   Age  speed
# 0     50  55.0   20.0
# 1     30  84.0   87.0
# 2     40  24.0   24.0
# 3     55  68.0  100.0
# 4     60  74.0   74.0
# 5     70  21.0   44.0
# 6      8  54.0   54.0
# 7     90   NaN    NaN
#    marks  Age  speed
# 0    4.0  4.0    1.0
# 1    7.0  7.0    6.0
# 2    2.0  2.0    2.0
# 3    5.0  5.0    7.0
# 4    6.0  6.0    5.0
# 5    1.0  1.0    3.0
# 6    3.0  3.0    4.0
# 7    NaN  NaN    NaN



###########################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54]),
#          "speed" :pd.Series([20,87,24,100,74,44,54]),
#          }
# df = pd.DataFrame(data1)
# print(df)
# df["marks"] = df["Age"]
# print(df)
#    marks   Age  speed
# 0     50  55.0   20.0
# 1     30  84.0   87.0
# 2     40  24.0   24.0
# 3     55  68.0  100.0
# 4     60  74.0   74.0
# 5     70  21.0   44.0
# 6      8  54.0   54.0
# 7     90   NaN    NaN
#    marks   Age  speed
# 0   55.0  55.0   20.0
# 1   84.0  84.0   87.0
# 2   24.0  24.0   24.0
# 3   68.0  68.0  100.0
# 4   74.0  74.0   74.0
# 5   21.0  21.0   44.0
# 6   54.0  54.0   54.0
# 7    NaN   NaN    NaN
