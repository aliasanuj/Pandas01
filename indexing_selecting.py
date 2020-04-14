###############################################################
# .loc() == Label based
# .iloc() == Integer based
# .ix() == Both Label and Integer based


###############################################################
# .loc()
# Pandas provide various methods to have purely label based indexing. When slicing, the start
# bound is also included. Integers are valid labels, but they refer to the label and not the position.
# .loc() has multiple access methods like −
#
# A single scalar label
# A list of labels
# A slice object
# A Boolean array
#
# loc takes two single/list/range operator separated by ','.
# The first one indicates the row and the second one indicates columns.




###############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.loc[:,'Age'])
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN
# 0    55.0
# 1    84.0
# 2    24.0
# 3    68.0
# 4    74.0
# 5    21.0
# 6    54.0
# 7     NaN
# Name: Age, dtype: float64






###############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.loc[:,'marks'])
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN
# 0    50
# 1    30
# 2    40
# 3    55
# 4    60
# 5    70
# 6     8
# 7    90




###############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.loc["marks":])
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN
# Empty DataFrame
# Columns: [marks, Age]
# Index: []





###############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.loc["Age":])
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN
# Empty DataFrame
# Columns: [marks, Age]
# Index: []




###############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.loc[[2,4,6,7,10,12,14,5]:"Age"])
# TypeError: '[2, 4, 6, 7, 10, 12, 14, 5]' is an invalid key




###############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.loc[2,4,6,7,10,12,14,5:"Age"])
# TypeError: cannot do label indexing on <class 'pandas.core.indexes.base.Index'> with these indexers [4] of <class 'int'>






###############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.loc[['a','b','c']:"Age"])
# TypeError: '['a', 'b', 'c']' is an invalid key




###############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54]),
#          "speed" :pd.Series([100,200,300,68,74,21,54]),
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.loc[:,['Age','speed']])
#    marks   Age  speed
# 0     50  55.0  100.0
# 1     30  84.0  200.0
# 2     40  24.0  300.0
# 3     55  68.0   68.0
# 4     60  74.0   74.0
# 5     70  21.0   21.0
# 6      8  54.0   54.0
# 7     90   NaN    NaN
#     Age  speed
# 0  55.0  100.0
# 1  84.0  200.0
# 2  24.0  300.0
# 3  68.0   68.0
# 4  74.0   74.0
# 5  21.0   21.0
# 6  54.0   54.0
# 7   NaN    NaN



###############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54]),
#          "speed" :pd.Series([100,200,300,68,74,21,54]),
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.loc[3:,['Age','speed']])
#    marks   Age  speed
# 0     50  55.0  100.0
# 1     30  84.0  200.0
# 2     40  24.0  300.0
# 3     55  68.0   68.0
# 4     60  74.0   74.0
# 5     70  21.0   21.0
# 6      8  54.0   54.0
# 7     90   NaN    NaN
#     Age  speed
# 3  68.0   68.0
# 4  74.0   74.0
# 5  21.0   21.0
# 6  54.0   54.0
# 7   NaN    NaN




###############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54]),
#          "speed" :pd.Series([100,200,300,68,74,21,54]),
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.loc[:,['Age','speed']])
#    marks   Age  speed
# 0     50  55.0  100.0
# 1     30  84.0  200.0
# 2     40  24.0  300.0
# 3     55  68.0   68.0
# 4     60  74.0   74.0
# 5     70  21.0   21.0
# 6      8  54.0   54.0
# 7     90   NaN    NaN
#     Age  speed
# 0  55.0  100.0
# 1  84.0  200.0
# 2  24.0  300.0
# 3  68.0   68.0
# 4  74.0   74.0
# 5  21.0   21.0
# 6  54.0   54.0
# 7   NaN    NaN




###############################################################
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(8, 4), index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])
# # Select few rows for multiple columns, say list[]
# print(df.loc[['a','b','f','h'],['A','C']])
#           A         C
# a  1.588854  0.085115
# b  0.274947  1.542207
# f  0.041937 -2.095217
# h -0.475685  0.178973



###############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54]),
#          "speed" :pd.Series([100,200,300,68,74,21,54]),
#          }
# df = pd.DataFrame(data1)
# print(df)
#    marks   Age  speed
# 0     50  55.0  100.0
# 1     30  84.0  200.0
# 2     40  24.0  300.0
# 3     55  68.0   68.0
# 4     60  74.0   74.0
# 5     70  21.0   21.0
# 6      8  54.0   54.0
# 7     90   NaN    NaN



###############################################################
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(8, 4),
# index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])
# # Select range of rows for all columns
# print(df)
# print(df.loc['a':'d'])
#           A         B         C         D
# a -0.546930 -0.507048 -2.236853 -1.925316
# b -0.800004 -0.860603 -1.120363  0.705366
# c  0.558034  0.085681 -0.428152  0.268037
# d -0.977106 -1.941815 -1.642988 -1.085863
# e -0.425805  0.396917  0.785847 -0.574135
# f  0.239817  1.735336  1.223952 -0.206469
# g  1.441784  0.377887  0.633387 -1.576395
# h -0.750919  0.150982  0.068751 -0.174174
#           A         B         C         D
# a -0.546930 -0.507048 -2.236853 -1.925316
# b -0.800004 -0.860603 -1.120363  0.705366
# c  0.558034  0.085681 -0.428152  0.268037
# d -0.977106 -1.941815 -1.642988 -1.085863




###############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54]),
#          "speed" :pd.Series([100,200,300,68,74,21,54]),
#          }
# df = pd.DataFrame(data1)
# print(df.loc[:,"Age"])
# 0    55.0
# 1    84.0
# 2    24.0
# 3    68.0
# 4    74.0
# 5    21.0
# 6    54.0
# 7     NaN



###############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54]),
#          "speed" :pd.Series([100,200,300,68,74,21,54]),
#          }
# df = pd.DataFrame(data1)
# print(df.loc[2:3,1:2])
# TypeError: cannot do slice indexing on <class 'pandas.core.indexes.base.Index'> with these indexers [1] of <class 'int'>



###############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([5,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,5,24,68,74,21,54]),
#          "speed" :pd.Series([100,5,300,68,74,21,54]),
#          }
# df = pd.DataFrame(data1)
# print(df.loc[1]>20)
# marks     True
# Age      False
# speed    False
# Name: 1, dtype: bool






###############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([5,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,5,24,68,74,21,54]),
#          "speed" :pd.Series([100,5,300,68,74,21,54,100]),
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.loc[7]>20)
#    marks   Age  speed
# 0      5  55.0    100
# 1     30   5.0      5
# 2     40  24.0    300
# 3     55  68.0     68
# 4     60  74.0     74
# 5     70  21.0     21
# 6      8  54.0     54
# 7     90   NaN    100
# marks     True
# Age      False
# speed     True
# Name: 7, dtype: bool





###############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([5,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,5,24,68,74,21,54]),
#          "speed" :pd.Series([100,5,300,68,74,21,54]),
#          }
# df = pd.DataFrame(data1)
# print(df.loc[2]>20)
# marks    True
# Age      True
# speed    True
# Name: 2, dtype: bool




###############################################################
# .iloc()
# Pandas provide various methods in order to get purely integer based indexing.
# Like python and numpy, these are 0-based indexing.
# The various access methods are as follows −
# == An Integer
# == A list of integers
# == A range of values



###############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([5,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,5,24,68,74,21,54]),
#          "speed" :pd.Series([100,5,300,68,74,21,54]),
#          }
# df = pd.DataFrame(data1)
# print(df.iloc[:])
#    marks   Age  speed
# 0      5  55.0  100.0
# 1     30   5.0    5.0
# 2     40  24.0  300.0
# 3     55  68.0   68.0
# 4     60  74.0   74.0
# 5     70  21.0   21.0
# 6      8  54.0   54.0
# 7     90   NaN    NaN



###############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([5,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,5,24,68,74,21,54]),
#          "speed" :pd.Series([100,5,300,68,74,21,54]),
#          }
# df = pd.DataFrame(data1)
# print(df.iloc[2:5])
#    marks   Age  speed
# 2     40  24.0  300.0
# 3     55  68.0   68.0
# 4     60  74.0   7





###############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([5,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,5,24,68,74,21,54]),
#          "speed" :pd.Series([100,5,300,68,74,21,54]),
#          }
# df = pd.DataFrame(data1)
# print(df.iloc[2:4, 1:5])
#     Age  speed
# 2  24.0  300.0
# 3  68.0   68.





###############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([5,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,5,24,68,74,21,54]),
#          "speed" :pd.Series([100,5,300,68,74,21,54]),
#          }
# df = pd.DataFrame(data1)
# print(df.iloc[2:4, 2:3])
#    speed
# 2  300.0
# 3   68.0




###############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([5,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,5,24,68,74,21,54]),
#          "speed" :pd.Series([100,5,300,68,74,21,54]),
#          }
# df = pd.DataFrame(data1)
# print(df.iloc[0:4, 0:3])
#    marks   Age  speed
# 0      5  55.0  100.0
# 1     30   5.0    5.0
# 2     40  24.0  300.0
# 3     55  68.0   68.0




###############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([5,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,5,24,68,74,21,54]),
#          "speed" :pd.Series([100,5,300,68,74,21,54]),
#          }
# df = pd.DataFrame(data1)
# print(df.iloc[0:4, 0:2])
#    marks   Age
# 0      5  55.0
# 1     30   5.0
# 2     40  24.0
# 3     55  68.0



###############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([5,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,5,24,68,74,21,54]),
#          "speed" :pd.Series([100,5,300,68,74,21,54]),
#          }
# df = pd.DataFrame(data1)
# print(df.iloc[2:4, 0:2])
#    marks   Age
# 2     40  24.0
# 3     55  68.0


###############################################################
# .ix()
# Besides pure label based and integer based, Pandas provides a hybrid method for
# selections and subsetting the object using the .ix() operator.


# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
# print(df[['A','B']])
#           A         B
# 0 -3.668412 -0.232867
# 1 -0.824876  0.496511
# 2  0.498475 -0.854420
# 3 -1.711619  0.403228
# 4  0.008772 -0.175005
# 5  1.218508  0.465182
# 6  2.688355  0.061993
# 7  0.318440  0.711069













