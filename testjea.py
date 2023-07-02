import cv2
import numpy as np

def draw_circle(image, center_x, center_y, radius):
    cv2.circle(image, (center_x, center_y), radius, (180, 180, 180), 1)

def check_pixel_values(image, radius, intensity_factor):
    height, width = image.shape[:2]
    used_pixels = np.zeros((height, width), dtype=np.uint8)  # เก็บสถานะของพิกัด pixel
    for row in range(height):
        for col in range(width):
            pixel_value = image[row, col]
            if pixel_value < 255 and used_pixels[row, col] == 0:
                draw_circle(image, col, row, radius)
                used_pixels[row-radius:row+radius, col-radius:col+radius] = 255  # ทำเครื่องหมายว่าพิกัดนี้ถูกใช้แล้ว
                # เพิ่มค่าสีให้กับพิกัดในพื้นที่ที่วงกลมอยู่โดยใช้ตัวดำเนินการบวก (+)
                image[row-radius:row+radius, col-radius:col+radius] = image[row-radius:row+radius, col-radius:col+radius] + intensity_factor

# กำหนดพิกัดและขนาดของวงกลม
radius = 59
intensity_factor = -20 # ปรับค่าตามต้องการ เพิ่มค่าสีให้กับภาพเรื่อย ๆ

image = cv2.imread('pic/CircleCW02.png', cv2.IMREAD_GRAYSCALE)

check_pixel_values(image, radius, intensity_factor)

# แสดงภาพที่ผ่านการสร้างวงกลม
cv2.imshow('Circle Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()



