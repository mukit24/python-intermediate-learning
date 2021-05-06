st1 = 'mukit hasan pranto'
if 'pranto' in st1:
    print('found sub string')

st2 = '  mukit hasan   '
st2 = st2.strip().upper()
print(st2)
print(st2.startswith('MUKIT'))
print(st2.endswith('PRANTO'))

print(st1.find('pranto'))
print(st1.count('n'))
print(st2.replace('HASAN','PRANTO'))

from timeit import default_timer as timer
my_list = st1.split()
print(my_list)
new_st = ' '.join(my_list)
print(new_st)

# join is much faster than using loop to create string from list
test = ['mukit'] * 1000000 
start = timer()
test_st = ' '.join(test)
end = timer()
print(end-start)

var1 = 3.455643
print('name is %s'%st1)
print('name={} and var is {:.3f}'.format(st1,var1))
print(f'var 1 is {var1:.2f}')