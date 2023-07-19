""" 
    读取每个词典文本向量的结果，并计算精确率


"""

import os
import ast

# 指定目录路径
dir_path = "resv2-100"

# 列出该目录下所有的文件（不包含子目录）
file_list = os.listdir(dir_path)

dict_list = {}
# 遍历文件列表
for file_name in file_list:
    # 拼接出文件的绝对路径
    file_path = os.path.join(dir_path, file_name)
    name_without_ext = os.path.splitext(file_name)[0]
    # 判断该路径指向的是否为文件
    if os.path.isfile(file_path):
        # 如果是文件，则进行读取操作
        with open(file_path, 'r',encoding='utf-8') as f:
            contents = f.read()
            # 输出文件名和内容
            # print("File name:", file_name)
            # print("File contents:", contents)
            dict_list[name_without_ext] = ast.literal_eval(contents)

# print(len(dict_list))
# print(len(dict_list['财经']))
err_dict = {}
for key in dict_list:
    for name in dict_list[key]:
        if name == key : continue
        err_dict[name] = err_dict.get(name,0) + 1

print(err_dict)


