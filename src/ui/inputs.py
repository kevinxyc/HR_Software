## @package inputs
#  UI subsystem input collection.
#  This module contains all the different types of input used in the program.
#  @see Input

class Input(Box):
    """
    An Input object is the actual display wrapped around a piece of information (Element) and is
    a box that can be displayed on screen.
    @see Element
    """
    
    ##@var type
    # int - Type of input
    
    def __init__(self):
        self.type = 0

    def createElement(self):
        """
        @brief Create a data element from the input box
        @return Element - The element representation of the input
        """
        pass

    def focus(self):
        """
        @brief Focus on the input box (this will also focus/show all its parents)
        @return void
        """
        pass

    def value(self):
        """
        @brief Get the current value of the input box
        @return mixed
        """
        pass
