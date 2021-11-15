#jupyter notebook file containing Journal class
# import dependencies

from entry import Entry



class Journal():
    """
    Journal is a base class, responsible for CRUD operations of the entire collection of 
    entries 


    Instance Attributes:
    
        filename (string) string identifying the csv file the journal reads and writes from
        entries (list)
    """
    def __init__(self, **kwargs):
        if("filename" in kwargs):
            try:
                self.filename = kwargs["filename"]
            except:
                print(f"{kwargs['filename']} does not exist")
                self.filename = None

        else:
            self.filename = None

    @classmethod
    def read(cls, file):
        return cls(filename=file)
    
    @classmethod
    def new(cls):
        return cls()

    def create_entry(self, entry_dict):
        """
        Expects dictionary object with the following keys:
            sleep_start, sleep_end, sleep_quality, sleep_location, sleep_interuptions,
            habits
            exercises 

        """
        if isinstance(entry_dict, dict) != True:
            return False
        
        else:
            entry = Entry()
            entry.create_sleep(entry_dict["sleep_start"], entry_dict["sleep_end"], entry_dict["sleep_quality"], entry_dict["sleep_location"], entry_dict["sleep_interuption"])

    
        


    # @classmethod
    # def add_entry(self):
    #     try:
    #         self._temp_entry = Entry().new()
    #         self.dataframe = self.dataframe.append(self._temp_entry)
    #         return True
    #     except:
    #         return False

    # # instance method self.write()
    # def write(self, file):
    #     try:
    #         self.dataframe.to_csv(file)
        
    #     except AttributeError:
    #         print("\nJournal object is empty: dataframe attribute is Nonetype\n")
    #         return False

    #     else:
    #         print(f"\nJournal object's dataframe successfully written to {file}\n")
    #         return True

    @property
    def temp_entry(self):
        return {
                "date" : [self._temp_entry.date],
                "time" : [self._temp_entry.time],
                "sleep_location" : [self._temp_entry.sleep.location],
                "fell_asleep_time" : [self._temp_entry.sleep.startime],
                "wake_up_time" : [self._temp_entry.sleep.endtime],
                "sleep_quality" : [self._temp_entry.sleep.quality]
        }





# columns = ["sleep_location", "fell_asleep_time", "wake_up_time", "sleep_quality",\
#   "tobacco_bool", "tobacco_start_time", "tobacco_location", "cigs_count", "tobacco_quality",\
#   "alcohol_bool", "alcohol_start_time", "alcohol_location", "drinks_count",\
#   "exercise1_bool", "exercis1e_type", "exercis1e_loc", "exercise1_start", "exercise1_end", "exercise1_intensity", "exercise1_quality",\
#   "exercise2_bool","exercise2_type", "exercise2_loc", "exercise2_start", "exercise2_end",\
#   "exercise2_intensity", "exercise2_quality"]