import random
import time
# day1 第一个程序
print("hello world")  # 重新运行 ctrl+f5

# 注释
# 单行注释（#后空一格）

"""

多行注释

"""

# 算术运算符： + - * / **（幂运算） //(整除） %（取余）
print("*" * 20)  # 字符串的拼接  ********************
print("-" + "+")  # 字符串的拼接  -+

# 变量
"""
变量的命名
1、以字母，下划线，数字组成
2、不能以数字开头，不能与关键字重复
3、用=进行变量的赋值
4、类名遵循大驼峰规则，即首字母大写；函数遵循小驼峰规则，即第二个单词首字母大写
"""

"""
变量的类型：
1、数值型：整型（int），浮点型（float），布尔型：True /= 0; False = 0，复数型（complex）
2、非数值型：字符串（str），列表[]，元组()：元素不重复，字典{}，集合
type("2")  # 用于查看变量类型
"""

"""
变量的输入
input("请输入一个整数：")  # input输入的内容为字符串型
int(input("请输入一个数字"))  # 将input输入的内容转化为整型 float()转换为浮点型
"""

'''
变量的格式化输出
print('格式化操作字符串' % 变量)
print('格式化操作字符串' % (变量1,变量2))
%s 字符串; %d 整数; %f 浮点数; %% 百分号

输出我的名字叫小明，请多关照
name = "小明"
print('我的名字叫 %s' % name)

输出我的学号是000001
student_number = 1
print('我的学号是 %06d' % student_number)

输出数据比例是10.00%
num = 0.1
print("输出数据比例是 %.2f%%" % (num*100))
'''

# 个人名片的输入
# name = input('请输入你的姓名：')  # ctrl+d 快速复制上一行的内容
# company = input('请输入你的公司：')
# title = input('请输入你的职位：')
# phone = input('请输入你的电话：')
# email = input('请输入你的邮箱：')
#
# print('*'*20)
# print(company)
# print()
# print('%s(%s)' % (name, title))
# print()
# print('电话：%s' % phone)
# print('邮箱：%s' % email)
# print('*'*20)

# has_ticket = True
# knife_length = int(input("请输入刀的长度："))
# if has_ticket:
#     print("有车票，允许进入安检")
#     if knife_length >= 20:
#         print("刀长%d，超过20厘米，不允许上车" % knife_length)
#     else:
#         print('刀长%d未超过20厘米，不允许上车'% knife_length)
# else:
#     print("没有车票，不允许进门")


# num = random.randint(1, 9)
# num = random.random()  # 随机生成0-1的小数

# 初始条件的设置——计数器
# while 条件1（判断计数器是否达到目标次数）:
#     条件满足时做的事情1
#     条件满足时做的事情2
#     条件满足时做的事情3
#     （。。。。）
#     while 条件2（判断计数器是否达到目标次数）:
#         条件满足时做的事情1
#         条件满足时做的事情2
#         条件满足时做的事情3
#         （。。。。）
#         处理条件2
#     处理条件1

# 计算0-100的和
# i = 0
# s = 0
# while i <= 100:
#     s += i
#     i += 1
# print(s)

# 计算0-100偶数和
# i = 0
# s = 0
# while i <= 100:
#     s += i
#     i += 2
# print(s)
#
# i = 0
# s = 0
# while i <= 100:
#     if i % 2 == 0:
#         s += i
#     i += 1
# print(s)


'''
*
**
***
****
*****
'''
# row = 1
# while row <= 5:
#     col = 1
#     while col <= row:
#         print("*", end='')
#         col += 1
#     print()
#     row += 1


# 打印九九乘法表
# row = 1
# while row <= 9:
#     col = 1
#     while col <= row:
#         print('%d * %d = %d' % (col, row, col*row), end='\t')
#         col += 1
#     print()
#     row += 1

'''
列表：[] 索引从0开始
list1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
增加元素(3)
list1.append(6)  # 在末尾添加元素6
list1.insert(3, 9)  # 在索引为3的位子上添加元素9
list1.extend("1")  #extend需要添加可以迭代的数据（即可以遍历的数据类型）
list1.extend((1,))

删除元素
list1.remove(2)  # 删除第一个出现的元素2
list1.pop(0)  # 删除该索引位置上的元素
list1.clear() # 清数所有元素
del list1   # 删除列表

查找元素
print(list1.index(1, 4)) # 从索引为4的位子开始往后找到的第一个元素1的索引值
print(list1[3])  # 查找索引为3的元素是什么

修改元素
list1[3] = 3

列表的统计方法
list1.sort()  # 升序排列
list1.sort(reverse=True)  # 降序排列
print(list1)  #sort在源列表进行修改，结果需打印源列表
print(list1.count(1))  # 查找元素1在列表中出现的次数
print(len(list1))  # 统计列表中元素的个数

循环遍历
for i in list1:
    print(i)

列表的切片
选出列表中索引为1-4的元素
print(list1[1:5])
在列表中隔一个数筛选出来
print(list1[::2])
将列表中的元素逆序打印出来
print(list1[::-1])
将列表中后四位数打印出来
print(list1[-4::])
将列表中后四位逆序打印出来
print(list1[:-5:-1])

列表推导式
[表达式 for 变量 in 容器]
[表达式 for 变量 in 容器 if 条件]
num_list = [i for i in range(1, 11)]
num_list = [i*10 for i in range(1, 11)]
num_list = [i for i in range(1, 11) if i % 2 == 0]

num_list = [(x, y) for x in range(1, 11) if x % 2 if x > 3
            for y in range(1, 11) if y == 9]

print(num_list)  # [(5, 9), (7, 9), (9, 9)] 1-10之间的奇数，==1表示为真，可以不书写
'''

# range生成1-9的数字
# for row in range(1, 10):
#     for col in range(1, row+1):
#         print('%d * %d = %d' % (col, row, col*row), end='\t')
#     print()

'''
tutle1 = (1, 2, 3, 4, 2, 4, 5, 6, 1)  # 元组是不可变的，不能进行增删改，常用于函数
tutle2 = (1, )
print(tutle1.count(1))
print(tutle1.index(2))
for i in tutle1:
    print(i)
'''

'''
# 列表是有序的对象集合，字典是无序的对象集合，使用键值对存储数据，
# 键(key)是索引，值(value)是数据，字典的键必须是唯一的
dict1 = {'name': 'zhaoqian', 'tile': 'stdent', 'age': 25}
dict2 = {'name': 'kaixin', 'weight': 50}

# 取值
print(dict1['name'])  # 如果key不存在会报错
print(dict1.get('name'))  # 如果key不存在不会报错

# 增加、修改
dict1['age'] = 26  # 如果key存在修改原来的值，不存在新建键值对
dict1.setdefault('gender', 'female')  # 如果key存在不会修改原来的值，不存在新建键值对
dict1.update(dict2)  # 将字典2中的值合并到字典1，如果有相同的键，会覆盖掉原来的

# 删除
# dict1.pop('name')  # 删除指定的键值对，不存在报错
# dict1.popitem()  # 随机删除键值对，一般最后一个
# dict1.clear()  # 清空键值对
# del dict1['age']  # 删除指定的键值对，不存在报错

print(dict1.keys())  # 获取所有的键的列表
print(dict1.values())  # 获取所有的值的列表
print(dict1.items())  # 获取所有的键值对(key, value)的元组列表

# 字典的循环遍历
for k, v in dict1.items():
    print(k, v)

# 字典的运用
card_list = [{'name': 'lili', 'age': 18},
             {'name': 'liri', 'age': 20}]

for i in card_list:
    print(i['name'])
'''

'''
列表去重
l1 = [1, 2, 3, 4, 5, 2, 3, 4]
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)

print(list(set(l1)))
'''
'''
集合是一个无序的不重复的序列
创建空集合用set()
param = {1, 2, 3}
# 增加
param.add(4)
param.update([5, 6, 7])  # 同extend，添加可迭代的数据
print(param)

# 删除
param.remove(9)  # 删除的元素不存在会报错
param.discard(9)  # 删除的元素不存在不会报错
'''


'''
print("\'你好\'")
print('\"你好\"')
s1 = 'hello world'
字符串的统计操作
print(len(s1))  # 统计字符串的长度
print(s1.count('l'))  # 统计子字符串出现的次数
print(s1.index('llo'))  # 统计子字符串第一个字母的索引

判断类型
str1 = '   \n\t\r'
print(str1.isspace())  # 判断是否为空白字符，全为空才为True

num1 = '1234'
num2 = '\u00b2'
num3 = '⑵'
num4 = '一百零一'
print(num1.isdecimal())  # 判断阿拉伯数字
print(num2.isdigit())  # 判断阿拉伯数字，\u00b2，⑵
print(num3.isdigit())
print(num4.isnumeric())  # 判断阿拉伯数字，\u00b2，⑵，汉字数字

print(s1.startswith('hello'))  # 判断字符串是否以指定的字符串开头
print(s1.endswith('world'))  # 判断字符串是否以指定的字符串结尾

查找和替换
print(s1.find('llo'))  # 查找指定的字符串，返回索引值，不存在返回-1
print(s1.replace('world', 'python'))  # 字符串不可变，replace执行后不改变原来的，生成一个新的字符串

大小写转换
world_str = 'aBcdE'
print(world_str.upper())  # 全部转换成大写
print(world_str.lower())  # 全部转换成小写
文本对齐/去处空白字符
poem_list = ['\t\n登鹳雀楼',
             '王之涣', '白日依山尽\t\n',
             '黄河入海流', '欲穷千里目', '更上一层楼']
for poem_str in poem_list:
    print(poem_str.strip().center(10, ' '))  
strip去除左右两边的空白字符
center居中对齐 10=width ' '以空格进行填充
拆分和连接
poem_str = "\t\n\t\n登鹳雀楼   王之涣   白日依山尽\t\n黄河入海流  \t\n欲穷千里目    \t\t更上一层楼"
print(poem_str)

poem_list = poem_str.split()
print(poem_list)  # 将字符串按空白拆分成字符串列表

poem_join = ','.join(poem_list)
print(poem_join)  # 将列表中的字符串用，连接
循环和切片同列表操作
'''

'''
def sum_2_num(num1, num2):
    """
    求和
    :param num1: 形式参数1，数字1
    :param num2: 形式参数2，数字2
    :return: 返回两个数字的和
    """

    return num1 + num2


print(sum_2_num(5, 7))
'''


# def print_line(char, times):
#     print(char * times)
#
#
# def print_lines(char, times):
#     for i in range(5):
#         print_line(char, times)
#
#
# print_lines("*", 20)

'''
def change(num):
    num = 100
    print('%s 的id是 %s' % (num, id(num)))


g_num = 10
change(g_num)
print('%s 的id是 %s' % (g_num, id(g_num)))
'''

'''
def change(num):
    global g_num
    g_num = 100

    print('%s 的id是 %s' % (num, id(num)))


g_num = 10
change(g_num)
print('%s 的id是 %s' % (g_num, id(g_num)))
'''

'''
def change(num_list):
    num_list.extend([1, 2, 3])
    print('%s 的id是 %s' % (num_list, id(num_list)))


g_num_list = [4, 5, 6]
change(g_num_list)
print('%s 的id是 %s' % (g_num_list, id(g_num_list)))
'''

'''
缺省参数
def student(name, weight, title='', gender=True):
    gender_text = '男'
    if not gender:
        gender_text = '女'

    print("%s%s是%s，体重%s" % (title, name, gender_text, weight))


student('小明', 50, '班长')
student('小美', 50, '班长', False)
student('小美', 50, gender=False)

'''

'''
def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


demo(1, 2, 3, 4, 5, name='judy', age=19)


def demo(*args, **kwargs):
    print(args)
    print(kwargs)


a = (1, 2, 3, 4)
b = {'name': 'lily', 'age': 19}
demo(*a, **b)


def demo(*args):
    num = 0
    for i in args:
        num += i
    return  num


print(demo(1, 2, 3, 4))
'''

'''
def num_print(num):
    print(num)
    if num == 1:
        return
    num_print(num-1)


num_print(4)


def sum_num(num):
    if num == 1:
        return 1
    return num + sum_num(num-1)


print(sum_num(3))
'''

'''
# lambda [arg1,[arg2..]]: expression
ret = lambda x, y: x + y
print(ret(2, 3))

infos = [{'name': 'lily', 'age': 10},
         {'name': 'libai', 'age': 20},
         {'name': 'liqian', 'age': 15}]

infos.sort(key=lambda x: x['age'])
print(infos)


def demo(a, b, func):
    ret = func(a, b)
    return ret


num = demo(11, 22, lambda x, y: x + y)
print(num)

'''

'''

# 闭包：函数的嵌套
# 1.在函数的内部再定义一个函数
# 2.外层函数的参数在内层函数中被引用
# 3.外层函数返回内层函数的引用
# 将这个函数以及使用到的变量称之为闭包


def test(num):
    def test_in(num_in):
        print("在函数test_in中 num_in是%d" % (num_in))
        return num_in + num
    return test_in


ret = test(20)
print(ret(50))


def num(a, b):

    def line(x):
        return a*x + b

    return line


line1 = num(2, 3)
print(line1(3))


def count(start=0):

    def inner():
        nonlocal start
        start += 1

        return start

    return inner


c = count()
print(c())
print(c())
'''


'''
def makeBold(fn):

    def wrapped():
        return '<b>' + fn() + '</b>'

    return wrapped


def makeItalic(fn):

    def wrapped():
        return '<i>' + fn() + '</i>'

    return wrapped


@makeBold
@makeItalic
def test():
    return 'hello world'


print(test())


# 不带参数的装饰器


def timefunc(func):

    def wrapper():
        print("%s called at %s" % (func.__name__, time.ctime()))
        func()

    return wrapper


@timefunc
def foo():
    print("i'm foo")


foo()


# 带参数的装饰器
def timefunc(func):

    def wrapper(a, b):
        print("%s called at %s" % (func.__name__, time.ctime()))
        print(a, b)
        func()

    return wrapper


@timefunc
def foo():
    print("i'm foo")


foo(2, 3)


def timefunc(func):

    def wrapper(a, b):
        print("%s called at %s" % (func.__name__, time.ctime()))
        print(a, b)
        func(a, b)

    return wrapper


@timefunc
def foo(a, b):
    print(a + b)


foo(2, 3)

def timefun_arg(pre = 'hello'):

    def timefun(func):

        def wrapped_func():
            print("%s called at %s %s" % (func.__name__, time.ctime(), pre))
            return func()

        return wrapped_func

    return timefun


@timefun_arg("sixstar")
def foo():
    print("i'm foo")


foo()

'''

# class 类名():
#
#     def 方法1(self, 参数列表):
#         pass
#
#     def 方法2(self, 参数列表):
#         pass
#
# 对象名 = 类名()
#
#
# class Cat():
#
#     def __init__(self, name, age):
#         print("初始化方法")
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print("%s爱吃鱼" % self.name)
#
#     def drink(self):
#         print("%s爱喝水" % self.name)
#
#
# # 创建对象的时候会自动调用__init__方法
# jiafei = Cat('jiafei', 6)
# tom = Cat('tom', 8)
# jiafei.drink()
# jiafei.eat()
# tom.eat()
#
#
# class Cat():
#     def __init__(self, name):
#         self.name = name
#         print("%s来了" % self.name)
#
#     def __del__(self):
#         print("%s走了" % self.name)
#
#
# tom = Cat("tom")
# print("*" * 50)

#
# class Cat():
#     def __init__(self, name):
#         self.name = name
#         print("%s来了" % self.name)
#
#     def __del__(self):
#         print("%s走了" % self.name)
#
#     def __str__(self):  # 必须返回字符串
#         return "我的名字是%s" % self.name
#
#
# tom = Cat("tom")
# print(tom)
# del tom
# print("*" * 50)


# class Person():
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
#     def run(self):
#         print("运动减肥，一次减0.5kg")
#         self.weight -= 0.5
#
#     def eat(self):
#         print("吃东西长肉，一次长1kg")
#         self.weight += 1
#
#     def __str__(self):
#         return "%s的体重现在是%.2f" % (self.name, self.weight)
#
#
# xiaoming = Person("小明", 75)
# xiaoming.eat()
# xiaoming.run()
# xiaoming.eat()
# print(xiaoming)


# class HouseIteam():
#     def __init__(self, name, area):
#         self.name = name
#         self.area = area
#
#     def __str__(self):
#         return "%s占地%.2f平米" % (self.name, self.area)
#
#
# bed = HouseIteam("席梦思", 4)
# chest = HouseIteam("衣柜", 2)
# table = HouseIteam("餐桌", 2.5)
# print(bed)
# print(chest)
# print(table)
#
#
# class House():
#     def __init__(self, house_type, total_area):
#         self.house_type = house_type
#         self.total_area = total_area
#         self.houseitem_list = []
#         self.free_area = self.total_area
#
#     def add_item(self, item):
#         if item.area > self.free_area:
#             print("%s太大，无法摆放")
#             return
#
#         self.houseitem_list.append(item.name)
#         self.free_area -= item.area
#
#         print("成功添加%s" % item.name)
#
#     def __str__(self):
#         return "户型：%s\n总面积：%.2f\n剩余面积：%.2f\n家具名称列表：%s" % (self.house_type, self.total_area, self.free_area, self.houseitem_list)
#
#
# house = House("两室一厅", 50)
# house.add_item(bed)
# house.add_item(chest)
# house.add_item(table)
# print(house)


# class Girl:
#     def __init__(self, name):
#         self.name = name
#         # 定义私有属性
#         self.__age = 18
#
#     # 定义私有方法
#     def __secret(self):
#         print("我的年龄是%d" % self.__age)
#
# xiaomei = Girl("小美")
# print(xiaomei.name)
#
# # 私有属性和私有方法在外部无法直接查看
# # xiaomei.__secret()
# # print(xiaomei.__age)
#
# # 但可以通过以下方法查看
# print(xiaomei._Girl__age)
# xiaomei._Girl__secret()

# class Animal(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print("eat")
#
#     def drink(self):
#         print("drink")
#
#
# class Dog(Animal):  # 继承自animal类
#
#     def eat(self):
#         super().eat()  # 扩展eat功能，除了吃，还最爱啃骨头
#         print("最爱啃骨头")
#
#     def drink(self):  # 重写父类的drink功能
#         print("喝水伸舌头")
#
#     def bark(self):  # 除了父类功能还有自己的功能
#         print("bark")
#
#
# class Cat(Animal):  # 猫类也继承自animal，并完全继承，无自身特点
#     pass
#
#
# beibei = Dog("贝贝")
# beibei.eat()
# beibei.drink()

# class Person(object):
#
#     def __init__(self, name):
#         self.name = name
#         self.__age = 18
#
#     def __secret(self):
#         print("%s的年龄是%d" % (self.name, self.__age))
#
#     def spy(self):
#         print("%s的年龄是%d" % (self.name, self.__age))
#         self.__secret()
#
#
# class Girl(Person):
#     pass
#
#
# xiaomei = Girl("小美")
# print(xiaomei.name)
# xiaomei.spy()


# class A(object):
#
#     def test(self):
#         print("A-TEST")
#
#     def demo(self):
#         print("A-DEMO")
#
#
# class B(object):
#
#     def test(self):
#         print("B-TEST")
#
#     def demo(self):
#         print("B-DEMO")
#
#
# class C(A, B):
#     pass
#
# c = C()
# c.test()
# c.demo()


# class Dog(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def game(self):
#         print("play")
#
#
# class Xiaotiandog(Dog):
#
#     def game(self):
#         print("play in the sky")
#
#
# class Person(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def play(self, dog):
#         print("%s play with %s" % (self.name, dog.name))
#         dog.game()
#
# xiaoming = Person("小明")
# wangcai = Dog("旺财")
# xiaotianquan = Xiaotiandog("飞天旺财")
# xiaoming.play(wangcai)
# xiaoming.play(xiaotianquan)


# class Tool(object):
#
#     # 以赋值的方式定义类属性
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#
#         # 针对类属性进行+1操作
#         Tool.count += 1
#
#     # 定义类方法
#     @classmethod
#     def show_tool_count(cls):
#         print("工具对象的总数为%s" % cls.count)
#
#     # 定义静态方法：不调用类方法和实例方法。不访问类属性和实例属性时使用静态方法
#     @staticmethod
#     def show_name():
#         print("这是一个工具类")
#
#
# tool1 = Tool("剪刀")
# tool2 = Tool("锤子")
# tool3 = Tool("钳子")
# print(Tool.count)
# Tool.show_name()
# Tool.show_tool_count()


# class MusicPlayer(object):
#
#     # 赋予一个类属性，保存对象的引用
#     instance = None
#
#     # 定义一个对象保存是否进行过初始化操作
#     init_flag = False
#
#     # 判断对象的引用是否被保存，没有则调用__new__函数返回引用，已保存则不改变
#     def __new__(cls, *args, **kwargs):
#         if cls.instance is None:
#             cls.instance = super().__new__(cls)
#
#         return cls.instance
#
#     # 所有对象仅调用一次初始化方法
#     def __init__(self):
#         if not MusicPlayer.init_flag:
#             print("初始化方法")
#             MusicPlayer.init_flag = True
#
#
# player1 = MusicPlayer()
# player2 = MusicPlayer()
# print(player1)
# print(player2)


# class Game(object):
#
#     top_score = 0
#
#     def __init__(self, player_name):
#         self.name = player_name
#
#     @staticmethod
#     def show_help():
#         print("这是游戏的帮助")
#
#     @classmethod
#     def show_top_score(cls):
#         print("历史最高分是%s" % cls.top_score)
#
#     def start_game(self):
#         print("%s开始游戏" % self.name)
#         Game.top_score = 90
#         print("游戏结束")
#
#
# Game.show_help()
# Game.show_top_score()
# xiaoming = Game("小明")
# xiaoming.start_game()
# Game.show_top_score()

# 捕获异常
# 捕获异常try:
#     num = int(input("请输入一个数："))
#     ret = 30/num
#     print(ret)
# except ValueError:
#     print("请输入一个数字")
# except ZeroDivisionError:
#     print("除数不能为0")
# except Exception as e:
#     print("未知错误：%s" % e)
# # 只有当程序没有异常的时候才会执行
# else:
#     print("正常执行程序")
# # 不管程序是否有异常均会执行
# finally:
#     print("程序执行完成")


# 抛出异常
# def set_pwd():
#
#     pwd = input("请输入密码：")
#
#     if len(pwd) >= 6:
#         return pwd
#
#     error_pwd = Exception("密码长度不够六位")
#     raise error_pwd
#
#
# try:
#     user = set_pwd()
#     print(user)
# except Exception as e:
#     print("发现错误：%s" % e)


# def demo1():
#     return int(input("请输入一个数字:"))
#
#
# def demo2():
#     return demo1()
#
#
# demo2()
#
# try:
#     print(demo2())
# except Exception as e:
#     print("未知错误：%s" % e)


# def set_pwd():
#
#     pwd = input("请输入密码：")
#
#     if len(pwd) >= 6:
#         return pwd
#
#     error_pwd = Exception("密码长度不够六位")
#     raise error_pwd
#
#
# if __name__ == '__main__':
#
#     try:
#         user = set_pwd()
#         print(user)
#     except Exception as e:
#         print("发现错误：%s" % e)


# f = open("1.txt", 'r', encoding="utf-8")  # open默认以只读的方式打开文件,当打开不存在的文件时会报错
# f_write = open("2.txt", 'w', encoding="utf-8")  # write当文件不存在时会新建文件
#
# b = f.read()  # 再一次运行中光标从头运行到结尾，所以再次读取会读取不到内容
# f_write.write(b)  # 复制粘贴
# f_write.write("你好")  # 在结尾处接着写入
#
#
# f.close()
# f_write.close()

# f = open("1.txt", encoding="utf-8")
# f_write = open("4.txt", "w", encoding="utf-8")
#
# while True:
#     text = f.readline()
#
#     if not text:
#         break
#
#     f_write.write(text)  # 按行复制
#     # print(text, end='')
#
#
# f.close()
# f_write.close()


