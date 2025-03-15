import cv2

img = cv2.imread('FC_Barcelona_(crest).svg.png')
cv2.imshow("Barca", img)
cv2.waitKey(0)
cv2.destroyAllWindows()