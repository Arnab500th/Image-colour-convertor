import cv2

img=cv2.imread(r"images\nature.webp")
#using raw strings due to the presence of back slashes,this reads the image given on the path
if img is None:
    print("ERROR:Image not found")
else:
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #converts the rgb image to HSV

    cv2.imshow("nature.webp",img)
    #shows the coloured image
    cv2.imshow("HSV",hsv)
    #shows the HSV version of the image

    cv2.imwrite(r"images\hsv_nature.jpg",hsv)#saves the generated pic in the iamges folder
    cv2.waitKey(0)