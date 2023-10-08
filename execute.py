

import DiseasePrediction as dp
import cv2



# img = cv2.imread("Tomato___Bacterial_spot (1).JPG")
# img = cv2.imread("Tomato___Early_blight (1).JPG")
img = cv2.imread("Tomato___healthy (1).JPG")

dp.predict(img)


