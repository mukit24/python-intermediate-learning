import random
print(random.random())
print(random.uniform(1,10))
print(random.randrange(1,20))

li = ['apple','banana','mango','lichu','strabery']
print(random.choice(li))
print(random.choices(li,k=2))
print(random.sample(li,2))
random.shuffle(li)
print(li)