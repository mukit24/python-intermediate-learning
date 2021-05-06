from itertools import product,permutations,combinations,combinations_with_replacement,accumulate,groupby

print('product')
list1 = [1,3]
list2 = [2,4]
prod = product(list1,list2)
print(list(prod))

print('\npermutations')
list3 = [1,2,3]
print(list(permutations(list3)))
print(list(permutations(list3,2)))

print('\ncombinations')
print(list(combinations(list3,2)))
print(list(combinations_with_replacement(list3,2)))

print('\naccumulate')
list4 = [1,2,4,6,8]
print(list(accumulate(list4)))

print('\ngroupby')
def greater_than_5(x):
    return x > 5
grp1 = groupby(list4,key=greater_than_5)
for key,value in grp1:
    print(key,list(value))