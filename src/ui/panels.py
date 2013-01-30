## @package panels
#  UI subsystem panel collection.
#  This module contains all the different types of panel layouts used in the program.
#  @see Panel

import wx
from base import *
from inputs import *

class Panel(Box, wx.Panel):
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
    
    def __init__(self, slug, **kwargs):
        """
        @param slug The unique slug assigned to this panel (Alternatively, a numeric ID may be used)
        @param parent The container of the Panel
        @param style The Panel style
        """
        Box.__init__(self)
        wx.Panel.__init__(self, parent=kwargs.get('parent', stub_win));
        self._slug = slug
        self.mode = 0
        self.zindex = 0
        self.style = kwargs.get('style', 0)
        self._parent = kwargs.get('parent', None)

    def set_parent(self, p):
        if self._parent == None or self.GetParent().GetId() != self._parent.GetId():
            self.Reparent(self, p)
        self._parent = p

    def get_slug(self):
        return self._slug.lower()
    
    def focus(self):
        """
        @brief Focus on the panel (brings parents into focus also). The parent must be already set.
        @return void
        """
        self.parent.show_panel(self)

        
class TextPanel(Panel):
    """
    A panel that contains only a scrollable label that can display a text passage
    of any length.
    This particular panel is static and will ignore all requests to add/remove boxes
    """

    def __init__(self, slug, text, **kwargs):
        """
        @note ...
        """
        Panel.__init__(self, slug, **kwargs)
        v0 = wx.BoxSizer(wx.VERTICAL)
        self._disp = wx.TextCtrl(self, -1, style=wx.TE_READONLY | wx.TE_MULTILINE | wx.TE_AUTO_URL | wx.TE_NOHIDESEL)
        self._disp.SetBackgroundColour(self.GetBackgroundColour())
        self.set_text(text)
        v0.Add(self._disp, 1, wx.EXPAND)
        self.SetSizer(v0)

        
    def set_text(self, text):
        """
        @param text The text to display on the main display label
        """
        self._disp.SetValue(text)


class InputPanel(Panel):
    """
    This panel process an Element list and dynamically create and place
    an Input list on itself.
    """

    def __init__(self, slug, **kwargs):
        """
        @param slug @see Panel
        """
        Panel.__init__(self, slug, **kwargs)
        self._cb = kwargs.get('callback', kwargs.get('cb', lambda vals: None))
        self._list = []

        t = wx.BoxSizer(wx.HORIZONTAL)
        self._sizer = wx.GridBagSizer(vgap=0, hgap=0)
        self._sizer.SetFlexibleDirection(wx.BOTH)
        t.Add(self._sizer, 1, wx.EXPAND)
        self.SetSizer(t)
        
    def _push_err_msg(self, msg):
        pass
    
    def _find_pos(self, i):
        #Find the row that the iTH item is on
        r, t, n = (0,0,0)
        for k in xrange(0, i+1, 1):
            x = self._list[k]
            #If next item goes on the next row
            if float(t+x.ratio) > int(r):
                r = r + 1 #Move to next row
                t = r - 1 #Add padding because the next item won't fit in space left
                n = k     #Record the first item on the row
            t = t + x.ratio
        r = r - 1
        #Row int(r) contains items n -> i
        c = sum(map(lambda x: int(float(x.ratio)/float(0.05)), self._list[n:i]))
        return (int(r), c)

    def insert_element(self, i, x):
        """
        @param x The Element being added
        """

        def set_element_val(e, val):
            e.value = val
            r = self._cb(e, val)
            if not (type(r) == bool and r == True):
                self._push_err_msg(r)
                return False
            else:
                return True
            
        ctrl = create_input(self, x)
        ctrl.add_cb(lambda val: set_element_val(x,val))
        x._ctrl = ctrl
        
        self._list.insert(i, x)
        
        p, sp = ( self._find_pos(i), (1,int(float(x.ratio)/float(0.05))) )
        if not self._sizer.CheckForIntersectionPos(p,sp):
            self._sizer.Add(ctrl, pos=p, span=sp, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.EXPAND )
        else:
            print "OVERLAP"

    def add_element(self, x):
        """
        @param x The Element being added
        """
        return self.insert_element(len(self._list), x)

    def rm_element(self, x):
        """
        @param x The Element or the index of the Element to remove
        @retval Boolean success/fail
        """
        i = x if type(x)==int else self._list.index(x)
        if i < 0:
            return False
        ctrl = self.pop(i)._ctrl
        self._list.Detach(ctrl)
        ctrl.Destroy()
        return True

    def get_values(self):
        """
        @brief Returns the Element list contained in this panel with its value(s) modified.
        """
        return self._list
