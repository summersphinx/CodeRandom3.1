import PySimpleGUI as sg
import pyglet
import os
import first
import webbrowser

path = os.getenv('LOCALAPPDATA') + '/XPlus Games/CodeRandom3/'
pyglet.font.add_file(path + 'fonts/Nunito.ttf')
pyglet.font.add_file(path + 'fonts/SourceSansPro.ttf')
sg.set_options(font=('Source Sans Pro Light', 16))

playing_game = True

docs_url = 'https://summersphinx.github.io/'
discord_url = 'https://discord.gg/pP6NftWD7Z'
credit_music = ['https://ludoloonstudio.itch.io', 'https://aekseer.itch.io/', 'https://nathangibson.myportfolio.com/']

# try:
if True:

    import cr3
    import cr3.sound as sound
    # import cr3.buggy as buggy

    # log = buggy.log
    sound.Play()

    while playing_game:
        color = cr3.Colors.GetColors()

        sett = cr3.Settings()
        print(sett.theme)
        print(sett.darkness)

        new_theme = cr3.Colors.MakeTheme(sett.theme, sett.darkness)
        sg.LOOK_AND_FEEL_TABLE['THEME'] = new_theme
        layout = cr3.Layouts()

        wn = sg.Window('CodeRandom3', layout, finalize=True, size=(1280, 720), resizable=True)
        active_menu_window = None
        side_left = True
        wn.bind("Esc", "_Enter")

        while True:

            event, values = wn.read(timeout=1000, timeout_key='REFRESH')

            if event != 'REFRESH':
                print(event)
                print(values)

            if event == 'REFRESH':
                sound.Play()

            if event == 'input' + '_Enter':
                side_left = not side_left
                wn['side left'].Update(visible=side_left)
                wn['tabgroup1'].Update(visible=not side_left)

            if event == 'quit' or wn.is_closed():
                playing_game = False
                break

            if event in ['docs', 'To Wiki']:
                webbrowser.open(docs_url)

            if event == 'discord':
                webbrowser.open(discord_url)

            if event in ['cred1', 'cred2', 'cred3']:
                t = int(event[-1])-1
                webbrowser.open(credit_music[t])

            if event in ['new', 'cont', 'settings', 'credits']:
                if active_menu_window is not None:
                    wn[active_menu_window].Update(visible=False)
                active_menu_window = event + '1'
                wn[active_menu_window].Update(visible=True)
            if event == 'save settings':
                for i in ['theme', 'dark mode', 'font a', 'font b', 'voice', 'voice vol', 'music', 'music vol']:
                    sett.save(i, values[i])
                sound.Volume()
                wn.close()
                break


# except Exception as e:
#     buggy.Splat.report(Exception, e)
