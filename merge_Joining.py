####################################################################
# Pandas has full-featured, high performance in-memory join operations idiomatically very
# similar to relational databases like SQL.
# Pandas provides a single function, merge, as the entry point for
# all standard database join operations between DataFrame objects −


####################################################################
# pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
# left_index=False, right_index=False, sort=True)


####################################################################
# left − A DataFrame object.
# right − Another DataFrame object.
# on − Columns (names) to join on. Must be found in both the left and right DataFrame objects.
# left_on − Columns from the left DataFrame to use as keys. Can either be column names or arrays with length equal to the 
#length of the DataFrame.
# right_on − Columns from the right DataFrame to use as keys. Can either be column names or arrays with length equal to the 
#length of the DataFrame.
# left_index − If True, use the index (row labels) from the left DataFrame as its join key(s). In case of a DataFrame with a 
#MultiIndex (hierarchical),
# the number of levels must match the number of join keys from the right DataFrame.
# right_index − Same usage as left_index for the right DataFrame.
# how − One of 'left', 'right', 'outer', 'inner'. Defaults to inner. Each method has been described below.
# sort − Sort the result DataFrame by the join keys in lexicographical order. Defaults to True, setting to False will 
#improve the performance substantially in many cases.



####################################################################
# import pandas as pd
# left = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
# right = pd.DataFrame(
#    {'id':[1,2,3,4,5],
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub4','sub3','sub6','sub5']})
# print(left)
# print(right)
#    id    Name subject_id
# 0   1    Alex       sub1
# 1   2     Amy       sub2
# 2   3   Allen       sub4
# 3   4   Alice       sub6
# 4   5  Ayoung       sub5
#    id   Name subject_id
# 0   1  Billy       sub2
# 1   2  Brian       sub4
# 2   3   Bran       sub3
# 3   4  Bryce       sub6
# 4   5  Betty       sub5




####################################################################
#Merge Two DataFrames on a Key
# import pandas as pd
# left = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
# right = pd.DataFrame({
# 	'id':[1,2,3,4,5],
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub4','sub3','sub6','sub5']})
# print(pd.merge(left,right,on='id'))
#    id  Name_x subject_id_x Name_y subject_id_y
# 0   1    Alex         sub1  Billy         sub2
# 1   2     Amy         sub2  Brian         sub4
# 2   3   Allen         sub4   Bran         sub3
# 3   4   Alice         sub6  Bryce         sub6
# 4   5  Ayoung         sub5  Betty         sub5



# import pandas as pd
# left = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
# right = pd.DataFrame({
# 	'id':[1,2,3,4,5],
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub4','sub3','sub6','sub5']})
# print(pd.merge(right,right, on='id'))
#    id Name_x subject_id_x Name_y subject_id_y
# 0   1  Billy         sub2  Billy         sub2
# 1   2  Brian         sub4  Brian         sub4
# 2   3   Bran         sub3   Bran         sub3
# 3   4  Bryce         sub6  Bryce         sub6
# 4   5  Betty         sub5  Betty         sub5




####################################################################
# import pandas as pd
# left = pd.DataFrame({
#    'id':[1,2,3,4,5,6],
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
# right = pd.DataFrame({
# 	'id':[1,2,3,4,5],
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub4','sub3','sub6','sub5']})
# print(pd.merge(left,right,on='id'))
# ValueError: arrays must all be same length




####################################################################
# import pandas as pd
# left = pd.DataFrame({
#    'id':[1,2,3,4,6],
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
# right = pd.DataFrame({
# 	'id':[1,2,3,4,5],
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub4','sub3','sub6','sub5']})
# print(pd.merge(left,right,on='id'))
#    id Name_x subject_id_x Name_y subject_id_y
# 0   1   Alex         sub1  Billy         sub2
# 1   2    Amy         sub2  Brian         sub4
# 2   3  Allen         sub4   Bran         sub3
# 3   4  Alice         sub6  Bryce         sub6





####################################################################
# import pandas as pd
# left = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
# right = pd.DataFrame({
# 	'id':[1,2,3,4,10],
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub4','sub3','sub6','sub5']})
# print(pd.merge(left,right,on='id'))
#    id Name_x subject_id_x Name_y subject_id_y
# 0   1   Alex         sub1  Billy         sub2
# 1   2    Amy         sub2  Brian         sub4
# 2   3  Allen         sub4   Bran         sub3
# 3   4  Alice         sub6  Bryce         sub6




####################################################################
#Merge Two DataFrames on a Key
# import pandas as pd
# left = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
# right = pd.DataFrame({
# 	'id':[1,2,3,4,5],
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub6','sub3','sub4','sub5']})
# print(pd.merge(left,right,on=['id','subject_id']))
#    id  Name_x subject_id Name_y
# 0   5  Ayoung       sub5  Betty





####################################################################
#Merge Two DataFrames on a Key
# import pandas as pd
# left = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
# right = pd.DataFrame({
# 	'id':[1,2,3,4,5],
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub6','sub3','sub6','sub5']})
# print(pd.merge(left,right,on=['id','subject_id']))
#    id  Name_x subject_id Name_y
# 0   4   Alice       sub6  Bryce
# 1   5  Ayoung       sub5  Betty





####################################################################
#Merge Two DataFrames on a Key
# import pandas as pd
# left = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
# right = pd.DataFrame({
# 	'id':[1,2,3,4,5],
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub6','sub3','sub6','sub5']})
# print(pd.merge(right,left ,on=['id','subject_id']))
#    id Name_x subject_id  Name_y
# 0   4  Bryce       sub6   Alice
# 1   5  Betty       sub5  Ayoung




####################################################################
# import pandas as pd
# left = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
# right = pd.DataFrame({
# 	'id':[1,2,3,4,5],
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub4','sub3','sub6','sub5']})
# print(pd.merge(left,right,on=['id','subject_id']))
#    id  Name_x subject_id Name_y
# 0   4   Alice       sub6  Bryce
# 1   5  Ayoung       sub5  Betty




####################################################################
#Merge Using 'how' Argument
# The how argument to merge specifies how to determine which keys are
# to be included in the resulting table.
# If a key combination does not appear in either the left or the right
# tables, the values in the joined table will be NA.
# Here is a summary of the how options and their SQL equivalent names −


# Merge Method	SQL Equivalent	Description
# left	LEFT OUTER JOIN	Use keys from left object
# right	RIGHT OUTER JOIN	Use keys from right object
# outer	FULL OUTER JOIN	Use union of keys
# inner	INNER JOIN	Use intersection of keys



####################################################################
# import pandas as pd
# left = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
# right = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub4','sub3','sub6','sub5']})
# print(pd.merge(left, right, on='subject_id', how='left'))
#    id_x  Name_x subject_id  id_y Name_y
# 0     1    Alex       sub1   NaN    NaN
# 1     2     Amy       sub2   1.0  Billy
# 2     3   Allen       sub4   2.0  Brian
# 3     4   Alice       sub6   4.0  Bryce
# 4     5  Ayoung       sub5   5.0  Betty




####################################################################
# import pandas as pd
# left = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
# right = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub4','sub3','sub6','sub5']})
# print(pd.merge(right, left, on='subject_id', how='left'))
#    id_x Name_x subject_id  id_y  Name_y
# 0     1  Billy       sub2   2.0     Amy
# 1     2  Brian       sub4   3.0   Allen
# 2     3   Bran       sub3   NaN     NaN
# 3     4  Bryce       sub6   4.0   Alice
# 4     5  Betty       sub5   5.0  Ayoung






####################################################################
# import pandas as pd
# left = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
# right = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub4','sub3','sub6','sub5']})
# print(pd.merge(left, right, on='subject_id', how='right'))
#    id_x  Name_x subject_id  id_y Name_y
# 0   2.0     Amy       sub2     1  Billy
# 1   3.0   Allen       sub4     2  Brian
# 2   4.0   Alice       sub6     4  Bryce
# 3   5.0  Ayoung       sub5     5  Betty
# 4   NaN     NaN       sub3     3   Bran




####################################################################
# import pandas as pd
# left = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
# right = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub4','sub3','sub6','sub5']})
# print(pd.merge(right, left, on='subject_id', how='right'))
# 0   1.0  Billy       sub2     2     Amy
# 1   2.0  Brian       sub4     3   Allen
# 2   4.0  Bryce       sub6     4   Alice
# 3   5.0  Betty       sub5     5  Ayoung
# 4   NaN    NaN       sub1     1    Alex




####################################################################
# import pandas as pd
# left = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
# right = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub4','sub3','sub6','sub5']})
# print(pd.merge(left, right, on='subject_id', how='outer'))
#    id_x  Name_x subject_id  id_y Name_y
# 0   1.0    Alex       sub1   NaN    NaN
# 1   2.0     Amy       sub2   1.0  Billy
# 2   3.0   Allen       sub4   2.0  Brian
# 3   4.0   Alice       sub6   4.0  Bryce
# 4   5.0  Ayoung       sub5   5.0  Betty
# 5   NaN     NaN       sub3   3.0   Bran




# import pandas as pd
# left = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
# right = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub4','sub3','sub6','sub5']})
# print(pd.merge(right,  left, on='subject_id', how='outer'))
#    id_x Name_x subject_id  id_y  Name_y
# 0   1.0  Billy       sub2   2.0     Amy
# 1   2.0  Brian       sub4   3.0   Allen
# 2   3.0   Bran       sub3   NaN     NaN
# 3   4.0  Bryce       sub6   4.0   Alice
# 4   5.0  Betty       sub5   5.0  Ayoung
# 5   NaN    NaN       sub1   1.0    Alex




#####################################################################
# import pandas as pd
# left = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
# right = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub4','sub3','sub6','sub5']})
# print(pd.merge(left, right, on='subject_id', how='inner'))
#    id_x  Name_x subject_id  id_y Name_y
# 0     2     Amy       sub2     1  Billy
# 1     3   Allen       sub4     2  Brian
# 2     4   Alice       sub6     4  Bryce
# 3     5  Ayoung       sub5     5  Betty





#####################################################################
# import pandas as pd
# left = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
# right = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub4','sub3','sub6','sub5']})
# print(pd.merge(right,left,  on='subject_id', how='inner'))
#    id_x Name_x subject_id  id_y  Name_y
# 0     1  Billy       sub2     2     Amy
# 1     2  Brian       sub4     3   Allen
# 2     4  Bryce       sub6     4   Alice
# 3     5  Betty       sub5     5  Ayoung




