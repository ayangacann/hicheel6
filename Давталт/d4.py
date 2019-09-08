# 4. n ээс m тоо хүртэлх 3т хуваагдах тооны нийлбэр ол

'''
a,b = [int(x) for x in input().split()] # энэ нь бичигдсэн сондгой тоонуудын нийлбэрийг харуулна
ih = max(a,b)
n=0
while ih >= min(a,b):
    if ih%2 == 1:
        print(ih)
        n = n + ih
    ih -=1
print("niilber", n) 
'''

n,m = [int(x) for x in input().split()]