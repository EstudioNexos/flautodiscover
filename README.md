# flautodiscover
Email settings autodiscover / autoconfig for outlook, thunderbird and others. Made with Python and Flask

Includes multilingual user help for configuring email clients.

## Python modules requirements and setup

Flask, Flask Ptrans, Flask Markdown and Xmltodict.

```git clone https://github.com/EstudioNexos/flautodiscover.git```

```pip install -r flautodiscover/requirements.txt```

![Screenshot of flautodiscover](https://raw.githubusercontent.com/EstudioNexos/flautodiscover/master/screenshot.jpg)

## Server requirements and setup

You can serve this app using your favourite wsgi method. We provide nginx+supervisor+gunicorn documentation.

You need to serve web application using an SSL certificate or Outlook will no work. (Pending)

Set your setup paths in flautodiscover/gunicorn_conf.py, fla_supervisor.conf and fla_nginx.conf

Copy fla_supervisor.conf to /etc/supervisor/conf.d/ and run supervisorctl update. Run supervisorctl status to check for errors.

Copy fla_nginx.conf to /etc/nginx/sites-available. Link /etc/nginx/sites-available/fla_nginx.conf to etc/nginx/sites-enabled/fla_nginx.conf. Run nginx -t to check for errors. Finally run service nginx reload.

## Domains requirements and setup

You will have to have access to domains DNS records.

Add two CNAME records to each domain you are serving mail for:

```
CNAME autodiscover mydomain.com
CNAME autoconfig mydomain.com
```
Go with your web browser to https://autodiscover.mydomain.com and you should be able to see web page and MUAs documentation.

## Translate to your users language

Duplicate file at lang/es-es.json to desired language code, eg: lang/fr-fr.json for french speakers.

Edit fr-fr.json "values" to french language.

More info: https://github.com/Skyscanner/flask-ptrans/blob/master/README.md

Note 1: lang files must be valid JSON files, do not leave trailing comas.

Note 2: You can contribute to this repo with your language files though web help is still unfinished and lang files may suffer a lot of changes.


