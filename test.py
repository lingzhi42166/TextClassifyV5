# 读取指定文本
def read_txt(path,model='normal'):
  global index_list
  txt_ = []
  if model == 'normal':
    with open(path,'r',encoding='utf-8') as f:
      txt = f.read()
      txt = txt.replace('[','')
      txt = txt.replace(']','')
      arr = txt.split(',')
    
      index = -1
      for i in arr: 
        i = i.strip()
        index+=1
        if i == '0':continue
        index_list.append(index)
        txt_.append(float(i))
    
  elif model == 'dict':
    with open(path,'r',encoding='utf-8') as f:
      txt = f.read()
      txt = txt.replace('[','')
      txt = txt.replace(']','')
      arr = txt.split(',')
      index = 0
      
      for i in arr:
        i = i.strip()
        if index in index_list:
          print(i)
          txt_.append(float(i))
        index+=1
  return txt_

if __name__ == '__main__':
  index_list = []
  # x = read_txt('res/星座/vec/彩票vec2/2.txt')
  x = read_txt('res/彩票/vec/彩票vec2/6.txt')

  y = read_txt('res\彩票\特征项权重.txt','dict')
  
  print(range(len(y)))
  x_ = []
  for index in range(len(y)):
    x_.append(y[index] - x[index])

  print(x_)

    
  
  