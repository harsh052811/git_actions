#!/bin/bash

uuid=$(uuidgen)
celery -A src.app.app worker -f /var/log/celery.worker.log -n $uuid@%h