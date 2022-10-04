FROM python:latest
WORKDIR /app
RUN pip install flask
RUN pip install flask-bcrypt
RUN pip install flask-login
RUN pip install -U Flask-SQLAlchemy
RUN pip install pytest
RUN pip install -U Flask-WTF
COPY . /app
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]