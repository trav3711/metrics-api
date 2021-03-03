FROM python:3.9.2-alpine3.13

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

ADD ./requirements.txt /api/requirements.txt

RUN set -ex \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /api/requirements.txt \
    && runDeps="$(scanelf --needed --nobanner --recursive /env \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u)" \
    && apk add --virtual rundeps $runDeps

ADD . /api
WORKDIR /api

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "metrics_api.wsgi:application"]
