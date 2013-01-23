import sys
import ui.all as ui
import defs as HRP

win = ui.Window(HRP.WIN_TITLE)
#sys.stdout = win.GetStdOut()
tpane = ui.TextPanel(win, "text_1", "INTRO TO PROGRAM AAAAAAAAAAAAA"+"...... "*100)
ttpane = ui.TextPanel(win, "text_2", "PANEL II")
tttpane = ui.TextPanel(win, "text_2", "PANEL III")
win.add_panel(tpane)
win.add_panel(ttpane)
win.show_panel(tpane)
win.show_panel(ttpane)
win.add_panel(tttpane,True)
epane = ui.ElementsPanel(win, "search")
x = ui.Element()
x.value = "HELLO"
x.type = "text"
x.ratio = 0.5
epane.add_element(x)
win.add_panel(epane, True)
ui.launch_win(win)
