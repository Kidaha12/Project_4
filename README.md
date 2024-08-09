Project_4
Group Members: Matthew Fontaine, David Kidaha, and Logan Canann

Description: This project explores the ability to identify dog breeds from a single picture through machine learning. The goal is to build a model capable of identifying the breed of a dog when given an image. With 120 breeds and a relatively small number of training images per class, the problem is more challenging than it initially appears.

Engineering: We extracted and loaded datasets from Kaggle and planned our approach. After initial cleaning of the raw files, we used Google Colab to develop the machine learning model using Spark. This project required us to use tools such as Pandas, Scikit-learn, OpenCV (cv2), OS, NumPy, TensorFlow, Keras, and Matplotlib.

Methodology:
We encountered some mid-project struggles. While we were able to generate images and predictions, they were not accurate at first. Although we didn’t fully resolve this issue, given more time and expertise, we believe we could achieve better accuracy. One key realization was that we were mistakenly training the breed names instead of training the model to associate images with the corresponding breeds. Once we corrected this, we began to see improvements in accuracy.

Large Data ML Project Pitfalls:
Model Complexity Leading to Overfitting/Underfitting: A model that is too complex risks overfitting (memorizing noise), while one that is too simple leads to underfitting (missing important patterns). Overfitting models perform well on training data but generalize poorly to new data.

Feature Selection: Instead of using all the dog breeds at once, we could have started by training the model on a single breed and gradually expanded to include more breeds. This might have helped manage the complexity of the dataset.

Evaluation Metrics: Rather than relying solely on accuracy, we should have considered additional metrics like precision, recall, or F1 score. These would have provided a more nuanced view of the model's performance, especially given the large and varied dataset.

Understanding Our Limits: Machine learning is not infallible. We underestimated the challenge of overcoming inherent biases in the dataset, such as various images of different dogs in a wide range of circumstances. ML models can struggle with context and nuance.

Data Quality: We could have employed better methods to ensure the model was not overwhelmed by irrelevant data, such as dogs in costumes, dogs hidden in corners, or multiple breeds in one image. Reducing the dataset size could have helped expedite the training process.

Tools: We faced challenges with our tools. The community version of Databricks had limitations, particularly with group collaboration settings. Google Colab, on the other hand, was limited by bandwidth, which restricted the size of the raw data we could use. Additionally, system failures, such as issues with libraries and dependencies not loading properly, slowed down the project's execution.

Front End Mechanics:
![image](https://github.com/user-attachments/assets/fcf7c409-7122-4c6e-b4f1-b811291d42f0)


Results: The model ran, but it likely overfitted initially, leading it to memorize the data rather than learn from it. While it isn't extremely accurate, the code runs and generates both the photo and prediction of the breed, with a little over half of the predictions being correct. Despite this, the model reports a 93% accuracy, indicating potential overfitting or an issue with how accuracy was calculated.
