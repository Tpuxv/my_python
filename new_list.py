list1=[2,4,9,16,25]
list2=[]
#1
for i in list1:
    list2.append(i**0.5)
print(list2)

#2
print(list(map((lambda x: x**0,5), list1)))

#3
print([i**0.5 for i in list1])

