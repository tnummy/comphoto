from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, \
                  abort, jsonify, Flask
from werkzeug import secure_filename
# from app.core.models.actions import Actions
from app.config import *
app = Flask(__name__, static_url_path = "", static_folder = "uploads")
import os
import time
from PIL import  Image, ImageChops, ImageFilter, ImageOps

mod = Blueprint('core', __name__)
@mod.route('/')
def index():
  return (render_template('core/index.html'))

@mod.route('/convert/<action>/<image_name>', methods=['GET', 'POST'])
def convert(action,image_name):
  # # actions = Actions()
  # image_path = gray(image_name)
  # # return image_path
  # return (render_template('core/convert.html', path=image_path, name=image_name))

  # return action
  if action == "gray":
      img = Image.open(UPLOAD_FOLDER + '/' + image_name).convert('L')
  elif action == "invert":
      img = Image.open(UPLOAD_FOLDER + '/' + image_name)
      img = ImageChops.invert(img)
  elif action == "sharpen":
      img = Image.open(UPLOAD_FOLDER + '/' + image_name).filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
  elif action == "contrast":
      img = Image.open(UPLOAD_FOLDER + '/' + image_name)
      img = ImageOps.autocontrast(img, cutoff=5, ignore=None)
  elif action == "equalize":
      img = Image.open(UPLOAD_FOLDER + '/' + image_name)
      img = ImageOps.equalize(img, mask=None)
  elif action == "solarize":
      img = Image.open(UPLOAD_FOLDER + '/' + image_name)
      img = ImageOps.solarize(img, threshold=128)
  filename = str(time.time()) + image_name
  img.save(SAVE_FOLDER + '/' + filename)
  image_path = 'results/' + filename
  return (render_template('core/convert.html', path=image_path, name=image_name))

@mod.route('/result/<image_name>')
def images(image_name):
  image_path = 'uploads/'+image_name
  return (render_template('core/result.html', path=image_path, name=image_name))

@mod.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['photo']
        if file:
            if allowed_file(file.filename):
                filename = str(time.time())+secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                return redirect("/result/"+filename)
            else:
              error = "Picture must be a jpg | jpeg | png | gif | bmp file type."
              return (render_template('core/index.html', error=error))
        else:
            error = "Please choose a picture to upload."
            return (render_template('core/index.html', error=error))
    else: 
        return (redirect('/'))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# def openImage(image_name):
#     return Image.open(UPLOAD_FOLDER + '/' + image_name)

# def saveImage(image, filename):
#     image.save(SAVE_FOLDER + '/' + filename)

# def setFilename(image_name):
#     return str(time.time()) + image_name

# def setPath(filename):
#     return 'results/' + filename

# # def convert(action, image_name):
# #     filename        = setFilename(image_name)
# #     path            = setPath(filename)
# #     image           = Image.open(image_name)
# #     converted_image = getattr(action)(image)
# #     saveImage(image, filename)
# #     return path

# def gray(image):
#     # return image.convert('L')
#     filename        = setFilename(image_name)
#     path            = setPath(filename)
#     image           = Image.open(image_name).convert('L')
#     saveImage(image, filename)
#     return path

# def invert(image):
#     return ImageChops.duplicate(image.convert('L'))