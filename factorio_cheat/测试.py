"""
__title__ = ''
__author__ = 'liqio'
__mtime__ = '2019/8/4'
"""
import os
import shutil
import re
import tools
import tkinter as tk
from fa_cheat_gui import SingleCheatArea
from tools import get_cheat_dict
from public_data import CHEAT_DICT


def modify_line(line_str, target_str, new_cheat_str):
    templist = line_str.partition(target_str)
    pn = re.compile(r'\d+(?:\.\d{1,2})?')
    newstr = re.sub(pn, str(new_cheat_str), templist[2], count=1)
    return templist[0] + templist[1] + newstr


def composing_test():
    for i in range(1,5):
        print(i)

    print(int(3.5))
    a = 3
    b = int(a+1) if a>int(a) else a
    print(b)
    print(isinstance(a, int))
    a = 25 / 3
    for i in range(1, ((int(a) + 1) if (a > int(a)) else int(a)) + 1):
        print(i)





def main():
    root = tk.Tk()
    tp = tk.Toplevel()
    
    tp.title = "hah"
    # tp.pack()
    root.mainloop()



if __name__ == "__main__":
    main()
