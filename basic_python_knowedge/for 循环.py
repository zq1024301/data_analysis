# for循环输出1-100之间的所有质数
# num = []
# for i in range(2, 101):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         num.append(i)
# print(num)

# 从键盘中输入5个学生的名字，存储到列表中，然后打印出每个学生名字中的第2个字母。
# student = []
# student2 = []
#
#
# def student_input(studenti):
#     """
#     :param studenti: 学生姓名
#     """
#     studenti = input("请输入学生的名字：")
#     if studenti not in student:
#         student.append(studenti)
#         student2.append(studenti[1])
#
#
# def times(a, b):
#     """
#     :param a: 输入几次学生姓名
#     :param b: 任意字符串，用来调用student_input程序
#     """
#     for i in range(a):
#         student_input(b)
#     print(student)
#     print(student2)
#
#
# times(5, '输入5个学生姓名')

# 使用字典来存储一个人的信息（姓名、年龄、学号、QQ、微信、住址等），这些信息来自键盘的输入。
# info = {}
# name = input("请输入姓名：")
# info["姓名"] = name
# age = input("请输入年龄：")
# info["年龄"] = age
# stu_num = input("请输入学号：")
# info["学号"] = stu_num
# print(info)
# for k, v in info.items():
#     print(k, v)

"""
有10个球分别为3红、3蓝、4白，球与球之间只有颜色的差别，
现需要将这10个球放入3个盒子，要求每个盒子至少有一个白球，
其余的球全部随机放，要求输出三个盒子里所有球的颜色，请用程序实现。
"""





"""
现有一字符串a = “abcdefg”，将字符串中的元素逐个输出，
并且在输出的时候如果字母是b则显示B。
"""
a = "abcdefg"
for i in a:
    if i != "b":
        print(i)
    else:
        print(i.upper())





