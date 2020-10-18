import re

#
#
# def name_def():
#     names = ["age", "_age", "1age", "age1", "a_age", "age_1_", "age!", "a#123", "__________"]
#
#     for name in names:
#         ret = re.match(r'^[a-zA-Z_][A-Za-z0-9_]*$', name)
#         if ret:
#             print("%s 符合变量名规则" % ret.group())
#         else:
#             print("%s 不符合变量名规则" % name)
#
#
# if __name__ == '__main__':
#     name_def()


# email = input("请输入您设置的邮箱账号：")
# ret = re.match(r'[a-zA-Z_0-9]{4,20}@(163|126|qq)\.com$', email)
# if ret:
#     print("%s 符合要求" % ret.group())
# else:
#     print("%s 不符合要求" % email)


# 匹配0-100之间的数字
# print(re.match(r'\d+', '8').group())
# print(re.match(r'\d{1,2}', '88').group())
# print(re.match(r'[1-9]?\d$', '08').group())
# print(re.match(r'[1-9]?\d$|100', '100').group())


# ret = re.match(r'(\d+)-?(\d+)', '010-12345678')
# ret = re.match(r'([^-]*)-?(\d+)', '010-12345678')
#
# print(ret.group(1))
# print(ret.group(2))

# 匹配标签<html>aaa</html>
# print(re.match(r'<(\w+)>.*</\1>', '<html>aaa</html>').group())
# print(re.match(r'<(\w+)><(\w+)>.*</\2></\1>', '<html><b>aaa</b></html>').group())
# print(re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>.*</(?P=name2)></(?P=name1)>', '<html><b>aaa</b></html>').group())

# print(re.search(r'\d+', '阅读次数为234,567').group())  # 仅能返回查到的第一个符合的部分
# print(re.findall(r'\d+', 'python=456, c=234, c++=123'))  # 返回字符串的列表
# print(re.sub(r'\d+', '998', 'python=456'))  # 用998替换456
#
#
# def add(temp):
#     strnum = temp.group()
#     num = int(strnum) + 1
#     return str(num)
#
#
# print(re.sub(r'\d+', add, 'python=456'))
#
#
# print(re.split(r':|,', 'info:zhangsan,25,changsha'))  # 以：或者，分割字符串返回字符串列表


# 贪婪和非贪婪
# print(re.match(r'.*(\d+-\d+-\d+-\d+)', 'this is a num 123-456-789-111').group(1))
# print(re.match(r'.*?(\d+-\d+-\d+-\d+)', 'this is a num 123-456-789-111').group(1))

print(re.match('c:\\\\', 'c:\\a\\b\\c').group())
print(re.match(r'c:\\', 'c:\\a\\b\\c').group())

