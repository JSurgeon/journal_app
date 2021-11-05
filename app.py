from journal import Journal

# # read in file 
file_csv = "journal.csv"

journal = Journal().read(file_csv)

journal.write("journal.csv")


