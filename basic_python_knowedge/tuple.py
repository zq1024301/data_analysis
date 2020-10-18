tutle1 = (1, 2, 3, 4, 2, 4, 5, 6, 1)  # 元组是不可变的，不能进行增删改，常用于函数

# 元组的查找
print(tutle1.index(3))  # 查找元素3在列表中第一次出现时的索引
print(tutle1.index(2, 3))  # 查找元素2在列表中索引>3时第一次出现时的索引

# 元组的统计
print(len(tutle1))
print(tutle1.count(2))  # 统计元素2在元组中出现的次数
