Tornado Validator
==================

Tornado Validator is a Python module for data validation.

Usage
------------

Here is a simple "Hello, world" example web app for Tornado:

code-block:: python

    class PostHandler(tornado.web.RequestHandler):
    def post(self):

        validation_rules = [
            {"field":"campo1", "type": int, "message": "O campo campo1 deve ser um inteiro."},
            {"field":"campo2", "type": bool, "message": "O campo campo2 deve ser booleano."},
            {"field":"campo3", "message": "O campo campo3 deve ser informado."}
        ]

        data = tornado.escape.json_decode(self.request.body)

        if validator.valid(data, validation_rules):
            json_response(self, data=data)
        else:
            json_response(self, data=validator.errors())

For full example view main.py file