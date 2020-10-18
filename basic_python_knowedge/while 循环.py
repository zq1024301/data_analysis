"""
使用while循环计算1~100的累积和（包含1和100）,但要求跳过所有个位为3的数。
"""
# num = 1
# sum = 0
# while num <= 100:
#     if num % 10 == 3:
#         num += 1
#         continue
#     print(num)
#     sum += num
#     num += 1
# print("1-100的和为:%d" % sum)


"""
从键盘获取一个数字，然后计算它的阶乘，例如输入的是3，
那么即计算3!的结果，并输出
"""
# num = int(input("请输入一个整数"))
# num0 = 1
# product = 1
# while num0 <= num:
#     product *= num0
#     num0 += 1
# print("您输入的数的阶乘为：%d" % product)


"""
使用while循环输出如下图形：（必须使用双重while循环实现）
*
* *
* * *
* * * *
* * * * *
"""

# 方法一
# i = 1
# while i <= 5:
#     print("*"*i)
#     i += 1

# 方法二
# row = 1
# while row <= 5:
#     col = 1
#     while col <= row:
#         print("*", end='')  # end=''表示打印完成后不换行，默认print换行
#         col += 1
#     print()  # 内循环执行完成后换行
#     row += 1


"""
使用while循环输出如下图形：（必须使用双重while循环实现）
    *
   * *
  * * *
 * * * *
* * * * *
"""
# row = 1
# while row <= 5:
#     print(" " * (5 - row), end='')
#     col = 1
#     while col <= row:
#          print("* ", end='')
#          col += 1
#     print()
#     row += 1


# 求 1+2!+3!+...+20! 的和
# sum = 0
#
# j = 1
# while j <= 20:
#     i = 1
#     product = 1
#     while i <= j:
#         product *= i
#         i += 1
#     sum += product
#     j += 1
# print("1+2!+3!+...+20! 的和为:%d" % sum)


"""
本金10000元存入银行，年利率是千分之三。
每过1年，将本金和利息相加作为新的本金。
计算5年后，获得的本金是多少？
"""
benjin = 10000
year = 1
while year <= 5:
    benjin *= 1.003
    year += 1
print("5年后获得的本金是:%.2f" % benjin)
