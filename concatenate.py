#################################################################
#Concatenation

# import pandas as pd
# one = pd.DataFrame({
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5'],
#    'Marks_scored':[98,90,87,69,78]},
#    index=[1,2,3,4,5])
#
# two = pd.DataFrame({
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub4','sub3','sub6','sub5'],
#    'Marks_scored':[89,80,79,97,88]},
#    index=[1,2,3,4,5])
# print(pd.concat([one,two]))
#      Name subject_id  Marks_scored
# 1    Alex       sub1            98
# 2     Amy       sub2            90
# 3   Allen       sub4            87
# 4   Alice       sub6            69
# 5  Ayoung       sub5            78
# 1   Billy       sub2            89
# 2   Brian       sub4            80
# 3    Bran       sub3            79
# 4   Bryce       sub6            97
# 5   Betty       sub5            88





#################################################################
# import pandas as pd
# one = pd.DataFrame({
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5'],
#    'Marks_scored':[98,90,87,69,78]},
#    index=[1,2,3,4,5])
#
# two = pd.DataFrame({
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub4','sub3','sub6','sub5'],
#    'Marks_scored':[89,80,79,97,88]},
#    index=[1,2,3,4,5])
# print(pd.concat([one,two],keys=['aaa','bbb']))
#          Name subject_id  Marks_scored
# aaa 1    Alex       sub1            98
#     2     Amy       sub2            90
#     3   Allen       sub4            87
#     4   Alice       sub6            69
#     5  Ayoung       sub5            78
# bbb 1   Billy       sub2            89
#     2   Brian       sub4            80
#     3    Bran       sub3            79
#     4   Bryce       sub6            97
#     5   Betty       sub5            88






#################################################################
# import pandas as pd
# one = pd.DataFrame({
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5'],
#    'Marks_scored':[98,90,87,69,78]},
#    index=[1,2,3,4,5])
#
# two = pd.DataFrame({
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub4','sub3','sub6','sub5'],
#    'Marks_scored':[89,80,79,97,88]},
#    index=[1,2,3,4,5])
# print(pd.concat([one,two],keys=['aaa']))
#          Name subject_id  Marks_scored
# aaa 1    Alex       sub1            98
#     2     Amy       sub2            90
#     3   Allen       sub4            87
#     4   Alice       sub6            69
#     5  Ayoung       sub5            78





#################################################################
# import pandas as pd
# one = pd.DataFrame({
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5'],
#    'Marks_scored':[98,90,87,69,78]},
#    index=[1,2,3,4,5])
#
# two = pd.DataFrame({
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub4','sub3','sub6','sub5'],
#    'Marks_scored':[89,80,79,97,88]},
#    index=[1,2,3,4,5])
# print(pd.concat([one,two],keys=['aaa','bbb','ccc']))
#          Name subject_id  Marks_scored
# aaa 1    Alex       sub1            98
#     2     Amy       sub2            90
#     3   Allen       sub4            87
#     4   Alice       sub6            69
#     5  Ayoung       sub5            78
# bbb 1   Billy       sub2            89
#     2   Brian       sub4            80
#     3    Bran       sub3            79
#     4   Bryce       sub6            97
#     5   Betty       sub5            88




#################################################################
# import pandas as pd
#
# one = pd.DataFrame({
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5'],
#    'Marks_scored':[98,90,87,69,78]},
#    index=[1,2,3,4,5])
# two = pd.DataFrame({
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub4','sub3','sub6','sub5'],
#    'Marks_scored':[89,80,79,97,88]},
#    index=[1,2,3,4,5])
# print(pd.concat([one,two],keys=['x','y'],ignore_index=True))
#      Name subject_id  Marks_scored
# 0    Alex       sub1            98
# 1     Amy       sub2            90
# 2   Allen       sub4            87
# 3   Alice       sub6            69
# 4  Ayoung       sub5            78
# 5   Billy       sub2            89
# 6   Brian       sub4            80
# 7    Bran       sub3            79
# 8   Bryce       sub6            97
# 9   Betty       sub5            88





#################################################################
# import pandas as pd
# one = pd.DataFrame({
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5'],
#    'Marks_scored':[98,90,87,69,78]},
#    index=[1,2,3,4,5])
# two = pd.DataFrame({
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub4','sub3','sub6','sub5'],
#    'Marks_scored':[89,80,79,97,88]},
#    index=[1,2,3,4,5])
# print(pd.concat([one,two],keys=['aaa','bbb'],ignore_index=True))
#      Name subject_id  Marks_scored
# 0    Alex       sub1            98
# 1     Amy       sub2            90
# 2   Allen       sub4            87
# 3   Alice       sub6            69
# 4  Ayoung       sub5            78
# 5   Billy       sub2            89
# 6   Brian       sub4            80
# 7    Bran       sub3            79
# 8   Bryce       sub6            97
# 9   Betty       sub5            88




#################################################################
# import pandas as pd
# one = pd.DataFrame({
#     "Name":["aaa","bbb","ccc","ddd","eee","fff"],
#      "Age":[10,20,30,40,50,60],
#     "marks":[44,55,66,77,88,99]
#     }, index=[1,2,3,4,5,6])
# two = pd.DataFrame({
#     "Name":["aaa","bbb","ccc","ddd","eee","fff"],
#      "Age":[10,20,30,40,50,60],
#     "marks":[44,55,66,77,88,99]
#     }, index=[1,2,3,4,5,6])
# print(pd.concat([one,two],axis=1))
#   Name  Age  marks Name  Age  marks
# 1  aaa   10     44  aaa   10     44
# 2  bbb   20     55  bbb   20     55
# 3  ccc   30     66  ccc   30     66
# 4  ddd   40     77  ddd   40     77
# 5  eee   50     88  eee   50     88
# 6  fff   60     99  fff   60     99






#################################################################
# import pandas as pd
# one = pd.DataFrame({
#     "Name":["aaa","bbb","ccc","ddd","eee","fff"],
#      "Age":[10,20,30,40,50,60],
#     "marks":[44,55,66,77,88,99]
#     }, index=[1,2,3,4,5,6])
# two = pd.DataFrame({
#     "Name":["aaa","bbb","ccc","ddd","eee","fff"],
#      "Age":[10,20,30,40,50,60],
#     "marks":[44,55,66,77,88,99]
#     }, index=[1,2,3,4,5,6])
# print(pd.concat([one,two]))
#   Name  Age  marks
# 1  aaa   10     44
# 2  bbb   20     55
# 3  ccc   30     66
# 4  ddd   40     77
# 5  eee   50     88
# 6  fff   60     99
# 1  aaa   10     44
# 2  bbb   20     55
# 3  ccc   30     66
# 4  ddd   40     77
# 5  eee   50     88
# 6  fff   60     99




#################################################################
# Concatenating Using append
# A useful shortcut to concat are the append instance methods on Series and DataFrame.
# These methods actually predated concat. They concatenate along axis=0, namely the index −





#################################################################
# import pandas as pd
# one = pd.DataFrame({
#     "Name":["aaa","bbb","ccc","ddd","eee","fff"],
#      "Age":[10,20,30,40,50,60],
#     "marks":[44,55,66,77,88,99]
#     }, index=[1,2,3,4,5,6])
# two = pd.DataFrame({
#     "Name":["aaa","bbb","ccc","ddd","eee","fff"],
#      "Age":[10,20,30,40,50,60],
#     "marks":[44,55,66,77,88,99]
#     }, index=[1,2,3,4,5,6])
# print(one.append(two))
#   Name  Age  marks
# 1  aaa   10     44
# 2  bbb   20     55
# 3  ccc   30     66
# 4  ddd   40     77
# 5  eee   50     88
# 6  fff   60     99
# 1  aaa   10     44
# 2  bbb   20     55
# 3  ccc   30     66
# 4  ddd   40     77
# 5  eee   50     88
# 6  fff   60     99




#################################################################
# import pandas as pd
# one = pd.DataFrame({
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5'],
#    'Marks_scored':[98,90,87,69,78]},
#    index=[1,2,3,4,5])
#
# two = pd.DataFrame({
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub4','sub3','sub6','sub5'],
#    'Marks_scored':[89,80,79,97,88]},
#    index=[1,2,3,4,5])
# print(one.append([two,one,two]))
#      Name subject_id  Marks_scored
# 1    Alex       sub1            98
# 2     Amy       sub2            90
# 3   Allen       sub4            87
# 4   Alice       sub6            69
# 5  Ayoung       sub5            78
# 1   Billy       sub2            89
# 2   Brian       sub4            80
# 3    Bran       sub3            79
# 4   Bryce       sub6            97
# 5   Betty       sub5            88
# 1    Alex       sub1            98
# 2     Amy       sub2            90
# 3   Allen       sub4            87
# 4   Alice       sub6            69
# 5  Ayoung       sub5            78
# 1   Billy       sub2            89
# 2   Brian       sub4            80
# 3    Bran       sub3            79
# 4   Bryce       sub6            97
# 5   Betty       sub5            88




#################################################################
# Time Series
# Pandas provide a robust tool for working time with Time series data, especially in the financial sector.
# While working with time series data, we frequently come across the following −
# Generating sequence of time
# == Convert the time series to different frequencies
# == Pandas provides a relatively compact and self-contained set of tools for performing the above tasks.



#################################################################
# Get Current Time
# import pandas as pd
# print(pd.datetime.now())
# 2020-04-10 20:34:06.842704



#################################################################
# import pandas as pd
# print(pd.Timestamp('2017-03-01'))
# 2017-03-01 00:00:00



#################################################################
# import pandas as pd
# print(pd.Timestamp(1586807498,unit='s'))
# 2020-04-13 19:51:38





#################################################################
# import pandas as pd
# print(pd.Timestamp(1586807498,unit='s'))
# 2020-04-24 00:14:15



#################################################################
# import pandas as pd
# print(pd.date_range("11:00", "13:30", freq="30min").time)
# [datetime.time(11, 0) datetime.time(11, 30) datetime.time(12, 0)
#  datetime.time(12, 30) datetime.time(13, 0) datetime.time(13, 30)]
#




#################################################################
# import pandas as pd
# print(pd.date_range("11:00", "13:30", freq="H").time)
# [datetime.time(11, 0) datetime.time(12, 0) datetime.time(13, 0)]



#################################################################
# Converting to Timestamps
# import pandas as pd
# print(pd.to_datetime(pd.Series(['Jul 31, 2009','2010-01-10', None])))
# 0   2009-07-31
# 1   2010-01-10
# 2          NaT
# dtype: datetime64[ns]


