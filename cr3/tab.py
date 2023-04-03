import PySimpleGUI as sg

def tab_group():
    main_tab = sg.Tab(
            title='Main',
            layout=[[]],
            key='main tab',
            expand_x=True,
            expand_y=True
    )

    code_tab = sg.Tab(
            title='Code',
            layout=[[]],
            key='code tab',
            expand_x=True,
            expand_y=True
    )

    tools_tab = sg.Tab(
            title='Tools',
            layout=[[]],
            key='tools tab',
            expand_x=True,
            expand_y=True
    )

    help_tab = sg.Tab(
            title='Help',
            layout=[[sg.Button('To Wiki')]],
            key='help tab',
            expand_x=True,
            expand_y=True
    )

