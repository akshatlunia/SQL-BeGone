import PySimpleGUI as sg

def newApiKey():
    layout = [[sg.Text("Enter your api_key")], [sg.PopupGetText("api_key:")], [sg.Button("Done")]]

    window = sg.Window("api_key input", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Done":
            break

    window.close()