""" 
    读取每个类别下的各词典生成的sparsity进行比较，数组的第一个元素表示第一个文本，哪个值大就属于哪一类
    读取后保存到字典数据类型如读取财经下的文本向量：财经:{财经sparsity:[],房产;[]}
    遍历字典，进行比较
"""
import os
import ast
import pkgs.FileOperations as file_oper
import time
def read_txt_files(path):
    """
    读取指定目录下的所有txt文件，返回文件内容的字符串列表
    """
    result = {}
    for file in os.listdir(path):  # 遍历目录下的所有文件
        if file.endswith('.txt'):  # 判断文件是否为txt文件
            file_path = os.path.join(path, file)  # 获取文件的绝对路径
            filename = os.path.splitext(file)[0]
            with open(file_path, 'r') as f:
                content = f.read()  # 读取文件内容
                result[filename] = ast.literal_eval(content)  # 将文件内容添加到结果中
    return result

def mian():
    classes_list = ['财经','彩票','房产','股票','家居','教育','科技','社会','时尚','时政','体育test','星座','游戏','娱乐']
    dict_class_list = classes_list
    
    class_='彩票'
    path_ = 'res/' + class_ + '/sparsity/'
    class_txt_dict = read_txt_files(path_)
    # print(len(class_txt_dict))
    # print(class_ + '======')
    # print(class_txt_dict)
    compare_dict = {}
    res_list = []
    number = 0
    # print(len(class_txt_dict))#14个 {1:[1000个]}
    for num in range(len(class_txt_dict['财经sparsity'])):#1000
        for i in class_txt_dict:
            # print(len(class_txt_dict[i]))#1000
            compare_dict[i] = class_txt_dict[i][num]
            # print(i)
        max_key = max(compare_dict, key=compare_dict.get)
        res = max_key.replace('sparsity', '')
        res_list.append(res)
        # print('文本'+ str(num) +'的结果：' + res)
        file_oper.save_file('resv2/60' + class_ + '.txt',res_list)
        if res == class_ :number+=1

    print(number)
    

    # for class_ in classes_list:
    #     path_ = 'res/' + class_ + '/sparsity/'
    #     class_txt_dict = read_txt_files(path_)
    #     print(len(class_txt_dict))
    #     print(class_ + '======')
    #     # print(class_txt_dict)
    #     compare_dict = {}
    #     res_list = []
    #     number = 0
    #     print(len(class_txt_dict))#14个 {1:[1000个]}
    #     for num in range(len(class_txt_dict['财经sparsity'])):#1000
    #         for i in class_txt_dict:
    #             # print(len(class_txt_dict[i]))#1000
    #             compare_dict[i] = class_txt_dict[i][num]
    #             # print(i)
    #         max_key = max(compare_dict, key=compare_dict.get)
    #         res = max_key.replace('sparsity', '')
    #         res_list.append(res)
    #         print('文本'+ str(num) +'的结果：' + res)
    #         if res == '财经':number+=1

    #     print(number)
    #     break

start_time = time.time()
mian()
end_time = time.time()
print('程序运行时间为：', end_time - start_time, '秒')

