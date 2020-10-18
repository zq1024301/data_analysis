# 1. 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# num = []
# for a in range(1, 5):
#     for b in range(1, 5):
#         for c in range(1, 5):
#             i = a * 100 + b * 10 + c
#             print(i)
#             num.append(i)
#             if a == b or b == c or c == a:
#                 num.remove(i)
# print(num)


# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
# 低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40
# 万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元
# 时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
# I = int(input("请输入当月利润："))
# if I <= 100000:
#     bonus = I * 0.1
# elif 100000 < I <= 200000:
#     bonus = 100000 * 0.1 + (I-100000) * 0.075
# elif 200000 < I <= 400000:
#     bonus = 100000 * 0.1 + 100000 * 0.075 + (I-200000) * 0.05
# elif 400000 < I <= 600000:
#     bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + (I-400000) * 0.03
# elif 600000 < I <= 1000000:
#     bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + (I-600000) * 0.015
# else:
#     bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015 + (I - 1000000) * 0.1
# print(bonus)

"""
3.题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
程序分析：
假设该数为 x。
1、则：x + 100 = n2, x + 100 + 168 = m2
2、计算等式：m2 - n2 = (m + n)(m - n) = 168
3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数
4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。
7、接下来将 i 的所有数字循环计算即可。
"""
# num = []
# for i in range(1, 85):
#     if (i + 168 / i) ** 2 - (i - 168 / i) ** 2 == 168 * 4 and i % 2 == 0 and (168/i) % 2 == 0:
#         num.append(i)
# print(num)
#
#
# nlist = []
# mlist = []
# for j in num:
#     n = (j - 168 / j) / 2
#     m = (j + 168 / j) / 2
#     if n ** 2 - 100 == m ** 2 - 268 and m >0 and n > 0:
#         nlist.append(n)
#         mlist.append(m)
# print(list(set(nlist)))
# print(list(set(mlist)))
#
# xlist = []
# for m in mlist:
#     x = m ** 2 - 268
#     xlist.append(x)
# print(xlist)


"""
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2
时需考虑多加一天：
"""
# str = input("请输入年月日：")
# a = str.split('.')
# nian = int(a[0])
# yue = int(a[1])
# ri = int(a[2])
#
# # 判断是否为闰年
# if nian % 4 == 0 and nian % 100 == 0 or nian % 400 == 0:
#     print("这一年是闰年")
#     if yue == 1:
#         print("%s 是这一年的 %d 天" % (str, ri))
#     if yue == 2:
#         tian = 31 + ri
#         print("%s 是这一年的 %d 天" % (str, tian))
#     if yue == 3:
#         tian = 31 + 29 + ri
#         print("%s 是这一年的 %d 天" % (str, tian))
#     if yue == 4:
#         tian = 31 + 29 + 31 + ri
#         print("%s 是这一年的 %d 天" % (str, tian))
#     if yue == 5:
#         tian = 31 + 29 + 31 + 30 + ri
#         print("%s 是这一年的 %d 天" % (str, tian))
#     if yue == 6:
#         tian = 31 + 29 + 31 + 30 + 31 + ri
#         print("%s 是这一年的 %d 天" % (str, tian))
#     if yue == 7:
#         tian = 31 + 29 + 31 + 30 + 31 + 30 + ri
#         print("%s 是这一年的 %d 天" % (str, tian))
#     if yue == 8:
#         tian = 31 + 29 + 31 + 30 + 31 + 30 + 31 + ri
#         print("%s 是这一年的 %d 天" % (str, tian))
#     if yue == 9:
#         tian = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + ri
#         print("%s 是这一年的 %d 天" % (str, tian))
#     if yue == 10:
#         tian = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + ri
#         print("%s 是这一年的 %d 天" % (str, tian))
#     if yue == 11:
#         tian = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + ri
#         print("%s 是这一年的 %d 天" % (str, tian))
#     if yue == 12:
#         tian = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + ri
#         print("%s 是这一年的 %d 天" % (str, tian))
# else:
#     print("这一年不是闰年")
#     if yue == 1:
#         print("%s 是这一年的 %d 天" % (str, ri))
#     if yue == 2:
#         tian = 31 + ri
#         print("%s 是这一年的 %d 天" % (str, tian))
#     if yue == 3:
#         tian = 31 + 28 + ri
#         print("%s 是这一年的 %d 天" % (str, tian))
#     if yue == 4:
#         tian = 31 + 28 + 31 + ri
#         print("%s 是这一年的 %d 天" % (str, tian))
#     if yue == 5:
#         tian = 31 + 28 + 31 + 30 + ri
#         print("%s 是这一年的 %d 天" % (str, tian))
#     if yue == 6:
#         tian = 31 + 28 + 31 + 30 + 31 + ri
#         print("%s 是这一年的 %d 天" % (str, tian))
#     if yue == 7:
#         tian = 31 + 28 + 31 + 30 + 31 + 30 + ri
#         print("%s 是这一年的 %d 天" % (str, tian))
#     if yue == 8:
#         tian = 31 + 28 + 31 + 30 + 31 + 30 + 31 + ri
#         print("%s 是这一年的 %d 天" % (str, tian))
#     if yue == 9:
#         tian = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + ri
#         print("%s 是这一年的 %d 天" % (str, tian))
#     if yue == 10:
#         tian = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + ri
#         print("%s 是这一年的 %d 天" % (str, tian))
#     if yue == 11:
#         tian = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + ri
#         print("%s 是这一年的 %d 天" % (str, tian))
#     if yue == 12:
#         tian = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + ri
#         print("%s 是这一年的 %d 天" % (str, tian))

# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# x = int(input("请输入一个整数:"))
# y = int(input("请输入一个整数:"))
# z = int(input("请输入一个整数:"))
# if x > y:
#     x, y = y, x
# else:
#     x = x
#     y = y
# if x > z:
#     x, z = z, x
# else:
#     x = x
#     z = z
# if y > z:
#     y, z = z, y
# else:
#     y = y
#     z = z
# print("%d < %d < %d" % (x, y, z))

# 题目：斐波那契数列



# 将一个列表的数据复制到另一个列表中
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# b = [2, 4]
# print(a)
# print(b)
# b = a.copy()
# print(b)

# 将一个列表的数据复制到另一个列表中
# for row in range(10):
#     for col in range(1, row+1):
#         print("%d * %d = %d" % (col, row, col*row), end="\t")
#     print()

# 题目：判断101-200之间有多少个素数，并输出所有素数。
a = []
for i in range(101, 201):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        a.append(i)
print(a)
print(len(a))

