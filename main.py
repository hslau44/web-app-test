# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import shutil
import time
from typing import Optional, List

import ocr
import util
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Visit the endpoint: /api/v1/extract_text to perform OCR."}


@app.post("/api/v1/extract_text")
async def extract_text(images: List[UploadFile] = File(...)):
    response = {}
    s = time.time()
    for img in images:
        print("Images Uploaded: ", img.filename)
        temp_file = util.save_file_to_server(img, path="./", save_as=img.filename)
        text = await ocr.read_image(temp_file)
        response[img.filename] = text
    response["Time Taken"] = round((time.time() - s),2)

    return response


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
