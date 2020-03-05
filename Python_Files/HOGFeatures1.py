import cv2
import numpy as np

img = cv2.imread("apple.jpg",1)
print(img)

res = cv2.resize(img,(64,128),interpolation = cv2.INTER_CUBIC)
#print("Resized image is :")
#print(res)

#Kx = np.array([-1,0,1])*50
#Ky = np.array([-1,0,1]).reshape(3,1)*50
#print("The Kernal in X Direction")
#print(Kx)
#print("The Kernal in Y Direction")
#print(Ky)
#gx = cv2.filter2D(img,-1,Kx)
gx = cv2.Sobel(res, cv2.CV_32F, 1, 0, ksize=1)
#gy = cv2.filter2D(img,-1,Ky)
gy = cv2.Sobel(res, cv2.CV_32F, 0, 1, ksize=1)
print("Filter in X Direction")
print(gx)
print("Filter in Y Direction")
print(gy)

mag ,angle = cv2.cartToPolar(gx,gy,angleInDegrees=True)
print("the magnitude is:")
print(mag)
print("the angle is:")
print(angle)
#g = (gx**2 + gy**2) **(1/2)
#print("the magnitude calculation is ")
#print(g)


cv2.imshow("image:",img)
cv2.imshow("resized image",res)
cv2.imshow("filter in x direction:",gx)
cv2.imshow("filter in Y direction:",gy)
cv2.imshow("magnitude",mag)
#cv2.imshow("Resized image is:",res)
#cv2.imshow("other image",g)

k = cv2.waitKey()
if k == 32:
    cv2.destroyAllWindows()