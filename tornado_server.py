import tornado.web
import tornado.ioloop
import currency

# Creating a tornado request handler class for handling requests to retrieve currency data.
class currencyHandler(tornado.web.RequestHandler):
    def get(self,coin):
        self.write(currency.getCoinData(coin))

# Creating a tornado request handler class for handling requests to retrieve about webpage.
class webPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("about.html")

# Creating a tornado request handler class for handling requests to retrieve default webpage.
class defaultHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

# Setting up tornado server.
if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/getCurrencyData/([a-z,-]+)",currencyHandler),
        (r"/about",webPageHandler),
        (r"/", defaultHandler)
    ])
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()