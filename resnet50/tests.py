from PIL import Image
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse
# from .factories import UserFactory
# from .models import UserProfile

from io import BytesIO
import glob
import os


# "borrowed" from easy_thumbnails/tests/test_processors.py
def create_image(storage, filename, size=(100, 100), image_mode='RGB', image_format='PNG'):
    """
    Generate a test image, returning the filename that it was saved as.

    If ``storage`` is ``None``, the BytesIO containing the image data
    will be passed instead.
    """
    data = BytesIO()
    Image.new(image_mode, size).save(data, image_format)
    data.seek(0)
    if not storage:
        return data
    image_file = ContentFile(data.read())
    return storage.save(filename, image_file)


class UploadTest(TestCase):
    # Credits to Cynthia Kiser
    # http://blog.cynthiakiser.com/blog/2016/06/26/testing-file-uploads-in-django/

    def test_image_upload(self):
        myClient = Client()

        # set up form data
        avatar = create_image(None, 'avatar.png')
        avatar_file = SimpleUploadedFile('front.png', avatar.getvalue(), content_type="image/png")
        form_data = {'image': avatar_file}
        response = myClient.post(reverse('resnet50:index'), form_data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(os.path.exists('media/images/front.png')) #Check if file has been uploaded.

        # Delete test upload
        files = glob.glob('media/images/front*')
        for file in files:
            os.remove(file)

    def test_uploading_non_image_file_errors(self):
        myClient = Client()

        # set up form data
        text_file = SimpleUploadedFile('front.png', b'this is some text - not an image')
        form_data = {'image': text_file}

        response = myClient.post(reverse('resnet50:index'), form_data)
        self.assertFormError(response, 'form', 'image', 'Upload a valid image. The file you uploaded was either not an image or a corrupted image.') #Check if error has occurred
        self.assertFalse(os.path.exists('media/images/front.png')) #Check if file has been uploaded.
