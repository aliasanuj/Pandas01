#working_with_text_data.py
# lower() == Converts stngs in the Series/Index to lower case.
# upper() == Converts strings in the Series/Index to upper case.
# len() == Computes String length().
# strip() == Helps strip whitespace(including newline) from each string in the Series/index from both the sides.
# split(' ') == Splits each string with the given pattern.
# cat(sep=' ') == Concatenates the series/index elements with given separator.
# get_dummies() == Returns the DataFrame with One-Hot Encoded values.
# contains(pattern) == Returns a Boolean value True for each element if the substring contains in the element, else False.
# replace(a,b) == Replaces the value a with the value b.
# repeat(value) == Repeats each element with specified number of times.
# count(pattern) == Returns count of appearance of pattern in each element.
# startswith(pattern) == Returns true if the element in the Series/Index starts with the pattern.
# endswith(pattern) == Returns true if the element in the Series/Index ends with the pattern.
# find(pattern) == Returns the first position of the first occurrence of the pattern.
# findall(pattern) == Returns a list of all occurrence of the pattern.
# swapcase == Swaps the case lower/upper.
# islower() == Checks whether all characters in each string in the Series/Index in lower case or not. Returns Boolean
# isupper() == Checks whether all characters in each string in the Series/Index in upper case or not. Returns Boolean.
# isnumeric() == Checks whether all characters in each string in the Series/Index are numeric. Returns Boolean.



###################################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df.str.lower())
# AttributeError: 'DataFrame' object has no attribute 'str'




#############################################################
# import pandas as pd
# import numpy as np
# s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])
# print(s)
# 0             Tom
# 1    William Rick
# 2            John
# 3         Alber@t
# 4             NaN
# 5            1234
# 6      SteveSmith
# dtype: object




#############################################################
# import pandas as pd
# import numpy as np
# s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])
# print(s.str.lower())
# 0             tom
# 1    william rick
# 2            john
# 3         alber@t
# 4             NaN
# 5            1234
# 6      stevesmith
# dtype: object




#############################################################
# import pandas as pd
# import numpy as np
# s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])
# print(s.str.upper())
# 0             TOM
# 1    WILLIAM RICK
# 2            JOHN
# 3         ALBER@T
# 4             NaN
# 5            1234
# 6      STEVESMITH
# dtype: object





#############################################################
# import pandas as pd
# import numpy as np
# s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])
# print(s.str.len())
# 0     3.0
# 1    12.0
# 2     4.0
# 3     7.0
# 4     NaN
# 5     4.0
# 6    10.0
# dtype: float64




#############################################################
# import pandas as pd
# import numpy as np
# s = pd.Series(['Tom', ' William Rick', '  John', 'Al  ber@t', np.nan, '1234','SteveSmith'])
# print(s.str.strip())
# 0             Tom
# 1    William Rick
# 2            John
# 3       Al  ber@t
# 4             NaN
# 5            1234
# 6      SteveSmith
# dtype: object





#############################################################
# import pandas as pd
# import numpy as np
# s = pd.Series(['Tom', ' William Rick', '  John', 'Al  ber@t', np.nan, '123 4','SteveSmith'])
# print(s.str.split())
# 0              [Tom]
# 1    [William, Rick]
# 2             [John]
# 3        [Al, ber@t]
# 4                NaN
# 5           [123, 4]
# 6       [SteveSmith]
# dtype: object




#############################################################
# import pandas as pd
# import numpy as np
# s = pd.Series(['Tom','William Ric kumar','John','Al  ber@t',np.nan,'123 4','SteveSmith'])
# print(s.str.split())
# 0                    [Tom]
# 1    [William, Ric, kumar]
# 2                   [John]
# 3              [Al, ber@t]
# 4                      NaN
# 5                 [123, 4]
# 6             [SteveSmith]
# dtype: object



#############################################################
# import pandas as pd
# import numpy as np
# s = pd.Series(['Tom', ' William Rick', '  John', 'Al  ber@t', np.nan, '123 4','SteveSmith'])
# print(s.str.cat(sep="-"))
# Tom- William Rick-  John-Al  ber@t-123 4-SteveSmith




#############################################################
# import pandas as pd
# import numpy as np
# s = pd.Series(['Tom', ' William Rick', '  John', 'Al  ber@t', np.nan, '123 4','SteveSmith'])
# print(s.str.get_dummies())
#      John   William Rick  123 4  Al  ber@t  SteveSmith  Tom
# 0       0              0      0          0           0    1
# 1       0              1      0          0           0    0
# 2       1              0      0          0           0    0
# 3       0              0      0          1           0    0
# 4       0              0      0          0           0    0
# 5       0              0      1          0           0    0
# 6       0              0      0          0           1    0



# import pandas as pd
# import numpy as np
# s = pd.Series(['Tom', ' William Rick', '  John', 'Al  ber@t', np.nan, '123 4','SteveSmith'])
# print(s.str.contains(' '))
# 0    False
# 1     True
# 2     True
# 3     True
# 4      NaN
# 5     True
# 6    False
# dtype: object




#############################################################
# import pandas as pd
# import numpy as np
# s = pd.Series(['Tom', ' William Rick', '  John', 'Al  ber@t', np.nan, '123 4','SteveSmith'])
# print(s.str.replace('S','#'))
# 0              Tom
# 1     William Rick
# 2             John
# 3        Al  ber@t
# 4              NaN
# 5            123 4
# 6       #teve#mith
# dtype: object



#############################################################
# import pandas as pd
# import numpy as np
# s = pd.Series(['Tom', ' William Rick', '  John', 'Al  ber@t', np.nan, '123 4','SteveSmith'])
# print(s.str.repeat(2))
# 0                        TomTom
# 1     William Rick William Rick
# 2                    John  John
# 3            Al  ber@tAl  ber@t
# 4                           NaN
# 5                    123 4123 4
# 6          SteveSmithSteveSmith
# dtype: object




#############################################################
# import pandas as pd
# import numpy as np
# s = pd.Series(['Tom', ' William Rick', '  John', 'Al  ber@t', np.nan, '123 4','SteveSmith'])
# print(s.str.count('4'))
# 0    0.0
# 1    0.0
# 2    0.0
# 3    0.0
# 4    NaN
# 5    1.0
# 6    0.0
# dtype: float64




#############################################################
# import pandas as pd
# import numpy as np
# s = pd.Series(['Tom', ' William Rick', '  John', 'Al  ber@t', np.nan, '123 4','SteveSmith'])
# print(s.str.count('l'))
# 0    0.0
# 1    2.0
# 2    0.0
# 3    1.0
# 4    NaN
# 5    0.0
# 6    0.0
# dtype: float64




#############################################################
# import pandas as pd
# import numpy as np
# s = pd.Series(['Tom', ' William Rick', '  John', 'Al  ber@t', np.nan, '123 4','SteveSmith'])
# print(s.str.startswith('A'))
# 0    False
# 1    False
# 2    False
# 3     True
# 4      NaN
# 5    False
# 6    False
# dtype: object



#############################################################
import pandas as pd
# import numpy as np
# s = pd.Series(['Tom', ' William Rick', '  John', 'Al  ber@t', np.nan, '123 4','SteveSmith'])
# print(s.str.endswith('m'))
# 0     True
# 1    False
# 2    False
# 3    False
# 4      NaN
# 5    False
# 6    False
# dtype: objec





#############################################################
# import pandas as pd
# import numpy as np
# s = pd.Series(['Tom', ' William Rick', '  John', 'Al  ber@t', np.nan, '123 4','SteveSmith'])
# print(s.str.find('c'))
# 0    -1.0
# 1    11.0
# 2    -1.0
# 3    -1.0
# 4     NaN
# 5    -1.0
# 6    -1.0
# dtype: float64





#############################################################
# import pandas as pd
# import numpy as np
# s = pd.Series(['Tom', ' William Rick', '  John', 'Al  ber@t', np.nan, '123 4','SteveSmith'])
# print(s.str.findall('c'))
# 0     []
# 1    [c]
# 2     []
# 3     []
# 4    NaN
# 5     []
# 6     []
# dtype: object





#############################################################
# import pandas as pd
# import numpy as np
# s = pd.Series(['Tom', ' William Rick', '  John', 'Al  ber@t', np.nan, '123 4','SteveSmith'])
# print(s.str.findall('l'))
# 0        []
# 1    [l, l]
# 2        []
# 3       [l]
# 4       NaN
# 5        []
# 6        []
# dtype: object





#############################################################
# import pandas as pd
# import numpy as np
# s = pd.Series(['Tom', ' William Rick', '  John', 'Al  ber@t', np.nan, '123 4','SteveSmith'])
# print(s.str.swapcase())
# 0              tOM
# 1     wILLIAM rICK
# 2             jOHN
# 3        aL  BER@T
# 4              NaN
# 5            123 4
# 6       sTEVEsMITH
dtype: object





#############################################################
# import pandas as pd
# import numpy as np
# s = pd.Series(['Tom', ' William Rick', 'john', 'Al  ber@t', np.nan, '123 4','SteveSmith'])
# print(s.str.islower())
# 0    False
# 1    False
# 2     True
# 3    False
# 4      NaN
# 5    False
# 6    False
# dtype: object





#############################################################
# import pandas as pd
# import numpy as np
# s = pd.Series(['Tom', ' William Rick', 'john', 'Al  ber@t', np.nan, '123 4','SteveSmith'])
# print(s.str.isupper())
# 0    False
# 1    False
# 2    False
# 3    False
# 4      NaN
# 5    False
# 6    False
# dtype: object




#############################################################
# import pandas as pd
# import numpy as np
# s = pd.Series(['Tom', ' William Rick', '1000', 'Al  ber@t', np.nan, 100 ,'SteveSmith'])
# print(s.str.isnumeric())
# 0    False
# 1    False
# 2     True
# 3    False
# 4      NaN
# 5      NaN
# 6    False
# dtype: object


