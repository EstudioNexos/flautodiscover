import os, uuid
import xmltodict
from ConfigParser import SafeConfigParser
from flask import Flask, request, render_template, make_response, redirect, abort
#~ from settings import *
from flaskext.markdown import Markdown
from flask_ptrans import ptrans

def local_path(*path_elements):
    return os.path.abspath(os.path.join(__file__, "..", *path_elements))

conf = SafeConfigParser()
conf.read('sample_conf.ini')
DEBUG = conf.get('general', 'debug')

app = Flask(__name__)
ptrans.init_localisation(local_path("lang"))
app.jinja_env.add_extension('flask_ptrans.ptrans.ptrans')
Markdown(app)


""" Default context """
context = {
    'server': conf.get('general', 'server'),
    'domain': conf.get('general', 'domain'),
    'ttl': conf.get('general', 'ttl'),
    'disable_pop': conf.get('general', 'disable_pop'),
    'imap': {
        'authentication': conf.get('imap', 'authentication'),
        'host':conf.get('imap', 'host'),
        'port':conf.get('imap', 'port'),
        'spa': conf.get('imap', 'spa'),
        'ssl': conf.get('imap', 'ssl'),
        'socket': conf.get('imap', 'socket')
        },
    'smtp': {
        'authentication': conf.get('smtp', 'authentication'),
        'host':conf.get('smtp', 'host'),
        'port':conf.get('smtp', 'port'),
        'spa': conf.get('smtp', 'spa'),
        'ssl': conf.get('smtp', 'ssl'),
        'tls': conf.get('smtp', 'tls'),
        'socket': conf.get('smtp', 'socket')
        },
    'pop': {
        'authentication': conf.get('pop', 'authentication'),
        'host':conf.get('pop', 'host'),
        'port':conf.get('pop', 'port'),
        'spa': conf.get('pop', 'spa'),
        'ssl': conf.get('pop', 'ssl'),
        'socket': conf.get('pop', 'socket')
        },
    #~ 'socket': DEFAULT_SERVER_SOCKET,
    'payload_identifier': '.'.join(('autodiscover.%s' % conf.get('general', 'server')).split('.')[::-1]),
    'company_name': conf.get('company', 'name'),
    'company_url': conf.get('company', 'url'),
    'company_contact': conf.get('company', 'contact'),
}

@app.before_request
def before_request():
    if DEBUG:
        print "HEADERS", request.headers
        print "REQ_path", request.path
        print "ARGS",request.args
        print "DATA",request.data
        print "FORM",request.form

@app.route("/Autodiscover/Autodiscover.xml", methods=['GET','POST',])
@app.route("/autodiscover/autodiscover.xml", methods=['GET','POST',])
@app.route("/autodiscover", methods=['GET','POST',])
def outlook_applemail():
    """ XML response for Outlook and Desktop Mail.
    Mac Mail only works for Exchange Services, untested. """
    data = xmltodict.parse(request.data)
    email = data['Autodiscover']['Request']['EMailAddress']
    try:
        schema =  data['Autodiscover']['Request']['AcceptableResponseSchema']
    except:
        schema = "http://schemas.microsoft.com/exchange/autodiscover/outlook/responseschema/2006a"
    mailbox, domain = email.split('@')
    context['domain'] = domain
    context['email'] = email
    context['name'] = mailbox
    context['schema'] = schema
    tpl = render_template('autodiscover.xml', **context)
    response = make_response(tpl)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route("/mail/config-v1.1.xml")
def thunderbird():
    """ XML response for Thunderbird. """
    email = request.args.get('emailaddress')
    mailbox, domain = email.split('@')
    context['domain'] = domain
    context['email'] = email
    context['name'] = mailbox
    tpl = render_template('autoconfig.xml', **context)
    response = make_response(tpl)
    response.headers["Content-Type"] = "application/xml"    
    return response
    
@app.route("/")
def index():
    """ Welcome page in HTML. """
    muas = [
        {'option':'macmail','name': 'Apple OSX Mail'},
        {'option':'outlook','name': 'Microsoft Outlook'},
        {'option':'gmailweb','name': 'Gmail Web'},
        {'option':'gmailandroid','name': 'Gmail Android'},
    ]
    template_doc = "doc/empty.html"
    locale = ptrans.best_locale()
    email = request.args.get('emailaddress')
    mua = request.args.get('mua')
    selected_mua = None
    context['email'] = ''
    try:
        locale = request.headers.get('Accept-Language').split(",")[0]
    except: pass
    if email and '.' in email and '@' in email and mua:
        mailbox, domain = email.split('@')
        context['domain'] = domain
        context['email'] = email
        selected_mua = mua
        template_doc = "doc/%s-%s.md" % (mua, locale)
    context['selected_mua'] = selected_mua
    context['template_doc'] = template_doc
    context['locale'] = locale
    context['muas'] = muas
    return render_template('hello.html', **context)

@app.route("/browserconfig.xml")
def ie():
    """ Just avoiding 404 log entries """
    tpl = render_template('browserconfig.xml', **context)
    response = make_response(tpl)
    response.headers["Content-Type"] = "application/xml"
    return response
    
@app.route("/email.mobileconfig")
def ios_applemail():
    """ XML response for iOS and Apple Mail. """
    email = request.args.get('emailaddress', None)
    if email:
        mailbox, domain = email.split('@')
        context['payload_uuid'] = uuid.uuid1()
        context['domain'] = domain
        context['email'] = email
        context['name'] = mailbox
        tpl = render_template('mobileconfig.xml', **context)
        response = make_response(tpl)
        response.headers["Content-Type"] = "application/x-apple-aspen-config; chatset=utf-8"
        response.headers["Content-Disposition"] = "attachment;filename=%s.mobileconfig" % domain
        return response
    abort(404)
    
if __name__ == "__main__":
    print DEBUG
    #~ app.run(debug=DEBUG, host=HOST, port=443, ssl_context='adhoc') #For development purposes only. pyOpenssl required
    app.run(debug=DEBUG, host=conf.get('general', 'host'), port=int(conf.get('general', 'port')))
