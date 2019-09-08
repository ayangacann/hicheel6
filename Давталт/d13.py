# 13. Өгүүлбэрийн үгүүдээс b үсгийг хас
'''
oguulber = input()
shine_oguulber = ""
for i in oguulber:
    if i != "b" and i != "B":
        shine_oguulber = shine_oguulber + i
print(shine_oguulber)
'''


oguulber = input() #batbaatar
urt = len(oguulber)-1    
too = 0
k = 0
shine=""
while k<=urt:
    if oguulber[k] != "b" and oguulber[k] != "B":
        shine = shine + oguulber[k]
    k+=1
print(shine,)