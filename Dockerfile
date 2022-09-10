FROM python:3.10.6
RUN pip install --upgrade pip
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000