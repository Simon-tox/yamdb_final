### Describtion
Docker is a platform for REST API of the service YaMDB on the bases Dlangob and PostgreSql 12.4
https://github.com/Simon-tox/yamdb_final/actions/workflows/main.yml/badge.svg
https://github.com/Simon-tox/yamdb_final/actions/workflows/main.yml/badge.svg?branch=feature-1
https://github.com/Simon-tox/yamdb_final/actions/workflows/main.yml/badge.svg?event=pull_request

### Commands for running the project

A step by step series of examples that tell you have to get a development env running

Clone a repository from the Gitgub

```
  git clone https://github.com/Simon-tox/infra_sp2.git

```
Go to the folder with a project

```

cd infra_sp2

```

Create the repository called Dockerfile and add there instructions

```
  touch Dockerfile

```
Command to build the image 

```
  docker build -t yamdb .

```
Command to run the container
```
  docker run -it -p 8000:8000 yamdb
 
```
Command to collect and run the project

```
  docker-compose up
 
```
  
### Command for creating a superuser

```
  python3 manage.py createsuperuser
  
  Then, follow the instructions below and press Enter
 
```

### Command for adding data to the database

```

  docker exec -it <CONTAINER ID> bash
  
```
To exit the container write 'exit'
 



* Hat tip to anyone who's code was used
* Inspiration
* etc
>>>>>>> 9e1d1c4cb9cdd4b2f9eeeca89f3d113383d8583b
