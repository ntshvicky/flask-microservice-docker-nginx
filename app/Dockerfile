FROM python:3.8-slim-buster
WORKDIR /app
# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 3001
COPY master.py .
# Run the application:
CMD gunicorn --bind 0.0.0.0:3001 --timeout 600 -w 4 master:app 