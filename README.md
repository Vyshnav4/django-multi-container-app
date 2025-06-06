#Django Polls with Docker Compose & PostgreSQL

Description: A classic Django polling application fully orchestrated with Docker Compose.
This project runs two separate services: a web container for the Django application and a db container for the PostgreSQL database,
demonstrating a complete and containerized development workflow.

 Build and Run the Containers
Open terminal, navigate to the project's root directory and run the following command:

docker-compose up --build

•	docker-compose up: This command starts up the services defined in docker-compose.yml file.
•	--build: This flag tells Docker Compose to build the image for your web service from the Dockerfile before starting the containers.

We will see a lot of output as Docker downloads the postgres and python images, installs your dependencies, and starts both the database and web server containers.
 
 Set Up the Database Inside the Container
 
Because the application is running inside a container, you need to run the manage.py commands inside that container.

Open a new terminal window (leave the docker-compose up command running in the first one) and run the following commands:

a. Find your container ID: First, list the running containers to find the ID or name of your web service container.

docker ps

b. Run the migrations:

Use docker-compose exec to run the migrations inside the web container.

docker-compose exec web python manage.py makemigrations polls
docker-compose exec web python manage.py migrate

c. Create a superuser: 
Now create a superuser, also inside the web container.

docker-compose exec web python manage.py createsuperuser

Follow the prompts to create admin user.
 
 
 View Application
 
Containerized Django application is now running and connected to its PostgreSQL database

•	Polls App: Open your web browser and go to http://127.0.0.1:8000/polls/

•	Admin Site: Go to http://127.0.0.1:8000/admin/ and log in with your new superuser credentials.

Stopping the Application

To stop the containers, go to the terminal where docker-compose up is running and press Ctrl+C. To remove the containers and the network, you can run:
docker-compose down

To also remove the database volume  use:

docker-compose down -v

Project Structure

myproject/
├── .dockerignore              
├── docker-compose.yml         
├── Dockerfile                 
├── manage.py                  
├── requirements.txt           
├── myproject/                
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py           
│   ├── urls.py
│   └── wsgi.py
└── polls/                    
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    │   ├── 0001_initial.py
    │   └── __init__.py
    ├── static/
    │   └── polls/
    │       └── style.css
    └── templates/
        └── polls/
            ├── detail.html
            ├── index.html
            └── results.html

