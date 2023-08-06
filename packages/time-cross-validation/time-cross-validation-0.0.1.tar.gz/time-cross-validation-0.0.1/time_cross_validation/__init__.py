# %%
import pandas as pd
# %%
class TimeCV:

    def __init__(self, X, train_sample_size = None, test_sample_size = None, step = 1):
        
        #initiate variables:
        self.X = X
        self.train_sample_size = train_sample_size
        self.test_sample_size = test_sample_size
        self.step = step

        if train_sample_size == None:
            self.train_sample_size = max(1,round(len(X)/3))
        if test_sample_size == None:
            self.test_sample_size = max(1, round(len(X)/10))

        #error handling:
        if len(X) == 0:
            raise IndexError("input array 'X' cannot have length zero.")
        if len(X) == 1:
            raise IndexError("input array 'X' cannot have length 1.")
        if train_sample_size > len(X):
            raise IndexError("train_sample_size cannot be larger than length of input variable (X).")
        if test_sample_size > len(X):
            raise IndexError("test_sample_size cannot be larger than length of input variable (X).")
        
        if step > len(X):
            raise IndexError("step cannot be larger than length of input variable.")


    def rolling_train_test_split(self):

        list_of_indexes = []
        for i in range(0, len(self.X) + 1 -(self.train_sample_size + self.test_sample_size), self.step):
            train_index = list(range(0+i,self.train_sample_size+i))
            test_index = list(range(self.train_sample_size+i,self.train_sample_size+i+self.test_sample_size))
            list_of_indexes.append((train_index, test_index))
        
        return list_of_indexes
        
        
    def expanding_train_test_split(self):

        list_of_indexes = []
        for i in range(0, len(self.X) + 1 -(self.train_sample_size + self.test_sample_size), self.step):
            train_index = list(range(0,self.train_sample_size+i))
            test_index = list(range(self.train_sample_size+i,self.train_sample_size+i+self.test_sample_size))
            list_of_indexes.append((train_index, test_index))
        
        return list_of_indexes




# %%

X = pd.DataFrame([10,20,10,4,5,1,7,20])
Y = pd.DataFrame([5,1,7,20,10,20,10,4])

CV = TimeCV(X,3,3,1)
for train_index, test_index in CV.expanding_train_test_split():
    print(train_index, test_index)
    x_train = X.iloc[train_index]
    x_test = X.iloc[test_index]
# %%
