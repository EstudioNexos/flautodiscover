from flask import Flask, request, render_template, make_response, redirect, abort
from settings import *
import xmltodict
import uuid
app = Flask(__name__)

""" Default context """
context = {
    'server': DEFAULT_SERVER_DOMAIN,
    'domain': DEFAULT_SERVER_DOMAIN,
    'imap': {'host':DEFAULT_SERVER_IMAP, 'port':DEFAULT_SERVER_IMAP_PORT},
    'smtp': {'host':DEFAULT_SERVER_SMTP, 'port':587},
    'socket': DEFAULT_SERVER_SOCKET,
    'payload_identifier': PAYLOAD_IDENTIFIER,
    'microsoft_spa': DEFAULT_MICROSOFT_SPA,
    'contact_company': DEFAULT_CONTACT_COMPANY,
    'contact_url': DEFAULT_CONTACT_URL,
}

@app.before_request
def before_request():
    if DEBUG:
        #~ print "HEADERS", request.headers
        #~ print "REQ_path", request.path
        #~ print "ARGS",request.args
        print "DATA",request.data
        #~ print "FORM",request.form

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
    #~ abort(404)

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
    #~ name = DEFAULT_SERVER_DOMAIN
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
    #~ app.run(debug=DEBUG, host=HOST, port=443, ssl_context='adhoc') #For development purposes only. pyOpenssl required
    app.run(debug=DEBUG, host=HOST, port=PORT)
