# 10. Өгөгдсөн тооны хуваагчдыг ол
n = int(input()) # 6
s = n   # s = 6
k = 0
while n>0:  # 6 5 4 3 2 1 
    if s % n == 0:
        print (n)
    n-=1