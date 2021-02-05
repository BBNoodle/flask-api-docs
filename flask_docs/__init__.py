# -*- coding: utf-8 -*- 
# @Time : 2/1/21 2:46 PM 
# @Author : mxt
# @File : __init__.py

from flask import (
    Flask, render_template, Blueprint
)


class BluePrint(Blueprint):
    url_map = dict()

    def __getattr__(self, item):
        if item == "url_map":
            return self.url_map
        else:
            return "Error Item!"

    def add_url_rule(self, rule, endpoint=None, view_func=None, **options):
        arguments = options.pop("args") if options.get('args') else dict()
        self.url_map.setdefault(rule, {"endpoint": endpoint, "args": arguments, "view_func": view_func})
        super().add_url_rule(rule, endpoint=endpoint, view_func=view_func, **options)


class Docs:
    _methods = set("HEAD OPTIONS".split(' '))

    def __init__(self,
                 app,
                 hide_docs=False,
                 default_headers=None):
        """

        :param app:
        :param hide_docs:
        :param default_headers:
        """
        self.app = app
        assert isinstance(app, Flask), "app must be a Flask object."
        self.hide_docs = hide_docs
        self.default_headers = default_headers
        self.init_config()

        if not self.app.config["HIDE_DOCS"]:
            self.add_docs_rule()

        self.init_docs_staticfiles()

    def __getattr__(self, item):
        if item == "url_map":
            iter_rules = self.app.url_map.iter_rules()
            return {item[0]: item[1] for item in self.__interface_iter(iter_rules)}
        else:
            return Exception("'item' gets an unknown content")

    def init_docs_staticfiles(self):
        docs_page = Blueprint("flask_docs", __name__, static_folder='static', static_url_path='/flask_docs',
                              template_folder='templates')
        self.app.register_blueprint(docs_page)

    def init_config(self):
        self.app.config.setdefault('HIDE_DOCS', self.hide_docs)
        self.app.config.setdefault('DEFAULT_HEADERS', self.default_headers or [])

    def add_docs_rule(self):
        self.app.add_url_rule('/flask_docs/', 'flask_docs', self.docs_view, methods=['GET'],
                              strict_slashes=False)

    def docs_view(self):
        a = self.__getattr__('url_map')
        return render_template('flask_docs/home.html', endpoints=a)

    def __interface_iter(self, url_iter):
        for item in url_iter:
            rule = item.rule
            endpoint = item.endpoint
            params = BluePrint.url_map.get(rule)
            if not params:
                continue
            methods = item.methods - self._methods
            return_data = {
                "url": rule,
                "methods": methods,
                "description": params['view_func'].__doc__,
                "params": params['args'],
                "renders": [
                    "application/json"
                ],
                "parses": [
                    "application/json"
                ]
            }
            yield endpoint, return_data
