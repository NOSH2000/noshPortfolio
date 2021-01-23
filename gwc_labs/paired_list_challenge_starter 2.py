

random_numbers = [29, 68, 69, 30, 20, 91, 62, 28, 36, 67, 40, 71, 71, 82, 71, 84, 96, 34, 40, 92, 57, 56, 86, 63, 88, 79, 48, 22, 12, 74,
86, 54, 94, 19, 73, 25, 23, 72, 74, 56,53, 52, 55, 10, 37, 48, 82, 84, 57, 45, 85, 48, 58, 56, 95, 21, 47, 98, 71, 38, 24, 51, 28, 71,
52, 33, 78, 78, 77, 24,17, 31, 85, 87, 86, 63, 23, 73, 40, 64, 35, 29, 10, 43, 99, 38, 63, 61, 76, 91, 64, 48, 23, 26, 19, 21, 17, 49, 15, 62]

#Level 1
multiples_of_5 =[]
for item in random_numbers:
    if item % 5 == 0:
        multiples_of_5.append(item) #adds number into the list
        print (item)
        print(multiples_of_5)
print ("---")


#Level 2
new = 0
for item in random_numbers:
    if item % 5 == 0 and item % 3 == 0:
        new += item
print ("Sum of all the multiples of 3 and 5: %s" %(new))
print("---")


#Level 3
sums = 0
for item in random_numbers:
    if item % 2 != 0 and item % 3 != 0 and item % 4 != 0 and item % 5 != 0 and item % 7 != 0 and item % 8 != 0:
        sums += item
print("Sum of all the prime numbers: %s" %(sums))
