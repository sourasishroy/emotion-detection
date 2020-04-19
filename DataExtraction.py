#(0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral)
import numpy as np
import pandas as pd

df=pd.read_csv("fer2013.csv")
train_X,train_Y,test_X,test_Y,predict_X,predict_Y=[],[],[],[],[],[]
for index, row in df.iterrows():
    val=np.array(row["pixels"].split(" "),'float32')
    if(row["Usage"]=="Training" or row["Usage"]=="PrivateTest"):
        train_Y.append(int(row["emotion"]))
        train_X.append(val)
    elif(row["Usage"]=="PublicTest"):
        test_Y.append(int(row["emotion"]))
        test_X.append(val)

train_X=np.array(train_X,'float32')
test_X=np.array(test_X,'float32')
train_Y=np.array(train_Y,'float32')
test_Y=np.array(test_Y,'float32')

train_X=train_X.reshape(train_X.shape[0],48,48,1)
test_X=test_X.reshape(test_X.shape[0],48,48,1)

np.save("train_X",train_X)
np.save("train_Y",train_Y)
np.save("test_X",test_X)
np.save("test_Y",test_Y)

