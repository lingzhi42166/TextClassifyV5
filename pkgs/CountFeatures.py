import pandas as pd
import pkgs.FileOperations as file_oper
import time
from collections import defaultdict


#1、统计各文本内的特征词词频 及各文本的词频比重 、 以及词频比重均值
def count_txt_key_features(segment_words_list,in_txt_fre_list_path,in_txt_fre_mean_list_path,in_txt_fre_mean_dict_path):#=> [[词，词],[词，词]]
  in_txt_fre_list = []
  in_txt_fre_sg_list = []
  in_txt_fre_mean_dict = {}
  #统计文本内词频
  for txt in segment_words_list:
    txt_dict = {}
    for key in txt:
      txt_dict[key] = txt_dict.get(key,0) + 1
    in_txt_fre_list.append(txt_dict)
  #统计文本内词频比重
  for txt_dict in in_txt_fre_list:
    txt_fre_sg_dict = {}
    txt_key_len = len(txt_dict)
    for key in txt_dict:
      key_sg = txt_dict[key] / txt_key_len 
      txt_fre_sg_dict[key] = key_sg
    in_txt_fre_sg_list.append(txt_fre_sg_dict)

  #统计文本内词频比重均值
  df_len = {}
  for txt_dict in in_txt_fre_sg_list: #[{},{}]
    for key in txt_dict: #1、对词频比重求和
      in_txt_fre_mean_dict[key] = in_txt_fre_mean_dict.get(key,0) + txt_dict[key]
      df_len[key] = df_len.get(key,0) + 1

  for key in in_txt_fre_mean_dict:
    in_txt_fre_mean_dict[key] = in_txt_fre_mean_dict[key] / df_len[key]



  #持久化
  file_oper.save_file(in_txt_fre_list_path,in_txt_fre_list,'each')
  file_oper.save_file(in_txt_fre_mean_list_path,in_txt_fre_sg_list,'each')
  file_oper.save_file(in_txt_fre_mean_dict_path,in_txt_fre_mean_dict)


#2、统计各词项的文档频率 以及文档频率比重
def count_df(in_txt_fre_list_path,doc_len,df_path,df_mean_dict_path):
  in_txt_fre_list = file_oper.read_file(in_txt_fre_list_path,'read_lines_arr')#[{词:tf,词:tf},{}]
  df_dict = {}
  #文档频率
  for txt in in_txt_fre_list:
    for key in txt:
      df_dict[key] = df_dict.get(key,0) + 1

  #文档频率比重
  df_mean_dict = {}
  for key in df_dict:
    df_mean_dict[key] = df_dict[key] / doc_len 

  #持久化
  file_oper.save_file(df_path,df_dict)
  file_oper.save_file(df_mean_dict_path,df_mean_dict)

#3、各词项权重值
def tf_df(in_txt_fre_mean_dict_path,df_mean_dict_path,tf_df_dict_path):
  in_txt_fre_mean_dict = file_oper.read_file(in_txt_fre_mean_dict_path,'read_dict')
  df_mean_dict = file_oper.read_file(df_mean_dict_path,'read_dict')

  tf_df_dict = {}

  for key in df_mean_dict:
    tf_df_dict[key] = in_txt_fre_mean_dict[key] * df_mean_dict[key]
  

  #持久化
  file_oper.save_file(tf_df_dict_path,tf_df_dict)


#4、dataframe
def create_data_frame(in_txt_fre_mean_dict_path,df_mean_dict_path,tf_df_dict_path,dfPath):
  in_txt_fre_mean_dict = file_oper.read_file(in_txt_fre_mean_dict_path,'read_dict')
  df_mean_dict = file_oper.read_file(df_mean_dict_path,'read_dict')
  tf_df_dict = file_oper.read_file(tf_df_dict_path,'read_dict')

  key_list = []
  tf_mean = []
  df_mean = []
  tf_df = []
  for key in in_txt_fre_mean_dict:
    key_list.append(key)
    tf_mean.append(in_txt_fre_mean_dict[key])
    df_mean.append(df_mean_dict[key])
    tf_df.append(tf_df_dict[key])

  data = {'词项':key_list,'词项词频比重均值':tf_mean,'词项文档频率比重':df_mean,'词项权重':tf_df}
  df = pd.DataFrame(data)
  df.to_csv(dfPath)


#5、df降序
def dec_df(dfPath,sorted_df_path):
  df = pd.read_csv(dfPath,index_col=0)
  sorted_df = df.sort_values(by='词项权重',ascending=False)
  sorted_df.to_csv(sorted_df_path)

#6、过滤
def filter_df(sorted_df_path,filtered_path,threshold): 
  df = pd.read_csv(sorted_df_path,index_col=0)
  df[df['词项权重']>threshold].to_csv(filtered_path)

#7、获取特征词和tf-df
def create_dict(filtered_path,key_path,key_tf_df_path,key_df_path):
  df = pd.read_csv(filtered_path,index_col=0)
  df_key_word_ = df['词项'].values
  df_tf_df_ = df['词项权重'].values
  df_df_ = df['词项文档频率比重'].values

  
  df_key_word = []
  df_tf_df = []
  df_df = {}
  for index in range(len(df_key_word_)):
    df_key_word.append(df_key_word_[index])
    df_tf_df.append(df_tf_df_[index])
    df_df[df_key_word_[index]] = df_df_[index]
  
  #持久化
  file_oper.save_file(key_path,df_key_word)
  file_oper.save_file(key_tf_df_path,df_tf_df)
  file_oper.save_file(key_df_path,df_df)



def countFeaturesMain(segment_words_list_path,outPath):
  segment_words_list = file_oper.read_file(segment_words_list_path,'read_lines_arr')
  
  doc_len = len(segment_words_list)
  # print(doc_len) 


  #1、统计各文本的词项词频
  in_txt_fre_list_path = outPath + '/各文本词频.txt' 
  in_txt_fre_mean_list_path = outPath + '/各文本词频比重.txt' 
  in_txt_fre_mean_dict_path = outPath + '/词频比重均值.txt'
  count_txt_key_features(segment_words_list,in_txt_fre_list_path,in_txt_fre_mean_list_path,in_txt_fre_mean_dict_path)

  #2、统计各词项的文档频率 并计算出文档频率比重
  df_path = outPath + '/各词项的文档频率.txt'
  df_mean_dict_path = outPath + '/各词项的文档频率比重.txt'
  count_df(in_txt_fre_list_path,doc_len,df_path,df_mean_dict_path)

  #3、计算权重值
  tf_df_dict_path = outPath + '/各词项tf_df.txt'
  tf_df(in_txt_fre_mean_dict_path,df_mean_dict_path,tf_df_dict_path)


  #4、生成dataFrame
  dfPath = outPath + '/df.csv'
  create_data_frame(in_txt_fre_mean_dict_path,df_mean_dict_path,tf_df_dict_path,dfPath)


  #5、对DF降序
  sorted_df_path = outPath + '/sorted_df.csv'
  dec_df(dfPath,sorted_df_path)

  #6、过滤
  filtered_path = outPath + '/filtered_df.csv'
  filter_df(sorted_df_path,filtered_path,0.0001)

  #7、获取过滤后的词典分别保存为词典和词典tf-df以及df
  key_path = outPath + '/词典.txt'
  key_tf_df_path = outPath + '/特征项权重.txt'
  key_df_path = outPath + '/特征项df.txt'

  create_dict(filtered_path,key_path,key_tf_df_path,key_df_path)