import pandas as pd
import os

# Credit Colors & Fonts for the Color Pallets used
class Colors:

    def __init__(self, path=os.getenv('LOCALAPPDATA') + '/XPlus Games/CodeRandom3/'):
        self.path = path
        self.color_dict = pd.read_csv(path + 'color_dict.csv', index_col=0, header=None).to_dict()

    def GetColors(self):
        df = pd.read_csv(self.path + 'color_dict.csv', index_col=0, header=None)
        color_list = df.values.tolist()
        color_dict = {}
        for i in range(len(color_list)):
            color_dict[df.index.values.tolist()[i]] = color_list[i]

        return color_dict
