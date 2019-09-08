# 9. n ээс m тоо хүртэлх тэгш тоонуудын тоог ол
a,b = [int(x) for x in input().split()]
ih = max(a,b)
n = 0
while ih >= min(a,b):
    if n//2 == 0:
        n+=1
    ih-=1
print(n)