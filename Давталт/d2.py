# 2. n ээс m тоо хүртэлх сондгой тооны нийлбэр ол

"""
a,b = [int(x) for x in input().split()]
ih = max(a,b)
while ih >= min(a,b):
    print(ih)
    ih -=1


a,b = [int(x) for x in input().split()] # энэ нь зөвхөн сондгой тоонуудыг харуулна
ih = max(a,b)
while ih >= min(a,b):
    if ih%2 == 1:
        print(ih)
    ih -=1
"""

a,b = [int(x) for x in input().split()] # энэ нь бичигдсэн сондгой тоонуудын нийлбэрийг харуулна
ih = max(a,b)
n=0
while ih >= min(a,b):
    if ih%2 == 1:
        print(ih)
        n = n + ih
    ih -=1
print("niilber", n) 