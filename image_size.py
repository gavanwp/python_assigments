"""import opencv-pyton is a python modul use for resize images"""
"""requests is a python modul use for get request"""
'''pyttsx is a python modul use for text to speech '''

import cv2
source = "160x160 (1).jpg"
scale_percentage = 50
image = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# showme = cv2.imshow("title", image)
width  = int(image.shape[1] * scale_percentage/100)
height = int(image.shape[0]*scale_percentage/100)
dsize = cv2.resize(image,(width,height)) 
cv2.imwrite("new_image.png",dsize)

cv2.waitKey(0)
