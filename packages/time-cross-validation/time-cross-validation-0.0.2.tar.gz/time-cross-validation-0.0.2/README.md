#Overview:

The package provides quick train/test split indexing for cross validation, specifically optimized for time series data.
There are two primary output options:
1. Expanding Window - in which the training window becomes larger with each fold and is always overlapping with part of the previous.
2. Rolling Window - in which the training window is of a fixed pre specified dimension, and it may or may not overlap depending on the rolling step specified.

#Example:

'''
from time_cross_validation import TimeCV
import pandas as pd

#sample X and Y variables:
X = pd.DataFrame([10,20,10,4,5,1,7,20])
Y = pd.DataFrame([5,1,7,20,10,20,10,4])

CV = TimeCV(X, train_sample_size = 3, 
                test_sample_size = 3, 
                step = 1)
for train_index, test_index in CV.expanding_train_test_split():
    x_train = X.iloc[train_index]
    x_test = X.iloc[test_index]
'''