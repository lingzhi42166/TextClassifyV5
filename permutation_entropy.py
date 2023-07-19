"""
求排列熵
"""
import numpy as np
from math import factorial
import os

# 读取指定文本
def read_txt(path):
  txt_ = []
  with open(path,'r',encoding='utf-8') as f:
      txt = f.read()
      txt = txt.replace('[','')
      txt = txt.replace(']','')
      arr = txt.split(',')
      for i in arr: 
        i = i.strip()
        if i == '0':continue
        
        txt_.append(i)
      
  return txt_

""" 数据持久化 """
def saveFile(path,data):
  f = open(path,'w+',encoding='utf-8')
  for i in data:
    f.write(str(i) +'\n')

  f.close()

def permutation_entropy(time_series, order=3, delay=1, normalize=False):
    x = np.array(time_series)  #x = [4, 7, 9, 10, 6, 11, 3]
    hashmult = np.power(order, np.arange(order))  #[1 3 9]
    # np.power()用于数组元素求n次方。
    # hashmult = np.power(np.arange(order),order )  #[0 1 8]

    # print(hashmult)

    #_embed的作用是生成上图中重构后的矩阵
    #argsort的作用是对下标排序，排序的标准是值的大小
    #比如第3行[9,10,6] 9的下标是0 6是2....， 6最小
    #所以排序后向量的第一个元素是6的下标2... 排完[201]
    # 我们发现argsort()函数是将x中的元素从小到大排列，提取其对应的index(索引)，然后输出到y 
    sorted_idx = _embed(x, order=order, delay=delay).argsort(kind='quicksort')
    # num = 0
    # for i in range(len(sorted_idx)):
    #   if(str(sorted_idx[i])=='[2 1 0]'):continue
    #   num+=1
    # print(num)
    # saveFile('sort.txt',sorted_idx)
    # print(np.array([0,0,0]).argsort(kind='quicksort')) [0 1 2]
    #np.multiply 对应位置相乘  hashmult是1 3 9  sum是求每一行的和
    #hashmult一定要保证三个一样的值顺序不同 按位乘起来后 每一行加起来 大小不同 类似赋一个权重
    hashval = (np.multiply(sorted_idx, hashmult)).sum(1)  #[21 21 11 19 11]  sum(1) 求数组每一行的和

    # print(np.multiply(sorted_idx, hashmult))
    # Return the counts
    """  函数是去除数组中的重复数字，并进行排序之后输出。 return_count为True时：会构建一个递增的唯一值的新列表，并返回新列表c 中的值在旧列表中的个数 counts """
    _, c = np.unique(hashval, return_counts=True)  #重小到大 每个数字出现的次数  #c是[2 1 2]  最小的11出现了2次 19 1次

    """ np.true_divide 将第一个数组中的数组元素除以第二个数组中的元素(所有操作均按元素进行)。 arr1和arr2必须具有相同的形状。按元素返回真除法。 """
    p = np.true_divide(c, c.sum())# 每种排列的概率
    # print(c.sum())
    pe = -np.multiply(p, np.log2(p)).sum()  #根据公式
    if normalize:#如果需要归一化
        pe /= np.log2(factorial(order))
    return pe


#将一维时间序列，生成矩阵
def _embed(x, order=3, delay=1):
    """Time-delay embedding.

    Parameters
    ----------
    x : 1d-array, shape (n_times)
        Time series
    order : int
        Embedding dimension (order)
    delay : int
        Delay.

    Returns
    -------
    embedded : ndarray, shape (n_times - (order - 1) * delay, order)
        Embedded time-series.
    """
    N = len(x)
    Y = np.empty((order, N - (order - 1) * delay)) #行 列 给定shape返回一个一维或者多维数组，数组的元素不为空，为随机产生的数据。 
    # print(Y)
    for i in range(order):
      # print(i * delay + Y.shape[1])
      Y[i] = x[i * delay:i * delay + Y.shape[1]]
      # print(len(Y[i])) #49326
    # print(Y.T[592])   #利用转置 巧妙的生成三列的矩阵
    # saveFile('Y_T.txt',Y.T)
    return Y.T


if __name__ == '__main__':

    
    path = "res/彩票/vec/vec1" #文件夹目录
    files= os.listdir(path) #得到文件夹下的所有文件名称
    
    res_list = []
    for txt in files:
      x = read_txt(path + '/' + txt)
      res = permutation_entropy(x, order=3, normalize=True)
      res_list.append(res)
    # x = read_txt('e/文本0的归一化TF-IDF.txt')
    # x = read_txt('res/彩票/vec/彩票vec2/6.txt')
    # x = read_txt('res/星座/vec/彩票vec2/6.txt')

    
    print(res_list)
    # num = 0
    # for index in res_list:
    #   if index >=0.8:
    #     num+=1
    # print(num)
    # print(permutation_entropy(x, order=3, normalize=True))