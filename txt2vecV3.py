import pkgs.FileOperations as file_oper
import ast
import matplotlib.pyplot as plt
import os
import time
 
def main(classes,dict_class):
    outBasePath = 'res'
    # classes = '财经'
    # dict_class = '彩票'
    # dict_class = classes
    test_outPath = outBasePath + '/' + classes  
    dict_outPath = outBasePath + '/' + dict_class  

    
    #1、读取文本 （因为放在一起了,所以只需要读取一个，然后遍历）
    txt_path = test_outPath + '/各文本词频比重.txt'
    
    txt_list = file_oper.read_file(txt_path,'read_lines_arr')[1000:2000]
    # txt_list = file_oper.read_file(txt_path,'read_lines_arr')

    # print(len(txt_list))

    
    # 2、读取词典
    dict_path = dict_outPath + '/词典.txt'
    dict_list = ast.literal_eval(file_oper.read_file(dict_path))

    #3、读取df
    df_path = dict_outPath + '/特征项df.txt'
    df_dict = file_oper.read_file(df_path,'read_dict')

    # 4、文本向量化

    txt2vec_path = test_outPath + '/vec/' + dict_class + 'vec2'
    txt2vec_plt_path = test_outPath + '/plt/' + dict_class + 'plt2'
    if not os.path.exists(txt2vec_path):
      os.makedirs(txt2vec_path)
    if not os.path.exists(txt2vec_plt_path):
      os.makedirs(txt2vec_plt_path)

    #只要前500个特征词
    dict_list = dict_list[:60]#60 100 120 150
    # print(len(dict_list))

    index = 0
    for txt in txt_list:
      # if index >=1000:break #只分类1000个
      index += 1
      txt_vec = []
      for key in dict_list:
        if key not in txt:
          txt_vec.append(0)
          continue
        num = df_dict[key] * txt[key]
        txt_vec.append(num)
      file_oper.save_file(txt2vec_path + '/' + str(index) + '.txt',txt_vec) #保存文本向量

      #先不画图了
      if index >100:continue #只画100张
      x = range(0,len(dict_list))
      y = txt_vec
      plt.plot(x, y)
      plt.savefig(txt2vec_plt_path + '/' + str(index) + '.png')
      # 不清理 figure 将有可能造成在第一幅中 plot 的线再次出现在第二幅图中。
      plt.clf()


# classes = '彩票'
# dict_class = '彩票'
# main(classes,dict_class)

classes_list = ['财经','彩票','房产','股票','家居','教育','科技','社会','时尚','时政','体育test','星座','游戏','娱乐']
dict_class_list = classes_list
# dict_class_list = ['彩票']

start_time = time.time()

for dict_class in dict_class_list:
  for classes in classes_list:
    main(classes,dict_class)
#   break
#测试运行时间
# for classes in classes_list:
#   main(classes,"彩票")
#测试运行时间
# main('彩票',"彩票")


end_time = time.time()
print('程序运行时间为：', end_time - start_time, '秒')