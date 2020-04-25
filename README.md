# Emotion-Detection
## Introduction
This project detects the emotion on person's face using deep convolutional neural networks and recommends songs according to the emotion. Our project is trained on kaggle dataset. The dataset consists of around 36000 grayscale, 48x48 sized face images with **seven** emotions - angry, disgusted, fearful, happy, neutral, sad and surprised.
Link to the dataset - https://www.kaggle.com/c/emotion-detection-from-facial-expressions/data
## Dependencies
- Python 3, OpenCV, Tensorflow
- To install the required packages, run `pip install -r requirements.txt`.
## Basic Usage
The repository is currently compatible with `tensorflow-2.0` and makes use of the **Keras API** using the `tensorflow.keras` library.
- First clone the repository 
`git clone https://github.com/sourasishroy/emotion-detection`
- Download the kaggle dataset from `Numpy(Data) Files`
- If you want to train this model, use: `cd emotion-detection` and then `python ModelTrain.py`
- If you want to view the predictions without training again, you can download the pre-trained model from [here](https://github.com/sourasishroy/emotion-detection/blob/master/model.h5) and then run: `cd emotion-detection` and
`python facedetection.py`
