FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . . 

RUN python download_resnet.py

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "ResNet50_App.wsgi"]`



