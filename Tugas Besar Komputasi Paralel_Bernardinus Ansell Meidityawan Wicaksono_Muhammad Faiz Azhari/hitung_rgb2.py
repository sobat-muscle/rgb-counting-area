from PIL import Image
import glob
import os
import csv

#Open a file to write the pixel data
with open('output_file.csv', 'w', newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerow(["img_name", "R", "G", "B"])

    #Path to file 
    for filename in glob.glob("*.jpg"):
        im = Image.open(filename) 
        img_name = os.path.basename(filename)

        #Load the pixel info
        pix = im.load()

        #Get a tuple of the x and y dimensions of the image
        width, height = im.size

        print(f'{filename}, Width {width}, Height {height}, pix {width}*{height}') # show progress

        #Read the details of each pixel and write them to the file
        for x in range(width):
            for y in range(height):
                r = pix[x,y][0]
                g = pix[x,y][1]
                b = pix[x,y][2]
                csv_output.writerow([img_name, r, g, b])
