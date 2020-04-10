IO Tools.py




# import pandas as pd
# df=pd.read_csv("aaa.csv")
# print(df)
#    S NO NAME  AGE      CITY  SALARY
# 0     1  aaa   10     patna   10000
# 1     2  bbb   20     noida   20000
# 2     3  ccc   30  banglore   30000
# 3     4  ddd   40     delhi   40000
# 4     5  eee   50       NaN   50000



# import pandas as pd
# df=pd.read_csv("aaa.csv",index_col=['S NO'])
# print(df)
#      NAME  AGE      CITY  SALARY
# S NO
# 1     aaa   10     patna   10000
# 2     bbb   20     noida   20000
# 3     ccc   30  banglore   30000
# 4     ddd   40     delhi   40000
# 5     eee   50       NaN   50000






# import pandas as pd
# import numpy as np
# df=pd.read_csv("aaa.csv", dtype={"SALARY": np.float64})
# print(df)
#    S NO NAME  AGE      CITY   SALARY
# 0     1  aaa   10     patna  10000.0
# 1     2  bbb   20     noida  20000.0
# 2     3  ccc   30  banglore  30000.0
# 3     4  ddd   40     delhi  40000.0
# 4     5  eee   50       NaN  50000.0







# import pandas as pd
# import numpy as np
# df=pd.read_csv("aaa.csv", names=['a','b','x','u','p'])
# print(df)
#       a     b    x         u       p
# 0  S NO  NAME  AGE      CITY  SALARY
# 1     1   aaa   10     patna   10000
# 2     2   bbb   20     noida   20000
# 3     3   ccc   30  banglore   30000
# 4     4   ddd   40     delhi   40000
# 5     5   eee   50       NaN   50000




# import pandas as pd
# import numpy as np
# df=pd.read_csv("aaa.csv", names=['a','b','x','u','p'], header=0)
# print(df)
#    a    b   x         u      p
# 0  1  aaa  10     patna  10000
# 1  2  bbb  20     noida  20000
# 2  3  ccc  30  banglore  30000
# 3  4  ddd  40     delhi  40000
# 4  5  eee  50       NaN  50000



import pandas as pd
import numpy as np
df=pd.read_csv("aaa.csv", skiprows=2)
# print(df)
#    2  bbb  20     noida  20000
# 0  3  ccc  30  banglore  30000
# 1  4  ddd  40     delhi  40000
# 2  5  eee  50       NaN  50000


