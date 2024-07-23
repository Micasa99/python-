money=5000000
name=None
name=input("请输入您的姓名")
def query(show_header):
    if show_header:
        print("--------查询余额--------")
    print(f"{name},您好，您的余额为：{money}元")
#定义存款函数
def saving(num):
    global money
    money += num
    print("--------存款--------")
    print(f"{name},您好，您存款{num}元成功")
    query(False)
#定义取款函数
def get_money(num):
    global money
    money -= num
    print("--------取款--------")
    print(f"{name},您好，您取款{num}元成功")
    query(False)
#定义主菜单函数
def main():
    print("-----------主菜单-----------")
    print(f"您好{name}，欢迎使用ATM。请选择操作")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")#字数差的较多，用多个\t制表符对齐
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")
#设置无限循环，确保程序不会退出
while True:
    keyboard_input=main()
    if keyboard_input == "1":
        query(True)
        continue    #查询完成后通过continue进入下一次循环，一进来回到主菜单
    elif keyboard_input == "2":
        num=input("您想要存入的金额")
        num=int(num)
        saving(num)
        continue
    elif keyboard_input == "3":
        num=input("您想要取出的金额")
        num=int(num)
        get_money(num)
        continue
    else:
        print("程序退出")
        break         #通过break退出循环


