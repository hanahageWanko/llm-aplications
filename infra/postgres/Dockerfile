FROM postgres:14.5-bullseye

COPY ./init/init.sql /docker-entrypoint-initdb.d/init.sql
EXPOSE 5432