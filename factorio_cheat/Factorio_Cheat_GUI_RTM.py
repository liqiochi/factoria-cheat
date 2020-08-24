import tkinter
import os
from tkinter.filedialog import askdirectory
from tools import get_cheat_dict, modifying_file, list2jsonfile, jsonfile2list, backupfile, restorefile
from public_data import README, CHEAT_DICT

final_cheat_dict = dict()
cheat_results = list()
backup_path = ""


class OutOfRangeValueError(Exception):
    pass


class MyToplevel(tkinter.Toplevel):
    def __init__(self, text, title=None, geometry='100x100'):
        super().__init__()
        self.text = text
        self.title(title)
        self.geometry(geometry)
        tkinter.Label(self, text=self.text).grid(row=1, column=1, sticky='e'+'w')
        tkinter.Button(self, text='OK', command=self.destroy).grid(row=2, column=1)
        self.grid()


class SingleCheatArea(tkinter.Frame):
    def __init__(self, row, col, name, cheat_pack, parent=None):
        super().__init__()
        self.name = name        
        self.dict = cheat_pack[name]
        self.c_name = self.dict['cn_name']
        self.grid(row=row, column=col)
        self.make_widgets()

    def process(self, ent):
        value = ent.get()
        try:
            if "." in value:
                self.dict['new_cheat_str'] = round(float(value), 2)
            else:
                self.dict['new_cheat_str'] = int(value)
            if self.name == 'belt_distance' or self.name == 'fast_belt_distance' or self.name == 'express_belt_distance':
                if 0 < int(value) < 256:
                    self.dict['new_cheat_str'] = int(value)
                else:
                    raise OutOfRangeValueError

            cheat_results.append(modifying_file(self.dict))
            MyToplevel('修改成功', title='修改结果')
        except ValueError:
            MyToplevel('请输入数字')
        except OutOfRangeValueError:
            MyToplevel('输入数字应在：(0, 256)区间', geometry='200x100')

    def callback(self, event):
        self.process(self.myent)

    def make_widgets(self):
        tkinter.Label(self, text=self.c_name, width=20, anchor='w', relief='groove').grid(row=0, column=0, sticky='w')
        cheat_value = tkinter.StringVar(value=self.dict['new_cheat_str'])
        self.myent = tkinter.Entry(self, textvariable=cheat_value)
        self.myent.bind("<KeyPress-Return>", self.callback)
        self.myent.grid(row=0, column=1, sticky='w')
        btn = tkinter.Button(self, text='处理', command=(lambda ent=self.myent: self.process(ent))).grid(row=0, column=2)


def get_directory():
    global final_cheat_dict
    global backup_path
    install_dir = askdirectory(initialdir=r'C:\Program Files (x86)\Steam\steamapps\common')
    backup_path = os.path.join(install_dir, "backup")
    final_cheat_dict = get_cheat_dict(cheat_dict=CHEAT_DICT, factorio_install_dir=install_dir)
    MyToplevel(install_dir, title='安装目录', geometry='500x100')


def cheat_all(ch_dict):
    for i in ch_dict.values():
        cheat_results.append(modifying_file(i))
    MyToplevel('修改成功', title='修改结果')


def create_all_frame(root, frm, ch_dict):
    frm_list = list()
    for i in ch_dict:
        frm_list.append(i)
    k = 0
    row = 0
    for i in range(1, int(len(ch_dict) / 3) + 1):
        for j in range(3):
            SingleCheatArea(i, j, frm_list[k], ch_dict, parent=root)
            # print(frm_list[k])
            k += 1
            row = i
    col = len(ch_dict) % 3
    if col != 0:
        row += 1
        for j in range(col):
            SingleCheatArea(row, j, frm_list[k], ch_dict, parent=root)
            # print(frm_list[k])
            k += 1

    tkinter.Button(frm, text='一键全修改', command=lambda x=ch_dict: cheat_all(x)).grid(row=0, column=0)


def show_readme(text=README):
    tp2 = tkinter.Toplevel()
    tp2.grid()
    tp2.title('帮助和说明')
    tp2.geometry('500x450')
    tkinter.Label(tp2, justify=tkinter.LEFT, text=text).grid(row=1, column=1, sticky='w')
    tkinter.Button(tp2, text='OK', command=tp2.destroy).grid(row=2, column=1)


def show_log():
    text = ''
    for i in cheat_results:
        text = text + i + '\n'

    tp3 = tkinter.Toplevel()
    tp3.title('修改结果')
    tp3.geometry('800x500')
    txt = tkinter.Text(tp3)
    txt.insert("1.0", text)
    scb = tkinter.Scrollbar(tp3)
    scb.config(command=txt.yview)
    txt.config(yscrollcommand=scb.set)
    txt.pack(side=tkinter.LEFT, expand=tkinter.YES, fill= tkinter.BOTH)
    scb.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    txt.config(state=tkinter.DISABLED)
    tkinter.Button(tp3, text='OK', command=tp3.destroy).pack(side=tkinter.BOTTOM)


def backup_file(jsonname="modified_files.json"):
    backup_list = list()
    for single_dict in final_cheat_dict.values():
        o_file = single_dict['path']
        if not o_file in backup_list:
            backup_list.append(o_file)
    # print(backup_list)
    for i in backup_list:
        backupfile(i, backup_path)
    list2jsonfile(backup_list, backup_path, filename=jsonname)

    text = "备份在：%s" % backup_path
    MyToplevel(text, geometry='500x100')


def restore_file(myfile="modified_files.json"):
    realpath = os.path.join(backup_path, myfile)
    backup_list = jsonfile2list(realpath)
    # {备份的文件名demo-entities.lua: 这个文件所在的路径~\entity}
    new_dict = dict()
    for i in backup_list:
        new_dict[os.path.basename(i)] = os.path.dirname(i)
    # print(new_dict)
    for i in os.listdir(backup_path):
        if i != "modified_files.json":
            newfile = os.path.join(backup_path, i)
            restorefile(newfile, new_dict[i])
    MyToplevel('已还原至上次备份')


def main():
    root = tkinter.Tk()
    root.title('Factorio Cheat')

    height = 30
    t = len(CHEAT_DICT)
    if t % 3 == 0:
        height *= t // 3 + 1
    else:
        height *= t // 3 + 2
    root.geometry('1000x%d' % height)  # 1行30像素

    first_line1 = tkinter.Frame(root)
    first_line2 = tkinter.Frame(root)
    first_line3 = tkinter.Frame(root)
    first_line1.grid(row=0, column=0)
    first_line2.grid(row=0, column=1)
    first_line3.grid(row=0, column=2)

    tkinter.Button(first_line1, text='打开安装目录', command=get_directory).grid(row=0, column=0, sticky='w')
    b = tkinter.Button(first_line1, text='初始化修改数据', command=(lambda r=root, f=first_line2: create_all_frame(r, f, final_cheat_dict)))
    b.grid(row=0, column=1)
    tkinter.Button(first_line2, text='显示修改结果', command=show_log).grid(row=0, column=1, sticky='e')
    tkinter.Button(first_line3, text='备份', command=backup_file).grid(row=0, column=0)
    tkinter.Button(first_line3, text='还原', command=restore_file).grid(row=0, column=1)
    tkinter.Button(first_line3, text='说明和帮助', command=show_readme).grid(row=0, column=3)

    root.mainloop()


if __name__ == "__main__":
    main()
