#定义全局变量
num=100
def test_a():
    print("num")
def test_b():
    global num#设置内部定义的变量为全局变量
    num=500
    print("num")
test_a()
test_b()
print("num")
#global关键字
#在函数内部修改全局变量变为局部变量。对全局变量无影响，；通过global修改