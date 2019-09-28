a = [1,2,3,4,5]
print(a)
b = input("Head Or Tail :").title()
if b == "Head":
    a.pop(a[0])
    print(a,sep=",")
if b == "Tail":
    a.pop(a[3])
    print(a,sep=",")
