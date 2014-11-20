import json
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line
import os
from .generator import Generator


_ENV_NAME_DC = 'PSF_DC'
_ENV_NAME_WORKER = 'PSF_WORKER'

try:
    _PSF_DC = int(os.environ[_ENV_NAME_DC])
except KeyError:
    _PSF_DC = 0

try:
    _PSF_WORKER = int(os.environ[_ENV_NAME_WORKER])
except KeyError:
    _PSF_WORKER = 0

define("debug", default=False, help="run in debug mode", type=bool)
define("address", default='localhost', help="run on the given address", type=str)
define("port", default=8910, help="run on the given port", type=int)
define("dc", default=_PSF_DC, help="Datacenter Identifier", type=int)
define("worker", default=_PSF_WORKER, help="Worker Identifier", type=int)


class IDHandler(tornado.web.RequestHandler):
    def get(self):
        generated_id = self.application.id_generator.get_next_id()
        self.set_header("Content-Type", "application/json")
        self.write(str(generated_id))
        self.flush() # avoid ETag, etc generation


class StatsHandler(tornado.web.RequestHandler):
    def get(self):
        stats = self.application.id_generator.stats

        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(stats))


class SnowflakeApplication(tornado.web.Application):
    def __init__(self, **settings):
        handlers = [
            (r'/', IDHandler),
            (r'/stats', StatsHandler),
        ]
        settings = {
            'debug': options.debug,
        }
        self.id_generator = Generator(options.dc, options.worker)
        super(SnowflakeApplication, self).__init__(handlers, **settings)


def main(): # pragma: no cover
    import logging.config
    import logging
    import os.path

    # setup logging
    logging.config.fileConfig(os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        'logging.ini',
    )))

    tornado.options.parse_command_line()

    http_server = tornado.httpserver.HTTPServer(SnowflakeApplication())

    print("Starting snowflake start at %s:%d" % (options.address, options.port))
    http_server.listen(options.port, options.address)

    try:
        tornado.ioloop.IOLoop.instance().start()
    except Exception:
        logging.exception('Snowflake server error')


if __name__ == "__main__":
    main()