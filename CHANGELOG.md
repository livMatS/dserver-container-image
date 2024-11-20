# Changelog for *dserver-container-image*

## 0.13.0

- ENH: Apply ProxyFix middelware
- DEP: updated pinned versions, in particular notification plugin 0.4.3

## 0.12.0

- DEP: updated pinned versions, in particular notification plugin 0.4.2

## 0.11.0

- DEP: updated pinned versions, in particular dservercore 0.21.0

## 0.10.1

- MAINT: fixed FLASK_APP env var and wsgi script import to use dtoolcore

## 0.10.0

- MAINT: rebrand from dtool-lookup-server to dserver
- DEP: use dserver-minimal meta package
- DEP: use current dserver-* plugin releases
- DEP: use Python 3.12 base image

## 0.9.0

- DEP: dtool-lookup-server 0.18.0
- DEP: mongo search and retrieve 0.2.0

## 0.8.1

- Rebuilt with more recent development versions of libraries

## 0.8.0

- ENH: Use openapi-enabled and mongo-refactored development branch of dtool-lookup-server
  -e git+https://github.com/jotelha/dtool-lookup-server.git@master#egg=dtool-lookup-server
  -e git+https://github.com/jotelha/dtool-lookup-server-search-plugin-mongo.git@main#egg=dtool-lookup-server-search-plugin-mongo
  -e git+https://github.com/jotelha/dtool-lookup-server-retrieve-plugin-mongo.git@main#egg=dtool-lookup-server-retrieve-plugin-mongo

## 0.7.0

- ENH: Use openapi-enabled development branch of dtool-lookup-server and according plugin branches
  -e git+https://github.com/jotelha/dtool-lookup-server.git@openapi#egg=dtool-lookup-server
  -e git+https://github.com/livMatS/dtool-lookup-server-plugin-scaffolding.git@openapi#egg=dtool-lookup-server-plugin-scaffolding
  -e git+https://github.com/livMatS/dtool-lookup-server-dependency-graph-plugin.git@openapi#egg=dtool-lookup-server-dependency-graph-plugin
  -e git+https://github.com/livMatS/dtool-lookup-server-direct-mongo-plugin.git@openapi#egg=dtool-lookup-server-direct-mongo-plugin
  -e git+https://github.com/livMatS/dtool-lookup-server-notification-plugin.git@openapi#egg=dtool-lookup-server-notification-plugin


## Before 0.7.0

no chnagelog kept
