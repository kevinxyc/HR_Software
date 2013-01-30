import sys
import ui.all as ui
import defs as HRP

win = ui.Window(HRP.WIN_TITLE)

#Test logger
sys.stdout = win.GetStdOut()

#Create some dummy panels
tpane = ui.TextPanel("text_1", "INTRO TO PROGRAM AAAAAAAAAAAAA"+"...... "*100, parent=win)
ttpane = ui.TextPanel("text_2", "PANEL II", parent=win)
tttpane = ui.TextPanel("text_2", "PANEL III", parent=win)

#Try flipping between panels
win.add_panel(tpane)
win.add_panel(ttpane)
win.show_panel(tpane)
win.show_panel(ttpane)
win.add_panel(tttpane,True)

#Test InputPanel
empane = ui.InputPanel("search", parent=win)

#Example data list
em_prof_p = [
    ui.Element(type="text", name="First Name", value="", ratio=0.5),
    ui.Element(type="text", name="Last Name", value="", ratio=0.5),
    ui.Element(type="select", name="Job Title", value="", opts=["Manager", "Associate", "CEO"], ratio=1),
    ui.Element(type="text", name="Phone", value="", ratio=1)
    ]

for x in em_prof_p:
    empane.add_element(x)
win.add_panel(empane, True)

#Show result
ui.launch_win(win)
