from base import *

class Panel(wx.Panel,Box):
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
    
    def __init__(self, parent, style):
        """
        @param parent The container of the Panel
        """
        #(id)
        wx.Panel.__init__(self, parent=parent);
        self.mode = 0
        self.zindex = 0
        self.style = style

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
        @param b The box ID/object ref to remove
        @return int - success/fail
        """
        pass

    def focus(self):
        """
        @brief Focus on the panel (brings parents into focus also)
        @return void
        """
