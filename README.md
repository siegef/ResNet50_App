# ResNet50 App
Django web application for performing simple image classification using ResNet50 model.

## Getting Started

### Installation
```
pip install -r requirements.txt
```

## How to Use
```
python manage.py runserver
```

Then in your browser, visit 
```
localhost:8000
```

You are ready to go! Just browse an image and click predict.
![Sample Image](sample.png "Browser page")

## Docker Container
To use an existing docker image
```
docker pull siegef/resnet50_app:1.0
docker run -p <PORT>:8000 -d --name <APP NAME> resnet50_app:1.0
```
Then access the webpage by going to
```
localhost:<PORT>
```
