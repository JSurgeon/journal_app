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
            try:
                self.filename = kwargs["filename"]
                self.dataframe = pd.read_csv(self.filename)
            except:
                print(f"{kwargs['filename']} does not exist")
                self.filename = None
                self.dataframe = None

        if("entries" in kwargs):
            self.dataframe = pd.DataFrame()
            for entry in kwargs["entries"]:
                df = pd.DataFrame({
                "date" : [entry.date],
                "time" : [entry.time],
                "sleep_location" : [entry.sleep.location],
                "fell_asleep_time" : [entry.sleep.startime],
                "wake_up_time" : [entry.sleep.endtime],
                "sleep_quality" : [entry.sleep.quality]
                #### need habit and exercise data: may need to rethink how those are stored or
                #### how this dataframe is created
                })  
                self.dataframe = self.dataframe.append(df)
        
        else:
            self.filename = None
            self.dataframe = None

    @classmethod
    def read(cls, file):
        return cls(filename=file)
    
    @classmethod
    def new(cls):

        response = input("Would you like to add a new entry? (y/n)")
        while (response.capitalize() != 'N') and (response.capitalize() != "Y"):
            response = input("Unacceptable response: please respond with 'y' to add a new entry or 'n' not to")

        entries_list = list()
        while response.capitalize() == 'Y':
            
            new_entry = Entry().new()

            entries_list.append(new_entry)

            response = input("Would you like to add another entry?")

            while (response.capitalize() != 'N') and (response.capitalize() != "Y"):
                response = input("Unacceptable response: please respond with 'y' to add a new entry or 'n' not to")

        return cls(entries=entries_list)
    
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





# columns = ["sleep_location", "fell_asleep_time", "wake_up_time", "sleep_quality",\
#   "tobacco_bool", "tobacco_start_time", "tobacco_location", "cigs_count", "tobacco_quality",\
#   "alcohol_bool", "alcohol_start_time", "alcohol_location", "drinks_count",\
#   "exercise1_bool", "exercis1e_type", "exercis1e_loc", "exercise1_start", "exercise1_end", "exercise1_intensity", "exercise1_quality",\
#   "exercise2_bool","exercise2_type", "exercise2_loc", "exercise2_start", "exercise2_end",\
#   "exercise2_intensity", "exercise2_quality"]