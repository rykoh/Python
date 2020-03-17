# $ env FLASK_APP=flaskblog.py flask run
# https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog
# Part 8
# Using Bootstrap HTML
'''Create a project folder and a venv folder within:
$ mkdir myproject
$ cd myproject
$ python3 -m venv venv'''

# pip install flask-sqlalchemy --user (create database)
# /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (location pip install packages)
# pip install --target=d:\somewhere\other\than\the\default package_name
# /Users/ryankohanski/Library/Python/2.7/lib/python/site-packages
# /usr/local/bin/python3

# Acces DB using terminal:
# from flaskblog import db
# db.create_all() or db.drop_all() which clears the db
# terminal: 
# from flaskblog.models import User, Post 
# user_1 = User(username='Ryan', email='ryan@demo.com', password='password')
# db.session.add(user_1)
# db.session.commit()
# User.query.all() (or .first())
# User.query.filter_by(username='Ryan').all()
# can be set to a variable
# User.query.get(ID#)  
# user.id or user.posts 
# can use post.author because of the backref in the user class

# starts with single module, to packages, to blueprints

#deployment:
# Python Flask Tutorial: Deploying Your Application (Option #1) - Deploy to a Linux Server
# https://www.youtube.com/watch?v=goToXTC96Co
# Python Flask Tutorial: How to Use a Custom Domain Name for Our Application
# https://www.youtube.com/watch?v=LUFn-QVcmB8
# Python Flask Tutorial: How to enable HTTPS with a free SSL/TLS Certificate using Let's Encrypt
# https://www.youtube.com/watch?v=Gdys9qPjuKs

from flaskblog import create_app

#could pass in a config but uses the config class created by default
app = create_app()

if __name__ == "__main__":
  app.run(debug=True)
