import pandas
import datetime
import numpy as np


class DataFrame (pandas.DataFrame):
    """
    ================================================
    Add a journal of comments to a pandas dataframe.
    ================================================
    When initialising the dataframe it is possbile to give a first comment: 
        
        df = DataFrame(comment=<my comment>)

    It is possible to add a new comment:
        
        df.add_comment(<my comment>)

    Print the journal:
        
        df.print_history()

    """
    def __init__(self, data=None, index=None, columns=None, dtype=None, copy=False, comment=None):
        super().__init__(data=None, index=None, columns=None, dtype=None, copy=False)
        self.attrs={}
        if comment != None:
            self.attrs["comment"] = comment
            self.attrs["history"] = {str(np.datetime64(datetime.datetime.now()).astype(str)): self.attrs["comment"]}
        else:
            self.attrs["history"] = {}

    def add_comment(self, message):
        self.attrs["comment"] = message
        self.attrs["history"][str(np.datetime64(datetime.datetime.now()).astype(str))] = self.attrs["comment"]

    def print_history(self, option="Full"):
        if option == "Full":
            for k in self.attrs["history"].keys():
                print(k, self.attrs["history"][k])
