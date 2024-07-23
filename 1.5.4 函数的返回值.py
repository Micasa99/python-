def add(a,b):
    result= a+b
    return result
r=add(1,2)
#无返回值函数返回 None 类型
#print(r=无返回值函数)----->结果None
#print(type(r=无返回值函数))---->结果<class 'NoneType'>
def say_hi():
    print("hi")
result=say_hi()
print(result)
print(type(result))
#None作用：1)if判断中，None等同于False，一般用于函数主动返回None，配合if判断做相关处理
def check_age(age):
    if age>18:
        return "success"
    else:
        return None
result=check_age(16)
if not result:
    print("未成年，不可进入")


#2） 声明无初始值的变量
name=None