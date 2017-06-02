# Project Hermes
This project is an internationalization solution for web applications.
## Prerequisites
### Python 2.7
##### Linux/UNIX
The latest versions of CentOS, Fedora, Redhat Enterprise (RHEL) and Ubuntu come with Python 2.7 out of the box.
To see which version of Python you have installed, open a command prompt and run
```
python --version
```
##### Mac OS X
```
brew install python
```
### pip
##### Linux/UNIX
The latest versions of CentOS, Fedora, Redhat Enterprise (RHEL) and Ubuntu come with Python 2.7 out of the box.
To see which version of Python you have installed, open a command prompt and run
```
apt-get update
apt-get -y install python-pip
```
##### Mac OS X
```
easy_install pip
```
## Installing
You will need to install the following
##### virtualenv
```
pip install virtualenv
```
Once you have virtualenv installed, just fire up a shell and create your own environment. I usually create a project folder and a venv folder within:
```
cd myproject
virtualenv venv
```
Now, whenever you want to work on a project, you only have to activate the corresponding environment. On OS X and Linux, do the following:
```
source venv/bin/activate
```
And if you want to go back to the real world, use the following command:
```
deactivate
```
##### setuptools
```
pip install --upgrade pip setuptools
```
##### Requirements Files
"Requirements files" are files containing a list of items to be installed using pip install like so:
```
pip install -r requirements.txt
```
## Deployment
Add additional notes about how to deploy this on a live system

## Built With
* [Flaks](http://flask.pocoo.org/docs/0.12/) - The web framework used
* [MongoDB](https://docs.mongodb.com/) - The database used
