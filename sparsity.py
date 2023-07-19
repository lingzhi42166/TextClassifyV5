from numpy import arange
import pkgs.FileOperations as file_oper
import ast
import os

#求文本向量的非零个数
def count_sparsity(vec_path,out_path,out_path_1):
  txt_path_list = file_oper.each_file(vec_path)[0:1000]
  class_num_arr = []
  for txt_path in txt_path_list: #求非零个数
    txt_vec = file_oper.read_file(txt_path,'read_dict')
    num = 0
    for key in txt_vec:
      if key == 0:continue
      num+=1
    class_num_arr.append(num)
  # print(len(class_num_arr))
    
  # class_num_arr = class_num_arr[0:1064]
  # print(len(class_num_arr))
  if not os.path.exists(out_path_1):
      os.makedirs(out_path_1)
  file_oper.save_file(out_path,class_num_arr)  #把每个文本的非零个数 持久化

def compute_(out_path):
  with open(out_path, 'r',encoding='utf-8') as f:
    txt_vec = ast.literal_eval(f.read())
  # print(len(txt_vec))
  # print(txt_vec)
  num = 0
  
  for index in txt_vec: #对于一类而言测试集的数量是一样的
    if index >= 15:
      num+=1
  num_list.append(num)
  print(num)
  return num 

# 读取稀疏性，然后进行比较
def compare_(out_base_path):
  files = os.listdir(out_base_path)
  res_list = []
  num = 0
  print(files)  #打印出来 按索引位置分配label
  all_vec_list = []
  for txt_name in files:
    if txt_name.endswith(".txt"):
      txt_path = out_base_path + "/" + txt_name
      # print(txt_path)
      with open(txt_path, 'r',encoding='utf-8') as f:
        txt_vec = ast.literal_eval(f.read())
      all_vec_list.append(txt_vec)
  print(all_vec_list)
  # for index in all_vec_list: #对于一类而言测试集的数量是一样的
  #   if all_vec_list[0][index] > all_vec_list[1][index]:
  #     res_list.append(0)  
  #   else:
  #     res_list.append(1)  

  # print(len(res_list))
  # print(res_list)

  # for index in res_list:
  #   if index == 1:
  #     num +=1
  # print(num) 


def main(class_,dict_class):
  # class_ = '娱乐' #选择要统计的类别
  # dict_class = '彩票' #选择生成文本向量的词典
  # dict_class = class_ #选择生成文本向量的词典
  # print(num_list)
  out_base_path = 'D:/onStudying/TextClassify/TextClassifyV5/res/'+ class_ +'/sparsity/'
  out_path_1 = out_base_path + dict_class
  out_path = out_path_1 +'sparsity.txt'
  # vec_path = 'I:/onStudying/TextClassify/TextClassifyV5/res/'+ class_ +'/vec'
  vec_path = 'D:/onStudying/TextClassify/TextClassifyV5/res/'+ class_ +'/vec/' + dict_class + 'vec2'
  # print(vec_path)
  count_sparsity(vec_path,out_path,out_path_1)  #统计非零个数
  #有几个文本的非零值数量大于10
  # compute_(out_path)
  
  #进行比较，哪个词典的非零值多 就属于哪一类
  # compare_(out_base_path)
  

  # num1 = 0
  # for key in class_num_arr:
  #   if key >=10:num1+=1
  # print(num1)


# class_ = '房产'
# dict_class = '房产'
# main(class_,dict_class)

classes_list = ['财经','彩票','房产','股票','家居','教育','科技','社会','时尚','时政','体育test','星座','游戏','娱乐']
# classes_list = ['彩票']
# dict_class_list = classes_list
dict_class_list = ['财经']
for dict_class in dict_class_list:
  num_list = []
  for class_ in classes_list:
    print('=========================================')
    print('词典:' + dict_class + ';' + '类别:' + class_)
    main(class_,dict_class)
  # number = sum(num_list)
  # print(number)
  break
