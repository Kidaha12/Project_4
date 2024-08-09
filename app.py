import os
import random
from flask import Flask, jsonify, request, render_template
from PIL import Image
import numpy as np
import tensorflow as tf
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Local directory containing images
LOCAL_IMAGE_DIR = 'static/images/train'

# Load your model
MODEL_PATH = 'dog_breed_identification.h5'
logging.info(f'Loading model from {MODEL_PATH}')
model = tf.keras.models.load_model(MODEL_PATH)
logging.info('Model loaded successfully')

def get_random_image_path():
    logging.info('Fetching random image from local directory')
    images = [img for img in os.listdir(LOCAL_IMAGE_DIR) if img.lower().endswith(('png', 'jpg', 'jpeg'))]
    if not images:
        logging.error('No images found in the local directory')
        return None
    random_image = random.choice(images)
    logging.info(f'Random image selected: {random_image}')
    return random_image

def preprocess_image(image):
    logging.info('Preprocessing image')
    image = image.resize((224, 224))  # Example size
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random-image', methods=['GET'])
def random_image():
    logging.info('Request received: /random-image')
    image_filename = get_random_image_path()
    if not image_filename:
        return jsonify({'error': 'No images found'}), 404
    image_url = f'/static/images/train/{image_filename}'
    logging.info(f'Image URL sent: {image_url}')
    return jsonify({'image_url': image_url})

@app.route('/predict', methods=['POST'])
def predict():
    logging.info('Request received: /predict')
    image_path = request.json.get('image_path')

    if not image_path:
        logging.error('No image path provided')
        return jsonify({'error': 'No image path provided'}), 400

    full_image_path = os.path.join(app.root_path, image_path.lstrip('/'))
    logging.info(f'Loading image from path: {full_image_path}')

    try:
        image = Image.open(full_image_path)
    except Exception as e:
        logging.error(f'Error loading image: {e}')
        return jsonify({'error': 'Failed to load image'}), 500

    processed_image = preprocess_image(image)
    predictions = model.predict(processed_image)
    predicted_class = np.argmax(predictions[0])

    # Example breed names mapping; replace with your actual mapping
    breed_names = ["Breed1", "Breed2", "Breed3"]  # Example list
    breed_name = breed_names[predicted_class]
    accuracy = np.max(predictions[0]) * 100  # Calculate accuracy as a percentage
    logging.info(f'Prediction made: {breed_name} with {accuracy:.2f}% confidence')

    return jsonify({'prediction': breed_name, 'accuracy': f'{accuracy:.2f}%'})

if __name__ == '__main__':
    logging.info('Starting Flask server')
    app.run(debug=True)
