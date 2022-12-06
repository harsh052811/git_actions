#!/bin/bash
uvicorn src.api:app --port=${PORT} --host=${HOST}