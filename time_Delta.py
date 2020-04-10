time_Delta.py




# import pandas as pd
# print(pd.Timedelta('2 days 2 hours 15 minutes 30 seconds'))
# #2 days 02:15:30


# import pandas as pd
# print(pd.Timedelta(6,unit='h'))
# # 0 days 06:00:00


# import pandas as pd
# print(pd.Timedelta(days=2))
# 2 days 00:00:00




# import pandas as pd
# print(pd.Timedelta(days=2))
# 2 days 00:00:00
#



# import pandas as pd
# s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
# td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
# df = pd.DataFrame(dict(A = s, B = td))
# print(df)
#            A      B
# 0 2012-01-01 0 days
# 1 2012-01-02 1 days
# 2 2012-01-03 2 days






# import pandas as pd
# s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
# td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
# df = pd.DataFrame(dict(A = s, B = td))
# df['C']=df['A']+df['B']
# print(df)
#            A      B          C
# 0 2012-01-01 0 days 2012-01-01
# 1 2012-01-02 1 days 2012-01-03
# 2 2012-01-03 2 days 2012-01-05






# import pandas as pd
# s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
# td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
# df = pd.DataFrame(dict(A = s, B = td))
# df['C']=df['A']+df['B']
# df['D']=df['C']+df['B']
# print(df)
#            A      B          C          D
# 0 2012-01-01 0 days 2012-01-01 2012-01-01
# 1 2012-01-02 1 days 2012-01-03 2012-01-04
# 2 2012-01-03 2 days 2012-01-05 2012-01-07






















