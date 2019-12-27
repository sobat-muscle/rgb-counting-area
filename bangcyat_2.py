import os
import re
from PIL import Image
from os import listdir
import datetime



def imageprocess(image_path):    
    img = Image.open(image_path).convert('RGB')
    width, height = img.size

    # The RGB values we will "snap" to
    colors = [255, 223, 191, 159, 127, 95, 63, 31, 0]

    original_color_count = {}
    color_count = {}
    # Loop through every pixel in the image and modify it
    for w in range(width):
        for h in range(height):
            current_color = img.getpixel((w, h))

            if current_color in original_color_count:
                original_color_count[current_color] += 1
            else:
                original_color_count[current_color] = 1

            r, g, b = current_color
            r_set = False
            g_set = False
            b_set = False

            #  Loop through our allowed values and find the closest value to snap to
            for i in range(len(colors)):
                color_one = colors[i]
                color_two = colors[i + 1]

                if not r_set:
                    if color_one >= r >= color_two:
                        distance_one = color_one - r
                        distance_two = r - color_two
                        r = color_one if distance_one <= distance_two else color_two
                        r_set = True

                if not g_set:
                    if color_one >= g >= color_two:
                        distance_one = color_one - g
                        distance_two = g - color_two
                        g = color_one if distance_one <= distance_two else color_two
                        g_set = True

                if not b_set:
                    if color_one >= b >= color_two:
                        distance_one = color_one - b
                        distance_two = b - color_two
                        b = color_one if distance_one <= distance_two else color_two
                        b_set = True

                if all((r_set, g_set, b_set)):
                    break

            # Set our new pixel back on the image to see the difference
            new_rgb = (r, g, b)
            img.putpixel((w, h), new_rgb)

            if new_rgb in color_count:
                color_count[new_rgb] += 1
            else:
                color_count[new_rgb] = 1

    # Save our new image
    filename, file_extension = os.path.splitext(image_path)
    new_path = "{}_new{}".format(filename, '.png')
    img.save(new_path)

    # Count and sort the colors
    all_colors = color_count.items()
    all_colors = sorted(all_colors, key=lambda tup: tup[1], reverse=True)
    try:
        # Print out the colors
        print("## All Colors ##")
        for i in range(10):
            try:
                print(all_colors[i])
            except:
                print("out of range")

        # Remove black, white and gray
        print("\n## All Colors Filtered ##")
        filtered_colors = [color for color in all_colors if not color[0][0] == color[0][1] == color[0][2]]
        z = 0
        for i in range(10):
            try:
                print(filtered_colors[i])            
            except:
                print("out of range")

        print("")
        original_color_count = len(original_color_count)
        print("Original Color Count: {}".format(original_color_count))
        new_color_count = len(color_count)
        print("New Color Count: {}".format(new_color_count))
        color_diff = original_color_count - new_color_count
        print("Reduced Color Count By: {}".format(color_diff))
    except Exception as e:
        print("error processing , file : " + image_path)
        print(e)

print(os.getcwd())
# Open image and get data

def printMS(time):
    secs = time.microseconds / 1000 
    return secs

def timeFromInt(msint):
    time = ""
    hour = 1-1
    menit = 1-1 
    detik = 1-1
    msmilidetik = 1-1
    if msint>1000:
        detik = msint/1000
        milidetik = msint % 1000
        if detik > 60:
            min = detik / 60
            sec = detik % 60
            if min > 60:
                hour = min / 60
                min = min % 60
    
    time = str(hour) + "hr, " +str(menit)+"min, "+str(detik)+"sec, "+str(milidetik)+"ms"
    return time

def logging(timeToWrite, number):
    f= open("Logs.txt","a+")
    f.write("\ntotal time:\t"+timeToWrite +"\tcounter:\t"+number)
    
    f.close

def logging_file(namafile, timetowrite):
    f= open("Output.txt","a+")
    f.write("\nfilename:\t"+namafile +"\ttime:\t"+timetowrite)
    f.close

folder = "gambar"

totalTime = 0
startcounter = 0
counter = 0

for filename in os.listdir(folder):
    if (filename.endswith(".jpg") or filename.endswith(".png")):                
        
        if filename.endswith("_new.png"):
            print ("skip "+filename)
            continue

        if counter < startcounter:
            counter +=1
            continue

        counter += 1

        print("processing...  " +filename)
        path = folder+os.sep+filename
        startTime = datetime.datetime.now()
        imageprocess(path)
        EndTIme = datetime.datetime.now()
        diffTime = EndTIme-startTime

        print("time execution for "+path+" is = "+str(printMS(diffTime))+"ms")
        totalTime+=printMS(diffTime)

        logging(str(totalTime), str(counter))
        logging_file(filename, str(printMS(diffTime)))
        continue    
    
    else:
        continue
try:
    print("\n\ntotal time execution is = ")+timeFromInt(totalTime)
    print("done")
except:
    print("done")
