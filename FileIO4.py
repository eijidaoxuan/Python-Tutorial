import sys                              #sys.argv > 2       sys.argv[0]=FileIO4.py
from PIL import Image                   #.gif (can animated gif) and .jpg and jpeg and .png

first_image = Image.open(sys.argv[1])  # Open the first image
images = []

for arg in sys.argv[2:]:
    image = Image.open(arg)
    images.append(image)



first_image.save(
    "gif_combination.gif", save_all = True , append_images = images, duration=100, loop = 0      #100 milisec each pic
)

image.close()     # Close the image files
first_image.close()  # Close the first image file