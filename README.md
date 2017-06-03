# Project Hermes
This project is an internationalization services for web applications.
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
To start the project execute run.py
```
python run.py
```
To make a service request you need to specify the template and language through the GET method
```
curl <path>/templates/<template_name>/<lang>
```
For example
```
curl localhost:5000/templates/header/en
```
And response the following:
```
{
  "fields": {},
  "status": true
}
```
Where "fields" are the fields that belong to the template and "status" indicates if it is answered correctly or if it has any errors.
In case of error looks like this:
```
{
  "error": 'Error message',
  "status": false
}
```
#### Seed
En caso de querer datos de prueba ejecutar setup.py
```
python setup.py
```
##Testing
ToDo
## Built With
* [Flaks](http://flask.pocoo.org/docs/0.12/) - The web framework used
* [MongoDB](https://docs.mongodb.com/) - The database used
