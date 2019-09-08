# 14. Өгөгдсөн тооны цифрүүдийн нийлбэрийг ол

'''
 print(sum(int(i) for i in str(input())))
'''

n = int(input())
s = 0
while n > 0: #123456
    a = n % 10
    s = s+a
    n = n//10 # энэ нь төгсгөх нөхцөл юм
print(s)


