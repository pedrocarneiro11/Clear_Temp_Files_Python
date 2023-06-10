# hello_wx.py
import PySimpleGUI as sg
import clear

layout = [[sg.Text("Press the button below to clear temp files from Windows")], [sg.Button("Clear Temp Files")]]

# sg.Window(title="Clear Temp Files", layout=[[]], margins=(100, 50)).read()
window = sg.Window("Clear Temp Files", layout, margins=(100, 50))

while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break
    if event == "Clear Temp Files":
        try:
            clear.clear_temp_files()
            sg.Popup("Done!", keep_on_top=True)
        except NotImplemented:
            sg.Popup("Erro!", keep_on_top=True)

window.close()
