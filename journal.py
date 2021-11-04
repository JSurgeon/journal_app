#jupyter notebook file containing Journal class
# import dependencies

from entry import Entry
import pandas as pd

class Journal():
    """
    Journal is a base class, responsible for CRUD operations of the entire collection of 
    entries 


    Instance Attributes:
    
        filename (string) string identifying the csv file the journal reads and writes from
    """
    def __init__(self, **kwargs):
        if("filename" in kwargs):
            self.filename = kwargs["filename"]
            ###### read file in and create dataframe
            self.dataframe = pd.read_csv(self.filename)
        
        if("columns" in kwargs):
            self.dataframe = pd.DataFrame(columns=kwargs["columns"])

    @classmethod
    def read(cls, file):
        if file:
            print("file called")
            return cls(filename=file)
        return None
    
    @classmethod
    def new(cls):
        columns = ["sleep_location", "fell_asleep_time", "wake_up_time", "sleep_quality",\
          "tobacco_bool", "tobacco_start_time", "tobacco_location", "cigs_count", "tobacco_quality",\
          "alcohol_bool", "alcohol_start_time", "alcohol_location", "drinks_count",\
          "exercise1_bool", "exercis1e_type", "exercis1e_loc", "exercise1_start", "exercise1_end", "exercise1_intensity", "exercise1_quality",\
          "exercise2_bool","exercise2_type", "exercise2_loc", "exercise2_start", "exercise2_end",\
          "exercise2_intensity", "exercise2_quality"]
        
        response = input("Would you like to add a new entry? (y/n)")
        while (response.capitalize() != 'N') and (response.capitalize() != "Y"):
            response = input("Unacceptable response: please respond with 'y' to add a new entry or 'n' not to")

        while response.capitalize() == 'Y':
            new_entry = Entry().new()

            # add new_entry to dataframe
            #...
            print(new_entry)

            response = input("Would you like to add another entry?")
            while (response.capitalize() != 'N') and (response.capitalize() != "Y"):
                response = input("Unacceptable response: please respond with 'y' to add a new entry or 'n' not to")

            
        return cls(columns=columns)
    
    # instance method self.write()
    def write(self, file):
        try:
            self.dataframe.to_csv(file)
        
        except AttributeError:
            print("Journal object is empty: dataframe attribute is Nonetype")
            return False

        else:
            print(f"Journal object's dataframe successfully written to {file}")
            return True
        
