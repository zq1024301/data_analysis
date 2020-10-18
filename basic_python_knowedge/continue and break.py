import random

"""
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，
其各个位上数字的立方和等于该数本身。例如：153是一个”水仙花数"，
因为153=1的三次方＋5的三次方＋3的三次方。
"""
# i = 100
# while i < 1000:
#     i1 = i // 100
#     i2 = i % 100 // 10
#     i3 = i % 100 % 10
#     if i != i1 * i1 * i1 + i2 * i2 * i2 + i3 * i3 * i3:
#         i += 1
#         continue
#     print(i)
#     i += 1

# 设计“过7游戏”的程序, 打印出1-100之间除了含7和7的倍数之外的所有数字
# i = 1
# while i <= 100:
#     if i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
#         i += 1
#         continue
#     print(i)
#     i += 1

"""
使用while，完成以下图形的输出。（每一行的星星不能用*乘以星星的数量来完成，须使用while嵌套）(较难)
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""
# row = 1  # 定义行数
# count = 1  # 定义当行的星星数
# while row <= 9:
#     if row != 1:
#         if row <= 5:
#             count += 2
#         else:
#             count -= 2
#     col = 1
#     while col <= count:
#         if col == 1:
#             print(" " * ((9 - count) // 2), end="")
#         print("*", end="")
#         col += 1
#     print()
#     row += 1


"""
使用while、if来完成剪刀石头布程序，要求，
当玩家第3次获胜时才退出游戏，否则继续玩。
"""
# times = 0
# while True:
#     computer = random.randint(0, 2)
#     player = int(input("请输入剪刀(0)石头(1)布(2)："))
#     if (player == 0 and computer == 2) or  (player == 1 and computer == 0) or (player == 2 and computer == 1):
#         print("你赢了")
#         times += 1
#     elif player == computer:
#         print("平局")
#     else:
#         print("你输了")
#     if times == 3:
#         break





"""
幸运猜猜猜：游戏随机给出一个0~99（包括0和99）的数字，然后让你猜是什么数字。
你可以随便猜一个数字，游戏会提示太大还是太小，从而缩小结果范围。
经过几次猜测与提示后，最终推出答案。在游戏过程中，记录你最终猜对时所需要的次数，
游戏结束后公布结果。  
说明： 
1~2次猜中，打印你太TM有才了！  
3~6次猜中，打印这么快就猜出来了，很聪明嘛！ 
大于7次猜中，打印猜了半天才猜出来，小同志，尚需努力啊！  
猜测次数最多20次。
"""
# num_computer = random.randint(0, 99)
# print(num_computer)
# num_player = int(input("请输入一个0-99的数字："))
# times = 1
# while True:
#     if num_computer > num_player:
#         num_player = int(input("请输入一个>%d的数字：" % num_player))
#         times += 1
# #
#     elif num_computer < num_player:
#         num_player = int(input("请输入一个<%d的数字：" % num_player))
#         times += 1
#     else:
#         if 1 <= times <= 2:
#             print("你太TM有才了")
#             break
#         elif 3 <= times <= 6:
#             print("这么快就猜出来了，很聪明嘛")
#             break
#         elif 7 <= times <= 20:
#             print("猜了半天才猜出来，小同志，尚需努力啊")
#             break
#         else:
#             print("机会已经用完")
#             break
# print(times)









