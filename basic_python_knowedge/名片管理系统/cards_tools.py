# 记录所有名片的列表
# card_list = []
card_list = [{'name': '赵倩', 'phone': '12345678909', 'qq': '2452364263', 'email': '2452364263@qq.com'},
             {'name': '张欣', 'phone': '14235678909', 'qq': '123456789', 'email': '123456789@qq.com'}]


def show_menu():
    """ 显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】v1.0")
    print("")
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("")
    print("0.退出系统")
    print("*" * 50)


def new_card():
    """新建名片"""
    print("-" * 50)
    print("功能：新建名片")
    # 提醒用户输入名片信息
    name = input("请输入您的姓名：")
    phone = input("请输入您的电话：")
    qq = input("请输入您的QQ：")
    email = input("请输入您的邮箱：")

    # 将信息保存到字典
    card_dict = {
        'name': name,
        'phone': phone,
        'qq': qq,
        'email': email
    }

    # 将字典保存在列表
    card_list.append(card_dict)

    print(card_list)

    # 提示名片添加成功
    print('已成功添加%s的名片' % (card_dict['name']))


def show_all():
    """显示全部"""
    print("-" * 50)
    print("功能：显示全部")

    # 判断是否有名片记录
    if len(card_list) == 0:
        print("还未录入名片")
        return

    for name in ['姓名', '电话', 'QQ', '邮箱']:
        print(name, end='\t\t\t\t')
    print()

    print("*" * 50)

    for card_dict in card_list:
        print('%s\t\t  %s\t\t%s\t\t%s' % (card_dict['name'],
                                          card_dict['phone'],
                                          card_dict['qq'],
                                          card_dict['email']))


def search_card():
    """查询名片"""
    print("-" * 50)
    print("功能：查询名片")

    # 提示用户输入要搜索的姓名
    find_name = input("输入你要查找的姓名：")

    # 遍历列表
    for card_dict in card_list:
        if find_name == card_dict['name']:
            print('姓名\t\t\t\t电话\t\t\t\tQQ\t\t\t\t邮箱')
            print('-' * 40)

            print('%s\t\t  %s\t\t%s\t\t%s' % (card_dict['name'],
                                              card_dict['phone'],
                                              card_dict['qq'],
                                              card_dict['email']))
            print('-' * 40)
            deal_card(card_dict)
            break
    else:
        print("没有找到%s的相关信息" % find_name)


def deal_card(find_dict):
    """
    :param find_dict: 找到的名片字典
    :return:
    """
    print(find_dict)

    action_str = input('请选择要执行的操作：'
                       '[1] 修改 [2] 删除 [0] 返回上一层')
    if action_str == '1':
        find_dict['name'] = input_info(find_dict['name'], "请输入姓名：")
        find_dict['phone'] = input_info(find_dict['phone'], "请输入电话：")
        find_dict['qq'] = input_info(find_dict['qq'], "请输入qq：")
        find_dict['email'] = input_info(find_dict['email'], "请输入邮箱：")
    if action_str == '2':
        card_list.remove(find_dict)
        print('删除成功')


def input_info(dict_value, tip_message):
    """
    :param dict_value: 字典中原有的值
    :param tip_message: 提示信息
    :return: 如果输入内容则返回输入内容，否则返回原字典的值
    """
    # 提示用户输入信息
    change_value = input(tip_message)

    # 判断用户是否输入信息，输入则修改，没输入则返回原字典的值
    if len(change_value) > 0:
        return change_value
    else:
        return dict_value
