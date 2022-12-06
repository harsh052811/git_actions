from .task import audio_to_trans
from celery import chain
from ..app import app


@app.task
def audio_to_transcription(links: dict):
    """
    link = dict {"id": <id>, "url": <url-to-file>}
    """
    
    pipeline = chain(
        audio_to_trans.s(links)    )
    return pipeline
