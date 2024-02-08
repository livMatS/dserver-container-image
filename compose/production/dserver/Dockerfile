FROM python:3.12.2-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
RUN mkdir -p /root/.config/dtool

# we expect out own configuration to change less frequently than the pinned Python package versions
COPY dtool/dtool.json /root/.config/dtool

COPY compose/production/dserver/wsgi.py /app
COPY compose/production/dserver/start /start
COPY compose/production/dserver/init_db /init_db
COPY compose/production/dserver/register_users_and_base_uris /register_users_and_base_uris
COPY compose/production/dserver/refresh_index /refresh_index
COPY compose/production/dserver/refresh_index /etc/cron.daily/refresh_index
COPY compose/production/dserver/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
# cron job needs "sourcible" env vars definition within container. However, the docker-style
# file_env does not treat quotes the same way as the shell. Therefore, we copy the env_file
# into the container to merely mark all environment variables to be defined via the container
# compose mechanism. Their actual values at image build time won't be taken into account.
# Instead, actual values are read at container launch (see start file):
COPY envs/production/dserver /refresh_index.envs.reference

# sample userand base_uri files
COPY compose/production/dserver/users /app
COPY compose/production/dserver/admin_users /app
COPY compose/production/dserver/base_uris /app

RUN chmod 0744 /etc/cron.daily/refresh_index
RUN chmod +x /init_db
RUN chmod +x /register_users_and_base_uris
RUN chmod +x /refresh_index
RUN sed -i 's/\r//' /start
RUN chmod +x /start

COPY compose/production/dserver/requirements.txt /requirements.txt
RUN apt-get --yes update && \
    apt-get --no-install-recommends --yes install gcc libc6-dev libpq-dev supervisor cron git && \
    pip install setuptools setuptools_scm && \
    pip install -r /requirements.txt && \
    apt-get remove --purge --autoremove -y gcc git && \
    rm -rf /var/lib/apt/lists/*
# remove importlib_metadata when https://github.com/IMTEK-Simulation/dserver-direct-mongo-plugin/issues/1 resolved

WORKDIR /app
