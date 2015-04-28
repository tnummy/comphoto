from PIL import ImageChops, Image
from app.config import *

class Actions(object):

    def openImage(self, image_name):
        return Image.open(UPLOAD_FOLDER + '/' + image_name)

    def saveImage(self, image, filename):
        image.save(SAVE_FOLDER + '/' + filename)

    def setFilename(self, image_name):
        return str(time.time()) + image_name

    def setPath(self, filename):
        return 'results/' + filename

    def convert(self, action, image_name):
        # filename    = setFilename(image_name)
        # path        = setPath(filename)
        # image       = getattr(self, action)(Image.open(image_name))
        # saveImage(image, filename)
        return "true"

    def gray(self, image):
        return image.convert('L')

    def invert(self, image):
        return ImageChops.duplicate(image.convert('L'))


