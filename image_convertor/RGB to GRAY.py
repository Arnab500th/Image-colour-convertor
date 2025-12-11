import cv2

img=cv2.imread(r"images\tiger.jpg")
#using raw strings due to the presence of back slashes,this reads the image given on the path
if img is None:
    print("ERROR:Image not found")
else:
    gray_scale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #converts the rgb image to gray scale

    cv2.imshow("tiger.jpg",img)
    #shows the coloured image
    cv2.imshow("Gray_scale",gray_scale)
    #shows the gray scaled version of the image

    cv2.imwrite(r"images\gray_scale.jpg",gray_scale)#saves the generated pic in the iamges folder
    cv2.waitKey(0)