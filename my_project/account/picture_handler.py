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
    print(ext_type)

    # email_hash = bcrypt.generate_password_hash(email).decode('utf-8')

    delete_file_if_exists(email)

    storage_name = str(email) + '.' + ext_type
    
    saveFile(pic_upload, filepath='static\profile_pics_70by70', storage_name=storage_name, new_width=70)
    saveFile(pic_upload, filepath='static\profile_pics_128by128', storage_name=storage_name, new_width=128)
    saveFile(pic_upload, filepath='static\profile_pics_200by200', storage_name=storage_name, new_width=200)
    saveFile(pic_upload, filepath='static\profile_pics_220by220', storage_name=storage_name, new_width=220)
    return storage_name


def saveFile(pic_upload, filepath, storage_name, new_width):

    filename = os.path.join(current_app.root_path, filepath, storage_name)
    pic = Image.open(pic_upload)

    print('Image size')
    print(pic.height)

    if pic.height > pic.width:
        aspect_ratio = (pic.height / pic.width)
        new_height = int(aspect_ratio * new_width)
    
    else:
        aspect_ratio = (pic.width / pic.height)
        new_height = int( new_width / aspect_ratio)

    print("ratio: " + str(aspect_ratio))

    print("new_width" + str(new_width))
    print("new_height" + str(new_height))

    output_size = (new_width, new_height)
    print(filename)
    pic.thumbnail(output_size)
    pic.save(filename)



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


def add_dish_pic(pic_upload, blog_id):
    filename = pic_upload.filename
    ext_type = filename.split('.')[-1]

    # email_hash = bcrypt.generate_password_hash(email).decode('utf-8')

    delete_file_if_exists(blog_id)

    storage_name = str(blog_id) + '.' + ext_type

    filepath = os.path.join(current_app.root_path, 'static\images', storage_name)
    print(filepath)
    
    # output_size = (400, 400)

    pic = Image.open(pic_upload)
    # pic.thumbnail(output_size)

    pic.save(filepath)

    return storage_name