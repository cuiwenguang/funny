import tornado.web
import tornado.ioloop
import tornado.options

from conf.routers import urls
from conf.settings import settings

def main():
    tornado.options.parse_command_line()
    app = tornado.web.Application(urls, **settings)
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()