
'''
# Нийлбэрийг олох
a, b = [int(x) for x in input().split()]
niilber = 0
for i in range (a,b+1): #2 6
    # i = 2
    print (i) #6
    niilber = niilber + i # 20
print("niilber", niilber)

'''
# ширхэгийг олох
ner = input()
k = 0
for i in ner:
    if i=="a" or i == "A":
        k +=1
print(k, "ширхэг орсон байна.")
