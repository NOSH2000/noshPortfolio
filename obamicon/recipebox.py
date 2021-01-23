 #
 # #DICTIONARY IN CODING
 # #### instructions={"sugar":"1 cup", " flour":"2 cups",}
 # #### print(ingredients["sugar"]) #will print 1 cup
#
# for item, amount in ingredients.item:
#     print(item, amount)
# print('')


#LIST
print("")
print("")
food = input("What recipe do you want? Cloud Eggs or peach cobblers?")
while (food !="peach" and food != "eggs" ):
    food = input("ERROR! What recipe do you want? Cloud Eggs or peach cobblers?")

if food == 'eggs' :
    print("")
    print("Cloud Eggs")
    instructions= ['INSTRUCTIONS:',
    '1. Preheat the oven to 350 degrees F.',
    "2. Line a baking sheet with parchment and coat with nonstick cooking spray.",
    "3. Line a baking sheet with parchment and coat with nonstick cooking spray.",
    "4. Line a baking sheet with parchment and coat with nonstick cooking spray.",
    "5. Add a large pinch of salt to the egg whites and beat with an electric mixer on low speed until stiff peaks form, 2 to 3 minutes.",
    "6. Dollop 4 large spoonfuls of the egg whites onto the prepared baking sheet and make a small well in the middle of each with the back of a spoon.",
    "7. Bake the whites until they are firm, no longer wet and just beginning to turn brown, about 6 minutes.",
    "8. Gently pour 1 yolk into the well of each white.",
    "9. Bake until the edges of the yolk just start to set while still being runny, 3 to 4 minutes.",
    "10.Season with salt.",
    '11.Serve on top of buttered brioche toast.']

    ingredients= ['INGREDIENTS:','Nonstick cooking spray', '4 large eggs', 'salt', '4 slices buttered brioche toast']


elif food =='peach':
    print("")
    print('INDIVIDUAL PEACH COBBLERS')
    ingredients=['INGREDIENTS:','Nonstick cooking spray', '2 1/2 pounds ripe peaches, pitted and cut into large chunks', '1 tablespoon cornstarch',
    '1/2 cup plus 2 tablespoons sugar','3/4 cup all-purpose flour','2 tablespoons ground flax seed','1/4 teaspoon kosher salt','3 tablespoons cold unsalted butter, cut into small pieces', '2 tablespoons reduced-fat buttermilk','Non-fat vanilla yogurt or frozen yogurt, for serving, optional' ]


    instructions= ['INSTRUCTIONS:', "1. Preheat the oven to 375 degrees F.", "2. Lightly coat eight 6-ounce ramekins with nonstick cooking spray and place on a rimmed baking sheet.", "3. Toss the peaches with the cornstarch and 2 tablespoons sugar in a large bowl.", "4. Let stand until juicy, about 10 minutes. Divide the peaches and juices among the ramekins.", '5. While the peaches sit, combine the flour, remaining 1/2 cup sugar, flax seed and salt.','6. Cut in the butter, using a fork or pastry cutter, until the mixture forms medium-size crumbs. Stir in the buttermilk until well moistened and large clumps hold together.','7. Sprinkle the topping evenly over the peaches. ', '8. Bake until the fruit is bubbling and the topping is golden brown and crisp, 40 to 45 minutes.', '9. Serve warm or at room temperature with vanilla yogurt or frozen yogurt if desired.']



print("")
for item in ingredients:
    print(item)
print("")

for item in instructions:
    print(item)

print("")
print("")
