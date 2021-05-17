# board_manager
Manage Your Trello Users from a single SUPER USER ACCOUNT that have access as admin to all the boards you want to manage.

## Technologies used

* Python 3.7.4

#### **NOTE:** ####
  - **All commands should be run in the project root directory**

## Prerequisites ##

* Install virtualenv globally
```
pip install virtualenv
```

## How do I get set up? ##

* Create the repository on the remote (for example via Bitbucket)

* Add your pip packages to PROJECT_DIRECTORY/requirements.txt

* And activate your newly created virtual environment
  ```
  PROJECT_DIRECTORY/.virtualenv/Scripts/activate
  ```

* Make sure VSCode's interpreter for python is set to the newly created
  virtual environment, and that the environment is active in the terminal.
  You should see a ```(.virtualenv)``` prefix in the terminal.

* Then install the packages needed there
  ```
  pip install -r PROJECT_DIRECTORY/requirements.txt
  ```

* Add your environment variables into the .dev_prod.env.template (WITHOUT VALUES, Just the variable names as a template)

* Copy PROJECT_DIRECTORY/.env.template to the root directory with the name .env

* Copy PROJECT_DIRECTORY/.dev_prod.env.template to the root directory with the name .dev.env and or .prod.env (This is where your production and development environment variables will be set)

* Fill in the variables needed in the files created above. DEBUG="TRUE" should be the only variable present in the .env file in the root of the project directory

* Next fill in the PROJECT_DIRECTORY/settings.py file if needed (Read the docstring and comments in the settings file)

* Use furo\furo\generate_secret_key.py to generate a secret key, place that on the SECRET_KEY varaible your .dev.env file

Django specific commands to get set up - DEVELOPMENT

```
python .\manage.py makemigrations

<!-- Make sure you're DEBUG is set to TRUE -->
python .\manage.py migrate

```
* Load in default planning data (required)
```
python .\manage.py loaddata planning_departments.json
python .\manage.py loaddata planning_processes_production.json
```

* Load in default process data for DEV (required for DEV)
```
python .\manage.py loaddata planning_processes_debug.json
```

* Load in default process data for LIVE (required for LIVE)
```
python .\manage.py loaddata planning_processes_production.json

```

* Load in default furo jobs data (required for DEV)
```
python .\manage.py loaddata engineering_jobs.json
```

python manage.py createsuperuser

<!-- Final step to run the Development environment -->
python .\manage.py runserver


* **Contact me by below details if any clarification is needed. Happy devving!**

## Contribution guidelines ##

* Branch of off the dev/master branch

* Make your changes, commit and push to your custom branch

* Create a pull request into the dev/master branch for review

* Make sure code is at least 80% unit tested

* Make sure that documentation has been generated

* See below naming conventions:
  * ```ClassFileName```
  * ```ClassName```
  * ```variable_name```
  * ```repository_name```
  * ```folder_name```

* Remove any unneeded folder structures or files

## Testing ##

* Running pytest unit tests manually
```
pytest ./
```

* Pytest coverage report in ./coverage directory (shared libraries are ignored for unit testing)

* For debugging tests, refer to the comment in the root file called pytest.ini

### Documenting ###

* Generating documentation (shared libraries are ignored)
```
pdoc --html ./ --output-dir docs --force
```

* The newly generated documentation should now be in the root folder called docs/

* This documentation is generated using the docstrings added in the python files

## Who do I talk to? ##

* Martin Cronje (Contributor) - <martin.cronje.home@gmail.com>

---
