import pandas as pd
import os
import PySimpleGUI as sg
from cr3.tab import tab_group
# from cr3.buggy import log

path = os.getenv('LOCALAPPDATA') + '/XPlus Games/CodeRandom3/'

class Settings:

    def __init__(self):
        settings_dict = pd.read_csv(path + 'settings.csv', index_col=0, header=None).to_dict()[1]
        print(settings_dict)
        self.theme = settings_dict['theme']
        self.darkness = settings_dict['dark mode'] == 'True'
        self.font_a = settings_dict['font a']
        self.font_b = settings_dict['font b']
        self.music_vol = float(settings_dict['music vol'])
        self.music = settings_dict['music'] == 'True'
        self.voice_vol = float(settings_dict['voice vol'])
        self.voice = settings_dict['voice']
        self.sfx_vol = float(settings_dict['sfx vol'])
        self.sfx = settings_dict['sfx'] == 'True'

    def save(self, to_change,  new_value):
        settings_dict = pd.read_csv(path + 'settings.csv', index_col=0, header=None).to_dict()[1]
        settings_dict[to_change] = new_value
        print(type(settings_dict))
        test = pd.DataFrame.from_dict(settings_dict, orient='index').to_csv(path + 'settings.csv')
        print(test)

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
        print(colors)

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
        [sg.Button('Tab', k='tabgroup', expand_x=True)],
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

    installed_fonts = sg.Text.fonts_installed_list()
    installed_fonts.extend(['Nunito', 'Source Sans Pro Light'])
    installed_fonts.sort()

    settings_fonts = [
        [sg.Text('Custom fonts provided by Google Fonts')],
        [sg.InputCombo(installed_fonts, expand_x=True, pad=(50, 10), default_value=sett.font_a, k='font a')],
        [sg.InputCombo(installed_fonts, expand_x=True, pad=(50, 10), default_value=sett.font_b, k='font b')]
    ]

    settings_music = [
        [sg.Slider([0, 1], default_value=sett.music_vol, orientation='h', resolution=0.01, expand_x=True, pad = (50, 10), k='music vol')],
        [sg.Checkbox('Mute', k='music', default=sett.music)]
    ]

    settings_sfx = [
        [sg.Slider([0, 1], default_value=sett.sfx_vol, orientation='h', resolution=0.01, expand_x=True, pad=(50, 10),
                   k='sfx vol')],
        [sg.Checkbox('Mute', k='sfx', default=sett.sfx)]
    ]

    settings_voice = [
        [sg.InputOptionMenu(['Robot', 'Off'], expand_x=True, pad=(30, 10), default_value=sett.voice,
                            k='voice', disabled=True)],
        [sg.Slider([0, 1], default_value=sett.voice_vol, orientation='h', resolution=0.01, expand_x=True, pad = (50, 10), k='voice vol', disabled=True)]
    ]

    settings = [
        [sg.Column(
                [
                    [sg.Frame('Theme', settings_theme, font=(sett.font_b + ' bold', 16), expand_x=True)],
                    [sg.Frame('Font', settings_fonts, font=(sett.font_b + ' bold', 16), expand_x=True)],
                    [sg.Frame('Music', settings_music, font=(sett.font_b + ' bold', 16), expand_x=True)],
                    [sg.Frame('Sound Effects', settings_sfx, font=(sett.font_b + ' bold', 16), expand_x=True)],
                    [sg.Frame('Speech [WIP]', settings_voice, font=(sett.font_b + ' bold', 16), expand_x=True)],
                ],
                scrollable=True,
                vertical_scroll_only=True,
                expand_y=True,
                expand_x=True
        )],
        [sg.Button('Save', k='save settings')]
    ]

    credits = [
        [sg.Text('My many thanks to the talented people who created the assets I used\n to make this game happen and add extra flare.', font=(sett.font_b, 20))],
        [sg.Text('Music', font=(sett.font_a, 18))],
        [sg.Text('LudoLoon Studio', font=(sett.font_b, 16)), sg.Button('url', k='cred1', font=(sett.font_b, 16))],
        [sg.Text('Aekseer', font=(sett.font_b, 16)), sg.Button('url', k='cred2', font=(sett.font_b, 16))],
        [sg.Text('Nathan Gibson', font=(sett.font_b, 16)), sg.Button('url', k='cred3', font=(sett.font_b, 16))],
    ]

    layout_left = [
        [
            sg.Frame('M\ne\nn\nu', menu, title_location='wn', vertical_alignment='c', element_justification='center', font=(sett.font_b + ' bold', 16)),
            sg.Frame('Pick Mode', start, expand_x=True, expand_y=True, visible=False, k='new1', font=(sett.font_b + ' bold', 16)),
            sg.Frame('Pick Save', cont, expand_x=True, expand_y=True, visible=False, k='cont1', font=(sett.font_b + ' bold', 16)),
            sg.Frame('Settings', settings, expand_x=True, expand_y=True, visible=False, k='settings1', font=(sett.font_b + ' bold', 16)),
            sg.Frame('Credits', credits, expand_x=True, expand_y=True, visible=False, k='credits1', font=(sett.font_b + ' bold', 16))
        ]
    ]

    layout = [
        [
            sg.Column(layout_left, expand_y=True, expand_x=True, k='side left'),
            # sg.Column([[tab_group()]], expand_x=True, expand_y=True, visible=True, k='tabgroup1')
        ]
    ]

    return layout