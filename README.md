# Emotion-Detection
## Introduction
This project detects the emotion on person's face using deep convolutional neural networks and recommends songs according to the emotion. Our project is trained on kaggle dataset. The tain-dataset consists of 36928 and test-dataset consists of around 3692 grayscale, 48x48 sized face images with **seven** emotions - angry, disgusted, fearful, happy, neutral, sad and surprised.
Link to the dataset - https://www.kaggle.com/c/emotion-detection-from-facial-expressions/data
## Dependencies
- Python 3.7.7, OpenCV 4.2.0, Tensorflow 2.1.0 and Tensorboard 2.1.0, numpy 1.18.1
- To install the required packages, run `pip install -r requirements.txt`.
## Basic Usage
The repository is currently compatible with `tensorflow-2.1.0` and makes use of the **Keras API** using the `tensorflow.keras` library.
- First clone the repository 
`git clone https://github.com/sourasishroy/emotion-detection`
- Download the kaggle dataset from `Numpy (Data) Files`
- If you want to train this model, use: `cd emotion-detection` and then `python ModelTrain.py`
- If you want to view the predictions without training again, you can download the pre-trained model from [here](https://github.com/sourasishroy/emotion-detection/blob/master/model.h5) and then run: `cd emotion-detection` and
`python facedetection.py`
## Algorithm
- The `haarcascade_frontalface_default.xml` is used to detect the face infront of webcam.
- The image of the detected face is resized to **48x48** and then passed to CNN.
- The network outputs a list of **scores** for seven classes of emotions.
- The emotion with **maximum** score is displayed on the screen.
## Accuracy
- With a simple **12-layer** CNN, the test accuracy reached **65.3%** in **150 epochs**.
![test](https://user-images.githubusercontent.com/60285133/80638635-6009f880-8a7e-11ea-8558-97007e8f2b78.jpeg)
- The train accuracy reached **90.7%** in **150 epochs**. 
![train](https://user-images.githubusercontent.com/60285133/80638582-4b2d6500-8a7e-11ea-9704-8e86c49f95d3.jpeg)
## Output
- Our output is -
![output](https://user-images.githubusercontent.com/60285133/80634967-dc99d880-8a78-11ea-93a8-46fe998063b7.jpeg)
## Project Made By - 
- Anush Shand - 181090011
- Sourasish Roy - 181090046
- Sahil Bhogate - 181090015
