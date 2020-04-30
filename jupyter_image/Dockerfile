FROM python:3.6-slim

ENV HOME=/app

RUN apt-get update && apt-get install -y \
 git

ADD requirements.txt /app/
WORKDIR $HOME
RUN pip install --upgrade pip \
   && pip install -r requirements.txt

RUN mkdir -p /root/.config/matplotlib
RUN echo "backend : Agg" > /root/.config/matplotlib/matplotlibrc

ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

RUN jupyter notebook --generate-config
RUN echo "c.NotebookApp.password='sha1:b2157e7e9d2f:a7483810bac9f433f9c7417714eea86d3e14d011'">>/app/.jupyter/jupyter_notebook_config.py

RUN echo "c.NotebookApp.notebook_dir ='/app/python_scripts'">>/app/.jupyter/jupyter_notebook_config.py

EXPOSE 8888
