#for 临时变量 in待处理的数据集（序列类型）
#    循环满足条件时执行的代码
#数据集可包含字符串，列表，元组等
name = "itheima"
for x in name:
    print(x)
    #for循环无法定义循环条件
#案例：统计文本中特定字符数目
name="itheima is a brand of itcast"
count=0
for x in name:
    if x=="a":
        count=count+1
print(f"{count}a in the sentence")

#2.range语句
#range（num） 获取一个从0开始到num（不包含num）的数字序列
#range(num1,num2)获取从num1（包含）到num2（不包含的数字序列）
#range(num1,num2,step) step:步长  EX:range(5,10,2)--->[5,7,9](步长默认为1)
for x in range(10):
    print(x)

for x in range(5,10):
    print(x)

for x in range(5,10,2):
    print(x)
#3.变量作用域
i=0
for i in range(5):
    print(i)
print(i)#不建议在for循环外部访问临时变量
