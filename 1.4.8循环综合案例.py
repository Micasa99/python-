money=10000
for i in range(1,21):
    import random
    score =random.randint(1,10)
    if score<5:
        print(f"该员工{i}绩效分{score}不满足，不发工资，下一位")
        continue
    if money>=1000:
        money-=1000
        print(f"员工{i}满足条件，发放工资1000，公司账户余额{money}元")
    else:
        print(f"公司账户余额：{money},不足")
        break