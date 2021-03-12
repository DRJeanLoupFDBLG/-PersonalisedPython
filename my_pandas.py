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
    
    A global description can be set, once defined it is protected by default:

        df.set_description(<description>, force_writing=False)

    It is possible to add a new comment:
        
        df.add_comment(<my comment>)

    Print the journal:
        
        df.print_history()

    """
    def __init__(self, data=None, index=None, columns=None, dtype=None, copy=False, comment=None):
        super().__init__(data=None, index=None, columns=None, dtype=None, copy=False)
        self.attrs={"journal":{}}
        if comment != None:
            self.attrs["journal"]["comment"] = comment
            self.attrs["journal"]["history"] = {str(np.datetime64(datetime.datetime.now()).astype(str)): self.attrs["journal"]["comment"]}
        else:
            self.attrs["journal"]["history"] = {}

    def set_description(self, message, force_writing=False):
        if ("description" in self.attrs["journal"]) and not force_writing:
            print("Description of the data already set!")
        else:
            self.attrs["journal"]["description"] = message

    def add_comment(self, message):
        self.attrs["journal"]["comment"] = message
        self.attrs["journal"]["history"][str(np.datetime64(datetime.datetime.now()).astype(str))] = self.attrs["journal"]["comment"]

    def print_history(self, option="Full"):
        if option == "Full":
            for k in self.attrs["journal"]["history"].keys():
                print(k, self.attrs["journal"]["history"][k])
