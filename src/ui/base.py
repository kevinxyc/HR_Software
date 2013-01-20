## @package base
#  UI subsystem base.
#  This module exports a symbol called ui that is a Window
#  @see Window

import wx
import defs as HRP
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
        self._navbtns = []
        self._pidx = -1

        h0 = wx.BoxSizer(wx.HORIZONTAL)
        v1 = wx.BoxSizer(wx.VERTICAL)
        v1v0 = wx.BoxSizer(wx.VERTICAL)

        #Quick function switcher + Helper board
        self._vmenu = wx.Panel(self, -1)
        vmenusize = (HRP.VMENU_COL_WIDTH*HRP.VMENU_COL_COUNT,-1)
        self._vmenu.SetMinSize(vmenusize)
        self._vmenu.SetMaxSize(vmenusize)
        self._vmenu._sizer = wx.GridSizer(0, HRP.VMENU_COL_COUNT, 0, 0)
        self._vmenu.SetSizer(self._vmenu._sizer)
        h0.Add(self._vmenu, 0, wx.ALIGN_LEFT | wx.EXPAND)

        #Top panel board + Bottom terminal
        self._term = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE | wx.TE_AUTO_URL | wx.TE_RICH | wx.TE_CHARWRAP | wx.TE_READONLY)
        self._term.SetMinSize((-1,HRP.TERM_HEIGHT))
        v1.Add(v1v0, 1, wx.EXPAND | wx.ALIGN_TOP)
        v1.Add(self._term, 0.3, wx.EXPAND | wx.ALIGN_BOTTOM)
        h0.Add(v1, 1, wx.EXPAND | wx.ALIGN_RIGHT)

        #Create log
        self._log = wx.LogTextCtrl(self._term)
        self._log.write = self._log.LogText
        
        self._sizer = v1v0
        self.SetSizer(h0)

        #Menubar at top of program Window
        self._menu = wx.MenuBar()
        mfile = wx.Menu()
        self._menu.Append(mfile, "&File")
        self.SetMenuBar(self._menu)

    def OnResize(self, e):
        """
        @brief 
        @param e The SizeEvent
        """
        pass

    def GetStdOut(self):
        """
        @brief Gets an object that outputs text to someplace in the Window
        @return Object with write() method
        """
        return self._log

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
        import os
        img = wx.Image(os.sep.join([".", "icons", p.get_slug()+".png"]), wx.BITMAP_TYPE_PNG).Scale(40, 40, wx.IMAGE_QUALITY_HIGH).ConvertToBitmap()
        b = wx.BitmapButton(self._vmenu, -1, img, style=0)
        b.SetBackgroundColour(self._vmenu.GetBackgroundColour())
        win = self
        b.Bind(wx.EVT_BUTTON, lambda e: win.show(p))
        self._vmenu._sizer.Add(b, 0)

        self._sizer.Insert(0, p, 1, wx.ALIGN_LEFT | wx.EXPAND)
        self._panes.append(p)
        self._navbtns.append(b)
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
        pids = map(lambda p: p.GetId(), self._panes)
        if type(p) == int and p not in pids :
            return
        if p.GetId() not in pids:
            return
        
        self.Freeze()
        if self._pidx >= 0:
            self._panes[self._pidx].Hide()
        p.Show()
        self.Layout()
        self.Thaw()
        
        self._pidx = pids.index(p.GetId())
        


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
