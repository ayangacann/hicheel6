# 12. Өгөгдсөн үгэнд а үсэг хэдэн удаа орсон байна вэ
'''
ner = input() #batbaatar
urt = len(ner)-1    
too = 0
while urt >= 0:
    if ner[urt] == "a" or ner[urt] == "A":
        too+=1
    urt-=1
print(too,"ширхэг а үсэг орсон байна")
'''

# хэрэв эсрэг талаас нь буюу 0-5 хүртэлх рүү гүйлгэх шаардлагатай бол while доторхыг эсрэгээр нь бичнэ.

ner = input() #batbaatar
urt = len(ner)-1    
too = 0
k = 0
while k<=urt:
    if ner[k] == "a" or ner[k] == "A":
        too+=1
    k+=1
print(too,"ширхэг а үсэг орсон байна")