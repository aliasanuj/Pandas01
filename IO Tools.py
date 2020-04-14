#IO Tools.py
#################################################################3




#################################################################3
# import pandas as pd
# df=pd.read_csv("aaa.csv")
# print(df)
#    S NO  NAME  AGE      CITY  SALARY  SALARY1  TOTAL
# 0      0  aaa   10     patna   10000      200    NaN
# 1      1  bbb   20     noida   20000      400    NaN
# 2      2  ccc   30  banglore   30000      600    NaN
# 3      3  ddd   40     delhi   40000      800    NaN
# 4      4  eee   50       NaN   50000     1000    NaN








#################################################################3
# import pandas as pd
# df = pd.read_csv("aaa.csv",index_col=['NAME'])
# print(df)
#       S NO   AGE      CITY  SALARY  SALARY1  TOTAL
# NAME
# aaa       0   10     patna   10000      200    NaN
# bbb       1   20     noida   20000      400    NaN
# ccc       2   30  banglore   30000      600    NaN
# ddd       3   40     delhi   40000      800    NaN
# eee       4   50       NaN   50000     1000    NaN




#################################################################3
# import pandas as pd
# df = pd.read_csv("aaa.csv",index_col=['S NO'])
# print(df)
#      NAME  AGE      CITY  SALARY  SALARY1  TOTAL
# S NO
# 0     aaa   10     patna   10000      200    NaN
# 1     bbb   20     noida   20000      400    NaN
# 2     ccc   30  banglore   30000      600    NaN
# 3     ddd   40     delhi   40000      800    NaN
# 4     eee   50       NaN   50000     1000    NaN





#################################################################3
# import pandas as pd
# import numpy as np
# df=pd.read_csv("aaa.csv", dtype={"SALARY": np.float64})
# print(df)
#    S NO NAME  AGE      CITY   SALARY  SALARY1  TOTAL
# 0     0  aaa   10     patna  10000.0      200    NaN
# 1     1  bbb   20     noida  20000.0      400    NaN
# 2     2  ccc   30  banglore  30000.0      600    NaN
# 3     3  ddd   40     delhi  40000.0      800    NaN
# 4     4  eee   50       NaN  50000.0     1000    NaN





#################################################################3
# import pandas as pd
# import numpy as np
# df=pd.read_csv("aaa.csv", names=['a','b','x','u','p'])
# print(df)
#              a         b       x        u      p
# S NO NAME  AGE      CITY  SALARY  SALARY1  TOTAL
# 0    aaa    10     patna   10000      200    NaN
# 1    bbb    20     noida   20000      400    NaN
# 2    ccc    30  banglore   30000      600    NaN
# 3    ddd    40     delhi   40000      800    NaN
# 4    eee    50       NaN   50000     1000    NaN





#################################################################3
# import pandas as pd
# import numpy as np
# df=pd.read_csv("aaa.csv", names=['a','b','x','u','p','c'])
# print(df)
#          a    b         x       u        p      c
# S NO  NAME  AGE      CITY  SALARY  SALARY1  TOTAL
# 0      aaa   10     patna   10000      200    NaN
# 1      bbb   20     noida   20000      400    NaN
# 2      ccc   30  banglore   30000      600    NaN
# 3      ddd   40     delhi   40000      800    NaN
# 4      eee   50       NaN   50000     1000    NaN






#################################################################3
# import pandas as pd
# import numpy as np
# df=pd.read_csv("aaa.csv", names=['a','b','x','u','p','c','A'])
# print(df)
#       a     b    x         u       p        c      A
# 0  S NO  NAME  AGE      CITY  SALARY  SALARY1  TOTAL
# 1     0   aaa   10     patna   10000      200    NaN
# 2     1   bbb   20     noida   20000      400    NaN
# 3     2   ccc   30  banglore   30000      600    NaN
# 4     3   ddd   40     delhi   40000      800    NaN
# 5     4   eee   50       NaN   50000     1000    NaN




################################################################3
# import pandas as pd
# import numpy as np
# df=pd.read_csv("aaa.csv", names=['a','b','x','u','p'], header=0)
# print(df)
#         a         b      x     u   p
# 0 aaa  10     patna  10000   200 NaN
# 1 bbb  20     noida  20000   400 NaN
# 2 ccc  30  banglore  30000   600 NaN
# 3 ddd  40     delhi  40000   800 NaN
# 4 eee  50       NaN  50000  1000 NaN





################################################################3
# import pandas as pd
# import numpy as np
# df=pd.read_csv("aaa.csv", names=['a','b','x','u','p','P'], header=0)
# print(df)
#      a   b         x      u     p   P
# 0  aaa  10     patna  10000   200 NaN
# 1  bbb  20     noida  20000   400 NaN
# 2  ccc  30  banglore  30000   600 NaN
# 3  ddd  40     delhi  40000   800 NaN
# 4  eee  50       NaN  50000  1000 NaN




################################################################3
# import pandas as pd
# import numpy as np
# df=pd.read_csv("aaa.csv", skiprows=2)
# print(df)
#    1  bbb  20     noida  20000   400  Unnamed: 6
# 0  2  ccc  30  banglore  30000   600         NaN
# 1  3  ddd  40     delhi  40000   800         NaN
# 2  4  eee  50       NaN  50000  1000         NaN




################################################################3
# import pandas as pd
# df = pd.read_csv("aaa.csv")
# print(df["AGE"])
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# Name: AGE, dtype: int64




################################################################3
# import pandas as pd
# df = pd.read_csv("aaa.csv")
# df['TOTAL'] = df["SALARY"] + df["SALARY1"]
# print(df)
#    S NO NAME  AGE      CITY  SALARY  SALARY1  TOTAL
# 0     0  aaa   10     patna   10000      200  10200
# 1     1  bbb   20     noida   20000      400  20400
# 2     2  ccc   30  banglore   30000      600  30600
# 3     3  ddd   40     delhi   40000      800  40800
# 4     4  eee   50       NaN   50000     1000  51000





