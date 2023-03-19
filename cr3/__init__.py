import pandas as pd
import os


# Credit Colors & Fonts for the Color Pallets used
class Colors:
    path = os.getenv('LOCALAPPDATA') + '/XPlus Games/CodeRandom3/'
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


