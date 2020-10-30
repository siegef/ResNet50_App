# ResNet50 App
Django web application for performing simple image classification using ResNet50 model.

## Getting Started

### Installation
Install the requirements by running:
```
pip install -r requirements.txt
```
Then install the ResNet model weights by:
```
python download_resnet.py
```

## How to Use
```
python manage.py runserver
```

Then in your browser, visit 
```
localhost:8000
```

<strong> Note: </strong> The program might take a few seconds to setup before starting the server.

You are ready to go! Just browse an image and click predict. \
<img src="sample.png" alt="Sample Image" title="Browser Page">

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
