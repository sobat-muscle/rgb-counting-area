import cv2

img = cv2.imread("raisa.jpg", 1)

px = img [100, 100]
print(px)

blue = img[:,:,0]
print(blue)

green = img[:,0,:]
print(green)

red = img[0,:,:]
print(red)

print(img.shape)
print(img.size)
