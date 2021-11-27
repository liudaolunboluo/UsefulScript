import sys
import os


def is_chinese(string):
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True

    return False


path = sys.argv[1]
if len(path) == 0:
    print("请输入要扫描的路径")
    exit()
chinese_list = []
for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        result = os.path.join(dirpath, filename)
        if str(result).endswith('.java') | str(result).endswith('.xml'):
            f = open(str(result), 'r')
            lines = f.readlines()
            count = 0
            for line in lines:
                count = count + 1
                if is_chinese(line):
                    chinese_list.append(str(result) + '：第' + str(count) + '行出现了中文')

if len(chinese_list) == 0:
    print(path + '目录下没有Java文件或者Xml文件出现了中文')
else:
    print(path + '目录下:' + '\n' + '\n'.join(chinese_list))
