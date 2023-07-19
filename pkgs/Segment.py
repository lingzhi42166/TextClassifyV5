from multiprocessing.resource_sharer import stop
import jieba 
import pkgs.FileOperations as file_oper

"""
1、分词 
需要注意的是 新词列表路径不能有中文,否则引入自定义词典会卡死
并且文件编码格式必须是UTF-8
2、去除停用词
"""
def load_stopword():
  f_stop = open('stopwords.txt', encoding='utf-8')  # 自己的中文停用词表
  sw = set()
  for line in f_stop:# strip() 方法用于移除字符串头尾指定的字符（默认为空格）
        sw.add(line.strip())
  f_stop.close()
  return sw


def segment_(dataPath,model='normal'):
    stopwords = load_stopword()
    if model == 'read_lines':
        data = file_oper.read_file(dataPath,model)#如果文本太大的话 不要一下子读取进来，读一句 分词一句
        keyList = []
        for s in data: #data=> ["文本1","文本2"]
            se_res = []
            raw_se_res = jieba.lcut(s.strip()) # return [词，词]  strip()去掉使用strip()函数去掉每行结束的\n。 jieba的毛病
            #遍历去除停用词，如果词在停用词表  则过掉
            for key in raw_se_res:
                if key in stopwords:continue #去除停用词列表中的词
                if len(key) == 1 : continue   #1个字符的也去掉
                se_res.append(key)
            keyList.append(se_res)
        return keyList # [[],[],[]]
    elif model == 'normal':
        keyList = jieba.lcut(data)
        return keyList

   
    

# 用于测试
# dataPath = '../Good/财经/AllIn.txt'
# res = segment_(dataPath,'read_lines')
#
# print(res)

