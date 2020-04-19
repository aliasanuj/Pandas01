########################################################
# There are two kinds of sorting available in Pandas. They are −
# == By label
# == By Actual Value


#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1, index=[1,2,4,5,9,7,4,6])
# print(df)
# print(df.sort_index())
#    marks   Age
# 1   30.0  84.0
# 2   40.0  24.0
# 4   60.0  74.0
# 5   70.0  21.0
# 9    NaN   NaN
# 7   90.0   NaN
# 4   60.0  74.0
# 6    8.0  54.0
#    marks   Age
# 1   30.0  84.0
# 2   40.0  24.0
# 4   60.0  74.0
# 4   60.0  74.0
# 5   70.0  21.0
# 6    8.0  54.0
# 7   90.0   NaN
# 9    NaN   NaN





#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1, index=[1,2,4,5,9,7,4,6,10])
# print(df)
# print(df.sort_index())
#     marks   Age
# 1    30.0  84.0
# 2    40.0  24.0
# 4    60.0  74.0
# 5    70.0  21.0
# 9     NaN   NaN
# 7    90.0   NaN
# 4    60.0  74.0
# 6     8.0  54.0
# 10    NaN   NaN
#     marks   Age
# 1    30.0  84.0
# 2    40.0  24.0
# 4    60.0  74.0
# 4    60.0  74.0
# 5    70.0  21.0
# 6     8.0  54.0
# 7    90.0   NaN
# 9     NaN   NaN
# 10    NaN   NaN




#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.sort_index())
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN





#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.sort_index(ascending=False))
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN
#    marks   Age
# 7     90   NaN
# 6      8  54.0
# 5     70  21.0
# 4     60  74.0
# 3     55  68.0
# 2     40  24.0
# 1     30  84.0
# 0     50  55.0






#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.sort_index(ascending=True))
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN




#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.sort_index(axis=0))
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN


#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.sort_index(axis=1))
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN
#     Age  marks
# 0  55.0     50
# 1  84.0     30
# 2  24.0     40
# 3  68.0     55
# 4  74.0     60
# 5  21.0     70
# 6  54.0      8
# 7   NaN     90





#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.sort_values(by="Age"))
#    marks   Age
# 0     50  55.0
# 1     30  84.0
# 2     40  24.0
# 3     55  68.0
# 4     60  74.0
# 5     70  21.0
# 6      8  54.0
# 7     90   NaN
#    marks   Age
# 5     70  21.0
# 2     40  24.0
# 6      8  54.0
# 0     50  55.0
# 3     55  68.0
# 4     60  74.0
# 1     30  84.0
# 7     90   NaN



#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54]),
#          "distance" :pd.Series([44,21,87,14,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.sort_values(by=["marks"]))
#    marks   Age  distance
# 0     50  55.0      44.0
# 1     30  84.0      21.0
# 2     40  24.0      87.0
# 3     55  68.0      14.0
# 4     60  74.0      74.0
# 5     70  21.0      21.0
# 6      8  54.0      54.0
# 7     90   NaN       NaN
#    marks   Age  distance
# 6      8  54.0      54.0
# 1     30  84.0      21.0
# 2     40  24.0      87.0
# 0     50  55.0      44.0
# 3     55  68.0      14.0
# 4     60  74.0      74.0
# 5     70  21.0      21.0
# 7     90   NaN       NaN




#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54]),
#          "distance" :pd.Series([44,21,87,14,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.sort_values(by=["marks","Age"]))
#    marks   Age  distance
# 0     50  55.0      44.0
# 1     30  84.0      21.0
# 2     40  24.0      87.0
# 3     55  68.0      14.0
# 4     60  74.0      74.0
# 5     70  21.0      21.0
# 6      8  54.0      54.0
# 7     90   NaN       NaN
#    marks   Age  distance
# 6      8  54.0      54.0
# 1     30  84.0      21.0
# 2     40  24.0      87.0
# 0     50  55.0      44.0
# 3     55  68.0      14.0
# 4     60  74.0      74.0
# 5     70  21.0      21.0
# 7     90   NaN       NaN
#only Marks will sort





#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54]),
#          "distance" :pd.Series([44,21,87,14,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.sort_values(by="marks", kind="mergesort"))
#    marks   Age  distance
# 0     50  55.0      44.0
# 1     30  84.0      21.0
# 2     40  24.0      87.0
# 3     55  68.0      14.0
# 4     60  74.0      74.0
# 5     70  21.0      21.0
# 6      8  54.0      54.0
# 7     90   NaN       NaN
#    marks   Age  distance
# 6      8  54.0      54.0
# 1     30  84.0      21.0
# 2     40  24.0      87.0
# 0     50  55.0      44.0
# 3     55  68.0      14.0
# 4     60  74.0      74.0
# 5     70  21.0      21.0
# 7     90   NaN       NaN



#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54]),
#          "distance" :pd.Series([44,21,87,14,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.sort_values(by="Age", kind="heapsort"))
#    marks   Age  distance
# 0     50  55.0      44.0
# 1     30  84.0      21.0
# 2     40  24.0      87.0
# 3     55  68.0      14.0
# 4     60  74.0      74.0
# 5     70  21.0      21.0
# 6      8  54.0      54.0
# 7     90   NaN       NaN
#    marks   Age  distance
# 5     70  21.0      21.0
# 2     40  24.0      87.0
# 6      8  54.0      54.0
# 0     50  55.0      44.0
# 3     55  68.0      14.0
# 4     60  74.0      74.0
# 1     30  84.0      21.0
# 7     90   NaN       NaN




#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54]),
#          "distance" :pd.Series([44,21,87,14,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.sort_values(by="distance", kind="quicksort"))
#    marks   Age  distance
# 0     50  55.0      44.0
# 1     30  84.0      21.0
# 2     40  24.0      87.0
# 3     55  68.0      14.0
# 4     60  74.0      74.0
# 5     70  21.0      21.0
# 6      8  54.0      54.0
# 7     90   NaN       NaN
#    marks   Age  distance
# 3     55  68.0      14.0
# 1     30  84.0      21.0
# 5     70  21.0      21.0
# 0     50  55.0      44.0
# 6      8  54.0      54.0
# 4     60  74.0      74.0
# 2     40  24.0      87.0
# 7     90   NaN       NaN



#############################################################
# import pandas as pd
# import numpy as np
# data1 = {"marks":pd.Series([50,30,40,55,60,70,8,90]),
#          "Age" :pd.Series([55,84,24,68,74,21,54]),
#          "distance" :pd.Series([44,21,87,14,74,21,54])
#          }
# df = pd.DataFrame(data1)
# print(df)
# print(df.sort_values(by="distance", kind="quicksort"))
# print(df.reset_index(drop=True))
#    marks   Age  distance
# 0     50  55.0      44.0
# 1     30  84.0      21.0
# 2     40  24.0      87.0
# 3     55  68.0      14.0
# 4     60  74.0      74.0
# 5     70  21.0      21.0
# 6      8  54.0      54.0
# 7     90   NaN       NaN
#    marks   Age  distance
# 3     55  68.0      14.0
# 1     30  84.0      21.0
# 5     70  21.0      21.0
# 0     50  55.0      44.0
# 6      8  54.0      54.0
# 4     60  74.0      74.0
# 2     40  24.0      87.0
# 7     90   NaN       NaN
#    marks   Age  distance
# 0     50  55.0      44.0
# 1     30  84.0      21.0
# 2     40  24.0      87.0
# 3     55  68.0      14.0
# 4     60  74.0      74.0
# 5     70  21.0      21.0
# 6      8  54.0      54.0
# 7     90   NaN       NaN
