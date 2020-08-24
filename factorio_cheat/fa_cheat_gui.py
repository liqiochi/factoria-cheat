import tkinter
from tkinter.filedialog import askdirectory
from tools import get_cheat_dict, modifying_file
from public_data import README, CHEAT_DICT

final_cheat_dict = dict()  # 使用get_cheat_dict()处理后获得真实地址的cheat_dict
cheat_results = list()  # 用于最后显示修改结果，记录的列表


class SingleCheatArea(tkinter.Frame):
    def __init__(self, row, col, name, cheat_pack, parent=None):
        super().__init__()
        self.name = name        
        self.dict = cheat_pack[name]
        self.c_name = self.dict['cn_name']  # 不能放在grid之后，否则会提示：'SingleCheatArea' object has no attribute 'dict'
        self.grid(row=row, column=col)
        self.make_widgets()

    def process(self, ent):
        value = ent.get()
        # print(type(value))
        if "." in value:
            self.dict['new_cheat_str'] = round(float(value), 2)
        else:
            self.dict['new_cheat_str'] = int(value)
        # print('value', value)
        # print(self.dict)
        cheat_results.append(modifying_file(self.dict))

        tp = tkinter.Toplevel()
        tp.grid()
        tp.title('修改结果')
        tp.geometry('100x100')
        tkinter.Label(tp, text='修改成功').grid(row=1, column=1, sticky='e'+'w')
        tkinter.Button(tp, text='ok', command=tp.destroy).grid(row=2, column=1)

    def make_widgets(self):
        tkinter.Label(self, text=self.c_name, anchor='w', relief='groove').grid(row=0, column=0, sticky='w')
        # value参数表示默认值
        cheat_value = tkinter.StringVar(value=self.dict['new_cheat_str'])
        myent = tkinter.Entry(self, textvariable=cheat_value)
        myent.grid(row=0, column=1, sticky='w')
        btn = tkinter.Button(self, text='处理', command=(lambda ent=myent: self.process(ent))).grid(row=0, column=2)


def get_directory():
    # 这里要用global的原因在于tcheat_dict重新指向了一个变量而不是在字典内部修改，指向被修改了。
    global final_cheat_dict
    install_dir = askdirectory(initialdir=r'C:\Program Files (x86)\Steam\steamapps\common')
    tcheat_dict = get_cheat_dict(cheat_dict=CHEAT_DICT, factorio_install_dir=install_dir)

    tp = tkinter.Toplevel()
    tp.grid()
    tp.title('安装目录')
    tp.geometry('500x100')
    tkinter.Label(tp, text=install_dir).grid(row=1, column=1, sticky='e'+'w')
    tkinter.Button(tp, text='ok', command=tp.destroy).grid(row=2, column=1)


def cheat_all(ch_dict):
    for i in ch_dict.values():
        cheat_results.append(modifying_file(i))
    
    tp = tkinter.Toplevel()
    tp.grid()
    tp.title('修改结果')
    tp.geometry('100x100')
    tkinter.Label(tp, text='修改成功').grid(row=1, column=1, sticky='e'+'w')
    tkinter.Button(tp, text='ok', command=tp.destroy).grid(row=2, column=1)


def create_all_frame(root, ch_dict):
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
    
    tkinter.Button(root, text='一键搞定', command=lambda x=ch_dict: cheat_all(x)).grid(row=0, column=2)


def show_readme(text=README):
    tp2 = tkinter.Toplevel()
    tp2.grid()
    tp2.title('帮助和说明')
    tp2.geometry('500x400')
    tkinter.Label(tp2, text=text).grid(row=1, column=1, sticky='w')
    tkinter.Button(tp2, text='ok', command=tp2.destroy).grid(row=2, column=1)


def show_log():
    text = ''
    for i in cheat_results:
        text = text + i + '\n'
    tp3 = tkinter.Toplevel()
    tp3.grid()
    tp3.title('修改结果')
    tp3.geometry('800x500')
    tkinter.Label(tp3, text=text).grid(row=1, column=1, sticky='w')
    tkinter.Button(tp3, text='ok', command=tp3.destroy).grid(row=3, column=1)


def initial_frame_disable_btn(r, btn):
    create_all_frame(r, final_cheat_dict)
    btn.config(state='disable')


def main():
    # mainloop()类似于协程中的loop = asyncio.get_event_loop()，主程序中的实例化过程比如Tk()、Button()等类似于协程函数，
    # main()在执行时，其他不需要等待的方法比如print()函数等会先执行，然后才会轮到控件的实例化过程。
    root = tkinter.Tk()
    root.title('factorio cheat')
    root.geometry('1200x400')

    tkinter.Button(root, text='打开安装目录', command=get_directory).grid(row=0, column=0, sticky='w')
    """
    创建类的实例是个普通的过程，会先执行；但此时上一个Button没创建，也不会返回tcheat_dict，
    所以SingleCheatArea()实例化要接收的tcheat_dict参数实际上是空的。为了避免这种情况，用lambda来延迟执行。
    默认参数不能是可变类型，但调用的时候可以：
    tkinter.Button(root, text='start', command=(lambda r=root, x=tcheat_dict: create_all_frame(r, x))).grid(row=0, column=1)  # 错误
    注意：lambda表达式内包的那个函数有括号。
    """
    # 不禁用初始化按钮
    b = tkinter.Button(root, text='初始化修改数据', command=(lambda r=root: create_all_frame(r, final_cheat_dict)))
    b.grid(row=0, column=1)

    # 禁用初始化按钮
    # b = tkinter.Button(root, text='初始化')
    # b.grid(row=0, column=1)
    # b.config(command=(lambda r=root, btn=b: initial_frame_disable_btn(r, btn)))

    tkinter.Button(root, text='显示修改结果', command=show_log).grid(row=0, column=3, sticky='e')
    tkinter.Button(root, text='说明和帮助', command=show_readme).grid(row=0, column=4)

    root.mainloop()


if __name__ == "__main__":
    main()
