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