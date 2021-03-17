A simple Docker Compose app to get the stats of a container, from within the container, using the docker.sock socket
* Uses the Docker Compose sample app for Python with Flask: https://docs.docker.com/compose/gettingstarted/ 
* Uses the Docker SDK for Python: https://docker-py.readthedocs.io/en/stable/index.html 
* Inspired by this StackOverflow post about docker.sock: https://stackoverflow.com/questions/62749397/connect-to-docker-sock-to-get-container-stats-using-python-socket-only 

Usage
* cd into directory
* `docker-compose up`