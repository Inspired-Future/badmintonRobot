import numpy as np
import cv2 as cv

def isNaN(num):
    return num == num

cap=cv.VideoCapture(0)
cm2pixel_x = 13/640.0
cm2pixel_y = 9.3/480.0
while(1):
    _,frame=cap.read()
    print(frame.shape)

    gray_image1=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    #gray_image1=frame
    #cv.imshow('Background', frame)
    cv.imshow('Background',gray_image1)

    k=cv.waitKey(5)

    if k==27:
        break
while(1):
    _,frame=cap.read()

    gray_image2=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    cv.imshow('Foreground',gray_image1)

    Difference = np.absolute(np.matrix(np.int16(gray_image1)))-np.matrix(np.int16(gray_image2))
    Difference[Difference<0]=0
    Difference[Difference>255]=255
    Difference=np.uint8(Difference)

    cv.imshow('Difference',Difference)
    BW=Difference
    BW[BW<=100]=0
    BW[BW>100]=1

    
    column_sums = np.matrix(np.sum(BW,0))
    column_numbers = np.matrix(np.arange(640))
    column_mult = np.multiply(column_sums,column_numbers)
    total = np.sum(column_mult)
    total_total = np.sum(np.sum(BW))
    column_location= total/total_total

    X_Location = column_location*cm2pixel_x

    
    row_sums = np.matrix(np.sum(BW,1))
    row_sums=row_sums.transpose()
    row_numbers = np.matrix(np.arange(480))
    row_mult = np.multiply(row_sums,row_numbers)
    total = np.sum(row_mult)
    total_total = np.sum(np.sum(BW))
    row_location= total/total_total

    Y_Location = row_location*cm2pixel_y   
    print (X_Location,Y_Location)
    if isNaN(column_location):
        print("iamhere")
        cv.circle(frame, (int(column_location),int(row_location)) , 30 , (255,255,0) , 5 )
    cv.imshow('frame', frame)
    k=cv.waitKey(5)

    #gray_image1=frame
    if k==27:
        break

cv.destroyAllWindows()

#print(frame)
