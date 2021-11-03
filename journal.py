# file containing journal class
from entry import Entry


class Journal():
    """
    Journal is a base class, responsible for CRUD operations of the entire collection of 
    entries 

    Class Attributes:
        
        QUALITIES (list of strings)
        
        exercise_list (list of strings)

    Instance Attributes:

        head (Entry) points to first Entry in the collection
    """

    QUALITIES = ["Terrible", "Bad", "Okay", "Good", "Great"]
    exercise_list = ["Basketball", "Run", "Walk", "Yoga", "Other"] # NEED TO MAKE DYNAMIC VIA ALL PAST ENTRIES; 
                                                                #REORDER SO 'OTHER' IS AT THE END ALWAYS
    def __init__(self, *args):
        # Initialization needs to read in a file, store the contents 
        self.filename = "FILLER"
        self._head = None

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"\
        "~~ Creating new journal entry ~~\n"\
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

