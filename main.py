import uvicorn  # Добавил os и unicorn, чтобы запуск происходил по команде "python main.py" / "python3 main.py"
import os  # Ниже код
import json
import base64
import io
import numpy as np
from PIL import Image
from fastapi import FastAPI, Request, Form, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')


def base_to_cv2(img):
    byte_img = base64.b64decode(img)
    image = Image.open(io.BytesIO(byte_img))
    return np.array(image)


@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


@app.post('/take_image')
def take_image(photo):
    print(photo)
    return Response(
        json.dumps({
            'success': True,
            'photo': photo
        }),
        media_type='application/json'
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host=os.environ.get("APP_HOST", "127.0.0.1"), port=int(os.environ.get("APP_PORT", "8000")),
                reload=True, log_level="info")
