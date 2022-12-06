from celery import shared_task
from ..model.model import Model
from ..crud.crud import dump


@shared_task()
def audio_to_trans(links: dict):
    model = Model()
    transcription=model.predict(links)
    return dump(transcription)