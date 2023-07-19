import pkgs.FileOperations as FileOper
from pkgs.TxtAllIn import txt_AllIn
from pkgs.Segment import segment_
from pkgs.CountFeatures import countFeaturesMain

import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


#第一步文本预处理
def process_txt(classes_path,outPath,allInTxtPaths,segment_words_list_path):

  FileOper.make_dir(outPath)

  # 1、所有文本放在一个txt中，每个文本只保留了中文
  only_chinese_arr = txt_AllIn(classes_path)  #后期的测试为了速度 改为只合并前2000个文本 如果生成词典的话记得修改回去
  FileOper.save_file(allInTxtPaths,only_chinese_arr,'each')

  # 2、分词并去停用词
  segment_words_list = segment_(allInTxtPaths,'read_lines')
  FileOper.save_file(segment_words_list_path, segment_words_list, 'each')




#2、统计
def count_features(segment_words_list_path,outPath):
  countFeaturesMain(segment_words_list_path,outPath)

if __name__ == "__main__":
  # corpusPath = 'I:/onStudying/TextClassify/THUCNews'   #清华语料库
  corpusPath = 'D:/onStudying/TextClassify/THUCNews'   #清华语料库

  # corpusPath = 'I:/onStudying/TextClassify/fudan'
  # outBasePath = 'fudan_res'
  outBasePath = 'res'
  classes = '娱乐'
  classes_path = corpusPath + '/' + classes
  outPath = outBasePath + '/' + classes

  #第一步文本预处理
  allInTxtPaths = outPath + '/allInTxt.txt' 
  segment_words_list_path = outPath + '/segment_words_list.txt'
  process_txt(classes_path,outPath,allInTxtPaths,segment_words_list_path)

  #第二步 统计类内词频、文档内词频、文档内词频均值、文档频率比重 以及TF-DF 生成DF以及词典
  count_features(segment_words_list_path,outPath)

  


