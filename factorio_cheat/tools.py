import os
from shutil import copy, copyfile
from re import compile, sub, findall
import json


def get_cheat_dict(cheat_dict, factorio_install_dir=r"C:\Program Files (x86)\Steam\steamapps\common\Factorio"):
    """构造最终版cheat_dict（带真实路径）"""
    data_dir = r"data\base\prototypes"
    install_dir = os.path.normpath(os.path.join(factorio_install_dir, data_dir))

    for i in cheat_dict.items():
        i[1]['path'] = os.path.join(install_dir, i[1]['path'])
    return cheat_dict


def modifying_file(single_cheat_dict):
    """修改文件并覆盖"""
    # 1.读取要修改的文件，获得一个所有字符串的列表
    strlist = []
    path = single_cheat_dict['path']
    with open(path, "r") as f:
        for i in f.readlines():
            strlist.append(i.rstrip())
        # print(strlist)

    # 2.找到要修改的那一行，修改后保存到列表
    # core_cheat(path, strlist, specified_front_num, specified_target_num, front_str, target_str, new_cheat_str)
    fb = core_cheat(strlist, single_cheat_dict)

    # 3.将列表转换为字符串并保存文件
    ListToStr(path, strlist)

    # 4.返回修改详情
    return fb


def core_cheat(strlist, single_cheat_dict):
    """定位到要修改的那一行：先模糊定位，再精确定位到某一行。"""
    actual_front_num = 0
    actual_target_num = 0
    # i是要修改的文件的总行数
    for i in range(len(strlist)):
        if single_cheat_dict['front_str'] in strlist[i]:
            actual_front_num += 1
        if actual_front_num == single_cheat_dict['specified_front_num']:
            if single_cheat_dict['target_str'] in strlist[i]:
                actual_target_num += 1
                if actual_target_num == single_cheat_dict['specified_target_num']:
                    # 显示在这一行修改了什么
                    fb = feedback(i, strlist[i], single_cheat_dict)
                    # 真正的修改程序
                    strlist[i] = modify_line(strlist[i], single_cheat_dict['target_str'], single_cheat_dict['new_cheat_str'])
    return fb


def modify_line(line_str, target_str, new_cheat_str):
    """核心逻辑：用新数据替换旧数据"""
    templist = line_str.partition(target_str)
    pn = compile(r'\d+(?:\.\d{1,2})?')
    newstr = sub(pn, str(new_cheat_str), templist[2], count=1)
    return templist[0] + templist[1] + newstr


def feedback(i, line_str, single_cheat_dict):
    """反馈：指出在什么位置旧数据被修改为新数据"""
    original_cheat_str = findall(r'\d+(?:\.\d{1,2})?', line_str.partition(single_cheat_dict['target_str'])[2])[0]
    feed_back = '{5}修改：在文件{0}第{1}行中的{2}{3}已经被改为：{4}。'.format(os.path.basename(single_cheat_dict['path']), i, 
    single_cheat_dict['target_str'], original_cheat_str, single_cheat_dict['new_cheat_str'], single_cheat_dict['cn_name'])
    print(feed_back)
    return feed_back


def ListToStr(path, strlist):
    """把列表中的元素重新组合成一个字符串并保存到文件中"""
    with open(path, "w") as nf:
        nf.write("\n".join(strlist))


def copyfile(cheatfilepath, newpath):
    """复制作弊文件到指定目录下"""
    copy(cheatfilepath, newpath)


def add_cheat_codes(path, codes):
    """添加作弊码到文件末尾"""
    with open(path, "a") as f:
        f.write("\n" + codes)


def backupfile(file, path):
    if os.path.exists(path):
        if os.path.isdir(path):
            copyfile(file, path)
        else:
            while os.path.exists(path):
                path += "1"
            os.mkdir(path)
            copyfile(file, path)
    else:
        os.mkdir(path)
        copy(file, path)


def restorefile(newpos, origpos):
    copyfile(newpos, origpos)


def save_modified_file(file, path):
    if os.path.exists(path):
        if os.path.isdir(path):
            copy(file, path)
        else:
            while os.path.exists(path):
                path += "1"
            os.mkdir(path)
            copy(file, path)
    else:
        os.mkdir(path)
        copy(file, path)


def list2jsonfile(mylist, path, filename='cheatfile.json'):
    with open(os.path.join(path, filename), 'w') as f:
        try:
            json.dump(mylist, f)
            print('saving sucessfully.')
        except IOError as e:
            print(e)


def jsonfile2list(myfile):
    with open(myfile, 'r') as f:
        return json.load(f)


def main():
    pass


if __name__ == "__main__":
    main()