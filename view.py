from PIL import Image
import numpy as np

file = input("Enter the image file name which consists of a digit number:")

img = Image.open(file)
img = img.resize((28, 28))
img = np.asarray(img)

#CLI image viewer
for i in range(0, 28):
	print('')
	for j in range(0, 28):
		print('\x1b[38;2;%d;%d;%dm'%(img[i,j,0], img[i,j,1], img[i,j,2])+'$'+'\x1b[0m', end='')
print('')
