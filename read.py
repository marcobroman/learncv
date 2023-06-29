import cv2 
import numpy as np

def mouseRGB(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        colorsB = frame[y,x,0]
        colorsG = frame[y,x,1]
        colorsR = frame[y,x,2]
        colors = frame[y,x]
        # print("Blue: ",colorsB)
        # print("Green: ",colorsG)
        # print("Red: ",colorsR)
        print("BGR======: ",str(colors).replace(" ",","))
        # print("Coordinates of pixel: X: ",x,"Y: ",y)
        print()


# read img
# img = cv2.imread("m.jpg",0)
# # img = cv2.resize(img,(400,400))
# img = cv2.resize(img,(0,0),fx=0.3,fy=0.3)
# img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
# cv2.imwrite("newimg.jpg",img)
# cv2.imshow("duck",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

capture = cv2.VideoCapture(0)
cv2.namedWindow('ori')
cv2.setMouseCallback('ori',mouseRGB)

#red boundary
# low, high =[104, 96, 180], [100, 67, 255]
#orange
low, high =[59,57,57], [82,81,77] # 142,166,209 - 179,188,226

#blues
# low, high = [50, 0, 0], [255, 255, 180]

lower = np.array(low, dtype = "uint8")
upper = np.array(high, dtype = "uint8")
#RGB

while True:
    isTrue,frame = capture.read()
    mask = cv2.inRange(frame, lower, upper)
    output = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("ori",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("out",output)
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()
cv2.destroyAllWindows()
