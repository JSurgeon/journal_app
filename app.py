from journal import Journal, Entry
FILENAME = "journal.csv"
# Welcome user
print("Welcome to the Journaling application!")

journal_obj = Journal.read(FILENAME)

response = input("\nWould you like to add a new entry? (y/n)\n")
while (response.capitalize() != 'N') and (response.capitalize() != "Y"):
    response = input("\nUnacceptable response, please respond with 'y' to add a new entry or 'n' not to:\n")

while response.capitalize() == 'Y':
    
    journal_obj.add_entry()
    

    response = input("\nWould you like to add another entry?")

    while (response.capitalize() != 'N') and (response.capitalize() != "Y"):
        response = input("Unacceptable response, please respond with 'y' to add a new entry or 'n' not to:\n")

# write out to file
journal_obj.write(FILENAME)
print(journal_obj)