import re

# 单选:C A D A D B B B C B

# 多选：BD  BD  ABCD  ABCD  AC

# 代码第一题
a = [1, 2, 3, 1, 2, 3, 3, 6, 2, 6, 1]
# 列表去重，赋值个新列表b
b = list(set(a))
# 查看列表b中的元素
print(b)
# 计算单一元素出现的次数
print(a.count(1))
print(a.count(2))
print(a.count(3))
print(a.count(6))
# 输出字典1，列出每个元素的个数
dict1 = {"1": 3, '2': 3, '3': 3, '6': 2}
print(dict1)


# 代码第二题
num = 1


def log_in():
    name = input("请输入用户名：")
    password = input("请输入密码：")

    if name == 'seven' and password == '123':
        print("登录成功")
    elif name == 'alex' and password == '456':
        print("登录成功")
    else:
        global num
        num += 1
        if num > 3:
            print("3次机会结束，请5分钟后再次尝试")
            return
        else:
            log_in()


log_in()


# 代码第三题
class Person(object):

    # 保存对象的引用
    instance = None

    # 保存是否进行初始化操作
    whether_init = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if not self.whether_init:
            print("进行初始化")
            self.whether_init = True


xiaoming = Person()
xiaomei = Person()
print(xiaoming)
print(xiaomei)


# 代码第四题
b = []
for i in range(5):
    a = int(input("请输入第%d个整数：" % (i+1)))
    b.append(a)
b.sort(reverse=True)
print(b)


# 代码第五题
S = """se234 1987-02-09 07:30:00
1987-02-10 07:25:00"""

ret = re.findall(r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}', S)
print(ret)
