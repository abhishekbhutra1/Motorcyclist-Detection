import cv2
from skimage import feature
from skimage import exposure

image = cv2.imread("apple.jpg",0)

(H, hogImage) = feature.hog(image, orientations=9, pixels_per_cell=(8, 8),
	cells_per_block=(2, 2), transform_sqrt=True, block_norm="L1",
	visualize=True)
print(H)
cv2.imshow("HOG Image", hogImage)
hogImage = exposure.rescale_intensity(hogImage, out_range=(0, 255))
hogImage = hogImage.astype("uint8")

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()