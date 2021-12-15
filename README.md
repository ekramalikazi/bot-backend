# python-flask-docker
Basic Python Flask app in Docker which prints the hostname and IP of the container

### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone https://github.com/ekramalikazi/bot-backend.git
$ docker build -t ekramalikazi/bot-backend .
```

### Run the container
Create a container from the image.
```
$ docker run --rm --name my-container -d -p 8080:8080 ekramalikazi/bot-backend
```

Now visit http://localhost:8080

```
http://localhost:8080/api/jenkins/call
```

