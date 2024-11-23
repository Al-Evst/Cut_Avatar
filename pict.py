from PIL import Image
image = Image.open("monro.jpg")
red, green, blue = image.split()
qv = 50
coordinates = (0, 0, red.width-qv*2, red.height)
coordinates1 = (qv, 0, red.width-qv, red.height)
cropped = red.crop(coordinates)
cropped1 = red.crop(coordinates1)
red_img = Image.blend(cropped, cropped1, 0.75)
coordinates2 = (qv*2, 0, blue.width, blue.height)
coordinates3 = (qv, 0, blue.width-qv, blue.height)
cropped2 = blue.crop(coordinates2)
cropped3 = blue.crop(coordinates3)
blue_img = Image.blend(cropped2, cropped3, 0.75)
coordinates4 = (qv, 0, green.width-qv, green.height)
green_img = green.crop(coordinates4)
new_image = Image.merge("RGB", (red_img, green_img, blue_img))
new_image.thumbnail((80, 80))
new_image.save("comb.jpg")
print(new_image.size)