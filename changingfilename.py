import re
import os
import hashlib


path = r"" #文件夹目录

s = []
#x = '.bt.xltd'
x = '[JYFanSub]'

def main1(path1):
    files = os.listdir(path1)  # 得到文件夹下的所有文件名称
    for file in files: #遍历文件夹
        if os.path.isdir(path1 + '\\' + file):
            main1(path1 + '\\' + file)
        else:
            files2 = os.listdir(path1 + '\\')
            #if not os.path.isdir(str(files2)):
            for file1 in files2:
                if x in file1:
                    #用‘’替换掉 X变量
                    n = str(path1 + '\\' + file1.replace(x,''))
                    n1 = str(path1 + '\\' + str(file1))
                    try:
                        os.rename(n1, n)
                        print(n)
                    except IOError:
                        continue

main1(path)


#此函数待修改 误用
def main2(path1): #只保留文件名的数字
    files = os.listdir(path1)  # 得到文件夹下的所有文件名称
    for file in files: #遍历文件夹
        if os.path.isdir(path1 + '\\' + file):
            main1(path1 + '\\' + file)
        else:
            files2 = os.listdir(path1 + '\\')
            for file1 in files2:
                x = file1.split(".")[0]
                x1 = file1.split(".")[-1]
                n = str(path1 + '\\' + x + x1)#新名
                n1 = str(path1 + '\\' + str(file1))#原名
                try:
                    os.rename(n1, n)
                except IOError:
                    continue
#main2(path)




#获得文件的MD5
def get_md5_02(file_path):
    f = open(file_path, 'rb')
    md5_obj = hashlib.md5()
    while True:
        d = f.read(8096)
        if not d:
            break
        md5_obj.update(d)
    hash_code = md5_obj.hexdigest()
    f.close()
    md5 = str(hash_code).lower()
    print(md5)




