import PySimpleGUI as sg
import pyglet
import os
import first
import webbrowser

path = os.getenv('LOCALAPPDATA') + '/XPlus Games/CodeRandom3/'
pyglet.font.add_file(path + 'fonts/Nunito.ttf')
pyglet.font.add_file(path + 'fonts/SourceSansPro.ttf')
sg.set_options(font=('Source Sans Pro Light', 16), titlebar_font='Nunito 16 bold')

playing_game = True

docs_url = 'https://summersphinx.github.io/'
discord_url = 'https://discord.gg/pP6NftWD7Z'

try:

    import cr3
    import cr3.buggy as buggy

    log = buggy.log

    while playing_game:
        color = cr3.Colors.GetColors()

        sett = cr3.Settings()
        print(sett.theme)
        print(sett.darkness)

        new_theme = cr3.Colors.MakeTheme(sett.theme, sett.darkness)

        sg.LOOK_AND_FEEL_TABLE['THEME'] = new_theme

        layout = cr3.Layouts()

        wn = sg.Window('CodeRandom3', layout, finalize=True, size=(1280, 720))

        active_menu_window = None

        while True:

            event, values = wn.read()

            log.info(event)
            log.info(values)

            if event == 'quit' or wn.is_closed():
                playing_game = False
                break

            if event == 'docs':
                webbrowser.open(docs_url)

            if event == 'discord':
                webbrowser.open(discord_url)

            if event in ['new', 'cont', 'settings']:
                if active_menu_window is not None:
                    wn[active_menu_window].Update(visible=False)
                active_menu_window = event + '1'
                wn[active_menu_window].Update(visible=True)
            if event == 'save settings':
                sett.save('theme', values['theme'])
                sett.save('dark mode', values['dark mode'])
                wn.close()
                break



except Exception as e:
    buggy.Splat.report(Exception, e)
