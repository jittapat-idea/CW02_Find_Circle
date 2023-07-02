import cv2

def check_pixel_values(image):
    height, width = image.shape[:2]
    for row in range(height):
        for col in range(width):
            pixel_value = image[row, col]
            print("Pixel value at ({}, {}): {}".format(row, col, pixel_value))

# โหลดภาพ
img = cv2.imread('pic/CircleCW02.png', cv2.IMREAD_GRAYSCALE)
# print(img)
# height, width = img.shape[:2]
# print("h: ",height)
# print("w: ",width)

# เรียกใช้ฟังก์ชันเพื่อเช็คค่าพิกเซลทั้งหมดในภาพ
check_pixel_values(img)

cv2.imshow("circle",img)
cv2.waitKey(0)
cv2.destroyAllWindows()