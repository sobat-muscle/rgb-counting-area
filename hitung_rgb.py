from PIL import Image
im = Image.open('raisa.jpg', 'r')

width, height = im.size
pixel_values = list(im.getdata()) 
print(im.format, im.size, im.mode)
