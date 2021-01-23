from PIL import Image

# RGB values for recoloring.
darkBlue = (0, 51, 76)
white = (255, 255, 255)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

# Import image.
print()
text="What picture do you want recolored? Options: morning sky, forest, squirrel taking pictures or of squirrels shopping "
print(text)
print()
user= input("Type in 'morning','forest','sunset', 'photo', 'shopping', 'yoga'")
print()
def pictures(pics):
    my_image = Image.open(pics) #change IMAGENAME to the path on your computer to the image you're using
    image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
    image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.

    recolored = []
    for pixel in image_list:
        (r,g,b)= pixel
        intensity= r + g + b
        if intensity < 182:
            pixel=darkBlue
            recolored.append(pixel)
        elif 182 <= intensity < 364:
            pixel= lightBlue
            recolored.append(pixel)
        elif 364 <= intensity < 546:
            pixel= yellow
            recolored.append(pixel)
        else:
            intensity >= 156
            pixel= white
            recolored.append(pixel)

# Create a new image using the recolored list. Display and save the image.
    new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
    new_image.putdata(recolored) #Adds the data from the recolored list to the image.
    new_image.show() #show the new image on the screen
    new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"

if user == "morning":
    pictures("blueSky.jpeg")

elif user == "forest":
    pictures("night_time.jpg")

elif user == "sunset":
    pictures("sunset.jpeg")

elif user == "shopping":
    pictures("squirrels.jpg")

elif user=="yoga":
    pictures("yoga.jpeg")

else:
    user == "photo"
    pictures("photo_squirrel.jpg")

print()
