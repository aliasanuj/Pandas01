#windowFunction.py


# For working on numerical data, Pandas provide few variants like rolling, expanding and exponentially
# moving weights for window statistics. Among these are sum, mean, median, variance, covariance, correlation, etc.
# We will now learn how each of these can be applied on DataFrame objects.



# import pandas as pd
# import numpy as np
#
# df = pd.DataFrame(np.random.randn(10, 4),
#    index = pd.date_range('1/1/2000', periods=10),
#    columns = ['A', 'B', 'C', 'D'])
# print(df.rolling(window=4).mean())
#                    A         B         C         D
# 2000-01-01       NaN       NaN       NaN       NaN
# 2000-01-02       NaN       NaN       NaN       NaN
# 2000-01-03       NaN       NaN       NaN       NaN
# 2000-01-04  0.563540 -0.521798  0.646420 -0.116904
# 2000-01-05  0.674365 -0.092358 -0.033566 -0.021414
# 2000-01-06  0.432185 -0.136122 -0.546352 -0.169739
# 2000-01-07  0.259291 -0.329536 -1.024802  0.122829
# 2000-01-08 -0.733187 -0.082129 -0.514561  0.733044
# 2000-01-09 -1.042211 -0.181183 -0.369917  0.500487
# 2000-01-10 -0.810391 -0.390391  0.179128  0.903757




# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(10, 4),
#    index = pd.date_range('1/1/2000', periods=10),
#    columns = ['A', 'B', 'C', 'D'])
# print(df.expanding(min_periods=4).mean())
#                    A         B         C         D
# 2000-01-01       NaN       NaN       NaN       NaN
# 2000-01-02       NaN       NaN       NaN       NaN
# 2000-01-03       NaN       NaN       NaN       NaN
# 2000-01-04  0.325304 -0.001888  0.577305  0.595122
# 2000-01-05  0.138966 -0.290149  0.600218  0.719033
# 2000-01-06  0.590343 -0.166360  0.379944  0.423209
# 2000-01-07  0.657514 -0.271413  0.160996  0.590965
# 2000-01-08  0.501505 -0.248942  0.139957  0.803674
# 2000-01-09  0.555946 -0.307417  0.013736  0.665379
# 2000-01-10  0.487680 -0.316211  0.095247  0.750156


import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(10, 4),
                  index=pd.date_range('1/1/2000', periods=10),
                  columns=['A', 'B', 'C', 'D'])
print(df.ewm(com=2).mean())
#                   A         B         C         D
# 2000-01-01 -0.649891  1.090328  0.355584 -0.716391
# 2000-01-02 -0.965120  0.085698  0.853546 -0.168693
# 2000-01-03 -1.189065 -1.261850  0.532502 -0.750300
# 2000-01-04 -0.451777 -1.269725 -0.375475 -1.123512
# 2000-01-05 -0.088120 -0.943360  0.776089 -0.585412
# 2000-01-06 -0.023666 -0.200075  0.500047 -0.886548
# 2000-01-07 -0.175993 -0.287948  0.870611 -0.553695
# 2000-01-08 -0.041377 -0.472424  0.117420 -0.622858
# 2000-01-09  0.149519  0.507394 -0.145436 -0.596742
# 2000-01-10 -0.052993  0.658983  0.136513 -0.471596





























































