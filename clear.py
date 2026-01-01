import os
import shutil
import getpass
from tkinter import messagebox


def clear_temp_files():
    username = getpass.getuser()

    del_dir1 = r"C:\Windows\Temp"
    del_dir2 = fr"C:\Users\{username}\AppData\Local\Temp"

    shutil.rmtree(del_dir1, ignore_errors=True)
    shutil.rmtree(del_dir2, ignore_errors=True)

    messagebox.showinfo("Concluído!", "Arquivos temporários foram removidos com sucesso!")


