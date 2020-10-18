str1 = "s说:'你好'"
str2 = 's说：“你好”'
str3 = "s说:\"你好\""
str4 = 's说:\'你好\''
print(str1)
print(str2)
print(str3)
print(str4)

"""
字符串的基本操作：
判断类型     9种
查找和替换   7种
大小写转换   5种
文本对齐     3种
去除空白字符  3种
拆分和连接   5种
"""

# 字符串的统计
# s1 = "hello world"
# print(len(s1))

# 统计一个子字符串在源字符串出现的次数
# print(s1.count("l"))

# 统计子字符串的位置
# print(s1.index("llo"))  # 返回第一个字符出现时的索引，不存在则报错
# print(s1.find("llo"))  # 如果找到，返回索引值，找不到，返回-1

# 字符串的判断
# 判断空白字符：
# s2 = "   \t\n\r"
# print(s2.isspace())
# 判断数字
# num_str1 = "123"
# print(num_str1.isdecimal())  # 判断全角数字
# num_str2 = "\u00b2"
# num_str3 = '⑵'
# print(num_str1.isdigit())
# print(num_str2.isdigit())  # 判断全角数字，unicode形式的数字及v2打印出来的⑵形式的数字
# print(num_str3.isdigit())
# num_str4 = "一百零一"
# print(num_str1.isnumeric())  # 判断全角数字，unicode形式的数字、⑵及汉字形式的数字
# print(num_str2.isnumeric())
# print(num_str3.isnumeric())
# print(num_str4.isnumeric())

# 判断字符串是否以指定的字符串开头
s1 = "hello world"
print(s1.startswith("hel"))
# 判断字符串是否以指定的字符串开头
print(s1.endswith("ld"))

# 替换字符串
print(s1.replace("world", "python"))  # 字符串是不可变类型，replace生成新的字符串，不改变源字符串

# 大小写转换
s2 = "abFnhJIihklN"
print(s2.upper())
print(s2.lower())

# 文本对齐
poem_list = [
    "\t\n登鹳雀楼",
    "王之涣",
    "白日依山尽\t\n",
    "黄河入海流",
    "欲穷千里目",
    "更上一层楼"
]
# print(poem_list)
# for poem_str in poem_list:
#     print(poem_str)
#
# for poem_str in poem_list:
#     # .strip表示删除两边空白字符 .center表示对齐的宽度以及填充用的字符
#     print(poem_str.strip().center(10, " "))

# 字符串的拆分和连接
poem_str = "\t\n登鹳雀楼  王之涣  白日依山尽\t\n   黄河入海流   欲穷千里目   更上一层楼"
poem_list1 = poem_str.split()  # 按空格将字符串分割成包含多个子字符串的列表
poem_str1 = ','.join(poem_list1)  # 将可迭代数据内的元素用，连接
print(poem_str1)
print(','.join(['1', '2', '3']))
print(','.join('123'))

