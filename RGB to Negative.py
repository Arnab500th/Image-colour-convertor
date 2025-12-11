import cv2

img=cv2.imread(r"images\pattern.webp")
#using raw strings due to the presence of back slashes,this reads the image given on the path
if img is None:
    print("ERROR:Image not found")
else:
    neg=cv2.bitwise_not(img)
    #converts the rgb image to negative

    cv2.imshow("nature.webp",img)
    #shows the coloured image
    cv2.imshow("Negative",neg)
    #shows the HSV version of the image

    cv2.imwrite(r"images\neg_pattern.jpg",neg)#saves the generated pic in the iamges folder
    cv2.waitKey(0)