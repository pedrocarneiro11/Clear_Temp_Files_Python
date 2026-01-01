from tkinter import *
from PIL import Image, ImageDraw
from tkinter import messagebox

import clear

def execute_clear_temp_files():
    try:
        clear.clear_temp_files()
    except Exception as e:
        messagebox.showerror("Erro!", f"Ocorreu um erro: {e}")


window = Tk()
window.title("Clear Temp Files")
window.config(padx=10, pady=100)

# Button
add_button = Button(text="Clear Temp Files", width=36, command=execute_clear_temp_files)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
