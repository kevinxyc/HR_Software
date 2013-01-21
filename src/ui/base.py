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

class Popup(wx.Frame,Box):
    """
    A popup window
    """
    def __init__(self, parent, title, **args):
        wx.Frame.__init__(self, parent, -1, title, **args)
        self._sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(self._sizer)

    def show_panel(self, p):
        p.Reparent(self)
        p.Show()
        self._sizer.Clear(False)
        self._sizer.Add(p, 1, wx.EXPAND)
        self.Layout()


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
        h0.Add(self._vmenu, 0, wx.ALIGN_LEFT)

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

        self.SetBackgroundColour(self._vmenu.GetBackgroundColour())
        self.SetMinSize((600,400))
        self.Fit()

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

    def popup(self, p, title):
        """
        @brief Creates a popup frame with the given panel and title
        @param p The panel to show on this frame
        @param title The string title to use
        @note If the panel is already added onto the current window, then it will
              be temporary removed and restored when the popup is closed
        @return None
        """
        d = Popup(self, title)
        idx = self.has_panel(p)
        if self.has_panel(p):
            self.rm_panel(p)
            win = self
            d.Bind(wx.EVT_CLOSE, lambda e: d.Destroy() and win.insert_panel(idx, p))
        d.show_panel(p)
        d.Show()

    def dialog(self, t, **args):
        """    
        mixed dialoge(String msg, int type)
        Creates a dialoge box of a given type with the given message.
        @param msg The message to display
        @param t A string describing the type of dialog
        @return The response given (depends on type) or None if failed
        """
        dtype = t+"Dialog"
        res = None
        if hasattr(wx, dtype):
            if 'caption' not in args:
                args['caption'] = args['message']
            cls = getattr(wx, dtype)
            dlg = cls(self, **args)
            res = dlg.ShowModal()
            if  res == wx.ID_OK:
                resf = ['GetValue', 'GetFilenames', 'GetPath', 'GetData', 'GetSelections', 'GetStringSelection']
                for f in resf:
                    if hasattr(dlg, f):
                        res = getattr(dlg, f)()
                        break
            else:
                resn = { wx.ID_OK:"OK", wx.ID_NO:"NO", wx.ID_YES:"YES", wx.ID_CANCEL:"CANCEL" }
                if res in resn:
                    res = resn[res]
                else:
                    res = None
            dlg.Destroy()
        return res


    def has_panel(self, p, pids=[]):
        """
        @brief Checks if the panel given is within the panel list
        @param p The panel ID/object ref
        @return index of panel in the list or -1 if not found
        """
        pids.extend(map(lambda p: p.GetId(), self._panes))
        if type(p) == int and p not in pids :
            return -1
        if p.GetId() not in pids:
            return -1
        return pids.index(p.GetId())


    def add_panel(self, p, show=False):
        """
        @brief Adds panel to the panel list. Only one panel may be displayed at a time.
        @param p The panel ID/object ref
        @return Boolean indicating success
        """        
        return self.insert_panel(len(self._panes), p, show)        
    
    def insert_panel(self, pos, p, show=False):
        """
        @brief Inserts panel intto the panel list. Only one panel may be displayed at a time.
        @param p The panel ID/object ref
        @return Boolean indicating success
        """
        import os

        if p.GetParent().GetId() != self.GetId():
            p.Reparent(self)

        w = HRP.VMENU_COL_WIDTH
        img = wx.Image(os.sep.join([".", "icons", p.get_slug()+".png"]), wx.BITMAP_TYPE_PNG).Scale(w, w, wx.IMAGE_QUALITY_HIGH).ConvertToBitmap()
        b = wx.BitmapButton(self._vmenu, -1, img, style=wx.NO_BORDER)
        b.SetBackgroundColour(self._vmenu.GetBackgroundColour())
        win = self
        b.Bind(wx.EVT_BUTTON, lambda e: win.show_panel(p))
        self._vmenu._sizer.Insert(pos, b, 0)

        if pos <= self._pidx:
            self._pidx = self._pidx + 1
        
        self._sizer.Insert(pos, p, 1, wx.ALIGN_LEFT | wx.EXPAND)
        self._panes.insert(pos, p)
        self._navbtns.insert(pos, b)

        if show:
            self.show_panel(p)
        else:
            p.Hide()
        self.Layout()

        return True
    
    def rm_panel(self, p):
        """
        @brief Removes a panel from the list. Only one panel may be displayed at a time.
        @param p The panel ID/object ref
        @return Boolean indicating success (False if the panel was not added in the first place)
        """
        idx = self.has_panel(p)
        if self._pidx == idx:
            if idx > 0:
                self.show_panel(self._panes[idx-1])
            else:
                self._pidx = -1

        if self._pidx > idx:
            self._pidx = self._pidx - 1

        if idx >= 0:
            self.Freeze()
            b = self._navbtns.pop(idx)
            p = self._panes.pop(idx)
            self._sizer.Detach(p)
            self._vmenu._sizer.Detach(b)
            b.Destroy()
            self.Layout()
            self.Thaw()
            return True
        else:
            return False
        

    def show_panel(self, p):
        """
        @brief Show the panel given on the main display section
        @param p The panel ID/object ref
        @return Boolean indicating success
        """
        pids = []
        if self.has_panel(p, pids) < 0:
            return False
                    
        self.Freeze()
        if self._pidx >= 0:
            self._panes[self._pidx].Hide()
            self._navbtns[self._pidx].SetBackgroundColour(self._vmenu.GetBackgroundColour())
        p.Show()
        self._sizer.Layout()
        self.Thaw()
        
        self._pidx = pids.index(p.GetId())
        self._navbtns[self._pidx].SetBackgroundColour(HRP.VMENU_SELECTED_COLOUR)
        return True
