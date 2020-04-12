#groupBy.py
###########################################################





###########################################################
# Any groupby operation involves one of the following operations on the original object. They are −
# == Splitting the Object
# == Applying a function
# == Combining the results
# Aggregation − computing a summary statistic
# Transformation − perform some group-specific operation
# Filtration − discarding the data with some condition



###########################################################
# import pandas as pd
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# print(df)
#      Team  Rank  Year  Points
# 0   Riders     1  2014     876
# 1   Riders     2  2015     789
# 2   Devils     2  2014     863
# 3   Devils     3  2015     673
# 4    Kings     3  2014     741
# 5    kings     4  2015     812
# 6    Kings     1  2016     756
# 7    Kings     1  2017     788
# 8   Riders     2  2016     694
# 9   Royals     4  2014     701
# 10  Royals     1  2015     804
# 11  Riders     2  2017     690




###########################################################
# import pandas as pd
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# print(df.groupby("Team"))
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0300E670>






###########################################################
# import pandas as pd
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# grouped = df.groupby("Team")
# for i in grouped:
#     print(i)
# ('Devils',      Team  Rank  Year  Points
# 2  Devils     2  2014     863
# 3  Devils     3  2015     673)
# ('Kings',     Team  Rank  Year  Points
# 4  Kings     3  2014     741
# 6  Kings     1  2016     756
# 7  Kings     1  2017     788)
# ('Riders',       Team  Rank  Year  Points
# 0   Riders     1  2014     876
# 1   Riders     2  2015     789
# 8   Riders     2  2016     694
# 11  Riders     2  2017     690)
# ('Royals',       Team  Rank  Year  Points
# 9   Royals     4  2014     701
# 10  Royals     1  2015     804)
# ('kings',     Team  Rank  Year  Points
# 5  kings     4  2015     812)




# import pandas as pd
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# grouped = df.groupby("Team")
# for i,j in grouped:
#     print(i)
# Devils
# Kings
# Riders
# Royals
# kings



# import pandas as pd
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# grouped = df.groupby("Team")
# for i,j in grouped:
#     print(j)
#      Team  Rank  Year  Points
# 2  Devils     2  2014     863
# 3  Devils     3  2015     673
#     Team  Rank  Year  Points
# 4  Kings     3  2014     741
# 6  Kings     1  2016     756
# 7  Kings     1  2017     788
#       Team  Rank  Year  Points
# 0   Riders     1  2014     876
# 1   Riders     2  2015     789
# 8   Riders     2  2016     694
# 11  Riders     2  2017     690
#       Team  Rank  Year  Points
# 9   Royals     4  2014     701
# 10  Royals     1  2015     804
#     Team  Rank  Year  Points
# 5  kings     4  2015     812




###########################################################
# import pandas as pd
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# grouped = df.groupby("Team")
# for i,j in grouped:
#     print(i)
# # Devils
# Kings
# Riders
# Royals
# kings




###########################################################
# import pandas as pd
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# print(df.groupby("Team"))
# for i in df.groupby("Team"):
#     print(i)
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x02EDE658>
# ('Devils',      Team  Rank  Year  Points
# 2  Devils     2  2014     863
# 3  Devils     3  2015     673)
# ('Kings',     Team  Rank  Year  Points
# 4  Kings     3  2014     741
# 6  Kings     1  2016     756
# 7  Kings     1  2017     788)
# ('Riders',       Team  Rank  Year  Points
# 0   Riders     1  2014     876
# 1   Riders     2  2015     789
# 8   Riders     2  2016     694
# 11  Riders     2  2017     690)
# ('Royals',       Team  Rank  Year  Points
# 9   Royals     4  2014     701
# 10  Royals     1  2015     804)
# ('kings',     Team  Rank  Year  Points
# 5  kings     4  2015     812)



# import pandas as pd
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# grouped = df.groupby("Points")
# for i,j in grouped:
#     print(i)
# 673
# 690
# 694
# 701
# 741
# 756
# 788
# 789
# 804
# 812
# 863
# 876





###########################################################
# import pandas as pd
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# print(df.groupby("Team").groups)
# {'Devils': Int64Index([2, 3], dtype='int64'),
# 'Kings': Int64Index([4, 6, 7], dtype='int64'),
# 'Riders': Int64Index([0, 1, 8, 11], dtype='int64'),
# 'Royals': Int64Index([9, 10], dtype='int64'),
# 'kings': Int64Index([5], dtype='int64')}





###########################################################
# import pandas as pd
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# grouped = df.groupby("Team").groups
# for i in grouped:
#     print(i)
# Devils
# Kings
# Riders
# Royals
# kings




###########################################################
# import pandas as pd
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# grouped = df.groupby("Team").groups
# for i,j in grouped:
#     print(j)
# ValueError: too many values to unpack (expected 2)




###########################################################
# import pandas as pd
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# print(df.groupby(['Team','Year']).groups)
# {('Devils', 2014): Int64Index([2], dtype='int64'), ('Devils', 2015): Int64Index([3], dtype='int64'), ('Kings', 2014): Int64Index([4], dtype='int64'), ('Kings', 2016): Int64Index([6], dtype='int64'), ('Kings', 2017): Int64Index([7], dtype='int64'), ('Riders', 2014): Int64Index([0], dtype='int64'), ('Riders', 2015): Int64Index([1], dtype='int64'), ('Riders', 2016): Int64Index([8], dtype='int64'), ('Riders', 2017): Int64Index([11], dtype='int64'), ('Royals', 2014): Int64Index([9], dtype='int64'), ('Royals', 2015): Int64Index([10], dtype='int64'), ('kings', 2015): Int64Index([5], dtype='int64')}



###########################################################
# import pandas as pd
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# group = df.groupby(['Team','Year']).groups
# for i,j in group:
#     print(i,j)
# Devils 2014
# Devils 2015
# Kings 2014
# Kings 2016
# Kings 2017
# Riders 2014
# Riders 2015
# Riders 2016
# Riders 2017
# Royals 2014
# Royals 2015
# kings 2015



###########################################################
# import pandas as pd
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# group = df.groupby(['Team','Year']).groups
# for i in group:
#     print(i)
# ('Devils', 2014)
# ('Devils', 2015)
# ('Kings', 2014)
# ('Kings', 2016)
# ('Kings', 2017)
# ('Riders', 2014)
# ('Riders', 2015)
# ('Riders', 2016)
# ('Riders', 2017)
# ('Royals', 2014)
# ('Royals', 2015)
# ('kings', 2015)




###########################################################
# import pandas as pd
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# group = df.groupby(['Team','Year']).groups
# for i,j in group:
#     print(i,j)
# Devils 2014
# Devils 2015
# Kings 2014
# Kings 2016
# Kings 2017
# Riders 2014
# Riders 2015
# Riders 2016
# Riders 2017
# Royals 2014
# Royals 2015
# kings 2015






###########################################################
# import pandas as pd
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# grouped = df.groupby("Year")
# for i,group in grouped:
#     print(i)
#
# 2014
# 2015
# 2016
# 2017



###########################################################
# import pandas as pd
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# grouped = df.groupby("Year")
# for i,j in grouped:
#     print(j)
#      Team  Rank  Year  Points
# 0  Riders     1  2014     876
# 2  Devils     2  2014     863
# 4   Kings     3  2014     741
# 9  Royals     4  2014     701
#       Team  Rank  Year  Points
# 1   Riders     2  2015     789
# 3   Devils     3  2015     673
# 5    kings     4  2015     812
# 10  Royals     1  2015     804
#      Team  Rank  Year  Points
# 6   Kings     1  2016     756
# 8  Riders     2  2016     694
#       Team  Rank  Year  Points
# 7    Kings     1  2017     788
# 11  Riders     2  2017     690



###########################################################
# import pandas as pd
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# grouped = df.groupby("Year")
# for i,group in grouped:
#     print(i)
#     print(group)
# 2014
#      Team  Rank  Year  Points
# 0  Riders     1  2014     876
# 2  Devils     2  2014     863
# 4   Kings     3  2014     741
# 9  Royals     4  2014     701
# 2015
#       Team  Rank  Year  Points
# 1   Riders     2  2015     789
# 3   Devils     3  2015     673
# 5    kings     4  2015     812
# 10  Royals     1  2015     804
# 2016
#      Team  Rank  Year  Points
# 6   Kings     1  2016     756
# 8  Riders     2  2016     694
# 2017
#       Team  Rank  Year  Points
# 7    Kings     1  2017     788
# 11  Riders     2  2017     690



###########################################################
# import pandas as pd
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# grouped = df.groupby("Year")
# for i,group in grouped:
#     print(group)
#      Team  Rank  Year  Points
# 0  Riders     1  2014     876
# 2  Devils     2  2014     863
# 4   Kings     3  2014     741
# 9  Royals     4  2014     701
#       Team  Rank  Year  Points
# 1   Riders     2  2015     789
# 3   Devils     3  2015     673
# 5    kings     4  2015     812
# 10  Royals     1  2015     804
#      Team  Rank  Year  Points
# 6   Kings     1  2016     756
# 8  Riders     2  2016     694
#       Team  Rank  Year  Points
# 7    Kings     1  2017     788
# 11  Riders     2  2017     690



###########################################################
# Select a Group
# Using the get_group() method, we can select a single group.
# import pandas as pd
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# aaa = df.groupby("Year")
# print(aaa.get_group(2014))
#      Team  Rank  Year  Points
# 0  Riders     1  2014     876
# 2  Devils     2  2014     863
# 4   Kings     3  2014     741
# 9  Royals     4  2014     701



###########################################################
# aggregations
# An aggregated function returns a single aggregated value for each group.
# Once the group by object is created, several aggregation operations can be performed on the grouped data.



###########################################################
# import numpy as np
# import pandas as pd
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# print(df)
# aaa = df.groupby("Year")
# print(aaa['Points'].agg(np.mean))
#       Team  Rank  Year  Points
# 0   Riders     1  2014     876
# 1   Riders     2  2015     789
# 2   Devils     2  2014     863
# 3   Devils     3  2015     673
# 4    Kings     3  2014     741
# 5    kings     4  2015     812
# 6    Kings     1  2016     756
# 7    Kings     1  2017     788
# 8   Riders     2  2016     694
# 9   Royals     4  2014     701
# 10  Royals     1  2015     804
# 11  Riders     2  2017     690
# Year
# 2014    795.25
# 2015    769.50
# 2016    725.00
# 2017    739.00
# Name: Points, dtype: float64






###########################################################
# import numpy as np
# import pandas as pd
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# print(df)
# aaa = df.groupby("Year")
# print(aaa.agg(np.size))
#       Team  Rank  Year  Points
# 0   Riders     1  2014     876
# 1   Riders     2  2015     789
# 2   Devils     2  2014     863
# 3   Devils     3  2015     673
# 4    Kings     3  2014     741
# 5    kings     4  2015     812
# 6    Kings     1  2016     756
# 7    Kings     1  2017     788
# 8   Riders     2  2016     694
# 9   Royals     4  2014     701
# 10  Royals     1  2015     804
# 11  Riders     2  2017     690
#       Team  Rank  Points
# Year
# 2014     4     4       4
# 2015     4     4       4
# 2016     2     2       2
# 2017     2     2       2





###########################################################
# import pandas as pd
# import numpy as np
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# print(df)
# grouped = df.groupby('Team')
# print(grouped)
# print(grouped['Points'].agg([np.sum, np.mean, np.std]))
#       Team  Rank  Year  Points
# 0   Riders     1  2014     876
# 1   Riders     2  2015     789
# 2   Devils     2  2014     863
# 3   Devils     3  2015     673
# 4    Kings     3  2014     741
# 5    kings     4  2015     812
# 6    Kings     1  2016     756
# 7    Kings     1  2017     788
# 8   Riders     2  2016     694
# 9   Royals     4  2014     701
# 10  Royals     1  2015     804
# 11  Riders     2  2017     690
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0331E670>
#          sum        mean         std
# Team
# Devils  1536  768.000000  134.350288
# Kings   2285  761.666667   24.006943
# Riders  3049  762.250000   88.567771
# Royals  1505  752.500000   72.831998
# kings    812  812.000000         NaN



###########################################################
# Transformations
# Transformation on a group or a column returns an object that is indexed
# the same size of that is being grouped. Thus, the transform should return a result that is the
# same size as that of a group chunk.



# import pandas as pd
# import numpy as np
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# grouped = df.groupby('Team')
# score = lambda x: (x - x.mean()) / x.std()*10
# print(grouped.transform(score))
#          Rank       Year     Points
# 0  -15.000000 -11.618950  12.843272
# 1    5.000000  -3.872983   3.020286
# 2   -7.071068  -7.071068   7.071068
# 3    7.071068   7.071068  -7.071068
# 4   11.547005 -10.910895  -8.608621
# 5         NaN        NaN        NaN
# 6   -5.773503   2.182179  -2.360428
# 7   -5.773503   8.728716  10.969049
# 8    5.000000   3.872983  -7.705963
# 9    7.071068  -7.071068  -7.071068
# 10  -7.071068   7.071068   7.071068
# 11   5.000000  11.618950  -8.157595




# Filtration
# Filtration filters the data on a defined criteria and returns the subset of data.
# The filter() function is used to filter the data.



# import pandas as pd
# import numpy as np
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# print(df)
# print(df.groupby('Team').filter(lambda x: len(x) >= 3))
#       Team  Rank  Year  Points
# 0   Riders     1  2014     876
# 1   Riders     2  2015     789
# 2   Devils     2  2014     863
# 3   Devils     3  2015     673
# 4    Kings     3  2014     741
# 5    kings     4  2015     812
# 6    Kings     1  2016     756
# 7    Kings     1  2017     788
# 8   Riders     2  2016     694
# 9   Royals     4  2014     701
# 10  Royals     1  2015     804
# 11  Riders     2  2017     690
#       Team  Rank  Year  Points
# 0   Riders     1  2014     876
# 1   Riders     2  2015     789
# 4    Kings     3  2014     741
# 6    Kings     1  2016     756
# 7    Kings     1  2017     788
# 8   Riders     2  2016     694
# 11  Riders     2  2017     690


# import pandas as pd
# import numpy as np
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
# df = pd.DataFrame(ipl_data)
# print(df)
# print(df.groupby('Team').filter(lambda x: len(x) <3))
#       Team  Rank  Year  Points
# 0   Riders     1  2014     876
# 1   Riders     2  2015     789
# 2   Devils     2  2014     863
# 3   Devils     3  2015     673
# 4    Kings     3  2014     741
# 5    kings     4  2015     812
# 6    Kings     1  2016     756
# 7    Kings     1  2017     788
# 8   Riders     2  2016     694
# 9   Royals     4  2014     701
# 10  Royals     1  2015     804
# 11  Riders     2  2017     690
#       Team  Rank  Year  Points
# 2   Devils     2  2014     863
# 3   Devils     3  2015     673
# 5    kings     4  2015     812
# 9   Royals     4  2014     701
# 10  Royals     1  2015     804





