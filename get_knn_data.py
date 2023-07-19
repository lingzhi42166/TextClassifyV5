import os
import shutil
# 指定目录路径 
dir_path = 'D:\onStudying\TextClassify\THUCNews'
# 目标目录路径
target_dir = 'D:\onStudying\TextClassify\KNN_data'
# 获取指定目录下所有文件夹
dirs = os.listdir(dir_path)
# 遍历每个文件夹
print(dirs)
num = 0;
for dir in dirs:
    # 读取文件夹下所有txt文件
    txt_files = os.listdir(dir_path + '/' + dir)  
    print(dir)
    # 只取前1000个txt文件   前1000[:1000]为训练数据  后1000[1000:2000]为测试数据
    # txt_files = txt_files[:1000]
    # txt_files = txt_files[1000:2000]

    print(len(txt_files))
    # 复制txt文件到目标文件夹
    
    for txt_file in txt_files: 
        
        txt_file = num
        # 源txt文件路径
        src_path = dir_path + '/' + dir + '/' + txt_file
        
        # 目标txt文件路径
        # dst_path = target_dir + '/' + dir + '/train_data'
        # dst_path = target_dir + '/' + dir + '/test_data/' 
        # dst_path = target_dir + '/test_data/' 
        dst_path = target_dir + '/train_data/' 
    
        # 如果目标文件夹不存在,则创建  mkdir无法创建多级目录
        if not os.path.exists(dst_path):
            os.makedirs(dst_path)
        
        to_path = dst_path + '/' + txt_file 
        # 复制文件
        shutil.copy(src_path, dst_path)
        num+=1