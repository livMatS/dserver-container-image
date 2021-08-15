# dtool lookup server container image

[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/jotelha/dtool-lookup-server?label=dockerhub)](https://hub.docker.com/repository/docker/jotelha/dtool-lookup-server) [![GitHub Workflow Status](https://img.shields.io/github/workflow/status/jotelha/dtool-lookup-server-container-image/publish)](https://github.com/jotelha/dtool-lookup-server-container-image/actions?query=workflow%3Apublish)

Part of https://github.com/jotelha/dtool-lookup-server-container-composition.

Provides https://github.com/jic-dtool/dtool-lookup-server in a container image for testing purposes. 

## Envionment variables

* `FLASK_APP`, default: `dtool_lookup_server`
* `SQLALCHEMY_DATABASE_URI`, default: `postgres://testing_user:testing_password@postgres:5432/dtool`
* `MONGO_URI`, defualt: `mongodb://mongodb:27017/dtool_info`
* `JWT_PUBLIC_KEY_FILE`, default: `/run/secrets/jwt_key.pub`
* `JWT_PRIVATE_KEY_FILE`, default: `/run/secrets/jwt_key`
* `SSL_CERT_FILE`, default: `/run/secrets/tls_cert.pem`
* `SSL_KEY_FILE`, default: `/run/secrets/tls_key.pem`
* `DTOOL_LOOKUP_SERVER_QUERY_DICT_VALID_KEYS`, default: `["free_text","creator_usernames","base_uris","uuids","tags","query"]`
* `DTOOL_LOOKUP_SERVER_ALLOW_DIRECT_AGGREGATION`, default: `False`
* `DTOOL_LOOKUP_SERVER_ENABLE_DEPENDENCY_VIEW`, default: `True`
* `DTOOL_LOOKUP_SERVER_DEPENDENCY_KEYS`, default: `["readme.derived_from.uuid","annotations.source_dataset_uuid"]`

See server and plugin documentations at

* https://github.com/jic-dtool/dtool-lookup-server#setup-and-configuration, 
* https://github.com/IMTEK-Simulation/dtool-lookup-server-dependency-graph-plugin#setup-and-configuration
* https://github.com/IMTEK-Simulation/dtool-lookup-server-direct-mongo-plugin

for further information on the effect of above environement variables.

## Secrets

* `/run/secrets/jwt_key.pub` - JSON web token, public
* `/run/secrets/jwt_key` - JSON web token, private
* `/run/secrets/tls_key.pem` - tls key for dtool lookup server
* `/run/secrets/tls_cert.pem` - tls certificate for dtool lookup server
