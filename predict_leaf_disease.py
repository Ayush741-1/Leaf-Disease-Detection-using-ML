from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from io import BytesIO

# Load the trained model
model = load_model('cnn_model.h5')

def predict_disease(file):
    """
    Predict the class of a leaf disease from an uploaded image file.

    Args:
    file (file-like object): An image file uploaded by the user.

    Returns:
    str: The predicted class of the leaf disease.
    """
    # Convert file to an image object
    img = image.load_img(BytesIO(file.read()), target_size=(64, 64))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    # Make prediction
    prediction = model.predict(img_array)
    
    # Interpret the prediction
    class_labels = ['Alternaria_Leaf_Spot', 'Healthy']
    predicted_class = class_labels[np.argmax(prediction)]

    return predicted_class
