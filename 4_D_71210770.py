a = int(input("Masukan bilangan 1 : "))
b = int(input("Masukan bilangan 2 : "))
c = int(input("Masukan bilangan 3 : "))

if (a>b and a>c):
    if(b>c):
        print("Urutan bilangan dari yang terbesar adalah : ",a, b, c)
    else:
        print("Urutan bilangan dari yang terbesar adalah : ",a, c, b)
elif (b>a and b>c):
    if(a>c):
        print("Urutan bilangan dari yang terbesar adalah : ",b, a, c)
    else:
        print("Urutan bilangan dari yang terbesar adalah : ",b, c, a)
else :
    if(a>b):
        print("Urutan bilangan dari yang terbesar adalah : ",c, a, b)
    else:
        print("Urutan bilangan dari yang terbesar adalah : ",c, b, a)