
from random import *


#Create the list of words you want to choose from.
word_list = ['Green and speckled legs,','Hop on logs and lily pads',
'Splash in cool water']
word_list0 = ['I am first with five','Then seven in the middle',
'Five again to end.']

word_list1=['Hive','Top','Gop','Drop','Fight']
word_list2=['Blop', 'Flop', 'Five','Ay','Tee-Tee']
word_list3=['Green','Slop','Seven','Hop', 'Nope']

#Generates a random integer.
for times in range (3):
    x = randint(0, len(word_list)-1)
    y = randint(0, len(word_list0)-1)
    print(word_list[x], word_list0[y])
print()


for by in range (3):
    x = randint(0, len(word_list)-1)
    y = randint(0, len(word_list0)-1)
    print(word_list1[x], word_list2[x], word_list3[x],
    word_list1[y], word_list2[y], word_list3[y])
print()
