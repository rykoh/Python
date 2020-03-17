
import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture):
  random_hex = secrets.token_hex(8)
  _, f_ext = os.path.splitext(form_picture.filename) # _ = f_name
  picture_fn = random_hex + f_ext
  picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
  # create new image with smaller size to save
  output_size = (125, 125)
  i = Image.open(form_picture)
  i.thumbnail(output_size)
  i.save(picture_path)

  return picture_fn
  # write a function to clean up the folder

def send_reset_email(user):
    # can use Jinja2 templates to make email nicer
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link: {url_for('reset_token', token=token, _external=True)} If you did not make this request then simply ignore this email and no changes will be made. The link will expire in 30 minutes.'''
    mail.send(msg)
