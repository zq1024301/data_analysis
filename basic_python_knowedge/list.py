list1 = [1, 2, 3, 4, 5, 1, 2, 3, 1, 3, 2, 4]
list2 = [1,]  # 当列表只含有一个元素的时候，后面需要加“，”

# 列表元素的增加
# list1.append(6)  # 在列表的末尾添加一个元素
# list1.extend([6, 7])  # 在列表1的基础上追加列表
# list1.extend(list2)  # 在列表1的基础上追加列表（可迭代的变量）
# list1.insert(2, 4)  # 在列表指定的索引位置添加元素

# 列表元素的删除
# a1 = list1.pop()  #删除列表中最后一个元素，并可以返回给一个变量
# a1 = list1.pop(1)  #删除列表中指定索引的元素，并可以返回给一个变量
# list1.remove(2)  #  删除列表中的第一次出现的指定元素
# list1.clear()  #清空列表
# del list1[2]  #删除列表中指定索引的元素

# 列表元素的修改
# list1[2] = 2  # 将指定索引的元素修改

# 列表的查找
# print(list1.index(5))  # 查找元素5在列表中第一次出现时的索引值
# print(list1[5])  # 查找索引为5的元素是什么

# 列表的统计
# print(len(list1))  # 统计列表中含有的元素的个数
# print(list1.count(2))  # 统计指定元素在列表中出现的次数

# 列表的排序
# list1.sort()
# list1.sort(reverse=True)

# 列表的切片
print(list1)
# 选出列表中索引为1-4的元素
# print(list1[1:5])  # 同range一样左闭右开

# 在列表中隔一个数筛选出来
# print(list1[::2])  # a:b:c a为起始切片位置；b为终点切片位置；c为步长

# 将列表中的元素逆序打印出来
# print(list1[::-1])

# 将列表中后四位数打印出来
# print(list1[-4::])

# 将列表中后四位逆序打印出来
print(list1[:-5:-1])

# 列表的遍历
# for i in list1:
#     print(i)

# 列表推导式：[变量 for 变量 in 序列 if 条件] 或 [表达式 for 变量 in 序列 if 条件]
# list3 = [i for i in range(1, 10)]  #生成列表
# list3 = [i*10 for i in range(1, 10)]  #生成列表
# list3 = [i for i in range(1, 10) if i % 2 == 0]  # 1-10(包括1，不包括10）之间的偶数
# list3 = [i for i in range(1, 10) if i % 2]  # 1-10(包括1，不包括10）之间的奇数，==1表示为真，可以不书写
# list3 = [(x, y) for x in range(1, 10) if x % 2 == 0 if x > 2 for y in range(1, 10) if y > 7 if y != 9]

# 列表去重
list3 = []
for i in list1:
    if i not in list3:
        list3.append(i)
print(list3)

print(list(set(list1)))  # 利用类型转换进行去重(集合是不重复的无序序列）

