FROM python:3.9-slim-buster
LABEL maintainer "helscn"

ENV APP_DIR=/app
WORKDIR $APP_DIR

# Copy project files and install python packages.
COPY . $APP_DIR
RUN cd $APP_DIR && pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt


# Define environment variables
ENV APP_PORT=8080 \
    APP_WORKERS=1 \
    APP_THREADS=5

# Declaration volumes
VOLUME $APP_DIR/uploads
VOLUME $APP_DIR/schedulers/jobs

# Expose http web server port
EXPOSE $APP_PORT

# Support health checking for auto-reload
HEALTHCHECK --interval=1m --timeout=10s CMD python healthcheck.py

# Start the web server with gunicorn
CMD gunicorn --workers=$APP_WORKERS --threads=$APP_THREADS --timeout 60 start:app --bind 0.0.0.0:$APP_PORT --preload
