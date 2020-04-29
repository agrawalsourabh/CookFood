import os
from PIL  import Image
from flask import url_for, current_app
from flask_bcrypt import Bcrypt
from my_project import app

bcrypt = Bcrypt(app)

IMG_UPLOAD_EXT = ['PNG', 'JPG' 'JPEG']

def add_profile_pic(pic_upload, email):
    filename = pic_upload.filename
    ext_type = filename.split('.')[-1]

    # email_hash = bcrypt.generate_password_hash(email).decode('utf-8')

    delete_file_if_exists(email)

    storage_name = str(email) + '.' + ext_type

    filepath = os.path.join(current_app.root_path, 'static\profile_pics', storage_name)
    print(filepath)
    
    output_size = (200, 200)

    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)

    pic.save(filepath)

    return storage_name


def is_image(file_name):


    if not '.' in file_name:
        return False

    ext = file_name.split('.')[-1]

    if ext.upper() in IMG_UPLOAD_EXT:
        return True
    else:
        return False


def delete_file_if_exists(email):
    file_png = os.path.join(current_app.root_path, 'static\profile_pics', str(email) + "." + "png")
    file_jpg = os.path.join(current_app.root_path, 'static\profile_pics', str(email) + "." + "jpg")
    file_jpeg = os.path.join(current_app.root_path, 'static\profile_pics', str(email) + "." + "jpeg")

    if os.path.exists(file_png):
        os.remove(file_png)
    if os.path.exists(file_jpg):
        os.remove(file_jpg)
    if os.path.exists(file_jpeg):
        os.remove(file_jpeg)