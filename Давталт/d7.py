# 8. a болон b тооны үржвэр ол
a,b = [int(x) for x in input().split()]
ih = max(a,b)
n = 0
while b > 0: # 3*5 = 3+3+3+3+3
    n=n+a
    b-=1
print("hariu",n)