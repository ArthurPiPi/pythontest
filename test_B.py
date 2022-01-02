import sys, shelve


def store_person(db):
    """
    让用户输入数据并存储到shelve对象中
    :param db:
    :return:
    """
    pid = input('请输入唯一的ID号：')
    person = {}
    person['姓名'] = input("姓名：")
    person['年龄'] = input("年龄：")
    person['电话'] = input("电话：")
    db[pid] = person


def lookup_person(db):
    '''
    让用户输入ID和所需的字段，并从shelf对象中获取相应的数据
    :param db:
    :return:
    '''
    pid = input('请输入ID号：')
    field = input("你想了解什么？（姓名，年龄，电话)")
    field = field.strip().lower()
    print(field.capitalize() + ':', db[pid][field])


def print_help():
    print("这里可以使用的命令有：")
    print("store,用于存储个人信息")
    print("lookup,用于查看个个信息")
    print("quit,保存并退出")
    print("?,帮助")


def enter_command():
    cmd = input("请输入命令（帮助请按输入？）")
    cmd = cmd.strip().lower()
    return cmd


def main():
    database = shelve.open('database.dat')
    try:
        while True:
            cmd = enter_command()
            if cmd == "store":
                store_person(database)
            elif cmd == "lookup":
                lookup_person(database)
            elif cmd=="?":
                print_help()
            elif cmd=="quit":
                return
    finally:
        database.close()


if __name__ == '__main__': main()
