import sys
import ui.all as ui
import defs as HRP

win = ui.Window(HRP.WIN_TITLE)
#sys.stdout = win.GetStdOut()
tpane = ui.TextPanel(win, "text_1", "INTRO TO PROGRAM AAAAAAAAAAAAA"+"...... "*100)
ttpane = ui.TextPanel(win, "text_2", "PANEL II")
win.addPane(tpane)
win.addPane(ttpane)
win.show(tpane)
ui.launch_win(win)
