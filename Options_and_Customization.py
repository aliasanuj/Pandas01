# Pandas provide API to customize some aspects of its behavior, display is being mostly used.
# The API is composed of five relevant functions. They are −
# get_option()
# set_option()
# reset_option()
# describe_option()
# option_context()

###############################################################
# import pandas as pd
# print(pd.get_option("display.max_rows"))
#60



###############################################################
# import pandas as pd
# print(pd.get_option("display.max_columns"))
# 0



###############################################################
# import pandas as pd
# pd.set_option("display.max_rows",80)
# print(pd.get_option("display.max_rows"))
# 80




###############################################################
# import pandas as pd
# pd.set_option("display.max_columns",80)
# print(pd.get_option("display.max_columns"))
# 80



###############################################################
# import pandas as pd
# pd.reset_option("display.max_rows")
# print(pd.get_option("display.max_rows"))
# 60




###############################################################
# import pandas as pd
# pd.describe_option("display.max_rows")
# print(pd.describe_option("display.max_rows"))
# isplay.max_rows : int
#     If max_rows is exceeded, switch to truncate view. Depending on
#     `large_repr`, objects are either centrally truncated or printed as
#     a summary view. 'None' value means unlimited.
# 
#     In case python/IPython is running in a terminal and `large_repr`
#     equals 'truncate' this can be set to 0 and pandas will auto-detect
#     the height of the terminal and print a truncated object which fits
#     the screen height. The IPython notebook, IPython qtconsole, or
#     IDLE do not run in a terminal and hence it is not possible to do
#     correct auto-detection.
#     [default: 60] [currently: 60]
# display.max_rows : int
#     If max_rows is exceeded, switch to truncate view. Depending on
#     `large_repr`, objects are either centrally truncated or printed as
#     a summary view. 'None' value means unlimited.
# 
#     In case python/IPython is running in a terminal and `large_repr`
#     equals 'truncate' this can be set to 0 and pandas will auto-detect
#     the height of the terminal and print a truncated object which fits
#     the screen height. The IPython notebook, IPython qtconsole, or
#     IDLE do not run in a terminal and hence it is not possible to do
#     correct auto-detection.
#     [default: 60] [currently: 60]
# None
