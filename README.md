# GitHub, TravisCI and Heroku working as a team!

- This project was created in order to test the integration between GitHub, TravisCI and Heroku. 

#### 1) Creating a new repository on GitHub

Follow the [original documentation][github-doc] to create a new repository. Once it's done. Let's write a simple Flask application with a unit test to test it. 

#### 2) Cloning the repository into our machine

Once the repository is created, we need to clone it into our local machine. To clone, we need to execute:

```git clone https://github.com/<git-user>/<repo-name>.git```


#### 3) Creating a virtualenv for our project

Assuming that you have ```virtualenv``` installed, now we have to create a new virtualenv in order to keep the dependencies isolated from our root system. So, to create it we need to execute:

```virtualenv <virtualenv-name>```

Once it's created, to activate it we execute:

```source <virtualenv-name>/bin/activate```

* Obs: we don't need to keep track of the virtualenv files, so, add the virtualenv directory on .gitignore.


#### 4) Installing Flask into virtualenv

Now that we're into the virtualenv, we need to install the libraries that we'll use in this project: Flask.

```pip install Flask```
```pip freeze > requirements.txt```


#### 5) Creating the Flask app

We'll create a very simple Flask app. The code is written below and it's in the ```api.py``` file. 

```python

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

```

#### 6) Creating the unit test file

The unit test file can be named as ```test.py``` and it will test the ```api.py```.

```python
import unittest
import api

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = api.app.test_client()

    def test_index(self):
        return_value = self.app.get('/')
        assert b'Hello, World' in return_value.data

if __name__ == '__main__':
    unittest.main()
```

Now that we have the ```api.py``` and the ```test.py``` we'll create the TravisCI integration.

#### 7) Creating the TravisCI integration

- In the profile page, click on Activate
- On Repository Acces, check the 'Only select repositories' and select the repository that you created above. 
- Click in 'Approve and install' 
- Refresh the 'Profile' page and the new repository will be shown. 

#### 8) Configuring TravisCI

To configure TravisCI we need to create a file called ```.travis.yml``` and insert the following information in it:

```yml
language: python
python:
  - "3.6"
install:
  - pip install -r requirements.txt
script:
  - pytest
```

and then, commit everything that we've done so far and check out the TravisCI console to see if everything's ok.


#### 9) Integrating with Heroku

Now that's everything's done with GitHub and TravisCI, we need to integrate it with Heroku. So:

- Create a new Heroku app
- Set the Deployment Method as GitHub, syncing with our repository created above. 
- Check the box where is written ```Wait for CI to pass before deploy```
- Then click in Enable Automatic Deploys.
- Create a new file called ```Procfile``` and insert the information below in it:

```python
web: FLASK_APP=api.py python -m flask run --host=0.0.0.0 --port=$PORT
```

Now we've done! Make some changes in the project and commit it to check if the TravisCI and the Heroku are working well together!


[github-doc]: https://help.github.com/articles/creating-a-new-repository/
