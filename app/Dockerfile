FROM python:3.9-slim-bullseye

# set environment variables.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# user uid and gid
ARG UID=1000
# from getent group docker
ARG GID=1000

RUN apt-get update && \ 
apt-get install netcat iputils-ping net-tools nano curl netcat vim telnet postgresql-client redis-tools -y && \
    rm -rf /var/lib/apt/lists/*

# creating and changing to non-root user. (-mr: creating a HOME directory)
RUN groupadd -g $GID -o app && \
    useradd -g $GID -u $UID -mr -d /home/app -o -s /bin/bash app

# changing user to "app"
USER app

# set work directory.
WORKDIR /home/app

# add /home/app/.local/bin to PATH
ENV PATH "$PATH:/home/app/.local/bin"

# upgrading pip and installing dependencies.
RUN pip install --upgrade pip
COPY --chown=app:app ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r /home/app/requirements.txt

# copy project
COPY --chown=app:app * /home/app/

# application port
EXPOSE 5000

# adding exec permission to entypoint.sh
RUN chmod +x /home/app/entrypoint.sh

ENTRYPOINT ["/home/app/entrypoint.sh"]
#CMD ["gunicorn app:app -k gevent --workers $WORKERS --thread $THREAD --bind 0.0.0.0:5000"]
