# file containing journal class
from entry import Entry


class Journal():
    """
    Journal is a base class, responsible for CRUD operations of the entire collection of 
    entries 

    Instance Attributes:

        head (Entry) points to first Entry in the collection
    """

    QUALITIES = ["Terrible", "Bad", "Okay", "Good", "Great"]
    exercise_list = ["Basketball", "Run", "Walk", "Yoga", "Other"] # NEED TO MAKE DYNAMIC VIA ALL PAST ENTRIES; 
                                                                #REORDER SO 'OTHER' IS AT THE END ALWAYS
    def __init__(self, filename):
        # Initialization needs to read in a file, store the contents 
        self.filename = "FILLER"


    # Class Methods
    @classmethod
    def quality_options(cls):
        """
        Returns string 
        """
        for i, value in enumerate(cls.QUALITIES):
            print(f'{i+1}) {value}')
        return cls.QUALITIES[ int( input() ) -1 ]   

    @classmethod
    def sleep_menu(cls):
        """
        Returns a Rest object
        """
        print("\nCollecting data about last night's sleep\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        sleep_location = input("\nWhere did you sleep?\n").capitalize()
        start_time = input("\nAbout when did you fall asleep last night?\n")  # NEED TO MAKE TIME OBJECT

        sleep_interuptions = int( input("\nHow many times were you woken up?\n") )
        
        print("\nHow well did you sleep?")
        sleep_quality = cls.quality_options()

        end_time = input("\nWhat time did you wake up this morning?\n") # NEED TO MAKE TIME OBJECT

        return Rest("Sleep", start_time, end_time, sleep_quality, sleep_location, sleep_interuptions)

    @classmethod
    def habit_menu(cls):
        """
        Returns a list of Habit objects or an empty list
        """
        print("\nCollecting data about today's Tobacco and Alcohol use\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        habit_list = list()
        for element in [("Tobacco", "cigs"), ("Alcohol", "drinks")]:
            response = input(f"\nDid you use {element[0]} today? (Y/N)\n").capitalize()

            if (response == "Y" or response == "Yes"):
                occured = int( input(f"\nWhat time did the {element[0]} use start?\n") )   # NEED TO MAKE  TIME OBJECT
                use_location = input(f"\nWhere did the {element[0]} use occur?\n").capitalize()
                amount = int( input(f"\nAmount of {element[1]}: ") )
                print(f"\nHow do you feel about the {element[0]} use?")
                use_quality = cls.quality_options()

                habit_list.append(Habit(f"{element[0]} Use", occured, use_quality, use_location, amount))

        return habit_list

    @classmethod
    def exercise_menu(cls):
        """
        Returns a list of Exercise objects or an empty list
        """
        print("Collecting data about today's Exercise\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        exercises = list()
        
        response = input("Did you exercise today? (Y/N)\n").capitalize()
        
        while (response == "Yes" or response == "Y"):
            exercises.append(cls.create_exercise())
            response = input("\nAdd another exercise for today? (Y/N)\n").capitalize()
        
        return exercises
        
    @classmethod
    def create_exercise(cls):
        """
        Returns an Exercise objects
        """
        print("Which exercise did you perform?")
        for i, value in enumerate(cls.exercise_list):
            print(f'{i+1}) {value}')
        exercise_name = cls.exercise_list[ int( input() ) -1 ]
        
        # if "Other", prompt user to input new exercise name
        if exercise_name == "Other":
            exercise_name = input("\nAwesome, you did something new! What exercise did you do?\n").capitalize()
        
        exercise_location = input(f"\nWhere did '{exercise_name}' occur?\n").capitalize()
        exercise_start = input(f"\nWhat time of day did '{exercise_name}' begin?\n")  # TIME!
        exercise_end = input(f"\nWhat time of day did '{exercise_name}' end?\n")  # TIME!
        exercise_intensity = input(f"\nOn a scale from 1-5, 5 being the greatest, how intense was '{exercise_name}'?\n")
        
        print(f"\nHow do you feel about today's '{exercise_name}'?")
        exercise_quality = cls.quality_options()

        return Exercise(exercise_name, exercise_start, exercise_end, exercise_quality, exercise_location, exercise_intensity)


