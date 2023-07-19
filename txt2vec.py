import pkgs.FileOperations as file_oper
import ast
import matplotlib.pyplot as plt
 
def main():
    outBasePath = 'res'
    classes = '体育test'
    dict_class = '彩票'
    test_outPath = outBasePath + '/' + classes  
    dict_outPath = outBasePath + '/' + dict_class  

    
    #1、读取文本 （因为放在一起了,所以只需要读取一个，然后遍历）
    txt_path = test_outPath + '/各文本词频比重.txt'
    
    txt_list = file_oper.read_file(txt_path,'read_lines_arr')


    
    # 2、读取词典
    dict_path = dict_outPath + '/词典.txt'
    dict_list = ast.literal_eval(file_oper.read_file(dict_path))

    #3、读取df
    df_path = dict_outPath + '/特征项df.txt'
    df_dict = file_oper.read_file(df_path,'read_dict')

    # 4、文本向量化

    txt2vec_path = test_outPath + '/vec/' + dict_class + 'vec'
    txt2vec_plt_path = test_outPath + '/plt/' + dict_class + 'plt'

    index = 0
    for txt in txt_list:
      index += 1
      txt_vec = []
      for key in dict_list:
        if key not in txt:
          txt_vec.append(0)
          continue
        num = df_dict[key] * txt[key]
        txt_vec.append(num)
      file_oper.save_file(txt2vec_path + '/' + str(index) + '.txt',txt_vec)
      if index >100:continue #只画100张
      x = range(0,len(dict_list))
      y = txt_vec
      plt.plot(x, y)
      plt.savefig(txt2vec_plt_path + '/' + str(index) + '.png')
      # 不清理 figure 将有可能造成在第一幅中 plot 的线再次出现在第二幅图中。
      plt.clf()





main()