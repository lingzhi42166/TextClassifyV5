import pkgs.FileOperations as file_oper


""" 
    用于将指定类的所有文本放在一个txt中，并只保留中文

"""

def txt_AllIn(corpusPath):
    only_chinese_arr = []
    txt_path_list = file_oper.each_file(corpusPath)
    # num = 1;
    for txtPath in txt_path_list:
        # if num>2000:break #只合并前2000个文本
        txt = file_oper.read_file(txtPath)
        only_chinese_arr.append(only_chinese(txt))
        # num+=1



    return only_chinese_arr


def only_chinese(content):
    content_str = ''
    for i in content:
        if is_chinese(i):
            content_str = content_str + i
    return content_str


def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False
