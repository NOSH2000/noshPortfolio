'''
## For loop
for students in range(20):
    print(students * 4)
##list of
list = ['cheese', 'milk', 'cup noodles']
for item in list:
    print(item)
print(len(list)) ### len= how many items are there in the list.

grocery =['ice cream', 'chocolate']
for food in grocery:
    print(food)

grocery1 =['ice cream1', 'chocolate1']
print(grocery1)

new = [list, grocery, grocery1]
print(new)
print(len(new))
'''

in_stock=["banana", 'MANGO','cheese']
grocery_list=['cheese', 'milk', 'banana']
x=0
for item in grocery_list:
    x +=1
    if item in in_stock:
        grocery= grocery_list[1]
        bought= True
        print("Item %s = %s" %(grocery, bought))
    else:
        grocery= grocery_list[x]
        bought = False
        print("Item %s = %s " %(grocery, bought))

'''
x=[1,2,3]
x.append([4,5])
print(x)

y=[1,2,3]
y.extend([4,5])
print(y)
'''
