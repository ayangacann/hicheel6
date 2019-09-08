# 3. n ээс m тоо хүртэлх тэгш тооны нийлбэр ол
a,b = [int(x) for x in input().split()]
ih = max (a,b)
n = 0
while ih >= min(a,b):
    if ih%2 == 0:
        print(ih)
        n = n + ih
    ih -=1
print("niilber",n)