# flautodiscover
Email settings autodiscover / autoconfig for outlook, thunderbird and others. Made with Python and Flask

Includes multilingual user help for configuring email clients.

## Python modules requirements

Flask, Flask Ptrans and Xmltodict

## Server requirements

You can serve this app using your favourite wsgi method. We provide nginx+supervisor+gunicorn documentation.

## Domains requirements

You will have to have access to domains DNS records.

## Translate to your users language

Duplicate file at lang/es-es.json to desired language code, eg: lang/fr-fr.json for french speakers.

Edit fr-fr.json "values" to french language.

Note 1: lang files must be valid JSON files, do not leave trailing comas.
Note 2: You can contribute to this repo with your language files though web help is still unfinished and lang files may suffer a lot of changes.
