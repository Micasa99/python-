#1.4.4 while的嵌套案例
#1.print输出语句自动换行，输出不换行：print("content",end='')
#2.制表符\t 效果等同于在键盘按tab，让多行字符串对齐 ex：
# print("Hello\tworld")
# print("it\tbest")
#案例：while循环输出99乘法表
i=1
while i<=9:
    j=1
    while j<=i:
        print(f"{j}*{i}={j*i}\t",end='')
        j+=1
    i+=1
    print()#输出空内容，用于实现换行