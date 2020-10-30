import keras
from keras.applications import resnet50

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.imagenet_utils import decode_predictions
# import matplotlib.pyplot as plt
import numpy as np


def predict(filename):

    # Load Keras' ResNet50 model
    resnet_model = resnet50.ResNet50(weights='imagenet') 

    # Load image and pre-process
    # filename = './kuma.jpg'
    # load an image in PIL format
    original_image = load_img(filename, target_size=(224, 224)) 
    # original_image = original_image.rotate(270, expand=True)

    # convert the PIL image (width, height) to a NumPy array (height, width, channel)
    numpy_image = img_to_array(original_image) 

    # Convert the image into 4D Tensor (samples, height, width, channels) by adding an extra dimension to the axis 0.
    input_image = np.expand_dims(numpy_image, axis=0) 

    # print('PIL image size = ', original_image.size)
    # print('NumPy image size = ', numpy_image.shape)
    # print('Input image size = ', input_image.shape)
    # plt.imshow(np.uint8(input_image[0])) 

    # ResNet Preprocess
    processed_image_resnet50 = resnet50.preprocess_input(input_image.copy()) 

    # Making predictions
    predictions_resnet50 = resnet_model.predict(processed_image_resnet50)
    label_resnet50 = decode_predictions(predictions_resnet50)
    print ('label_resnet50 = ', label_resnet50) 