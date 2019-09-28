import math
a=int(input("Số Thứ Nhất : "))
b=int(input("Số Thứ  Hai : "))
c=int(input("Số Thứ Ba : "))

denta= b*b-4*a*c

if denta<0:
    print("Ko Có Nghiệm")
if denta>0:
    d=(-b-math.sqrt(denta))/(2*a)
    e=(-b+math.sqrt(denta))/(2*a)
    print("x1 : ",d,"x2 : ",e)
if denta==0:
    f=-b/(2*a)
    print("x1 = x2 =",f)