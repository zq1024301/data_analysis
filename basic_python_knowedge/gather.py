# 创建空集合
set()

# 集合是一个无序的不重复的序列
param = {1, 2, 3, 4}

# 集合的增加
param.add(5)
param.update([5, 6, 7])

# 集合的删除
param.remove(8)  # 删除不存在的元素会报错
param.discard(8)  # 删除不存在的元素不会报错

print(param)













