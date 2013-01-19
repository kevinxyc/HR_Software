## @package base
#  UI subsystem base.
#  This module exports a symbol called ui that is a Window
#  @see Window


import defs as HRP
import wx
from ui import hr_app

def launch_win(win):
    """    
    The main event loop for this Window. The window will repetitively recieve events/dispatch it
    in this loop.
    @note This function will not return until the current Window is closed
    @param win The main Window to display
    @return None
    """
    global hr_app
    win.Show()
    hr_app.SetTopWindow(win)
    hr_app.MainLoop()



class Box(object):
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
    

class Window(wx.Frame,Box):
    """
    A Window is a special box at the top level    
    """

    def __init__(self, title):
        #(parent, id, title)
        wx.Frame.__init__(self, None, -1, title)
        self._panes = []
        self._sizer = wx.BoxSizer(wx.HORIZONTAL)
        self._pidx = -1

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

    def addPane(self, p, show=True):
        """
        void addPane(Panel p)
        Adds panel to panel layer. Only one panel may be displayed at a time.
        @param p The panel ID/object ref
        @return None
        """
        #(wxWindow, proportion, flag)
        self._sizer.Add(p, 1, wx.EXPAND)
        self._panes.append(p)
        if show:
            self.show(p)
        else:
            p.Hide()

    
    def rmPane(self, p):
        """
        void rmPane(Panel p)
        Removes a panel layer. Only one panel may be displayed at a time.
        @param p The panel ID/object ref
        @return None
        """        
        pass
    
    def show(self, p):
        """
        void show(Panel p)
        Show the panel given
        @param p The panel ID/object ref
        @return None
        """
        pids = map(lambda p: p.GetID(), self._panes)
        if type(p) == int and p not in pids :
            return
        if p.GetID() not in pids:
            return
        
        if self._pidx >= 0:
            self._panes[self._pidx].Hide()
        p.Show()
        self.Layout()

        self._pidx = self._panes.index(p.GetID())
        


class Element(object):
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
