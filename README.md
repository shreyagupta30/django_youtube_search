## Django youtube Search
An application which fetches latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## Installation and setup through virtualenv

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

## Installation and setup through docker
In order to proceed with this step, make sure you have docker and docker compose installed in your system. 
- Run the commands below:
``` bash 
docker-compose build
docker-compose up
```
**This runs the backend server at default port `8000`.
  Open [http://localhost:8000](http://localhost:8000) to view it in the browser.**<br />

## API Routes and queries

- `localhost:8000/api/key` - This route is used to add your API key for Youtube API. You can add multiple keys and it will select the key whose usage quota limit is not yet surpassed.
<img src = "https://github.com/shreyagupta30/django_youtube_search/blob/master/assets/Screenshot%202021-04-16%20at%202.53.40%20AM.png?raw=true"/>

- `localhost:8000/api/videos` - This route fetches latest videos in reverse chronological order for a predefined search query. In this example, I am using "ipl" as my query. It can be changed accordingly in `backend.app.services`. 
<img src = "https://github.com/shreyagupta30/django_youtube_search/blob/master/assets/Screenshot%202021-04-16%20at%202.58.14%20AM.png?raw=true"/>

- `localhost:8000/api/videos?page=n`- This route returns pages of the query, where n is page number you need to see. Currently every page shows 10 videos which can be changed in `backend.app.views` accordingly.

<img src = "https://github.com/shreyagupta30/django_youtube_search/blob/master/assets/Screenshot%202021-04-16%20at%202.58.56%20AM.png?raw=true"/>


- `localhost:8000/api/videos?search=<keyword>` - This filters the videos containing the `keyword` mentioned in either title or description or both of the videos.
<img src = "https://github.com/shreyagupta30/django_youtube_search/blob/master/assets/Screenshot%202021-04-16%20at%203.00.02%20AM.png?raw=true"/>
We can see in the image below that there are no video with keyword `dog`
<img src = " https://github.com/shreyagupta30/django_youtube_search/blob/master/assets/Screenshot%202021-04-16%20at%203.00.39%20AM.png?raw=true"/>


