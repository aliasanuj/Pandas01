series:
axes == Returns a list of the row axis labels
dtype == Returns the dtype of the object.
empty == Returns True if series is empty.
ndim == Returns the number of dimensions of the underlying data, by definition 1.
size == Returns the number of elements in the underlying data.
values == Returns the Series as ndarray.
head() == Returns the first n rows.
tail() == Returns the last n rows.


DataFrame:
T == Transposes rows and columns.
axes == Returns a list with the row axis labels and column axis labels as the only members.
dtypes == Returns the dtypes in this object.
empty == True if NDFrame is entirely empty [no items]; if any of the axes are of length 0.
ndim == Number of axes / array dimensions.
shape == Returns a tuple representing the dimensionality of the DataFrame.
size == Number of elements in the NDFrame.
values == Numpy representation of NDFrame.
head() == Returns the first n rows.
tail() == Returns last n rows.

