## @package panels
#  UI subsystem panel collection.
#  This module contains all the different types of panel layouts used in the program.
#  @see Panel

import wx
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
    
    def __init__(self, parent, slug, **args):
        """
        @param parent The container of the Panel
        """
        #(id)
        wx.Panel.__init__(self, parent=parent);
        self.mode = 0
        self.zindex = 0
        self.style = 0 if 'style' not in args else args['style']
        self._slug = slug
        self._parent = parent

    def addBox(self, b, x, y):
        """
        @brief Add a box to the panel
        @param b The box to add
        @param x Suggested X position 
        @param y Suggested Y position
        @return int - sucess/fail
        """
        pass

    def get_slug(self):
        return self._slug.lower()

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


class TextPanel(Panel):
    """
    A panel that contains only a scrollable label that can display a text passage
    of any length.
    """

    def __init__(self, parent, slug, text):
        """
        @note ...
        """
        Panel.__init__(self, parent, slug)
        v0 = wx.BoxSizer(wx.VERTICAL)
        self._disp = wx.TextCtrl(self, -1, style=wx.TE_READONLY | wx.TE_MULTILINE | wx.TE_AUTO_URL | wx.TE_NOHIDESEL)
        self._disp.SetBackgroundColour(self.GetBackgroundColour())
        self.setText(text)
        v0.Add(self._disp, 1, wx.EXPAND)
        self.SetSizer(v0)

        
    def setText(self, text):
        """
        @param text The text to display on the main display label
        """
        self._disp.SetValue(text)
