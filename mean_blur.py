# import numpy as np
# import cv2

# img = cv2.imread('pic/CircleCW02.png', cv2.IMREAD_GRAYSCALE)

# output = cv2.medianBlur(img,5)

# cv2.imshow('Circle Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

# read image
img = cv2.imread('pic/CircleCW02.png', cv2.IMREAD_GRAYSCALE)

# # convert to HSV and extract saturation channel
# gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

output = cv2.medianBlur(img,5)
# threshold
thresh = cv2.threshold(output, 175, 255, cv2.THRESH_BINARY)[1]

# count number of white pixels
count = np.sum(np.where(thresh == 255))
print("count =",count)


# display it
cv2.imshow('Circle Image', img)
cv2.imshow("THRESH", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()