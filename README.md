## Django youtube Search
An application which fetches latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## Installation and setup 

### Setup and running of project (Backend)
- Fork the repository and clone it.
- The project used `pipenv` to manage dependencies.
- Install [Pipenv](https://pypi.org/project/pipenv/) using the following command: 
``` bash
pip install pipenv
```
- Navigate to the project directory and initialize the environment using the following command - 
``` bash
pipenv shell --python 3.8
```
- The above step also activates the environment, for activating the environment in subsequent sessions type the following command:
```bash
pipenv shell
```
- At the root of your project directory <br>

```bash
pipenv install
pre-commit install
```

- This will setup the project requirements and pre-commit test hooks!

- After the above setup, run

```bash
 - python manage.py makemigrations
 - python manage.py migrate
```
- Start the backend server
  `python manage.py runserver`
  
**This runs the backend server at default port `8000`.
  Open [http://localhost:8000](http://localhost:8000) to view it in the browser.**<br />

