from collections import Counter,namedtuple,defaultdict,OrderedDict,deque
st = "my name is mukit hasan pranto"
print(Counter('aabcc'))
dict_st = Counter(st)

for key,value in dict_st.items():
    print('{}---{}'.format(key,value))
    
print(dict_st.most_common(2))
li = ['apple','banana','apple',5,5,9,0,9,5,'apple','banana',5,0]
dict_li = Counter(li)
print(dict_li)
print(dict_li.most_common(1)[0])
ct = Counter({'mukit':2,'pranto':3})
print(list(ct.elements()))

Student = namedtuple('Student',['name','age','discipline'])
st = Student('mukit',23,'CSE')
print(st)
print(st.discipline)

dic = defaultdict(int)
dic['mukit']=23
dic['pranto']=22
print(dic)
print(dic['hasan'])

#in python 3.8 both orderdict and dic are same..both maintain order
or_dic = OrderedDict()
or_dic['name']='mukit'
or_dic['age']=23
or_dic['dis']='CSE'
print(or_dic)
or_dic['age']=22
print(or_dic)
normal_dic ={}
normal_dic['name']='mukit'
normal_dic['age']=23
normal_dic['dis']='CSE'
print(normal_dic)
normal_dic['age']=22
print(normal_dic)

li = ['mukit','hasan']
d_li = deque(li)
d_li.append('pranto')
d_li.appendleft('MD')
print(d_li)
d_li.popleft()
print(d_li)

