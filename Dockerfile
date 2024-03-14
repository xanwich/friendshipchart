FROM python:3.11-bookworm
RUN apt-get update \
    && apt-get install graphviz libgraphviz-dev -y
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
RUN python models.py
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]