# a4-cookiecutter

This is a [cookiecutter template](https://cookiecutter.readthedocs.io/en/latest/) that can be used to set up a participation platform using our participation library [adhocracy4](https://github.com/liqd/adhocracy4) and the CMS [wagtail](https://wagtail.io/).

When using the cookiecutter a new [django](https://www.djangoproject.com/) project with all functionalities already in place will be created. After the setup you can start customizing the platform for your own needs.

Functionalities already included are:
* User registration via Email (done with [allauth](https://django-allauth.readthedocs.io/en/latest/overview.html)) and login
* A general structure of [organisations, projects, modules and phases](https://github.com/liqd/adhocracy4/blob/master/docs/datamodel.md)
* An administration interface that can be used to create new participation projects
* A number of participation templates that you can choose from. Almost all of them are optional, which means you can tell the cookiecutter to add them or not:
  * Ideacollection/Brainstorming: users can hand in their ideas concerning a specific topic
  * Ideacollection/Brainstorming with Map (optional): Ideas can be located on a map inside a predefined area (e.g. your city)
  * Polls (optional): create a poll which users can take part in
  * Documents (optional): create a document with chapters and paragraphs and let user comment on it.
* A landing page with some [streamfield blocks](http://docs.wagtail.io/en/v2.0/topics/streamfield.html) to add some info to your landing page.
* Tests for all features you decided to use
* Basic styling with [Twitter Bootstrap](https://getbootstrap.com/)


## How to use the cookiecutter

### Prerequisite
Please make sure you have the following installed:
* [Python 3](https://www.python.org/downloads/)
* [Sqlite](https://www.sqlite.org/index.html) (best version: 3.25.0)
* libmagic
* [node.js](https://nodejs.org/en/)

When python3 is installed you can install the Cookiecutter via [pip](https://en.wikipedia.org/wiki/Pip_(package_manager)). To do so open a terminal and type in the following:

```
$ pip install cookiecutter
```

### Use the adhocracy4-cookiecutter
When you are done with installing cookiecutter you can navigate (with the terminal) to a directory where you want to save your new project.
Then type the following to your terminal and press enter:

```
$ cookiecutter gh:liqd/a4-cookiecutter
```

The cookiecutter will now ask you the following things in order to set up the project you like for you. In the brackets behind the question you can see the default value - if you want to stick to that just hit enter.

##### 1) Project Name:
First you have to decide for a project name. The default value is 'Project Name', so if you don't type anything your Project Name will be 'Project Name'. The Project Name will appear on your Landing Page. You can change it later.
```
project_name [Project Name]:
```

##### 2) project slug:
The default project slug is autogenerated from the project name. If you want to use a different slug make sure not to use any whitespaces or minuses. **This value will be used in a lot of places and it is hard to change it later, so choose wisely**.
```
project_slug [project_name]:
```

##### 3) project_app_prefix:
The default value is the same as the project slug and it is best to stick to it.
```
project_app_prefix [project_name]:
```

##### 4) Do you want to able to set up Projects, where users can add ideas on a map?
The default vlaue is [y], which means yes. If you type 'n' the programming code for displaying maps will not be added.
```
add_maps_and_mapideas_app [y]:
```

##### 5) Do you want to use polls?
The default vlaue is [y], which means yes. If you type 'n' the programming code for polls will not be added.
```
add_polls_app [y]:
```

##### 6) Do you want users to comment on documents?
The default vlaue is [y], which means yes. If you type 'n' the programming code for documents will not be added.
```
add_documents_app [y]:

```

Now, you are done. There should be a new directory with the name of your project_slug. Use the terminal to navigate to your newly created project.


## Next steps
When you changed to your project directory, execute the following commands to get started.

##### Step 1) Install all requirements and create a database
This will also create virtual env for you (don't worry if you don't know what that is). So just type in the next command and hit enter

```
$ make install
```

##### Step 2) Make sure everything is set up right
To see if the installed apps are working like they are meant to be, run the tests.

```
$ make test
```

##### Step 3) Add some data (called fixtures) to you database
This step will add some dummy data to your database which makes it easier for you to get started and to test your new project. This step will add an organisation called 'Liqd', a dummy idea collection project and the three users 'admin@liqd.net', 'initiator@liqd.net' and 'user@liqd.net'. They all have the same password 'password'.

```
$ make fixtures
```

##### Step 4) Start server
Now you are ready, type in the following command, hit enter.
```
$ make server
```
##### Step 5) Browse to website
Now you should have your local webserver running, s open a browser and navigate to 'localhost:8000'


##### Step 6) Login
Up in the right corner there should be login link. Click that and login with 'initiator@liqd.net' and 'password'. As soon as you are logged in there should be a user dropdown underneath the username, if you open this there is a link to 'liqd'. If you click it you will see the administration interface for the 'liqd'organisation.

##### Step 7) Update Landingpage
When you login as admin@liqd.net and navigate to the landing page there should be a round button with a bird on it. If you click on it, you get the possibility to edit the page.

##### Step 8) Get coding!
There are lots of tutorials for Django and wagtail around. Check them out and see what you want to add.
