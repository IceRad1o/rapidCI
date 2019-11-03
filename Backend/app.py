import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world")


def make_server():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    server = make_server()
    server.listen(9000)
    print("Server start at port: 9000")
    tornado.ioloop.IOLoop.current().start()


