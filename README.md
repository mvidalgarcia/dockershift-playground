# dockershift-playground
Minimum example of Docker + OpenShift deployment

## Install
```sh
git clone https://github.com/mvidalgarcia/dockershift-playground.git
cd dockershift-playground
```

## Run
### Local
```sh
export FLASK_APP=app/hello.py
flask run
```

### Docker
```sh
docker-compose up --build
```

### OpenShift
