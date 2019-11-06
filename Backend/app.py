import tornado.ioloop
import tornado.web

from Backend.register_github import RegisterGit


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Test server")



def make_server():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/user/register_github", RegisterGit),
        (r"/user/get_test_result", )
    ])


if __name__ == "__main__":
    server = make_server()
    server.listen(9000)
    print("Server start at port: 9000")
    tornado.ioloop.IOLoop.current().start()


