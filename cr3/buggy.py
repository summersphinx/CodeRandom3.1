import logzero
import os
from bugsplat import BugSplat
import datetime
import PySimpleGUI as sg
import traceback

project_name = 'CodeRandom3'

if not os.path.exists(f'{os.getenv("LOCALAPPDATA")}/XPlus Games/{project_name}/logs'):
    os.makedirs(f'{os.getenv("LOCALAPPDATA")}/XPlus Games/{project_name}/logs', True)


t = str(datetime.datetime.now()).replace(':', '_')
log_name = f'{os.getenv("LOCALAPPDATA")}/XPlus Games/{project_name}/logs/{t} - log.log'
print(log_name)

with open(log_name, 'x') as fh:
    pass
log = logzero.setup_logger(name='Logger', logfile=log_name)

log.info('Buggy Loaded')


class Splat:

    def __init__(self, exception, email, log, user):
        bugsplat = BugSplat(f'{project_name}', f'{project_name}', '0.1.1')
        if log:
            # noinspection PyTypeChecker
            bugsplat.post(exception, app_key='app_key', email=email, additional_file_paths=[log_name], user=user)
        else:
            bugsplat.post(exception, app_key='app_key', email=email, user=user)

    def report(self, exception):
        log.error(traceback.format_tb(exception.__traceback__))
        layout = [
            [sg.Image(f'{os.getenv("LOCALAPPDATA")}/XPlus Games/{project_name}/bugsplat-brand.png', s=(50, 50)), sg.Text('An error has occurred. If you wish to help this game be better, then feel free to submit the bug below.')],
            [sg.Frame('Error:', [
                [sg.Multiline('', disabled=True, k='error', s=(70, 15))]
            ])],
            [sg.Frame('Optional', [[sg.Text('Name:'), sg.Input('', k='name'), sg.Text('Email:'), sg.Input('', tooltip='Your email address. This is if I need to reach you.', k='email')]])],
            [sg.Checkbox('Send bug report', k='send'), sg.Checkbox('Send log File', k='log'), sg.Frame('', [[sg.Button('Finish')]], expand_x=True, element_justification='right', border_width=0)]
        ]

        erwn = sg.Window('Uh Oh!', layout, finalize=True, icon=f'{os.getenv("LOCALAPPDATA")}/XPlus Games/{project_name}/bugsplat.ico')
        erwn['error'].update(traceback.format_tb(exception.__traceback__))
        event, values = erwn.read(close=True)
        if values is None:
            pass
        elif values['send']:
            Splat(exception, values['email'], values['log'], values['name'])
