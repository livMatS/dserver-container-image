# dserver container image

[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/jotelha/dserver?label=dockerhub)](https://hub.docker.com/repository/docker/jotelha/dserver) [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/livMatS/dserver-container-image/publish.yml?branch=main)](https://github.com/livMatS/dserver-container-image/actions?query=workflow%3Apublish)

Part of https://github.com/livMatS/dserver-container-composition.

Provides https://github.com/jic-dtool/dserver together with several plugins in a container image for testing purposes.

To build manually for testing purposes, run

    docker build -t jotelha/dserver -f compose/production/dserver/Dockerfile .

## Envionment variables

Environment variables are found in `envs/production/dserver`:

```
BIND_TO="0.0.0.0:5000"

# a plain text list of all users, one user per line
DSERVER_USER_FILE=/app/users
# a plain text list of all users with admin privileges, must also appear in user list above
DSERVER_ADMIN_USER_FILE=/app/admin_users
# a plain text list of all base URIs to index, one entry per line
DSERVER_BASE_URI_FILE=/app/base_uris

# core flask app config
FLASK_APP=dserver
LOGLEVEL=warning

# dump all http requests to server application to stdout for debugging purposes
DUMP_HTTP_REQUESTS=false

SQLALCHEMY_DATABASE_URI=postgresql://testing_user:testing_password@postgres:5432/dtool

JWT_PUBLIC_KEY_FILE=/run/secrets/jwt_key.pub
JWT_PRIVATE_KEY_FILE=/run/secrets/jwt_key

SSL_CERT_FILE=/run/secrets/tls_cert.pem
SSL_KEY_FILE=/run/secrets/tls_key.pem

# search plugin configuration
SEARCH_MONGO_URI=mongodb://mongodb:27017/
SEARCH_MONGO_DB=dtool_info
SEARCH_MONGO_COLLECTION=datasets

# search plugin configuration
RETRIEVE_MONGO_URI=mongodb://mongodb:27017/
RETRIEVE_MONGO_DB=dtool_info
RETRIEVE_MONGO_COLLECTION=datasets

# direct mongo plugin configuration
DSERVER_MONGO_URI=mongodb://mongodb:27017/
DSERVER_MONGO_DB=dtool_info
DSERVER_MONGO_COLLECTION=metadata

DSERVER_QUERY_DICT_VALID_KEYS=["free_text","creator_usernames","base_uris","uuids","tags","query"]
DSERVER_ALLOW_DIRECT_AGGREGATION=False

# dependency graph plugin configuration
DSERVER_ENABLE_DEPENDENCY_VIEW=True
DSERVER_DEPENDENCY_KEYS=["readme.derived_from.uuid","annotations.source_dataset_uuid"]

# notification plugin configuration
DSERVER_NOTIFY_BUCKET_TO_BASE_URI={"test-bucket": "s3://test-bucket"}
DSERVER_NOTIFY_ALLOW_ACCESS_FROM="0.0.0.0/0"
```

Server and plugins each have their own set of environment variables.
See server and plugin documentations at

* https://github.com/jic-dtool/dserver#setup-and-configuration
* https://github.com/jic-dtool/dtool-lookup-server-search-plugin-mongo
* https://github.com/jic-dtool/dtool-lookup-server-retrieve-plugin-mongo
* https://github.com/livMatS/dserver-dependency-graph-plugi
* https://github.com/livMatS/dserver-direct-mongo-plugin
* https://github.com/livMatS/dserver-notification-plugin

for further information on the effect of above environment variables.

## Secrets

* `/run/secrets/jwt_key.pub` - JSON web token, public
* `/run/secrets/jwt_key` - JSON web token, private
* `/run/secrets/tls_key.pem` - tls key for dtool lookup server
* `/run/secrets/tls_cert.pem` - tls certificate for dtool lookup server
