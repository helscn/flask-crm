FROM python:3.8
LABEL maintainer "helscn"

ENV APP_DIR=/app
WORKDIR $APP_DIR

# Copy project files and install python packages.
COPY . $APP_DIR
RUN cd $APP_DIR
    && pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt


# Define environment variables
ENV APP_PORT=8000 \
    APP_WORKERS=1 \
    APP_THREADS=5 \

# Declaration volumes
VOLUME $APP_DIR/uploads
VOLUME $APP_DIR/schedulers/jobs

# Expose http web server port
EXPOSE $APP_PORT

# Support auto-reload
HEALTHCHECK CMD curl -fs http://localhost:%APP_PORT || exit 1

# Start the web server with gunicorn
CMD gunicorn --workers=$APP_WORKERS --threads=$APP_THREADS --timeout 60 start:app 0.0.0.0:$APP_PORT --preload
