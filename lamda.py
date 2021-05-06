add10 = lambda x: x+10
print(add10(24))

mul = lambda x,y: x*y
print(mul(5,3))

points2D = [(1,3),(3,-2),(7,8),(-3,8),(2,6)]
points2D_sorted = sorted(points2D,key= lambda x: x[0]+x[1])
print('Sorted By Sum {}'.format(points2D_sorted))

print('\n map,filter,reduce')
listA = [2,3,5,6,10,11,13,14]
plus_2 = map( lambda x: x+2, listA)
print(list(plus_2))

jst_even = filter( lambda x: x%2==0, listA)
print(list(jst_even))

from functools import reduce
listB = [1,2,3,4]
total_sum = reduce( lambda x,y: x + y,listB)
print(total_sum)

