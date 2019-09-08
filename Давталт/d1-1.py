# Багаас их рүү харуулаад дараа нь нийлбэрийг нь олж байна. 
a, b = [int(x) for x in input().split()] # эхлээд их багыг олж байгаа, дараа нь тэрнээс тэр хүртэлх тоонуудыг олж байна.
ih = max (a, b)
baga = min(a, b)
niilber = 0
while baga <= ih:
    niilber = niilber + baga
    print(baga)
    baga+=1
print("niilber: ", niilber)