import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Load the saved model
cnn_model = tf.keras.models.load_model('cnn_model.h5')

# Directory for test images
test_data_dir = 'dataset'

# Data preprocessing for testing
test_datagen = ImageDataGenerator(rescale=1.0/255.0)  # Normalize pixel values

# Load test data
test_generator = test_datagen.flow_from_directory(
    test_data_dir,
    target_size=(64, 64),      # Size of the images
    batch_size=32,
    class_mode='categorical',  # Since you have two classes
    shuffle=False
)

# Evaluate the model
test_loss, test_acc = cnn_model.evaluate(test_generator)

print(f'Test accuracy: {test_acc}')
print(f'Test loss: {test_loss}')
