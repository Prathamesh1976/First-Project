import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        with open('templates/index.html', 'r') as f:
            self.response.write(f.read())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
