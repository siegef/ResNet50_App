FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

COPY . . 

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "ResNet50_App.wsgi"]`



