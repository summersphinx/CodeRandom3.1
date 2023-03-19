import cr3
import PySimpleGUI as sg
from time import sleep

color = cr3.Colors.GetColors()

for each in color.keys():
    pass
    # print(each)

new_theme = cr3.Colors.MakeTheme('Rose')
print()
print(new_theme, '\n\n\n\n')

sg.LOOK_AND_FEEL_TABLE['THEME'] = new_theme

sg.theme("THEME")
sg.test()
