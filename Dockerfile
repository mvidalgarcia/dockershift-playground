FROM centos:7

RUN yum install -y python-devel python-virtualenv

RUN mkdir -p /opt/dockershift/
RUN virtualenv /opt/dockershift/venv

ARG pip="/opt/dockershift/venv/bin/pip"

RUN ${pip} install --upgrade pip
RUN ${pip} install https://github.com/mvidalgarcia/dockershift-playground/releases/download/v0.0.0/dockershift_playground-0.0.0-py2-none-any.whl

COPY entrypoint.sh /opt/dockershift/entrypoint.sh
RUN chmod 755 /opt/dockershift/entrypoint.sh

EXPOSE 8000

COPY hello.cfg /opt/dockershift/hello.cfg

ENTRYPOINT /opt/dockershift/entrypoint.sh
