
import wx
import warnings

hr_app = wx.App(False)
stub_win = wx.Frame(None, -1, "")

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    wx.InitAllImageHandlers()
