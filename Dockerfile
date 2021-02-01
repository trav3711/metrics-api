FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /metrics_backend_api
WORKDIR /metrics_backend_api
COPY . /metrics_backend_api/
EXPOSE 8080
RUN pip install -r ./requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["gunicorn", "--bind", ":8080", "--workers", "3", "metrics_api.wsgi:application"]
