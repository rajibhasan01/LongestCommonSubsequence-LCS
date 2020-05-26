def lsg(i,z):
    c = 0
    losagu = 1
    for a in z:
        if a%i == 0:
            temp = a/i
            x.append(temp)
            c = c+1
            continue
        else:
            y.append(a)
            continue
    if c>1:
        s.append(i)
        p = x+y
        x.clear()
        y.clear()
        lsg(i,p)
    else:
        p =z
        x.clear()
        y.clear()
        if i < m:
            lsg(i+1,p)
        else:
            new_array = s+p
            for n in new_array:
                losagu = losagu * n
            print(losagu)


s = []
x = []
y = []
list = []
number = int(input("Enter length of the array: "))
for j in range(number):
    data = int(input("Enter value: "))
    list.append(data)

m = int(max(list)/2)
lsg(2,list)
