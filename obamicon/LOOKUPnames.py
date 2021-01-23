
names=[1,3,5,6,7,9,10,12,13] ##9
#index 0,1,2,3,4,5, 6, 7, 8

print(names)
num = input("What's your number")
num = int(num)


lower_limit = 0 ##index
upper_limit = len(names) - 1 ## length - 1 = 8 which is the index
middle_limit= (upper_limit + lower_limit) // 2

while names[lower_limit] < num and num < names[middle_limit]:
    upper_limit = middle_limit
    middle_limit= (upper_limit + lower_limit) // 2

while names[middle_limit] < num and num < names[upper_limit]:
    lower_limit = middle_limit
    middle_limit= (upper_limit + lower_limit) // 2

if names[middle_limit] == num:
     print("%s is in the position %s" %(num, middle_limit))

elif names[lower_limit] == num:
    middle_limit = lower_limit
    print("%s is in the position %s" %(num, middle_limit))

elif names[upper_limit] == num:
    middle_limit = upper_limit
    print("%s is in the position %s" %(num, middle_limit))
    
elif num < names[middle_limit] :
    while names[lower_limit] < num and num < names[middle_limit]:
        upper_limit = middle_limit
        middle_limit= (upper_limit + lower_limit) // 2

if names[middle_limit] == num:
     print("%s is in the position %s" %(num, middle_limit))

elif names[lower_limit] == num:
    middle_limit = lower_limit
    print("%s is in the position %s" %(num, middle_limit))

elif names[upper_limit] == num:
    middle_limit = upper_limit
    print("%s is in the position %s" %(num, middle_limit))

else:
    print("ERROR! Not in the list.")



#
# mid = 4 # position of middle_limit
# low = 0 # position of lower_limit
# up  = 8 # position of upper_limit
#
# while lower_limit < num and num < middle_limit:
#     lower_limit  = names[low + 1]
#     middle_limit = names[mid - 1]
#     low += 1
#     mid -= 1
#
# while middle_limit < num and num < upper_limit:
#     middle_limit = names[mid + 1]
#     upper_limit  = names[up - 1]
#     mid += 1
#     up -= 1
#
# if middle_limit == num:
#
#     print("found it")
#
# elif upper_limit == num:
#     print("found it")
#
# elif lower_limit == num:
#     print("found it")
#
# else:
#     print("error")
