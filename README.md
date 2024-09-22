# Leaf Disease Detection Project

DEMO-> https://drive.google.com/file/d/1CjsvdQrfAQZEUfMm74vfqecijrt7IgCl/view?usp=sharing

Dataset Available at Kaggle

## Description

This project aims to detect leaf diseases using machine learning techniques. It utilizes a Convolutional Neural Network (CNN) to classify leaf images into healthy or diseased categories. The web application allows users to upload leaf images and get real-time predictions on whether the leaf is healthy or affected by Alternaria Leaf Spot or other diseases.

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: TensorFlow/Keras
- **Dataset**: Images of healthy leaves and leaves affected by Alternaria Leaf Spot
- **Libraries**:
  - Flask
  - TensorFlow
  - Keras
  - h5py
  - NumPy
  - scikit-learn

## Diseases

- **Alternaria Leaf Spot**: A common fungal disease affecting various crops, characterized by circular lesions on the leaves.
- **Healthy**: Leaves that are not affected by any visible disease.

## Project Structure:

LeafDiseaseDetection/
│
├── dataset/                # Contains the images of leaves
│   ├── Healthy/            # Healthy leaf images
│   └── Alternaria_Leaf_Spot/  # Diseased leaf images
│
├── train_model.py          # Code for loading data, building the CNN, and training the model
├── evaluate_model.py       # Code for evaluating the model
├── predict_leaf_disease.py # Code for predicting leaf disease on new images
├── server.py               # Flask server file for handling requests and serving the frontend
├── cnn_model.h5            # Saved trained model file (after training)
├── requirements.txt        # List of Python packages required for the project
│
├── frontend/               # Contains the frontend code
│   ├── index.html          # HTML file for the frontend
│   ├── style.css           # CSS file for styling
│   └── script.js           # JavaScript file for handling form submission
│
└── README.md               # Project overview and setup instructions


How It Works

Image Upload: Users upload a leaf image through the web interface.
Prediction: The image is sent to the backend, where it is processed and classified by the CNN model.
Result Display: The result (prediction) is displayed on the frontend.

Security

File Upload Security: Ensure that only image files are uploaded. This is handled in the server.py file by checking the file type.
Sanitize Inputs: The server code should handle unexpected inputs gracefully and avoid executing untrusted code.
Model Security: Protect the trained model file and ensure it’s not accessible publicly.
Future Improvements
Add More Diseases: Extend the model to recognize additional leaf diseases.
User Authentication: Implement user login to keep track of predictions and user activity.
Model Optimization: Explore model optimization techniques to improve accuracy and reduce inference time.
