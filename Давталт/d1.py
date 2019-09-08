# 1. a ээс b хүртэлх тооний нийлбэр ол

# while a > = b:
#     print(a)
#     a = a - 1

# a, b = [int(x) for x in input().split()] # эхлээд их багыг олж байгаа, дараа нь тэрнээс тэр хүртэлх тоонуудыг олж байна.
# ih = max (a, b)
# baga = min(a, b)
# while ih >= baga:
#     print(ih)
#     ih -=1

a, b = [int(x) for x in input().split()] # эхлээд их багыг олж байгаа, дараа нь тэрнээс тэр хүртэлх тоонуудыг олж байна.
ih = max (a, b)
baga = min(a, b)
niilber = 0
while ih >= baga:
    niilber = niilber + ih
    print(ih)
    ih -=1
print("niilber: ", niilber)
