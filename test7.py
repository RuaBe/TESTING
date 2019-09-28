
a = [1,2,3,4,5]
print(a)
b = int(input("Điền số bạn muốn :"))
a.insert(0,b)
print(*a,sep=",")