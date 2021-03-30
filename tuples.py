tp = ('mukit')
print(type(tp))
tp1 = ('mukit',)
print(type(tp1))
tp2= (1,2,3,4,5,6)
first,*rest,last = tp2
print('first=',first,',rest=',rest,',last=',last)
print(list(tp2))

#list vs tuple
import sys
my_list = ['mukit',23]
my_tuple = tuple(my_list)
print(sys.getsizeof(my_tuple))
print(sys.getsizeof(my_list))

