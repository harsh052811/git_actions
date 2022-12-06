import whisper
from datetime import datetime


class Model:
    __instance = None

    def __init__(self, name="base"):
        if Model.__instance is None:
            self.model = whisper.load_model(name)

        else:
            return self.model

    def predict(self, links):
        id = links["id"]
        url = links["url"]

        try:
            result = self.model.transcribe(url)
            transcript = result["text"]

        except Exception as e:
            print("model:predict exception = {}".format(e))
            return {"id": id, "transcript": 'failed'}

        return {"id": id, "transcript": transcript}
