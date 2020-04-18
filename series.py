# data --- data takes various forms like ndarray, list, constants
# index --- Index values must be unique and hashable, same length as data. Default np.arrange(n) if no index is passed.
# dtype  --- dtype is for data type. If None, data type will be inferred
# copy --- Copy data. Default False


#pandas.Series( data, index, dtype, copy)

###########################################################
#import the pandas library and aliasing as pd
# import pandas as pd
# s = pd.Series()
# print(s)
# Series([], dtype: float64)



############################################################
#import the pandas library and aliasing as pd
# import pandas as pd
# import numpy as np
# data = np.array(['a','b','c','d'])
# s = pd.Series(data)
# print (s)
# 0    a
# 1    b
# 2    c
# 3    d
# dtype: object



############################################################
#import the pandas library and aliasing as pd
# import pandas as pd
# import numpy as np
# data = np.array(['a','b','c','d'])
# s = pd.Series(data,index=[2,3,4,5])
# print (s)
# 2    a
# 3    b
# 4    c
# 5    d
# dtype: object




############################################################
# import pandas as pd
# import numpy as np
# data = np.array(['a','b','c','d'])
# s = pd.Series(data,index=[2,3,4,5,6])
# print (s)
# ValueError: Length of passed values is 4, index implies 5.




##################################
# import pandas as pd
# import numpy as np
# data = np.array(['a','b','c','d','e','f','g'])
# s = pd.Series(data,index=[2,3,4,5,6,"aa",9])
# print (s)
# 2     a
# 3     b
# 4     c
# 5     d
# 6     e
# aa    f
# 9     g
# dtype: object





############################################################
#import the pandas library and aliasing as pd
# import pandas as pd
# import numpy as np
# data = {'a' : 0., 'b' : 1., 'c' : 2.}
# s = pd.Series(data)
# print(s)

# a    0.0
# b    1.0
# c    2.0
# dtype: float64





############################################################
#import the pandas library and aliasing as pd
# import pandas as pd
# import numpy as np
# data = {'a' : 0, 'b' : 1, 'c' : 2,'x':" "}
# s = pd.Series(data)
# print(s)
# a    0
# b    1
# c    2
# x
# dtype: object



############################################################
#import the pandas library and aliasing as pd
# import pandas as pd
# import numpy as np
# data = {'a' : 0, 'b' : 1, 'c' : 2,'x':np.NAN}
# s = pd.Series(data)
# print(s)
# a    0.0
# b    1.0
# c    2.0
# x    NaN


############################################################
#import the pandas library and aliasing as pd
# import pandas as pd
# import numpy as np
# data = {'a' : 0, 'b' : 1, 'c' : 2,'x':np.nan}
# s = pd.Series(data)
# print(s)
# a    0.0
# b    1.0
# c    2.0
# x    NaN
# dtype: float64




############################################################
#import the pandas library and aliasing as pd
# import pandas as pd
# import numpy as np
# data = {'a' : 0., 'b' : 1., 'c' : 2.}
# s = pd.Series(data,index=['b','c','d','a'])
# print (s)
# #
# b    1.0
# c    2.0
# d    NaN
# a    0.0
# dtype: float64




##################################
# import pandas as pd
# import numpy as np
# data = {'a' : 0., 'b' : 1., 'c' : 2.}
# s = pd.Series(data,index=['b','c','d','a'])
# print (s.fillna(111))
# b      1.0
# c      2.0
# d    111.0
# a      0.0
# dtype: float64




##################################
# import pandas as pd
# import numpy as np
# data = {'a' : 0., 'b' : 1., 'c' : 2.}
# s = pd.Series(data,index=['b','c','d','a'])
# print (s.fillna())
# ValueError: Must specify a fill 'value' or 'method'.







##################################
#import the pandas library and aliasing as pd
# import pandas as pd
# import numpy as np
# s = pd.Series(5, index=[0, 1, 2, 3])
# print(s)
#
# 0    5
# 1    5
# 2    5
# 3    5
# dtype: int64





##################################
#import the pandas library and aliasing as pd
# import pandas as pd
# import numpy as np
# s = pd.Series(5, index=[0, 1, 2, 3,'a'])
# print(s)
# 0    5
# 1    5
# 2    5
# 3    5
# a    5
# dtype: int64




##################################
# import pandas as pd
# import numpy as np
# s = pd.Series("5", index=[0, 1, 2, 3,'a'])
# print(s)
# 0    5
# 1    5
# 2    5
# 3    5
# a    5





##################################
#import the pandas library and aliasing as pd
# import pandas as pd
# import numpy as np
# s = pd.Series(5)
# print(s)
#
# 0    5
# dtype: int64
#


##################################
# import pandas as pd
# s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
# #retrieve the first element
# print(s)
# a    1
# b    2
# c    3
# d    4
# e    5
# dtype: int64




##################################
# import pandas as pd
# s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e','f'])
# #retrieve the first element
# print(s)
# ValueError: Length of passed values is 5, index implies 6.
#



##################################
# import pandas as pd
# s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
# #retrieve the first element
# print(s[2])
# 3



##################################
# import pandas as pd
# s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
# #retrieve the first element
# print(s['c'])
# print(s['p'])
# 3KeyError: 'p'
# error






##################################
# import pandas as pd
# s = pd.Series([7,8,9,10,11],index = ['a','b','c','d','e'])
# #retrieve the first element
# print(s[2])
# 9



##################################
# import pandas as pd
# s = pd.Series([7,8,9,10,11],index = ['a','b','c','d','e'])
# #retrieve the first element
# print(s[2:])
# c     9
# d    10
# e    11
# dtype: int64




##################################
# import pandas as pd
# s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
# #retrieve the first three element
# print(s[:3])
# a    1
# b    2
# c    3
# dtype: int64



##################################
# import pandas as pd
# s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
# #retrieve the first three element
# print(s[:])
# a    1
# b    2
# c    3
# d    4
# e    5
# dtype: int64


##################################
# import pandas as pd
# s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
# #retrieve the first three element
# print(s[3:])
# d    4
# e    5
# dtype: int64



##################################
# import pandas as pd
# s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
# #retrieve the last three element
# print (s[-3:])
# c    3
# d    4
# e    5
# dtype: int64




##################################
# import pandas as pd
# s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
# #retrieve a single element
# print(s['c'])
# 3




##################################
# import pandas as pd
# s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
# #retrieve multiple elements
# print(s[['a']])
# a    1
# dtype: int64




##################################
# import pandas as pd
# s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
# #retrieve multiple elements
# print(s[['a','c','d']])
# a    1
# c    3
# d    4
# dtype: int64



##################################
# import pandas as pd
# s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
# #retrieve multiple elements
# try :
#     print(s['f'])
# except KeyError:
#     print("not present")
# not present




##################################
# import pandas as pd
# s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
# #retrieve multiple elements
# try :
#     print(s['f'])
# except  KeyError as e:\
#     print("not present")
#not present




##############################33
# import pandas as pd
# import numpy as np
# s = pd.Series([1,2,3,4,np.nan],index = ['a','b','c','d','e'])
# #retrieve the first element
# print (s)
# a    1.0
# b    2.0
# c    3.0
# d    4.0
# e    NaN
# dtype: float64




# import pandas as pd
# import numpy as np
# s = pd.Series([1,2,3,4,5],index = ['a','b','c','d',np.nan])
# #retrieve the first element
# print (s)
# a      1
# b      2
# c      3
# d      4
# NaN    5
# dtype: int64



#####################################
# import pandas as pd
# import numpy as np
# s = pd.Series([1,2,3,4,np.nan],index = ['a','b','c','d','e'])
# #retrieve the first element
# print (s['e'])
# nan




########################################3
# import pandas as pd
# s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
# #retrieve the first element
# print (s)
# a    1
# b    2
# c    3
# d    4
# e    5
# dtype: int64

########################################3



