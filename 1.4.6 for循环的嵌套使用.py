i=0
for i in range(101):
    print("today is the ",i,"day")
    for j in range(1,11):
        print(f"the{j}th rose")
    print("love")
print(f"success in the {i} day")
#案例 for99
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}\t",end='')
    print()