from imgpro import * 
image = Image.open(fileName) 
image.save("a.png")
img = cv2.imread("a.png") 
       
median = cv2.medianBlur(img, 5)
cv2.imshow("Median", median)
cv2.waitKey(0)
cv2.destroyAllWindows()