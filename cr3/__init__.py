import pandas as pd
import os
import PySimpleGUI as sg
from cr3.buggy import log

path = os.getenv('LOCALAPPDATA') + '/XPlus Games/CodeRandom3/'

class Settings:

    def __init__(self):
        settings_dict = pd.read_csv(path + 'settings.csv', index_col=0, header=None).to_dict()[1]
        log.info(settings_dict)
        self.theme = settings_dict['theme']
        self.darkness = settings_dict['dark mode'] == 'True'

    def save(self, to_change,  new_value):
        settings_dict = pd.read_csv(path + 'settings.csv', index_col=0, header=None).to_dict()[1]
        settings_dict[to_change] = new_value
        log.debug(type(settings_dict))
        test = pd.DataFrame.from_dict(settings_dict, orient='index').to_csv(path + 'settings.csv')
        log.info(test)

# Credit Colors & Fonts for the Color Pallets used
class Colors:

    color_dict = pd.read_csv(path + 'color_dict.csv', index_col=0, header=None).to_dict()

    @staticmethod
    def GetColors(path=path):
        df = pd.read_csv(path + 'color_dict.csv', index_col=0, header=None)
        color_list = df.values.tolist()
        color_dict = {}
        for i in range(len(color_list)):
            color_dict[df.index.values.tolist()[i]] = color_list[i]

        return color_dict

    @staticmethod
    def MakeTheme(colors, dark_mode=False):
        '''
        "BACKGROUND": "#ffffff",
        "TEXT": "#1a1a1b",
        "INPUT": "#dae0e6",
        "TEXT_INPUT": "TEXT",
        "SCROLL": "#a5a4a4",
        "BUTTON": ("#FFFFFF", "#0079d3")
        '''
        if type(colors) == "<class 'str'>":
            colors = [colors]*6

        color_tree = Colors.GetColors()
        if dark_mode:
            color_tree[colors].reverse()
        log.info(colors)

        theme = {
            'BACKGROUND': color_tree[colors][0],
            'TEXT': color_tree[colors][5],
            'INPUT': color_tree[colors][3],
            'TEXT_INPUT': color_tree[colors][0],
            'SCROLL': color_tree[colors][4],
            'BUTTON': (color_tree[colors][0], color_tree[colors][4]),
            'PROGRESS': (color_tree[colors][3], color_tree[colors][3]),
            'BORDER': 1,
            'SLIDER_DEPTH': 0,
            'PROGRESS_DEPTH': 0
        }
        return theme


def Layouts():
    sg.theme('THEME')
    sett = Settings()

    menu = [
        [sg.Button('Back', k='back', expand_x=True, visible=False)],
        [sg.Button('New Game', k='new', expand_x=True)],
        [sg.Button('Continue', k='cont', expand_x=True)],
        [sg.Button('Docs', k='docs', expand_x=True)],
        [sg.Button('Settings', k='settings', expand_x=True)],
        [sg.Button('Credits', k='credits', expand_x=True)],
        [sg.Button('Discord', k='discord', expand_x=True)],
        [sg.Button('Quit', k='quit', expand_x=True)],
    ]

    start = [
        [sg.Listbox(os.listdir(path+'/modes'), expand_x=True, expand_y=True)],
        [sg.Button('< Start New Game >', k='start new', expand_x=True)]
    ]

    cont = [
        [sg.Listbox(os.listdir(path+'/saves'), expand_x=True, expand_y=True)],
        [sg.Button('< Continue >', k='cont save', expand_x=True)]
    ]

    settings_theme = [
        [sg.InputOptionMenu(Colors.GetColors(path).keys(), expand_x=True, pad=(50, 10), default_value=sett.theme, k='theme')],
        [sg.Checkbox('Dark Mode', k='dark mode', default=sett.darkness)]
    ]

    settings = [
        [sg.Column(
                [
                    [sg.Frame('Theme', settings_theme)]
                ],
                scrollable=True,
                vertical_scroll_only=True,
                expand_y=True,
                expand_x=True
        )],
        [sg.Button('Save', k='save settings')]
    ]

    layout = [
        [sg.Text('CodeRandom3', font='Nunito 24 bold')],
        [
            sg.Frame('M\ne\nn\nu', menu, title_location='wn', vertical_alignment='c', element_justification='center'),
            sg.Frame('Pick Mode', start, expand_x=True, expand_y=True, visible=False, k='new1'),
            sg.Frame('Pick Save', cont, expand_x=True, expand_y=True, visible=False, k='cont1'),
            sg.Frame('Settings', settings, expand_x=True, expand_y=True, visible=False, k='settings1')
        ]
    ]

    return layout
