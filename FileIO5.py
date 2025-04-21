from PIL import Image

with Image.open("picture.jpg") as img:
    print(img.size)  # Output the size of the image
    print(img.format)  # Output the format of the image
    print(img.mode)  # Output the mode of the image (e.g., RGB, L, etc.)
    img.show()  # Display the image
    img0 = img.rotate(180)  # Rotate the image by 180 degrees 
    img0.save("picture_rotated.jpg")  # Save the rotated image

from PIL import ImageFilter

with Image.open("picture.jpg") as img:
    img1 = img.filter(ImageFilter.BLUR)  # Apply a blur filter to the image
    img1.save("picture_blurred.jpg")  # Save the blurred image
    img2 = img.filter(ImageFilter.FIND_EDGES) # Apply an edge detection filter to the image
    img2.save("picture_edges.jpg")  # Save the image with edges detected
    