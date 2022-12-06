from pydantic import BaseModel
import whisper
import secrets
import os
from .model.model import Model
from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()


class Audio(BaseModel):
    audio_link: str

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = os.getenv("API_USER").encode("utf8")
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = os.getenv("API_PASS").encode("utf8")
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    valid_user= is_correct_username and is_correct_password
    if not valid_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.post('/speech_to_text', status_code=200)
def audio(audio: Audio,username: str = Depends(get_current_username)):
    model = Model()
    data = {
        'id':'123',
        'url': audio.audio_link
    }
    result = model.predict(data)

    return result['transcript']