import tensorflow
from tensorflow.keras.models import model_from_json
import numpy as np
import cv2
from tensorflow.keras.preprocessing.image import load_img, img_to_array

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")
# load weights into new model

X_predict=np.load("predict_X.npy")
Y_predict=np.load("predict_Y.npy")
X_predict/=255.0
Y=loaded_model.predict_classes(X_predict)

print(Y_predict.shape)
count=0
for i in range(X_predict.shape[0]):
    if(Y[i]==Y_predict[i]):
        count+=1

print(count/Y_predict.shape[0])

#img_array = img_to_array(img)
