import os
import wget

current_dir = os.getcwd()

files = [
    'color_dict.csv',
    'settings.csv',
    'fonts/Nunito.ttf',
    'fonts/SourceSansPro.ttf',
    'img/Clock_Black.png',
    'img/Clock_White.png',
    'modes/1 - Tutorial/data.csv',
    'modes/1 - Tutorial/Demo.txt',
    'modes/1 - Tutorial/Intro.txt',
    'modes/2 - Standard/stuff.txt',
    'bugsplat-brand.png',
    'bugsplat.ico',
    'audio/music/a.mp3',
    'audio/music/b.mp3',
    'audio/music/c.mp3',
    'audio/music/d.mp3',
    'audio/music/e.mp3',
    'audio/music/f.mp3',
    'audio/music/g.mp3',
]
if os.path.exists(os.getenv('LOCALAPPDATA') + '/XPlus Games/CodeRandom3'):
    os.chdir(os.getenv('LOCALAPPDATA') + '/XPlus Games/CodeRandom3')
else:
    os.makedirs(os.getenv('LOCALAPPDATA') + '/XPlus Games/CodeRandom3')
    os.chdir(os.getenv('LOCALAPPDATA') + '/XPlus Games/CodeRandom3')


for file in files:
    if '/' in file:
        if not os.path.exists(file[:file.rindex('/')]):
            os.makedirs(file[:file.rindex('/')])
    if not os.path.exists(file):
        print(file)
        wget.download(f'https://raw.github.com/summersphinx/cr3.1-stuff/main/{file}', file)
if not os.path.exists('saves'):
    os.makedirs('saves')
os.chdir(current_dir)
