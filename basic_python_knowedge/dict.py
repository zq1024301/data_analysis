dict1 = {"names": "小明", "score": 90}  # 字典使用键值对保存数据，字典的键是索引且唯一
dict2 = {"names": "张三", "title": "班长"}

# 从字典中获取值
# print(dict1["names"])  # 如果key不存在会报错
# print(dict1.get("sex"))  # 如果key不存在不会报错，打印none
# print(dict1.keys())  # 获取字典中的所有键
# print(dict1.values())  # 获取字典中的所有键
# print(dict1.items())  # 获取字典中的所有键值对的元组

# 从字典中增加/修改
# dict1["score"] = 95  # 如果键存在修改值
# dict1["sex"] = "男"  # 如果键不存在，新建键值对
# dict1.setdefault("student_number", "2018721005")  # 如果键存在不修改值,如果键不存在，新建键值对
# dict1.update(dict2)  # 将字典2的值合并到字典1中，如果键重复，则覆盖原键值对

# 从字典中删除
# dict1.pop("sex")  # 删除指定的键值对，如果不存在，则会报错
# dict1.popitem()  # 字典是无序的，会随机删除一个键值对（但默认是删除最后一个）
# dict1.clear()  # 清空字典
# del dict1["names"]  # 删除指定的键值对，如果不存在，则会报错
# print(dict1)

# 字典的循环遍历
# for k in dict1:
#     print("%s: %s" % (k, dict1[k]))
#
# for k, v in dict1.items():
#     print(k, v)

# 字典的应用
list1 = [{"names": "小明", "score": 90}, {"names": "张三", "score": 93}]
# for dict0 in list1:
#     print(dict0)

find_name = input("请输入你要查找的姓名：")
for dict0 in list1:
    print(dict0)
    if find_name in dict0["names"]:
        print("查找到%s的相关信息" % find_name)
        break
else:
    print("查无此人")
