###########################################################333
# data  -- data takes various forms like ndarray, series, map, lists, dict, constants and also another DataFrame.
# index  -- For the row labels, the Index to be used for the resulting frame is Optional Default np.arange(n) if no index is passed.
# columns -- For column labels, the optional default syntax is - np.arange(n). This is only true if no index is passed.
# dtype -- Data type of each column.
# copy -- This command (or whatever it is) is used for copying of data, if the default is False.




###########################################################333
# Create DataFrame
# A pandas DataFrame can be created using various inputs like −
#
# Lists
# dict
# Series
# Numpy ndarrays
# Another DataFrame



###########################################################333
# import pandas as pd
# df = pd.DataFrame()
# print(df)
# Empty DataFrame
# Columns: []
# Index: []



###########################################################333
# import pandas as pd
# data = [1,2,3,4,5,6]
# df = pd.DataFrame(data)
# print(df)
#    0
# 0  1
# 1  2
# 2  3
# 3  4
# 4  5
# 5  6



###########################################################333
# import pandas as pd
# data = [1,2,3,4,5,6]
# df = pd.DataFrame(data,index=[7,7,7,7,7,7])
# print(df)
#    0
# 7  1
# 7  2
# 7  3
# 7  4
# 7  5
# 7  6



###########################################################333
# import pandas as pd
# data = ["a","b","c","d","e"]
# df = pd.DataFrame(data)
# print(df)
#    0
# 0  a
# 1  b
# 2  c
# 3  d
# 4  e



###########################################################333
# import pandas as pd
# list1 = [["anuj",20],["anuj",21],["anuj",22]]
# df = pd.DataFrame(list1,columns=["name","marks"])
# print(df)
#    name  marks
# 0  anuj     20
# 1  anuj     21
# 2  anuj     22





###########################################################333
# import pandas as pd
# list1 = [["anuj",20],["anuj",21],["anuj",22]]
# df = pd.DataFrame(list1)
# print(df)
#       0   1
# 0  anuj  20
# 1  anuj  21
# 2  anuj  22




###########################################################
# import pandas as pd
# list1 = [["anuj",20],["anuj",21],["anuj",22]]
# df = pd.DataFrame(list1)
# print(df)
#      0   1
# 0  anuj  20
# 1  anuj  21
# 2  anuj  22




###########################################################
# import pandas as pd
# list1 = [["anuj",20],["anuj",21],["anuj",22]]
# df = pd.DataFrame(list1,index=[10,11,12])
# print(df)
#        0   1
# 10  anuj  20
# 11  anuj  21
# 12  anuj  22




###########################################################
# import pandas as pd
# list1 = [["anuj",20],["anuj",21],["anuj",22],["dohdsu","nfdsjf","ohfudhg"]]
# df = pd.DataFrame(list1)
# print(df)
#         0       1        2
# 0    anuj      20     None
# 1    anuj      21     None
# 2    anuj      22     None
# 3  dohdsu  nfdsjf  ohfudhg





###########################################################
# import pandas as pd
# data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
# df = pd.DataFrame(data,)
# print(df)
#     Name  Age
# 0    Tom   28
# 1   Jack   34
# 2  Steve   29
# 3  Ricky   42



###########################################################
# import pandas as pd
# data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42,55]}
# df = pd.DataFrame(data,)
# print(df)
# ValueError: arrays must all be same length




###########################################################
# import pandas as pd
# data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
# df = pd.DataFrame(data,index=[2,2,2,2])
# print(df)
#     Name  Age
# 2    Tom   28
# 2   Jack   34
# 2  Steve   29
# 2  Ricky   42



###########################################################
# import pandas as pd
# data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
# df = pd.DataFrame(data)
# print(df)
#     Name  Age
# 0    Tom   28
# 1   Jack   34
# 2  Steve   29
# 3  Ricky   42





###########################################################
# import pandas as pd
# data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
# df = pd.DataFrame(data,columns=[5,5,5,5])
# print(df)
# Empty DataFrame
# Columns: [5, 5, 5, 5]
# Index: []




###########################################################
# import pandas as pd
# data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
# df = pd.DataFrame(data,columns=['a','b','c','d'])
# print(df)
# Empty DataFrame
# Columns: [a, b, c, d]
# Index: []



###########################################################
# import pandas as pd
# data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
# df = pd.DataFrame(data,index=[5,5,5,5])
# print(df)
#     Name  Age
# 5    Tom   28
# 5   Jack   34
# 5  Steve   29
# 5  Ricky   42


###########################################################
# import pandas as pd
# data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
# df = pd.DataFrame(data,index = [5,5])
# print(df)
#    a   b     c
# 5  1   2   NaN
# 5  5  10  20.0




###########################################################
# import pandas as pd
# data = [{"a":5,"b":6},{"a":5,"b":6,"c":7}]
# df1 = pd.DataFrame(data,index=[2,2])
# print(df1)
# df2 = pd.DataFrame(data, columns=['a','b','d'])
# print(df2)
#    a  b    c
# 2  5  6  NaN
# 2  5  6  7.0
#
#    a  b   d
# 0  5  6 NaN
# 1  5  6 NaN



###########################################################
# import pandas as pd
# data = [{"a":5,"b":6},{"a":5,"b":6,"c":7}]
# df1 = pd.DataFrame(data,index=[2,2])
# print(df1)
# df2 = pd.DataFrame(data, columns=['a','b','d','x','c'])
# print(df2)
#    a  b    c
# 2  5  6  NaN
# 2  5  6  7.0
#    a  b   d   x    c
# 0  5  6 NaN NaN  NaN
# 1  5  6 NaN NaN  7.0




###########################################################
# import pandas as pd
# d = {'one' : pd.Series([1, 2, 3], index=['a', 'b','c']),
#      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
# df = pd.DataFrame(d)
# print(df)
#    one  two
# a  1.0    1
# b  2.0    2
# c  3.0    3
# d  NaN    4




###########################################################
# import pandas as pd
# d = {'one' : pd.Series([1, 2, 3], index=['a', 'b','c']),
#      'two' : pd.Series([1, 2, 3], index=['a', 'b', 'c'])}
# df = pd.DataFrame(d)
# print(df)
#    one  two
# a    1    1
# b    2    2
# c    3    3



###########################################################
# import pandas as pd
# d = {'one' : pd.Series([1, 2, 3, 4], index=['a', 'b','c','d']),
#      'two' : pd.Series([1, 2, 3], index=['a', 'b', 'c'])}
# df = pd.DataFrame(d)
# print(df)
#    one  two
# a    1  1.0
# b    2  2.0
# c    3  3.0
# d    4  NaN



###########################################################
# import pandas as pd
# d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
# df = pd.DataFrame(d)
# print(df ['one'])
# a    1.0
# b    2.0
# c    3.0
# d    NaN
# Name: one, dtype: float64



###########################################################
# import pandas as pd
# d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#      'two' : pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd','e'])}
# df = pd.DataFrame(d)
# print(df ['one'])
# a    1.0
# b    2.0
# c    3.0
# d    NaN
# e    NaN
# Name: one, dtype: float64



###########################################################
# import pandas as pd
# d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c','d'])} #both should be equal
# df = pd.DataFrame(d)
# print(df ['one'])
# a    1.0
# b    2.0
# c    3.0
# d    NaN
# Name: one, dtype: float64



###########################################################
# import pandas as pd
# d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
# d["three"] = pd.Series([5,5,5], index=['c', 'd', 'e'])
# df = pd.DataFrame(d)
# print(df)
#    one  two  three
# a  1.0  1.0    NaN
# b  2.0  2.0    NaN
# c  3.0  3.0    5.0
# d  NaN  4.0    5.0
# e  NaN  NaN    5.0





###########################################################
# import pandas as pd
# d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
# d["three"] = pd.Series([5,5,5], index=['c', 'd', 'e','xx'])
# df = pd.DataFrame(d)
# print(df)
# #ValueError: Length of passed values is 3, index implies 4.




###########################################################
# import pandas as pd
# d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b'])}
# d["three"] = pd.Series([5,5,5,5], index=['c', 'd', 'e','xx'])
# df = pd.DataFrame(d)
# print(df)
#ValueError: Length of passed values is 4, index implies 2.





###########################################################
# import pandas as pd
# d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'd','e'])}
# d["three"] = pd.Series([5,5,5,5], index=['c', 'd', 'e','xx'])
# df = pd.DataFrame(d)
# print(df)
#     one  two  three
# a   1.0  1.0    NaN
# b   2.0  2.0    NaN
# c   3.0  NaN    5.0
# d   NaN  3.0    5.0
# e   NaN  4.0    5.0
# xx  NaN  NaN    5.0






###########################################################
# import pandas as pd
# d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#      'two' : pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])}
# d["three"] = pd.Series([5,5,5], index=['c', 'd', 'e'])
# df = pd.DataFrame(d)
# df["sum"] = df["one"] + df["two"] + df["three"]
# print(df)
#    one   two  three   sum
# a  1.0  10.0    NaN   NaN
# b  2.0  20.0    NaN   NaN
# c  3.0  30.0    5.0  38.0
# d  NaN  40.0    5.0   NaN
# e  NaN   NaN    5.0   NaN
#





###########################################################
# import pandas as pd
# d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#      'two' : pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])}
# d["three"] = pd.Series([5,5,5], index=['c', 'd', 'e'])
# df = pd.DataFrame(d)
# print(df)
#    one   two  three
# a  1.0  10.0    NaN
# b  2.0  20.0    NaN
# c  3.0  30.0    5.0
# d  NaN  40.0    5.0
# e  NaN   NaN    5.0





###########################################################
# import pandas as pd
# d = {"one": pd.Series([1,2,3], index=["a","b","c"]) ,
#      "two": pd.Series([1,2,3,4], index=["a","b","c","d"]),
#      "three": pd.Series([1,2,3,5], index=["a","b","c","e"]) }
# df = pd.DataFrame(d)
# print(df)
#    one  two  three
# a  1.0  1.0    1.0
# b  2.0  2.0    2.0
# c  3.0  3.0    3.0
# d  NaN  4.0    NaN
# e  NaN  NaN    5.0




###########################################################
# import pandas as pd
# d = {"one": pd.Series([1,2,3], index=["a","b","c"]) ,
#      "two": pd.Series([1,2,3], index=["a","c","e"]),
#      "three": pd.Series([1,2,3,5], index=["a","b","x","d"]) }
# df = pd.DataFrame(d)
# print(df)
#    one  two  three
# a  1.0  1.0    1.0
# b  2.0  NaN    2.0
# c  3.0  2.0    NaN
# d  NaN  NaN    5.0
# e  NaN  3.0    NaN
# x  NaN  NaN    3.0




###########################################################
# import pandas as pd
# d = {"one": pd.Series([1,2,3], index=["a","b","c"]) ,
#      "two": pd.Series([1,2,3,4], index=["a","b","c","d"]),
#      "three": pd.Series([1,2,3,5], index=["a","b","c","e"]) }
# df = pd.DataFrame(d)
# del df["two"]
# print(df)
#    one  three
# a  1.0    1.0
# b  2.0    2.0
# c  3.0    3.0
# d  NaN    NaN
# e  NaN    5.0



###########################################################
# import pandas as pd
# d = {"one": pd.Series([1,2,3], index=["a","b","c"]) ,
#      "two": pd.Series([1,2,3,4], index=["a","b","c","d"]),
#      "three": pd.Series([1,2,3,5], index=["a","b","c","e"]) }
# df = pd.DataFrame(d)
# df.pop("two")
# print(df)
#    one  three
# a  1.0    1.0
# b  2.0    2.0
# c  3.0    3.0
# d  NaN    NaN
# e  NaN    5.0




###########################################################
# import pandas as pd
# d = {"one": pd.Series([1,2,3], index=["a","b","c"]) ,
#      "two": pd.Series([1,2,3,4], index=["a","b","c","d"]),
#      "three": pd.Series([1,2,3,5], index=["a","b","c","e"]) }
# df = pd.DataFrame(d)
# del df
# print(df)
# NameError: name 'df' is not defined





###########################################################
# import pandas as pd
# d = {"one": pd.Series([1,2,3], index=["a","b","c"]) ,
#      "two": pd.Series([1,7,3,8], index=["a","b","c","d"]),
#      "three": pd.Series([1,20,10,5], index=["a","b","c","e"]) }
# df = pd.DataFrame(d)
# print(df.loc['d'])
# one      NaN
# two      8.0
# three    NaN
# Name: d, dtype: float64




###########################################################
# import pandas as pd
# d = {"one": pd.Series([1,2,3], index=["a","b","c"]) ,
#      "two": pd.Series([1,7,3,8], index=["a","b","c","d"]),
#      "three": pd.Series([1,20,10,5], index=["a","b","c","e"]) }
# df = pd.DataFrame(d)
# print(df.loc['2'])
#error




###########################################################
# import pandas as pd
# d = {"one": pd.Series([1,2,3], index=["a","b","c"]) ,
#      "two": pd.Series([1,7,3,8], index=["a","b","c","d"]),
#      "three": pd.Series([1,20,10,5], index=["a","b","c","e"]) }
# df = pd.DataFrame(d)
# print(df.loc[2])
#error




###########################################################
import pandas as pd
# d = {"one": pd.Series([1,2,3], index=["a","b","c"]) ,
#      "two": pd.Series([1,7,3,8], index=["a","b","c","d"]),
#      "three": pd.Series([1,20,10,5], index=["a","b","c","e"]) }
# df = pd.DataFrame(d)
# print(df)
#    one  two  three
# a  1.0  1.0    1.0
# b  2.0  7.0   20.0
# c  3.0  3.0   10.0
# d  NaN  8.0    NaN
# e  NaN  NaN    5.0



###########################################################
# import pandas as pd
# d = {"one": pd.Series([1,2,3], index=["a","b","c"]) ,
#      "two": pd.Series([1,7,3,8], index=["a","b","c","d"]),
#      "three": pd.Series([1,20,10,5], index=["a","b","c","e"]) }
# df = pd.DataFrame(d)
# print(df.loc['b'])
# one       2.0
# two       7.0
# three    20.0
# Name: b, dtype: float64




###########################################################
# import pandas as pd
# d = {"one": pd.Series([1,2,3], index=["a","b","c"]) ,
#      "two": pd.Series([1,7,3,8], index=["a","b","c","d"]),
#      "three": pd.Series([1,20,10,5], index=["a","b","c","e"]) }
# df = pd.DataFrame(d)
# print(df.loc[1])
# TypeError: cannot do label indexing on <class 'pandas.core.indexes.base.Index'> with these indexers [1] of <class 'int'>




###########################################################
# import pandas as pd
# d = {"one": pd.Series([1,2,3], index=["a","b","c"]) ,
#      "two": pd.Series([1,7,3,8], index=["a","b","c","d"]),
#      "three": pd.Series([1,20,10,5], index=["a","b","c","e"]) }
# df = pd.DataFrame(d)
# print(df)
# print(df.iloc[2])
#    one  two  three
# a  1.0  1.0    1.0
# b  2.0  7.0   20.0
# c  3.0  3.0   10.0
# d  NaN  8.0    NaN
# e  NaN  NaN    5.0
# one       3.0
# two       3.0
# three    10.0
# Name: c, dtype: float64





###########################################################
# import pandas as pd
# d = {"one": pd.Series([1,2,3], index=["a","b","c"]) ,
#      "two": pd.Series([1,7,3,8], index=["a","b","c","d"]),
#      "three": pd.Series([1,20,10,5], index=["a","b","c","e"]) }
# df = pd.DataFrame(d)
# print(df.iloc[2])
# one       3.0
# two       3.0
# three    10.0
# Name: c, dtype: float64





###########################################################
# import pandas as pd
# d = {"one": pd.Series([1,2,3], index=["a","b","c"]) ,
#      "two": pd.Series([1,7,3,8], index=["a","b","c","d"]),
#      "three": pd.Series([1,20,10,5], index=["a","b","c","e"]) }
# df = pd.DataFrame(d)
# print(df.iloc[3])
# one      NaN
# two      8.0
# three    NaN
# Name: d, dtype: float64



###########################################################
# import pandas as pd
# d = {"one": pd.Series([1,2,3], index=["a","b","c"]) ,
#      "two": pd.Series([1,7,3,8], index=["a","b","c","d"]),
#      "three": pd.Series([1,20,10,5], index=["a","b","c","e"]) }
# df = pd.DataFrame(d)
# print(df.iloc[4])
# one      NaN
# two      NaN
# three    5.0
# Name: e, dtype: float64



###########################################################
# import pandas as pd
# d = {"one": pd.Series([1,2,3], index=["a","b","c"]) ,
#      "two": pd.Series([1,7,3,8], index=["a","b","c","d"]),
#      "three": pd.Series([1,20,10,5], index=["a","b","c","e"]) }
# df = pd.DataFrame(d)
# print(df)
#    one  two  three
# a  1.0  1.0    1.0
# b  2.0  7.0   20.0
# c  3.0  3.0   10.0
# d  NaN  8.0    NaN
# e  NaN  NaN    5.0




###########################################################
# import pandas as pd
# d = {"one": pd.Series([1,2,3], index=["a","b","c"]) ,
#      "two": pd.Series([1,7,3,8], index=["a","b","c","d"]),
#      "three": pd.Series([1,20,10,5], index=["a","b","c","e"]) }
# df = pd.DataFrame(d)
# print(df[:])
#    one  two  three
# a  1.0  1.0    1.0
# b  2.0  7.0   20.0
# c  3.0  3.0   10.0
# d  NaN  8.0    NaN
# e  NaN  NaN    5.0



###########################################################
# import pandas as pd
# d = {"one": pd.Series([1,2,3], index=["a","b","c"]) ,
#      "two": pd.Series([1,7,6,8], index=["a","b","c","d"]),
#      "three": pd.Series([1,20,10,5], index=["a","b","c","e"]) }
# df = pd.DataFrame(d)
# print(df[2:4])
#    one  two  three
# c  3.0  6.0   10.0
# d  NaN  8.0    NaN



###########################################################
# import pandas as pd
# df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
# print(df)
#    a  b
# 0  1  2
# 1  3  4





###########################################################
# import pandas as pd
# df = pd.DataFrame([[1, 2], [3, 4, 5 ]], columns = ['a','b','c'])
# df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','f'])
# df = df.append(df2)
# print(df)
#    a    b    c    f
# 0  1  2.0  NaN  NaN
# 1  3  4.0  5.0  NaN
# 0  5  NaN  NaN  6.0
# 1  7  NaN  NaN  8.0



###########################################################
# import pandas as pd
# df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
# df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
# df = df.append(df2)
# # Drop rows with label 0
# print(df)
# df = df.drop(0)
# print(df)
#    a  b
# 0  1  2
# 1  3  4
# 0  5  6
# 1  7  8
#    a  b
# 1  3  4
# 1  7  8

