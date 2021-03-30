my_info = {
    'name':'Mukit',
    'age':23,
    'address':'shariatpur',
}

sajid_info = dict(name='sajid', age=23)
print(sajid_info)
sajid_info['address']='Dhaka'
print(sajid_info)
sajid_info.pop('address')
print(sajid_info)

for key in my_info:
    print(key)

for value in my_info.values():
    print(value)

for key,value in my_info.items():
    print(key,'---',value)