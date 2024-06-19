#!/bin/sh
exec gunicorn app:app --workers 2 --thread 2 --log-level info --bind 0.0.0.0:5000 