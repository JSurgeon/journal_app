# file containing journal class
from entry import Entry
import pandas as pd


class Journal():
    """
    Journal is a base class, responsible for CRUD operations of the entire collection of 
    entries 


    Instance Attributes:

        head (Entry) points to first Entry in the collection
        filename (string) string identifying the csv file the journal reads and writes from
    """

                                                            #REORDER SO 'OTHER' IS AT THE END ALWAYS
    def __init__(self):
        # Initialization needs to read in a file, store the contents 
        self.filename = None
        self._head = None
    
    @classmethod
    def read(cls, filename):
        if filename:
            cls._df = pd.read_csv(filename)
        print(cls._df)




        



