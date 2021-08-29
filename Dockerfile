# Building frontend quasar project
FROM node:14-buster-slim as frontend

WORKDIR /app

# Copy frontend files and building project.
COPY ./frontend /app/frontend
RUN cd /app/frontend \
    && yarn global add @quasar/cli --registry=https://registry.npm.taobao.org \
    && yarn --registry=https://registry.npm.taobao.org \
    && quasar build

###########################################

# Building backend flask-app project
FROM python:3.9-slim-buster as backend
LABEL maintainer "helscn"

WORKDIR /app

# Copy project files and install python packages.
COPY ./backend /app
COPY --from=frontend /app/frontend/dist/ /app/frontend/dist/
RUN cd /app && pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt


# Define environment variables
ENV APP_PORT=8080 \
    APP_WORKERS=1 \
    APP_THREADS=1

# Declaration volumes
VOLUME /app/uploads
VOLUME /app/schedulers/jobs

# Expose http web server port
EXPOSE $APP_PORT

# Support health checking for auto-reload
HEALTHCHECK --interval=1m --timeout=10s CMD python healthcheck.py

# Start the web server with gunicorn
CMD gunicorn --workers=$APP_WORKERS --threads=$APP_THREADS --timeout 60 start:app --bind 0.0.0.0:$APP_PORT --preload
