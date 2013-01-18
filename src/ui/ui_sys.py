## @package ui_sys
#  UI subsystem.
#  This module exports a symbol called ui that is a Window
#  @see Window


class Box(Object):
    """
    A Box is the base unit of display
    In accordance with the box model, a box can be layered and positioned
    in horizontal/vertically on a display.
    """

    ##@var x
    # X cordinate of box

    ##@var y
    # Y cordinate of box

    ##@var w
    # Width of box

    ##@var h
    # Height of box

    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0        

    def draw(self, container):
        """    
        void draw(Box container)
        @param container Draws box within the container. If container is none, then the box is simply redrawn.
        """        
        pass
    

class Window(Box):
    """
    A Window is a special box at the top level    
    """            

    def style(self, style):
        """
        @brief Sets the style of the Window
        @param style An int to give the window a certain style
        @return void
        """
        pass


    def dialoge(self, msg, type):
        """    
        mixed dialoge(String msg, int type)
        Creates a dialoge box of a given type with the given message.
        @param msg The message to display
        @param type
        @return The response given (depends on type)
        """        
        pass

    def addPane(self, p):
        """
        void addPane(Panel p)
        Adds panel to panel layer. Only one panel may be displayed at a time.
        @param p The panel ID/Object ref
        @return None
        """        
        pass

    
    def rmPane(self, p):
        """
        void rmPane(Panel p)
        Removes a panel layer. Only one panel may be displayed at a time.
        @param p The panel ID/Object ref
        @return None
        """        
        pass
    
    def show(self, p):
        """
        void show(Panel p)
        Show the panel given
        @param p The panel ID/Object ref
        @return None
        """
        pass
    
    def dispatch_event(self, block):
        """    
        void dispatch_event(int block)
        The main event loop for this Window. The window will recieve events/dispatch it
        in this loop. Calling this function does one iteration of this task.
        @param block If false and no events need dispatching, then the function returns immediately.
        @return None
        """        
        pass


class Panel(Box):
    """
    A Panel object is a display layer or "page" that contains an assortment of children elements
    and boxen
    """
    
    ##@var mode
    # int - Current state: Hidden(0), Showing(1)

    ##@var zindex
    # int - The stack priority in the box model

    ##@var style
    # int - Style for the panel
    
    def __init__(self):
        self.mode = 0
        self.zindex = 0
        self.style = 0

    def addBox(self, b, x, y):
        """
        @brief Add a box to the panel
        @param b The box to add
        @param x Suggested X position 
        @param y Suggested Y position
        @return int - sucess/fail
        """
        pass

    def rmBox(self, b):
        """
        @brief Remove the given box from the panel
        @param b The box ID/Object ref to remove
        @return int - success/fail
        """
        pass

    def focus(self):
        """
        @brief Focus on the panel (brings parents into focus also)
        @return void
        """

class Element(Object):
    """
    An Element object represents a piece of information to be displayed on screen.
    """

    ##@var type
    # int - Type of data

    ##@var value
    # mixed - Value of data

    ##@var ord
    # int - Order of data (Where the data belongs on the list)

    def __init__(self):
        self.type = 0
        self.value = 0
        self.ord = 0

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
