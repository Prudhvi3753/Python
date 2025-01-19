'''my_dict={'name':'john','age':30,'city':'New York'}
print(my_dict.get('name')) #access items
my_dict['name']='prudhvi' #update values
print(my_dict)'''

d={}
a=input("enter name:")
age=int(input("enter age:"))
city=input("enter city")

d['name']=a
d['age']=age
d['city']=city

d['name']='prudhvi'
print(d)
print(d['name'])