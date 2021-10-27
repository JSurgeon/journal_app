# file containing journal class
from j_node import Node


class Journal():
    """
    Journal is a base class, responsible for CRUD operations of the entire collection of 
    entries and the interface the user interacts with 
    """
    def __init__(self, filename):
        # Initialization needs to read in a file, store the contents using 
        # the Node class
        self._head = Node()
        


