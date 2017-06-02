# dockershift-playground
Minimum example of Docker + OpenShift deployment

## Install
```sh
$ git clone https://github.com/mvidalgarcia/dockershift-playground.git
$ cd dockershift-playground
```

## Run
### Local
```sh
$ export FLASK_APP=app/hello.py
$ flask run
```

### Docker
```sh
$ docker-compose up --build
```

### OpenShift

Import app from `docker-compose`:
```sh
$ oc import docker-compose -f docker-compose.yml
```

Create template from running app:
```sh
$ oc export all -o yaml --as-template=dockershift-template > dockershift-template.yaml
```

Add `hello.cfg` file as a ConfigMap:
```sh
$ oc create configmap settings --from-file=conf_key=hello.cfg
```

Import YAML template in OpenShift and create application:
1. _Add to project_
2. _Import YAML/JSON_ tab
3. _Browse..._ and select `dockershift-template.yaml`
4. _Create_ and _Continue_
5. _Create_

or do the same from terminal:
```sh
$ oc new-app -f dockershift-template.yaml
```

Apply changes to template:
```sh
$ oc process -f dockershift-template.yaml | oc apply -f -
```
