#!/bin/sh
exec gunicorn app:app --workers 20 --thread 20 --log-level info --bind 0.0.0.0:5000 
