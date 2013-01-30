## @package inputs
#  UI subsystem input collection.
#  This module contains all the different types of input used in the program.
#  @see Input

import wx

from base import *

def create_input(p, x):
    t = x.type.lower().replace(' ','')
    #General ctrls with no special parameters/formatting
    g = wxInput(x, parent=p)
    if t is "text":
        g.set_ctrl(wx.TextCtrl(g))
    else:
        #If no control matches, then throw in a general textbox
        g.set_ctrl(wx.TextCtrl(g))
    return g

class Input(Box, wx.Panel):
    """
    An Input object is the actual display wrapped around a piece of information (Element) and is
    a box that can be displayed on screen.
    @see Element
    """
    
    def __init__(self, element, **kwargs):
        Box.__init__(self)
        wx.Panel.__init__(self, kwargs.get('parent', stub_win), -1)
        self._cblist = []
        self._element = element

    def create_element(self):
        """
        @brief Create a data element from the input box
        @return Element - The element representation of the input
        """
        import copy
        return copy.deepcopy(self._element)

    def add_cb(self, cb):
        """
        @brief Adds a callback function for processing value changes
        @param cb The function should take one paramter - The string representation of the value. If a False value is returned then it is considered
        an error
        """
        self._cblist.append(cb)

    def rm_cb(self, cb):
        """
        @brief Removes the callback from the calllist
        """
        #@TODO Confirm this works for lambdas and closures
        self._cblist.remove(cb)
    
    def _invoke_all_cb(self, value):
        """
        @brief Invokes all callbacks and return False if any is False
        """
        self._element.value = value
        return all(map(lambda cb: cb(value), self._cblist))

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

class wxInput(Input):
    """
    A basic label and wrapper around wxCtrls
    """
    def __init__(self, x, **kwargs):
        Input.__init__(self, x, **kwargs)

        lbl = wx.StaticText(self, -1, x.desc)
        self._ctrl = kwargs.get("ctrl", None)
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self._sizer.Add(lbl, wx.ALIGN_TOP)
        self.SetSizer(self._sizer)
        self.set_ctrl(self._ctrl)
        
    def set_ctrl(self, ctrl):
        if ctrl is not None:
            if ctrl.GetParent().GetId() != self.GetId():
                ctrl.Reparent(self)
            if self._ctrl is not None:
                self._sizer.Detach(self._ctrl)
            self._sizer.Add(ctrl, wx.ALIGN_BOTTOM | wx.EXPAND | wx.ALL)
            self._ctrl = ctrl

class ImageInput(Input):
    """

    """
    def __init__(self, x):
        Input.__init__(self, x)
        if len(x.value) > 0:
            self._img = wx.Image(x.value, wx.BITMAP_TYPE_PNG).Scale(w, w, wx.IMAGE_QUALITY_HIGH).ConvertToBitmap()
