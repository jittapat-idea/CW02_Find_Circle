# import cv2
# import numpy as np

# # def draw_circle(image, center_x, center_y, radius):
# #     height, width = image.shape[:2]
# #     for y in range(height):
# #         for x in range(width):
# #             if (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2:
# #                 image[y, x] = 255

# def check_pixel_values(image,radius):
#     height, width = image.shape[:2]
#     for row in range(height):
#         for col in range(width):
#             pixel_value = image[row, col]
#             if pixel_value > 230:
#                 # draw_circle(image, col, row, radius)
#                 cv2.circle(image, (col, row), radius, (180, 180, 180),1)

# # กำหนดพิกัดและขนาดของวงกลม

# radius = 10

# image = cv2.imread('pic/CircleCW02.png', cv2.IMREAD_GRAYSCALE)
# image = cv2.equalizeHist(image)

# check_pixel_values(image,radius)

# # แสดงภาพที่ผ่านการสร้างวงกลม
# cv2.imshow('Circle Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

def draw_circle(image, center_x, center_y, radius):
    cv2.circle(image, (center_x, center_y), radius, (180, 180, 180), 1)

def check_pixel_values(image, radius):
    height, width = image.shape[:2]
    used_pixels = np.zeros((height, width), dtype=np.uint8)  # เก็บสถานะของพิกัด pixel
    for row in range(0,height,3):
        for col in range(0,width,3):
            pixel_value = image[row, col]
            if pixel_value == 255 :#and used_pixels[row, col] == 0 
                draw_circle(image, col, row, radius)
                used_pixels[row-radius:row+radius, col-radius:col+radius] = 255  # ทำเครื่องหมายว่าพิกัดนี้ถูกใช้แล้ว
    

# กำหนดพิกัดและขนาดของวงกลม
radius = 59

image = cv2.imread('pic/CircleCW02.png', cv2.IMREAD_GRAYSCALE)
# image = cv2.equalizeHist(image)
output = cv2.medianBlur(image,25)
# # threshold
thresh = cv2.threshold(output, 175, 255, cv2.THRESH_BINARY)[1]
# Blur = cv2.GaussianBlur(image,(5,5),5.0,borderType=cv2.BORDER_REFLECT)
edges = cv2.Canny(thresh,200,255)
# cv2.imshow("THRESH", thresh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

check_pixel_values(edges, radius)

# แสดงภาพที่ผ่านการสร้างวงกลม
cv2.imshow('Circle Image', edges )
cv2.waitKey(0)
cv2.destroyAllWindows()


