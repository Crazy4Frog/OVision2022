import uvicorn  # Добавил os и unicorn, чтобы запуск происходил по команде "python main.py" / "python3 main.py"
import os  # Ниже код
import json
import base64
import io
import numpy as np
from PIL import Image
from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


app = FastAPI()

app.mount("/static", StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')


class Data(BaseModel):
    data: str


def base_to_cv2(img):
    byte_img = base64.b64decode(img)
    image = Image.open(io.BytesIO(byte_img))
    return np.array(image)


@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


@app.post('/take_image')
async def take_image(data: Data):
    photo_base64 = data.data.split(';')[1].split(',')[1]
    print(base_to_cv2(photo_base64))
    return Response(
        json.dumps({
            'photo': photo_base64,
        }), 
        media_type='application/json')


if __name__ == "__main__":
    uvicorn.run("main:app", host=os.environ.get("APP_HOST", "127.0.0.1"),
                port=int(os.environ.get("APP_PORT", "8000")),
                reload=True, log_level="info")
