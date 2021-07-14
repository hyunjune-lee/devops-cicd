FROM mariadb:latest

ENV MYSQL_ROOT_PASSWORD=mysecret
ENV MYSQL_DATABASE=daily_quiz
ENV MYSQL_DATABASE_DB=daily_quiz

COPY *.sql /docker-entrypoint-initdb.d/
