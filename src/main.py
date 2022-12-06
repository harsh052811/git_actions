from .crud.crud import retrive
from datetime import date, timedelta
from .util.pipeline import audio_to_transcription
from src.util.task import audio_to_trans
DATE_FMT = "%Y-%m-%d"


def fetch_url():
    today = date.today()
    yesterday = today - timedelta(days=1)
    yesterday_dt = yesterday.strftime(f"{DATE_FMT} 00:00:00")
    yesterday_dt1 = yesterday.strftime(f"{DATE_FMT} 23:59:59")

    links = retrive(yesterday_dt, yesterday_dt1)
    return links


def process_file(links: dict):
    for id, url in links.items():
        task = audio_to_trans.delay({"id": id, "url": url})

# Driver code


if __name__ == "__main__":

    links = fetch_url()
    process_file(links)
