a = int(input("Nilai a :"))
b = int(input("Nilai b :"))
c = int(input("Nilai C :"))
D = b**2 - 4*a*c
x = (-b+D/2)/2*a
y = (-b-D/2)/2*a
if D<0:
    print("Fungsi tersebut tidak memiliki akar rill")
elif D>0:
    print("Akar dari persamaan tersebut adalah",x,"dan",y)
else:
    D==0
    print("Fungsi tersebut memiliki akar kembar yaitu",x)