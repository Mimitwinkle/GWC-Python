from PIL import Image

# RGB values for recoloring.
AdarkBlue = (0, 51, 76)
Ared = (217, 26, 33)
AlightBlue = (112, 150, 158)
Ayellow = (252, 227, 166)

BdarkBlue = (0, 105, 137)
Bdarkgrey = (145, 165, 173)
BlightBlue = (58,169,185)
Blightgrey = (234, 235, 237)

CdarkBlue = (45, 49, 66)
Corange = (239, 131, 84)
ClightBlue = (159,175,203)
Cwhite = (245,247,249)

Dgreen = (9,82,86)
Dlightgreen = (90,170,149)
Dgrey = (96,132,147)
Dlightgrey = (192,214,223)

Eblack = (69,69,69)
Elightgrey = (174,174,174)
Edarkgrey = (135,135,135)
Ewhite = (249,249,249)

# Import image.
my_image = Image.open("hudson.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.

scheme = input("Pick a color scheme:\n\nAmerica\nBlue\nOrange\nGreen\nGreyscale\n\n")

if scheme == "america":
    for pixel in image_list:
        px = pixel[0] + pixel[1] + pixel[2]
        if px <= 182:
            recolored.append(AdarkBlue)
        elif px <= 364:
            recolored.append(Ared)
        elif px <= 546:
            recolored.append(AlightBlue)
        elif px > 546:
            recolored.append(Ayellow)

elif scheme == "blue":
    for pixel in image_list:
        px = pixel[0] + pixel[1] + pixel[2]
        if px <= 182:
            recolored.append(BdarkBlue)
        elif px <= 364:
            recolored.append(Bdarkgrey)
        elif px <= 546:
            recolored.append(BlightBlue)
        elif px > 546:
            recolored.append(Blightgrey)

elif scheme == "orange":
    for pixel in image_list:
        px = pixel[0] + pixel[1] + pixel[2]
        if px <= 182:
            recolored.append(CdarkBlue)
        elif px <= 364:
            recolored.append(Corange)
        elif px <= 546:
            recolored.append(ClightBlue)
        elif px > 546:
            recolored.append(Cwhite)

elif scheme == "green":
    for pixel in image_list:
        px = pixel[0] + pixel[1] + pixel[2]
        if px <= 182:
            recolored.append(Dgreen)
        elif px <= 364:
            recolored.append(Dgrey)
        elif px <= 546:
            recolored.append(Dlightgreen)
        elif px > 546:
            recolored.append(Dlightgrey)

elif scheme == "greyscale":
    for pixel in image_list:
        px = pixel[0] + pixel[1] + pixel[2]
        if px <= 182:
            recolored.append(Eblack)
        elif px <= 364:
            recolored.append(Edarkgrey)
        elif px <= 546:
            recolored.append(Elightgrey)
        elif px > 546:
            recolored.append(Ewhite)


# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("Recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
#print(image_list) #How computer sees image
