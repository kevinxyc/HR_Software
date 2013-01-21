
import wx
import warnings

hr_app = wx.App(False)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    wx.InitAllImageHandlers()
