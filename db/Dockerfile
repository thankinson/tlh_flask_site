FROM mysql:latest
LABEL maintainer="admin@email.com"
ENV MYSQL_ROOT_PASSWORD password
ADD CreateTable.sql /docker-entrypoint-initdb.d
EXPOSE 3306