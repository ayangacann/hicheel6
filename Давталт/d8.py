# 9. n ээс m тоо хүртэлх сондгой тоонуудын тоог ол
a,b = [int(x) for x in input().split()]
ih = max(a,b)
baga = min(a,b)
n = 0
while ih >= baga:
    if ih%2==1:
        n+=1
    ih-=1
print(n)