# Newspaper Agency

You are the chief in the newspaper agency.
And you are working with great team of Redactors.
But you don't track Newspapers, published by your agency,
in a proper way. For that purpose you decided to create a system
for tracking Redactors, assigned to Newspapers.
So you will always know, who were the publishers of each Newspaper.

# Try it
Use the following user to log in and check the functionality of the website:
```
Username: admin
Password: passwordadmin
```

# Check it out
Now this link doesn't work
[Newspaper Agency project deployed to Heroku](Link_will_be_here)

# Installation

Python3 must be already installed
```
git clone git@github.com:muhactive/newspaper-agency.git
cd newspaper-agency
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrare
python manage.py runserver
```
# Secret Key
In main folder you'll find a file .env_sample.
In this file an example of DJANGO_SECRET_KEY is stored,
required for the project.
You may need create a file .env 
and write here you secret key as in example.

# Features

* Authentication functionality for Redactor/User
* Adding, delete and update new redactors, articles, topics
* Search function and pagination
* Powerful admin panel for advanced managing
* Login/Logout

# DB Structure
![db_structure.png](static%2Fimages%2Fdb_structure.png)

# Demo

![readme_login.png](static%2Fimages%2Freadme_login.png)
![readme_home.png](static%2Fimages%2Freadme_home.png)
![readme_redactor_detail.png](static%2Fimages%2Freadme_redactor_detail.png)
![readme_create_redactor.png](static%2Fimages%2Freadme_create_redactor.png)
![readme_delete.png](static%2Fimages%2Freadme_delete.png)