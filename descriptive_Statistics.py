#Descriptive Statistics


#Descriptive Statistics

# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
#    'Lee','David','Gasper','Betina','Andres']),
#    'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df)
#       Name  Age  Rating
# 0      Tom   25    4.23
# 1    James   26    3.24
# 2    Ricky   25    3.98
# 3      Vin   23    2.56
# 4    Steve   30    3.20
# 5    Smith   29    4.60
# 6     Jack   23    3.80
# 7      Lee   34    3.78
# 8    David   40    2.98
# 9   Gasper   30    4.80
# 10  Betina   51    4.10
# 11  Andres   46    3.65


# import pandas as pd
# import numpy as np
# # Create a Dictionary of series
# d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack',
#                         'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
#      'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
#      'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])
#      }
# # Create a DataFrame
# df = pd.DataFrame(d)
# print(df.sum())
# Name      TomJamesRickyVinSteveSmithJackLeeDavidGasperBe...
# Age                                                     382
# Rating                                                44.92
# dtype: object
#
#




# import pandas as pd
# import numpy as np
# # Create a Dictionary of series
# d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack',
#                         'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
#      'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
#      'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 'aaa'])
#      }
# # Create a DataFrame
# df = pd.DataFrame(d)
# print(df.sum())
# Name    TomJamesRickyVinSteveSmithJackLeeDavidGasperBe...
# Age                                                   382
# dtype: object



# import pandas as pd
# import numpy as np
# # Create a Dictionary of series
# d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack',
#                         'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
#      'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
#      'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.4])
#      }
# # Create a DataFrame
# df = pd.DataFrame(d)
# print(df)
# df["age+TRating"]= df["Age"] + df["Rating"]
# print(df)
#       Name  Age  Rating  age+TRating
# 0      Tom   25    4.23        29.23
# 1    James   26    3.24        29.24
# 2    Ricky   25    3.98        28.98
# 3      Vin   23    2.56        25.56
# 4    Steve   30    3.20        33.20
# 5    Smith   29    4.60        33.60
# 6     Jack   23    3.80        26.80
# 7      Lee   34    3.78        37.78
# 8    David   40    2.98        42.98
# 9   Gasper   30    4.80        34.80
# 10  Betina   51    4.10        55.10
# 11  Andres   46    3.40        49.40


# import pandas as pd
# import numpy as np
# # Create a Dictionary of series
# d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack',
#                         'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
#      'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
#      'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65]),
#      'aaa': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65]) }
# # Create a Data rame
# df = pd.DataFrame(d)
# print(df.sum(1))
# 0     33.46
# 1     32.48
# 2     32.96
# 3     28.12
# 4     36.40
# 5     38.20
# 6     30.60
# 7     41.56
# 8     45.96
# 9     39.60
# 10    59.20
# 11    53.30
# dtype: float64


# import pandas as pd
# import numpy as np
# # Create a Dictionary of series
# d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack',
#                         'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
#      'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
#      'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65]),
#      'aaa': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65]) }
# # Create a Data rame
# df = pd.DataFrame(d)
# print(df.sum())
# Name      TomJamesRickyVinSteveSmithJackLeeDavidGasperBe...
# Age                                                     382
# Rating                                                44.92
# aaa                                                   44.92
# dtype: object


# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
#    'Lee','David','Gasper','Betina','Andres']),
#    'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df.mean())
# Age       31.833333
# Rating     3.743333
# dtype: float64



# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
#    'Lee','David','Gasper','Betina','Andres']),
#    'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df.mean(1))
# 0     14.615
# 1     14.620
# 2     14.490
# 3     12.780
# 4     16.600
# 5     16.800
# 6     13.400
# 7     18.890
# 8     21.490
# 9     17.400
# 10    27.550
# 11    24.825
# dtype: float64



# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
#    'Lee','David','Gasper','Betina','Andres']),
#    'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df.std())
# Age       9.232682
# Rating    0.661628
# dtype: float64



# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
#    'Lee','David','Gasper','Betina','Andres']),
#    'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df.std(1))
# 0     14.686608
# 1     16.093750
# 2     14.863385
# 3     14.453263
# 4     18.950462
# 5     17.253405
# 6     13.576450
# 7     21.368767
# 8     26.177093
# 9     17.819091
# 10    33.163308
# 11    29.945972
# dtype: float64


# Functions & Description
# Sr.No.	Function	Description
# 1	count()	Number of non-null observations
# 2	sum()	Sum of values
# 3	mean()	Mean of Values
# 4	median()	Median of Values
# 5	mode()	Mode of values
# 6	std()	Standard Deviation of the Values
# 7	min()	Minimum Value
# 8	max()	Maximum Value
# 9	abs()	Absolute Value
# 10	prod()	Product of Values
# 11	cumsum()	Cumulative Sum
# 12	cumprod()	Cumulative Product



# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
#    'Lee','David','Gasper','Betina','Andres']),
#    'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df.min())
# Name      Andres
# Age           23
# Rating      2.56
# dtype: objec




# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
#    'Lee','David','Gasper','Betina','Andres']),
#    'Age':pd.Series([25,26,25,23,30,1,23,34,40,30,51,2]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df.min(1))
# 0     4.23
# 1     3.24
# 2     3.98
# 3     2.56
# 4     3.20
# 5     1.00
# 6     3.80
# 7     3.78
# 8     2.98
# 9     4.80
# 10    4.10
# 11    2.00
# dtype: float64



# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
#    'Lee','David','Gasper','Betina','Andres']),
#    'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df.describe())
#              Age     Rating
# count  12.000000  12.000000
# mean   31.833333   3.743333
# std     9.232682   0.661628
# min    23.000000   2.560000
# 25%    25.000000   3.230000
# 50%    29.500000   3.790000
# 75%    35.500000   4.132500
# max    51.000000   4.800000


# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
#    'Lee','David','Gasper','Betina','Andres']),
#    'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df.describe(include=['object']))
#         Name
# count     12
# unique    12
# top     Jack #it will continue change the name after each running.
# freq



# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
#    'Lee','David','Gasper','Betina','Andres']),
#    'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df.describe(include=['number']))
#              Age     Rating
# count  12.000000  12.000000
# mean   31.833333   3.743333
# std     9.232682   0.661628
# min    23.000000   2.560000
# 25%    25.000000   3.230000
# 50%    29.500000   3.790000
# 75%    35.500000   4.132500
# max    51.000000   4.800000


# import pandas as pd
# import numpy as np
# #Create a Dictionary of series
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
#    'Lee','David','Gasper','Betina','Andres']),
#    'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
# }
# #Create a DataFrame
# df = pd.DataFrame(d)
# print(df.describe(include='all'))
#          Name        Age     Rating
# count      12  12.000000  12.000000
# unique     12        NaN        NaN
# top     Smith        NaN        NaN
# freq        1        NaN        NaN
# mean      NaN  31.833333   3.743333
# std       NaN   9.232682   0.661628
# min       NaN  23.000000   2.560000
# 25%       NaN  25.000000   3.230000
# 50%       NaN  29.500000   3.790000
# 75%       NaN  35.500000   4.132500
# max       NaN  51.000000   4.800000

# 
# object − Summarizes String columns
# number − Summarizes Numeric columns
# all − Summarizes all columns together (Should not pass it as a list value)


