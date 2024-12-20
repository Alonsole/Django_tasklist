FROM python:3.10-alpine
ENV PYTHONDONTRITEBYTECODE="1"
ENV PYTHONBUFFERED="1"
WORKDIR /app
ENV APP_HOME=/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8000

RUN python manage.py collectstatic --noinput


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "task_list.wsgi"]

