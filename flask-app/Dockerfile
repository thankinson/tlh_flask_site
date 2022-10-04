FROM python:latest
WORKDIR /app
RUN pip install flask
RUN pip install flask-bcrypt
RUN pip install flask-login
RUN pip install -U Flask-SQLAlchemy
RUN pip install pytest
RUN pip install -U Flask-WTF
RUN pip install wtforms
RUN pip install wtforms[email]
RUN python3 -m pip install PyMySQL
RUN python3 -m pip install PyMySQL[rsa]
COPY . /app
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]