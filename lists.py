list1 = ['apple','banana','mango']
print(list1)

list1.insert(1,'lemon')
print(list1)

list1.pop()
print(list1)

list1.append('cherry')
list1.remove('cherry')
print(list1)

list1.reverse()
print(list1)

list2 = [4,1,89,45,12,7]
new_list2 = sorted(list2)
print(str(new_list2)+' '+str(list2))

list3 = ['mukit'] * 3
print(list3)

print(list1+list3)

list4 = list2[:3]
print(list4)

copy_list3 = list3.copy()
copy_list3.append('pranto')
print(str(list3)+''+str(copy_list3))

#list comprehension
list5 = [x for x in range(10)]
print(list5)
list6 = [x for x in list5 if x > 4]
print(list6)
upp_list1 = [x.upper() for x in list1]
print(upp_list1)
# names = [input(f'name {x+1}=') for x in range(int(input('num=')))]
# print(names)
x = [int(x) for x in input("Enter multiple value: ").split()]
print("Number of list is: ", x)

