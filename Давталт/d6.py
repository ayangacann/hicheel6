# 6. a тоог b зэрэгт дэвшүүл
a,b = [int(x) for x in input().split()]
ih = max(a,b)
n = 1
while b > 0: 
    print(a,b)  # 3**5 = 3*3*3*3*3
    n=n*a
    b-=1
print("hariu",n)
