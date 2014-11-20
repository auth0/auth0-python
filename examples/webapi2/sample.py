import json
import os
import urllib
import urllib2
import webapp2

from dotenv import Dotenv

# Load Env variables
env = None

try:
  env = Dotenv('./.env')
except IOError:
  env = os.environ

## CHANGE THIS
PORT = 3000
CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"
DOMAIN = "your-domain.auth0.com"
CALLBACK_URL = "http://localhost:%d/callback" % PORT

MAIN_PAGE_HTML = """\
<html>
  <body>
    <script src="http://cdn.auth0.com/js/lock-6.6.1.min.js"></script>
    <script type="text/javascript">

      var lock = new Auth0Lock('%s', '%s');

    </script>
    <button onclick="lock.show()">Login</button>
  </body>
</html>
""" % (CLIENT_ID, DOMAIN)

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.write(MAIN_PAGE_HTML)

class LoginCallback(webapp2.RequestHandler):

    def get(self):
      code = self.request.get("code")
      base_url = "https://{domain}".format(domain=DOMAIN)
      data = urllib.urlencode([('client_id', CLIENT_ID),
                               ('redirect_uri', CALLBACK_URL),
                               ('client_secret', CLIENT_SECRET),
                               ('code', code),
                               ('grant_type', 'authorization_code')])
      req = urllib2.Request(base_url + "/oauth/token", data)
      response = urllib2.urlopen(req)
      oauth = json.loads(response.read())
      userinfo = base_url + "/userinfo?access_token=" + oauth['access_token']

      response = urllib2.urlopen(userinfo)
      data = response.read()

      ## print user data
      self.response.write(data)


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/callback', LoginCallback)
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(application, host='127.0.0.1', port=PORT)

if __name__ == '__main__':
    main()

