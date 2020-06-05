from os import mkdir
from os.path import isdir
from time import sleep
import datetime
import cv2
from threading import Thread
from shutil import copyfile
cap = cv2.VideoCapture(0)

while True:
    now = str(datetime.datetime.now())[:19].replace(':','_')
    if not isdir(now[:10]):
        mkdir(now[:10])
    ret,frame = cap.read()
    if ret:
        fn = now[:10]+'\\'+now+'.jpg'
        cv2.imwrite(fn,frame)
    sleep(5)
    cap.release()


now = str(datetime.datetime.now())[:19].replace(':','_')
dirName = now[:10]
tempAviFile = dirName+'\\'+'.avi'
if not isdir(dirName):
    mkdir(dirName)

aviFile = cv2.VideoWriter(tempAviFile,
                          cv2.VideoWriter_fourcc('M','J','P','G'),
                          25,(640,480))

def write():
    while cap.isOpened():
        ret,frame = cap.read()
        if  ret:
            aviFile.write(frame)
    aviFile.release()
Thread(target=write).start()

input('按任意键结束')
cap.release()