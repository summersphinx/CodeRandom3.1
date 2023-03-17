import logzero
import os
from bugsplat import BugSplat
import datetime
import PySimpleGUI as sg

if not os.path.exists(f'{os.getenv("LOCALAPPDATA")}/XPlus Games/CodeRandom3'):
    os.makedirs(f'{os.getenv("LOCALAPPDATA")}/XPlus Games/CodeRandom3', True)


t = str(datetime.datetime.now()).replace(':', '_')
log_name = f'{os.getenv("LOCALAPPDATA")}/XPlus Games/CodeRandom3/{t} - log.log'
print(log_name)

with open(log_name, 'x') as fh:
    pass
log = logzero.setup_logger(name='Logger', logfile=log_name)

log.info('Buggy Loaded')


class Splat:

    layout = [
        [sg.Text(
            'An error has occurred. If you wish to help this game be better, then feel free to submit the bug below.')],
        [sg.Frame('Error:', [
            [sg.Multiline('', disabled=True, k='error')]
        ])],
        [sg.Text('Email'), sg.Input('', tooltip='Your email address. This is if I need to reach you.', k='email')],
        [sg.Checkbox('Send bug report', k='send'), sg.Checkbox('Restart Game', k='restart')]
    ]

    erwn = sg.Window('Uh Oh!', layout)
    event, values = erwn.read(close=True)

    def __init__(self, exception):
        email = 'summersphinx@duck.com'
        bugsplat = BugSplat('CodeRandom3', 'CodeRandom3.1', '0.1.1')
        bugsplat.post(exception, app_key='app_key', email=email)


try:
    print('This will not work' + 7)
except Exception as e:
    Splat(e)
