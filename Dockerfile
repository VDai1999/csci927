# Fetching official base image for python
FROM python:3.9-alpine

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r ./requirements.txt
CMD ["gunicorn", "activity_enrollment.wsgi:application"]
# CMD ["python", "manage.py", "runserver"]

# # Setting up the work directory
# # WORKDIR . /app

# # Preventing python from writing
# # pyc to docker container
# ENV PYTHONDONTWRITEBYTECODE 1

# # Flushing out python buffer
# ENV PYTHONUNBUFFERED 1

# # Updating the os
# # RUN apk update 

# # Installing python3
# # RUN apk add python3-dev

# # Copying requirement file
# COPY ./requirements.txt ./

# # Upgrading pip version
# RUN pip install --upgrade pip

# # Installing dependencies
# RUN pip install gunicorn

# # Installing dependencies
# RUN pip install --no-cache-dir -r ./requirements.txt

# # Copying all the files in our project
# COPY . .
# # CMD ["gunicorn","--bind", ":5000", "core.wsgi:application"]