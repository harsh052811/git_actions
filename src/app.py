from celery import Celery
from celery.schedules import crontab
app = Celery(
    __name__,
    backend='redis://127.0.0.1:6379/0',
    broker='redis://127.0.0.1:6379/0'
)
app.autodiscover_tasks(
    ["src.util.task", 'src.util.pipeline'], force=True)
app.conf.result_backend_transport_options = {
    'retry_policy': {
        'timeout': 5.0
    }
}















