import cv2

img = cv2.imread('test.png')

cv2.imshow('spring',img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('result.png',img)
    cv2.destroyAllWindows()
