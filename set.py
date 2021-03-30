set1 = {1,2,4,5,3,2,1}
print(set1)
print(set('helloo'))

st = 'Mukit Hasan Pranto'
new_st = set(("".join(st.split())).lower())
print('Distinct Letters:',len(new_st))

setA = {1,2,3,4,5}
setB = {4,5,6,7,8}
setC = {1,2,3}

print(setA.union(setB))
print(setA.intersection(setB))
print(setA.difference(setB))
print(setC.issubset(setA))

#immutable set
set2 = frozenset([2,3,4,5,5])
print(set2)