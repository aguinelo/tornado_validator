import tornado.web
import json
from datetime import datetime
from bson import json_util
from pymongo import MongoClient
from tornado_validator import validator

def json_response(handler=None, return_code=1, data=[], mensagem=""):
    handler.set_header("Content-Type", "application/json") 
    handler.content_type = 'application/json'
    handler.write(json.dumps({"return_code": return_code, "data" : data, "message": mensagem}, default=json_util.default))

class PostHandler(tornado.web.RequestHandler):
    def post(self):

        validation_rules = [
            {"field":"campo1", "type": int, "message": "O campo campo1 deve ser um inteiro."},
            {"field":"campo2", "type": bool, "message": "O campo campo2 deve ser booleano."},
            {"field":"campo3", "message": "O campo campo3 deve ser informado."} #required only
        ]

        data = tornado.escape.json_decode(self.request.body)

        if validator.valid(data, validation_rules):
            json_response(self, data=data)
        else:
            json_response(self, data=validator.errors())

def main():
    app = tornado.web.Application([
        (r"/post", PostHandler),
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
