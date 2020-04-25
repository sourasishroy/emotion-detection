import cv2 
import tensorflow
from datetime import datetime
import statistics as st
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow import keras
from tensorflow.keras.models import model_from_json
import spotify_playlists as spt
from collections import Counter 

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")
loaded_model.summary()
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
emotion_dict={0:"Angry",1:"Disgust",2:"Fear",3:"Happy",4:"Sad",5:"Surprise",6:"Neutral",10:"Loading"}
cap = cv2.VideoCapture(0) 
count=0
emotion=[]
emotion1=[]
cur_emotion=10
while 1: 
    ret, img = cap.read() 
    faces = face_cascade.detectMultiScale(img, 1.32, 5) 
    for (x,y,w,h) in faces: 
        #cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
        count+=1
        crop_img = img[y-30: y + h+30, x-30: x +w+30]
        crop_img=cv2.resize(crop_img,(48,48)) 
        gray=cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        img_pixels = tensorflow.keras.preprocessing.image.img_to_array(gray)
        img_pixels=img_pixels.reshape(1,48,48,1)
        img_pixels/=255.0
        cur_emotion=loaded_model.predict_classes(img_pixels)[0]
        emotion.append(loaded_model.predict_classes(img_pixels)[0])

    cv2.putText(img,emotion_dict[cur_emotion],(290,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    if(count==20):
            occurence_count = Counter(emotion)
            emotion.sort()
            print(occurence_count)
            if(emotion[-1]==6 and occurence_count[6]==10 and len(set(emotion))==2):
                final_emotion=emotion[0]
            else:
                try: 
                    final_emotion=st.mode(emotion)                    
                except st.StatisticsError:
                    final_emotion=max(occurence_count.values())
                    
            print("Your average emotion was",emotion_dict[final_emotion])
            spt.final(emotion_dict[final_emotion])
            emotion1=[]
            emotion1=emotion
            emotion=[]
            count=0

    cv2.putText(img,str(datetime.now()),(10,30), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)
    #cv2.imwrite(filename='saved_img'+str(count)+'.jpg', img=img)
    cv2.imshow('img',img)
            
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
cap.release() 
cv2.destroyAllWindows()

