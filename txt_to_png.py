# scripts to convert pascal voc annotation format to yolo formate
import glob
import os
import re
import argparse
from PIL import Image 
from os import path
import json


ap = argparse.ArgumentParser()
ap.add_argument("-a", "--annotation", required=True, help="Path to the annotation folder")
args = vars(ap.parse_args())
os.chdir(args["annotation"])

all_pascal_voc = glob.glob("*txt")
print ("all files - ", all_pascal_voc)

regex = re.compile('[^a-zA-Z]')

# total list
lst = []
# loop through all Pascal VOC annotation file and record the location of the bounding boxes and classes
for pascal_voc in all_pascal_voc:

    lst.append(sum(1 for line in open(pascal_voc)))
json.dump( lst, open( "cow_histogram_steer.json", 'w' ) )
print (lst, len(lst))




    # path_f = pascal_voc.replace(".txt", ".png")
    # if path.exists(path_f)==True:
    #     path_f = path_f
    # else:
    #     path_f = pascal_voc.replace(".txt", ".jpg")
    # i = 0


    # my_file = open(pascal_voc, "r")
    # img = Image.open(path_f)
    # # record the location of the bounding boxes and classes
    # for line in my_file:
    #     lst = line.split(" ")
    #     wd , ht = float(lst[3])*.5, float(lst[4][:-1])*.5
    #     x1, x2 = (float(lst[1])-wd)*2560, (float(lst[1])+wd)*2560
    #     y1, y2 = (float(lst[2])-ht)*1440, (float(lst[2])+ht)*1440
    #     print (x1,y1,x2,y2)
    #     im1 = img.crop([int(x1), int(y1), int(x2), int(y2)])

    #     nw_path = str(i)+str(path_f)
    #     name = os.path.join("sit",nw_path)
    #     im1.save(name)
        
    #     i+=1
