import cv2
from deepface import DeepFace

def make_prediction(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    predictions = DeepFace.analyze(image, actions=['age', 'gender'])

    return predictions