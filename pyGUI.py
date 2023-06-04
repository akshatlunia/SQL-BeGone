import PySimpleGUI as sg
import main
from importlib import reload
from sys import modules
import os.path
if os.path.exists('./variables.py'):
    import variables
api_key = ""
try:
    api_key = variables.api_key
except:
    print("Please enter your api_key in variables.py!")
    print("Get yours at https://platform.openai.com/account/api-keys")
    sg.popup_error("Please enter your api_key!\nGet yours at https://platform.openai.com/account/api-keys")

system = "You are a SQL code generator. Your responses will only contain SQL code. Encapsulate all output in SQL comments."
messages = [{"role": "system", "content": system}]
completion = ""

user_input_column = [
    [sg.Text("Welcome to SQL BeGone")],
    [sg.Text("Enter your request below.")],
    [sg.Text("Please allow extra time for long message streams and/or long requests.")],
    [sg.Multiline(size=(50, 10),
              key="-MESSAGE-")],
    [sg.Button("Submit"), sg.Button("Clear Message Stream")],
    [sg.Button("Enter api_key"), sg.Button("Exit")]
]

system_output_column = [
    [sg.Text("ChatBot output:")],
    [sg.Multiline(size=(50, 15),
                key="-RESPONSE-",
                auto_size_text=False,
                write_only=False)]

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
        if key != None:
            f = open("variables.py", "w+")
            f.write("api_key = '"+key+"'")
            f.close()
            if 'variables' not in modules:
                import variables
            reload(variables)
            api_key = key

    if event == "Submit":
        prompt = window["-MESSAGE-"].get()
        completion, tokens = main.GUIinputPrompt(prompt, messages, api_key)

        if completion == "-1Error":
            sg.popup_error("Invalid API key, please try a different one")

        else:
            tokens = tokens - 5
            winOut = "You've used " + str(tokens) + " tokens.\n\n" + completion
            window["-RESPONSE-"].update(winOut)
    
    if event == "Clear Message Stream":
        messages = [{"role": "system", "content": system}]

window.close()