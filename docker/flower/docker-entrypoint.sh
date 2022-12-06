#!/bin/bash
celery -A src.app.app flower --port=5555 --host='0.0.0.0' --conf=flowerconfig.py -f /var/log/celery.flower.log 