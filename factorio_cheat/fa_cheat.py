import os
from tools import get_cheat_dict, modifying_file, list2jsonfile, jsonfile2list
from public_data import README, CHEAT_DICT

"""
def modifying_file(
        path, specified_front_num=0, specified_target_num=1,
        front_str="", target_str="", new_cheat_str=""):
    修改文件并覆盖
    :param path: 要修改的文件的地址
    :param specified_front_num: identified_str出现的次数（出现指定次数后才是真正的定位符）
    :param specified_target_num: target_str出现的次数
    :param front_str: 要修改字符串的前导字符（用于定位要修改的字符串）
    :param target_str: 定位符（后面就是要修改的字符串）
    :param new_cheat_str: 修改后的字符串
"""


def main():
    cheat_dict = get_cheat_dict(cheat_dict=CHEAT_DICT)
    for single_cheat_dict in cheat_dict.values():
        modifying_file(single_cheat_dict)
        # print(single_cheat_dict)
    # pass
    # list2jsonfile(cheat_dict, r'e:\\')
    # print(jsonfile2list('cheatfile.json'))


if __name__ == '__main__':
    main()
