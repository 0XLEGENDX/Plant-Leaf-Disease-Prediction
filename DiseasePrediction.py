import cv2
from matplotlib import pyplot as plt
import os
import numpy as np
# import serial
import time
import urllib.request  


from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model


filepath = r'C:\Programming\Python\Plant Disease Prediction\Plant-Leaf-Disease-Prediction\model.h5'
model = load_model(filepath)

print("Model Loaded Successfully")

def predict(img):

    tomato_plant = img
    #tomato_plant = cv2.imread(r'C:\Users\anura\OneDrive\Desktop\tomatoleaf\Plant-Leaf-Disease-Prediction/Dataset/test/Tomato___Bacterial_spot (1).JPG')
    test_image = cv2.resize(tomato_plant, (128,128)) # load image 
    
    test_image = img_to_array(test_image)/255 # convert image to np array and normalize
    test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
    
    result = model.predict(test_image) # predict diseased palnt or not
    
    pred = np.argmax(result, axis=1)
    print(pred)
    if pred==0:
        print( "Tomato - Bacteria Spot Disease")
        
    elif pred==1:
        print("Tomato - Early Blight Disease")
            
    elif pred==2:
        print("Tomato - Healthy and Fresh")
            
    elif pred==3:
        print("Tomato - Late Blight Disease")
        
    elif pred==4:
        print("Tomato - Leaf Mold Disease")
            
    elif pred==5:
        print("Tomato - Septoria Leaf Spot Disease")
            
    elif pred==6:
        print("Tomato - Target Spot Disease")
            
    elif pred==7:
        print("Tomato - Tomoato Yellow Leaf Curl Virus Disease")
    elif pred==8:
        print("Tomato - Tomato Mosaic Virus Disease")
            
    elif pred==9:
        print("Tomato - Two Spotted Spider Mite Disease")
    
    else:
        print("No Diseases Found")

    

# def writetoArduino(x):
#     arduino.write(bytes(x, 'utf-8'))


# def write_read(x):
    
#     #time.sleep(0.05)
#     data = arduino.readline().decode('utf-8').rstrip()
#     return data




# cap = cv2.VideoCapture(0)
# # arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

# infected_plants = []
# good_plants = []
# interrupt = 1
# sendSMS = False


# while True:
#     num = 0
#     value = write_read(num)

#     print(value)

#     if(value == "Send SMS True"):
#         sendSMS = True

#     if(value == "Send SMS False"):
#         sendSMS = False

    

#     if(value=="90" or value=="160"):
#         print("1")
#         ret,frame = cap.read()

#         if(ret):
#             print("2")
#             time.sleep(2)
#             prediction = predict(frame)

#             if(prediction in range(0,10) and sendSMS):
#                 try:
#                     webUrl = urllib.request.urlopen('https://www.fast2sms.com/dev/bulkV2?authorization=s7QM0kG8zI8dj9UGUDsJ0cm3Y7veZXKvtOWMkUVEliv18vzjecqviGI55uWd&variables_values=Plant%20Disease%20Detected%20Please%20Check.&route=otp&numbers=9404347906')  
#                 except:
#                     pass
#         writetoArduino("0");


