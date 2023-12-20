FROM python:alpine

RUN pip --no-cache-dir install pysnowflake 

ENTRYPOINT ["snowflake_start_server"]
