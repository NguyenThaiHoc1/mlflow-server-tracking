FROM postgres:13

COPY entrypoint/init.sql /docker-entrypoint-initdb.d/init.sql
RUN chmod +x /docker-entrypoint-initdb.d/*
