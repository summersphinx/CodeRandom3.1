import PySimpleGUI as sg

def tab_group():
    main = sg.Tab(
            title='Main',
            layout=[[]],
            key='main tab',
            expand_x=True,
            expand_y=True
    )

    code = sg.Tab(
            title='Code',
            layout=[[]],
            key='code tab',
            expand_x=True,
            expand_y=True
    )

    tools = sg.Tab(
            title='Tools',
            layout=[[]],
            key='tools tab',
            expand_x=True,
            expand_y=True
    )

    help = sg.Tab(
            title='Help',
            layout=[[sg.Button('To Wiki')]],
            key='help tab',
            expand_x=True,
            expand_y=True
    )

    return sg.TabGroup([[main, code, tools, help]], expand_y=True, expand_x=True, k='tabgroup2')
