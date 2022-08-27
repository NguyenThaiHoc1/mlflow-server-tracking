FROM apache/airflow:2.1.0
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         build-essential libopenmpi-dev iputils-ping\
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \

RUN apt-get update
USER airflow
RUN pip install --no-cache-dir plotly==4.9
RUN pip install --no-cache-dir svglib==1.1.0
RUN pip install --no-cache-dir fpdf2
RUN pip install psycopg2-binary
