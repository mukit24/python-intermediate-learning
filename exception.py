age = 20
if age < 18 :
    raise Exception('Voter Age Must BE Greater Than OR Equal to 18')

try: 
    a = 5/0
except:
    print('Errors Occur')
finally:
    print('this always executed')

try:
    b = 50 + 'yo'
except Exception as e:
    print('Error is {}'.format(e))
else:
    print('every thing is fine')

# own exception
class valueTooBigError(Exception):
    pass

class valueTooSmalError(Exception):
    def __init__(self,msg,value):
        self.msg = msg
        self.value = value


def test(x):
    if x > 500:
        raise valueTooBigError('Value is High')
    if x < 100:
        raise valueTooSmalError('Value is too small',x)

test(400)

try:
    test(50)
except Exception as e:
    print(e.msg,e.value)


