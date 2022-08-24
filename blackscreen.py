import cv2
import numpy as np

cap=cv2.VideoCapture(0)
image=cv2.imread("sce.jpeg")

while (True):

    ret,frame=video.read()
    frame = cv2.resize( frame,(640,480))
    image = cv2.resize( image,(640,480))

    l_black=np.array([140,153,70])
    u_black=np.array([30,30,0])

    mask=cv2.inRange(frame,l_black,u_black)
    res=cv2.bitwise_and(frame,frame,mask=frame)

    f= frame - res 
    f=np.where(f == 0 ,image,f)
    cv2.imshow("video",frame)
    cv2.imshow("mask",f)
    if (cv2 waitKey(1) & 0xFF == ord('q')):
        break

    cap.release() 
    cv2.destroyAllWindows()




