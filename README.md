# Project_4
Group Members: Matthew Fontaine, David Kidaha, and Logan Canann
Description: In this project we explored the ability to identify dog breeds from a single picture through the understanding of machine learning. The goal is to build a model that can identify the breed of a dog when given an image. There are 120 breeds, and a relatively small number of training images per class, which makes the problem harder than it originally seems.

Engineering: We Extracted and Loaded data sets from Kaggle and worked on where to get started. After initial cleaning of the raw files, we used CoLab to house the machine learning using Spark. This project required us to use Pandas, SKlearn, cv2, os, Numpy, Tenser flow, Keras, and Matplotlib.

Methodology
Some mid project struggles were that we were able to get images and predictions produced but not quite correct at first. We didn't quite have the time to solve this solution completely, but with the right amount of time and know how it's something we can come to a concultion and find some real accuracy in. What we found was we were training the breed names rather than training the breed images to corrisponding images of the breeds, with that the increase of accuaracy started coming.

Results
The model ran but likely overfit at first and started looking to memorize the data instead of learn it, it isn't extremely accurate however the code runs and populates both photo and prediction of breed getting a little over half of the predictions correct. However, the learning claims to be getting 93% accuracy. 
