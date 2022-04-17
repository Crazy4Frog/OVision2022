import base64
from PIL import Image
import json


def processImage(imgb64, counter):
    image = base64.b64decode(imgb64)
    img1 = Image.open(io.BytesIO(x))
    img2 = cv2.imread(r'./imageToSave.png')

    cv2.imshow('image', np.array(img1))
    cv2.waitKey(0)
    # smthng do with Image
    success = False
    age = 0
    sex = 0
    emotions = 0
    mask = False
    glasses = False
    response_data = {'success': success,
                     'age': age,
                     'sex': sex,
                     'emotions': emotions,
                     'mask': mask,
                     'glasses': glasses}
    response = json.dumps(response_data)
    return response
