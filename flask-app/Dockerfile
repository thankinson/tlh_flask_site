FROM python:latest
WORKDIR /flask-app
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
COPY . /flask-app
EXPOSE 5000
RUN python3 create.py
ENTRYPOINT ["python", "app.py"]