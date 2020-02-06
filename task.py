import time as tm
import os
import cv2
import numpy as np
##################
#Add libraries to import here



##################

def function():

    string = os.getcwd()
    os.chdir(os.getcwd() + '/images')
    ls = os.listdir()

    kernel = np.zeros((140,140),np.uint8)
    kernel[60:80,60:80] = (1)

    dataType = [('i', int), ('j', int), ('score', int)]

    images = []

    #load images into memory list
    for i in range(len(ls)):
        images.append(cv2.imread(ls[i]))

    k = np.ones((3,3),np.uint8)

    os.chdir(string + '/data')

    #process individual image
    for i in range(len(images)):
        NoOfCharchters = len(ls[i]) - 4
        BGColour = images[i][0,0]
        mask = cv2.bitwise_not(cv2.inRange(images[i],BGColour,BGColour))
        img_erosion = cv2.erode(mask, k, iterations=3) 
        #cv2.imshow(str(i),img_erosion)
        #img_dilation = cv2.dilate(img_erosion, k, iterations=1)
        #cv2.imshow(str(40*i),img_dilation)
        #masked = cv2.bitwise_and(images[i],images[i],mask=img_dilation)
        #cv2.imshow(str(40*i),img_erosion)
        roi = []
        values = []
        for j in range(7):
            x = 0 + 75*j
            bw = img_erosion[5:145,x:x+140]
            #cv2.imshow(str(i)+str(j),bw)
            #ret,thresh1 = cv2.threshold(img_erosion,10,255,cv2.THRESH_BINARY)
            roi.append(bw)
            #cv2.imshow(str(i)+str(j),roi[j])
            values.append((i,j,(roi[j]*kernel).sum()))
            #print(values[j])
        mem = np.array(values,dtype=dataType)
        mem = np.sort(mem,order='score')
       # print(mem)
        mem2 = []
       # print(NoOfCharchters)
        for l in range(NoOfCharchters):
            mem2.append(mem[6-l])
        arr = np.array(mem2,dtype=dataType)
        arr = np.sort(arr, order='j')
        print(arr[1][1])
        
        for e in range(NoOfCharchters):
             
            cv2.imshow(str(i)+str(j),roi[2])
            #img = cv2.bitwise_and(images[i][5:145,x:x+140],images[i][5:145,x:x+140],mask=nMask)
            #cv2.imshow(str(i)+str(l-1),img)
            cv2.imwrite(ls[i][e]+str(i)+'.jpeg',roi[arr[e][1]])
            #cv2.imwrite(ls[i][e]+str(i)+'.png',)
            #FI.append(images[i][])
        #cv2.imshow(ls[i],img)
        # lower = np.array(images[i][0,0,0])
        # upper = np.array(images)

    #In this function you have to implement the method to import all the images 
    #present in the same directory apply processing and return individual alphabets
    #in the same directory after the processing.
    #If there are multiple generated images of the same alphabet then name 
    #the file as Alphabet_name_count.jpg/png
    
    # k = cv2.waitKey(0) & 0xFF
    # if k == ord('x'):
    #      cv2.destroyAllWindows
    # pass


##################
#Dont change the code below
##################
tic = tm.perf_counter()
function()
toc = tm.perf_counter()

print(toc-tic)