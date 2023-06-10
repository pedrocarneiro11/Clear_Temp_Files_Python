import os
import shutil
import getpass


def clear_temp_files():
    username = getpass.getuser()

    del_dir1 = r"C:\Windows\Temp"
    del_dir2 = fr"C:\Users\{username}\AppData\Local\Temp"

    shutil.rmtree(del_dir1, ignore_errors=True)
    shutil.rmtree(del_dir2, ignore_errors=True)


