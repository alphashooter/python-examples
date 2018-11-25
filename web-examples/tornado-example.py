from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
from tornado.routing import PathMatches


class MainHandler(RequestHandler):
    def get(self):
        self.write('hello, world!')


class HelloHandler(RequestHandler):
    def get(self, name):
        self.write('hello, %s!' % name)


class TemplateHandler(RequestHandler):
    def get(self, name):
        self.render('templates/tornado-template.html', name=name)


if __name__ == "__main__":
    app = Application([
        (r"/", MainHandler),
        (PathMatches(r'/hello/(?P<name>\w+)'), HelloHandler),  # regex route
        (PathMatches(r'/template/(?P<name>\w*)'), TemplateHandler)  # regex route
    ])
    app.listen(8888)
    IOLoop.current().start()
