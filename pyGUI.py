import PySimpleGUI as sg
import main

system = "You are a SQL code generator. Your responses will only contain SQL code. Encapsulate all output in SQL comments."
messages = [{"role": "system", "content": system}]

user_input_column = [
    [sg.Text("Welcome to SQL BeGone")],
    [sg.Text("Enter your request below")],
    [sg.Multiline(size=(50, 10),
              key="-MESSAGE-")],
    [sg.Button("Submit")],
    [sg.Button("Enter api_key"), sg.Button("Exit")]
]

system_output_column = [
    [sg.Text("ChatBot output:")],
    [sg.Multiline(size=(50, 15),
                key="-RESPONSE-",
                auto_size_text=False)]

]
                        
layout = [[sg.Column(user_input_column),
            sg.VSeparator(),
            sg.Column(system_output_column)]]

window = sg.Window("SQL BeGone", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Enter api_key":
        key = sg.popup_get_text("Enter your api key: ", title="api_key")

        f = open("test.txt", "w+")
        f.write(key)
        f.close()
    if event == "Submit":
        prompt = window["-MESSAGE-"].get()
        messages = main.GUIinputPrompt(prompt, messages)
        print(messages)

window.close()