import os
import ast
"""
用于文件操作
1、遍历指定文件夹的文件  each_file
"""
def each_file(path):
    txt_path_list = []
    for list in os.listdir(path):
        txt_path_list.append(path + '/' +list)
    return txt_path_list

# 读取文本，如果mode为readline 表示按行读取  用于读取AllIn文本的
def read_file(path,mode='normal'):
    with open(path,'r',encoding='UTF-8',errors='ignore') as f:
        if mode == 'normal':
            return f.read()
        elif mode == 'read_lines':
            dataList = []
            for line in f.readlines():
                if line.isspace(): continue  # 空行不要
                dataList.append(line)
            return dataList 
        elif mode == 'read_lines_arr':
            dataList = []
            for line in f.readlines():
                if line.isspace(): continue  # 空行不要
                line = ast.literal_eval(line)
                # print(line)
                dataList.append(line)
               
            return dataList 
        elif mode == 'read_dict':
          return ast.literal_eval(f.read())

# 保存文件，如果mode为each 则data是数组 需要遍历
def save_file(out_path,data,mode='normal'):
    newF = open(out_path, 'w+', encoding='UTF-8')
    if mode =='each':
        for each in data:
            if type(each) != 'str':each = str(each)
            newF.write(each + '\r\n')  # 每篇文章\r\n分开
        newF.close()
    elif mode == 'each_R':
        num = len(data)
        for each in data:
            num-=1
            if type(each) != 'str':each = str(each)
            if num>=1:
                newF.write(each + '\r')  
            else:
                newF.write(each)  
        newF.close()
    else:
        newF.write(str(data))
        newF.close()


def make_dir(out_path):
    if not os.path.exists(out_path):
        os.makedirs(out_path)

def save_txt_in_File(out_path,data):
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    newF = open(out_path, 'w+', encoding='utf-8')

    for each in data:
        # print(each)
        newF.write(each + '\r\n')

    newF.close()

if __name__ == '__main__':
    pass

elif __name__ == 'pkgs.FileOperations':
    pass